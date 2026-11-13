# -*- coding: utf-8 -*-
"""抓取 dev.emby.media 的 Emby REST API 文档，输出结构化 JSON。

用法: python3 tools/crawl_emby_api.py [--output-dir DIR] [--raw-dir DIR]
      --output-dir 默认 tools/_data；--raw-dir 可选，按 SHA-256 保存原始响应字节。
输出: tools/_data/services.json   每个服务的接口清单
      tools/_data/models.json     全局数据模型定义（按名称去重）
"""
import argparse
import json
import os
import re
import ssl
import sys
import time
import html as htmllib
import urllib.request
import urllib.error
from urllib.parse import urljoin, urlparse
from datetime import datetime, timezone
import hashlib
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor

from model_registry import model_identity, normalize_services

BASE = "https://dev.emby.media/reference/RestAPI"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_data")

SERVICES = [
    "ActivityLogService", "ArtistsService", "AudioService", "BackupApi",
    "BifService", "BrandingService", "ChannelService", "CodecParameterService",
    "CollectionService", "ConfigurationService", "ConnectService",
    "ContentService", "DeviceService", "DisplayPreferencesService",
    "DlnaServerService", "DlnaService", "DynamicHlsService",
    "EncodingInfoService", "EnvironmentService", "FeatureService",
    "FfmpegOptionsService", "GameGenresService", "GenericUIApiService",
    "GenresService", "HlsSegmentService", "ImageService", "InstantMixService",
    "ItemLookupService", "ItemRefreshService", "ItemUpdateService",
    "ItemsService", "LibraryService", "LibraryStructureService",
    "LiveStreamService", "LiveTvService", "LocalizationService",
    "MediaInfoService", "MoviesService", "MusicGenresService",
    "NotificationsService", "OfficialRatingService", "OpenApiService",
    "PackageService", "PartyService", "PersonsService", "PlaylistService",
    "PlaystateService", "PluginService", "RemoteImageService",
    "ScheduledTaskService", "SessionsService", "StudiosService",
    "SubtitleOptionsService", "SubtitleService", "SuggestionsService",
    "SyncService", "SystemService", "TagService", "ToneMapOptionsService",
    "TrailersService", "TvShowsService", "UniversalAudioService",
    "UserLibraryService", "UserNotificationsService", "UserService",
    "UserViewsService", "VideoHlsService", "VideoService", "VideosService",
    "WebAppService",
]

CTX = ssl.create_default_context()
FETCH_RECORDS = []
RAW_DIR = None
FETCH_LOCK = threading.Lock()
KNOWN_MISSING_DETAILS = {'/BackupRestore/BackupInfo', '/BackupRestore/Restore',
                         '/BackupRestore/RestoreData'}


class CrawlError(RuntimeError):
    pass


class FetchError(CrawlError):
    def __init__(self, url, cause):
        super().__init__('FAIL %s %s' % (url, cause))
        self.url = url
        self.status = getattr(cause, 'code', None)


class HTTPSOnlyRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).scheme != 'https':
            raise CrawlError('Refusing insecure redirect: ' + newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


OPENER = urllib.request.build_opener(urllib.request.HTTPSHandler(context=CTX), HTTPSOnlyRedirect())


class RawWriteError(CrawlError):
    """Raw evidence must be durable before the corresponding snapshot can publish."""


def record_response(url, final_url, status, headers, payload):
    digest = hashlib.sha256(payload).hexdigest()
    record = {'url': url, 'final_url': final_url, 'status': status,
              'sha256': digest, 'etag': headers.get('ETag'),
              'last_modified': headers.get('Last-Modified')}
    if RAW_DIR is not None:
        temporary = None
        try:
            os.makedirs(RAW_DIR, exist_ok=True)
            fd, temporary = tempfile.mkstemp(prefix='.raw-', dir=RAW_DIR)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, os.path.join(RAW_DIR, digest))
            record['raw_file'] = digest
        except OSError as exc:
            raise RawWriteError('Cannot save raw response for %s: %s' % (url, exc)) from exc
        finally:
            if temporary is not None and os.path.exists(temporary):
                os.unlink(temporary)
    with FETCH_LOCK:
        FETCH_RECORDS.append(record)


def get(url, tries=5):
    if urlparse(url).scheme != 'https':
        raise CrawlError('HTTPS required: ' + url)
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'EmbyRestApiDocs/1.0', 'Accept': 'text/html',
            })
            with OPENER.open(req, timeout=60) as response:
                if urlparse(response.geturl()).scheme != 'https':
                    raise CrawlError('Insecure response URL')
                payload = response.read()
                if not payload:
                    raise CrawlError('Empty response: ' + url)
                record_response(url, response.geturl(), response.status, response.headers, payload)
                return payload.decode('utf-8', 'replace')
        except RawWriteError:
            raise
        except urllib.error.HTTPError as exc:
            with exc:
                payload = exc.read()
                record_response(url, exc.geturl(), exc.code, exc.headers, payload)
            last = exc
            if exc.code in (400, 401, 403, 404):
                break
        except (OSError, CrawlError) as exc:
            last = exc
        if i + 1 < tries:
            time.sleep(1.5 * (i + 1))
    raise FetchError(url, last)


def discover_services(page):
    names = set()
    for href in re.findall(r'''href=["']([^"']+)["']''', page, re.I):
        parsed = urlparse(urljoin(BASE + '.html', htmllib.unescape(href)))
        if parsed.netloc != urlparse(BASE).netloc:
            continue
        match = re.fullmatch(r'/reference/RestAPI/([A-Za-z][A-Za-z0-9_]*)\.html', parsed.path)
        if match:
            names.add(match.group(1))
    if not names:
        raise CrawlError('Official service directory contained no services')
    missing = set(SERVICES) - names
    if missing:
        raise CrawlError('Official directory unexpectedly lost known services: ' + ', '.join(sorted(missing)))
    return sorted(names)


def text(fragment):
    """把 HTML 片段压成纯文本。"""
    fragment = re.sub(r"(?is)<(script|style).*?</\1>", "", fragment)
    fragment = re.sub(r"(?i)<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"(?s)<[^>]+>", "", fragment)
    fragment = htmllib.unescape(fragment)
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in fragment.split("\n")]
    return " ".join([ln for ln in lines if ln]).strip()


def cells(row):
    return [text(c) for c in re.findall(r"(?is)<td.*?</td>", row)]


def split_rows(table):
    body = table
    m = re.search(r"(?is)<tbody>(.*?)</tbody>", table)
    if m:
        body = m.group(1)
    return re.findall(r"(?is)<tr.*?</tr>", body)


def table_after(haystack, anchor_regex):
    """取 anchor 之后的第一张 table。"""
    m = re.search(anchor_regex, haystack, re.I)
    if not m:
        return None
    start = m.end()
    tm = re.search(r"(?is)<table.*?</table>", haystack[start:])
    return tm.group(0) if tm else None


HEADERS = {"name", "in", "type", "default", "notes", "status code", "description", "samples"}


def data_rows(table):
    out = []
    for row in split_rows(table):
        c = cells(row)
        if not c or not c[0]:
            continue
        if c[0].lower() in HEADERS:
            continue
        out.append(c)
    return out


def parse_params(page):
    table = table_after(page, r"<h5>Parameters</h5>")
    if not table:
        # 有的页面参数表在 <h3>...parameters... 下
        table = table_after(page, r"<h5>Request Parameters</h5>")
    if not table:
        return []
    out = []
    for c in data_rows(table):
        if len(c) < 5:
            c = c + [""] * (5 - len(c))
        name = c[0]
        stripped = name.lstrip("*")
        note = c[4].lower().strip()
        if name.startswith('*'):
            required, source = 'required', 'name_marker'
        elif note.startswith('required'):
            required, source = 'required', 'notes'
        elif note.startswith('optional'):
            required, source = 'optional', 'notes'
        else:
            required, source = 'unknown', 'unspecified'
        out.append({
            "name": stripped,
            "in": c[1],
            "type": c[2],
            "required": required,
            "required_source": source,
            "default": c[3],
            "notes": c[4],
        })
    return out


def parse_responses(page):
    table = table_after(page, r"<h5>Responses</h5>")
    if not table:
        return []
    out = []
    for c in data_rows(table):
        if len(c) < 4:
            c = c + [""] * (4 - len(c))
        if not re.match(r"^\d{3}$", c[0]):
            continue
        out.append({"status": c[0], "type": c[1], "description": c[2]})
    return out


def parse_definitions(page):
    i = page.find('id="definitions"')
    if i < 0:
        return []
    body = page[i:]
    defs = []
    blocks = re.split(r'(?is)<h3\s+id="[^"]+"\s+class="text-capitalize"', body)
    for blk in blocks[1:]:
        name_m = re.search(r"(?is)>([^<]+)</h3>", blk)
        if not name_m:
            continue
        name = text(name_m.group(1))
        if not name:
            continue
        enum = []
        em = re.search(r"(?is)<h5>Enum Values</h5>(.*?)</ul>", blk)
        if em:
            enum = [text(x) for x in re.findall(r"(?is)<li>(.*?)</li>", em.group(1))]
        fields = []
        tm = re.search(r"(?is)<table.*?</table>", blk)
        if tm:
            for c in data_rows(tm.group(0)):
                if len(c) < 3:
                    c = c + [""] * (3 - len(c))
                fields.append({"name": c[0], "type": c[1], "notes": c[2]})
        desc = ""
        dm = re.search(r"(?is)<div>(.*?)</div>", blk)
        if dm:
            desc = text(dm.group(1))
        defs.append({"name": name, "description": desc, "enum": enum, "fields": fields})
    return defs


def parse_operation(url):
    page = get(url)
    if not page:
        raise CrawlError('Empty operation document: ' + url)
    i = page.find('class="refdoc"')
    body = page[i:] if i > 0 else page

    mm = re.search(
        r'(?is)<span class="opspan opspan-(\w+)">[^<]*</span>(.*?)</code>', body)
    if not mm:
        raise CrawlError('Unrecognized operation markup: ' + url)
    method = mm.group(1).lower()
    path = text(mm.group(2))

    sm = re.search(r'(?is)<div class="markdown level0 summary">(.*?)</div>', body)
    summary = text(sm.group(1)) if sm else ""
    dm = re.search(r'(?is)<div class="markdown level0 description">(.*?)</div>', body)
    description = text(dm.group(1)) if dm else ""
    dep = re.search(r"(?i)Requires authentication as (\w+)", description)
    auth = dep.group(1).lower() if dep else ""

    responses = parse_responses(body)
    if not responses:
        raise CrawlError('Operation contains no parsed responses: ' + url)
    return {
        "method": method,
        "path": path,
        "summary": summary,
        "description": description,
        "auth": auth,
        "params": parse_params(body),
        "responses": responses,
        "definitions": parse_definitions(body),
    }


def parse_service(name):
    url = "%s/%s.html" % (BASE, name)
    page = get(url)
    if not page:
        raise CrawlError('Empty service document: ' + url)
    ops = []
    parts = re.split(r'(?=<a class="xref" href=")', page)
    for part in parts[1:]:
        hm = re.match(r'(?s)<a class="xref" href="([^"]+)"', part)
        if not hm:
            continue
        href = hm.group(1)
        h3 = re.search(r"(?is)<h3[^>]*>([^<]+)</h3>", part)
        mw = re.search(r'(?is)<span class="opspan opspan-(\w+)">[^<]*</span>(.*?)</code>', part)
        if not mw:
            continue
        summ = re.search(r'(?is)<div class="markdown level1 summary">(.*?)</div>', part)
        if not href.startswith(name + "/"):
            href = name + "/" + href
        op_url = "%s/%s" % (BASE, href)
        try:
            detail = parse_operation(op_url)
        except FetchError as exc:
            if exc.status != 404 or text(mw.group(2)) not in KNOWN_MISSING_DETAILS or name != 'BackupApi':
                raise
            detail = {
                "method": mw.group(1).lower(),
                "path": text(mw.group(2)),
                "summary": text(summ.group(1)) if summ else "",
                "description": "",
                "auth": "",
                "params": [],
                "responses": [],
                "definitions": [],
                "incomplete": True,
                "incomplete_reason": "http_404_allowlisted",
            }
        listed_key = (mw.group(1).lower(), text(mw.group(2)))
        detail_key = (detail['method'].lower(), detail['path'])
        if detail_key != listed_key:
            raise CrawlError('Operation detail does not match service listing: %r != %r at %s'
                             % (detail_key, listed_key, op_url))
        detail["name"] = text(h3.group(1)) if h3 else ""
        detail["doc_url"] = op_url
        ops.append(detail)
    if not ops:
        raise CrawlError('Service contains no parsed operations: ' + name)
    keys = [(op['method'], op['path']) for op in ops]
    if len(set(keys)) != len(keys):
        raise CrawlError('Duplicate operations: ' + name)
    return {"service": name, "url": url, "operations": ops}


def publish_snapshot(payloads, output_dir=OUT):
    """Stage JSON before publication; roll back existing bytes on replace failure.

    Each file replacement is atomic. This is not a multi-file transaction against
    power loss or concurrent readers; callers must serialize snapshot writers.
    """
    os.makedirs(output_dir, exist_ok=True)
    staged, backups, replaced = {}, {}, []
    try:
        for filename, value in payloads.items():
            if os.path.basename(filename) != filename or filename in ('.', '..'):
                raise ValueError('Snapshot filename must be a basename')
            target = os.path.join(output_dir, filename)
            if os.path.exists(target):
                with open(target, 'rb') as original:
                    backups[filename] = original.read()
            else:
                backups[filename] = None
            fd, temporary = tempfile.mkstemp(prefix='.snapshot-', suffix='.tmp', dir=output_dir)
            staged[filename] = temporary
            with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                json.dump(value, stream, ensure_ascii=False, indent=1, sort_keys=True)
                stream.write('\n')
                stream.flush()
                os.fsync(stream.fileno())
        for filename, temporary in staged.items():
            os.replace(temporary, os.path.join(output_dir, filename))
            replaced.append(filename)
    except BaseException:
        for filename in reversed(replaced):
            target = os.path.join(output_dir, filename)
            original = backups[filename]
            if original is None:
                # Exact basename was validated above; target is owned by us.
                os.unlink(target)
            else:
                fd, temporary = tempfile.mkstemp(prefix='.rollback-', dir=output_dir)
                try:
                    with os.fdopen(fd, 'wb') as stream:
                        stream.write(original)
                        stream.flush()
                        os.fsync(stream.fileno())
                    os.replace(temporary, target)
                finally:
                    if os.path.exists(temporary):
                        os.unlink(temporary)
        raise
    finally:
        for temporary in staged.values():
            if os.path.exists(temporary):
                os.unlink(temporary)


def validate_snapshot(previous, current):
    """Reject destructive reductions pending an explicit upstream/manual review."""
    def operations(services):
        return {(svc['service'], op['method'].lower(), op['path']): op
                for svc in services for op in svc['operations']}
    old, new = operations(previous), operations(current)
    missing = old.keys() - new.keys()
    if missing:
        raise CrawlError('Previously recorded operations disappeared; review upstream changes before publishing: '
                         + repr(sorted(missing)))
    for key, operation in old.items():
        replacement = new[key]
        old_params = {(p['name'].lstrip('*'), p.get('in', '')) for p in operation.get('params', [])}
        new_params = {(p['name'].lstrip('*'), p.get('in', '')) for p in replacement.get('params', [])}
        lost = old_params - new_params
        if lost:
            raise CrawlError('Parameters disappeared; manual review required for %r: %r' % (key, sorted(lost)))
        new_definitions = {model_identity(d): d for d in replacement.get('definitions', [])}
        for definition in operation.get('definitions', []):
            identity = model_identity(definition)
            candidate = new_definitions.get(identity, {})
            old_fields = {field['name'] for field in definition.get('fields', [])}
            new_fields = {field['name'] for field in candidate.get('fields', [])}
            lost_fields = old_fields - new_fields
            lost_values = set(definition.get('enum', [])) - set(candidate.get('enum', []))
            if lost_fields or lost_values:
                raise CrawlError('Model fields/enum disappeared; manual review required for %r %s: %r / %r'
                                 % (key, identity, sorted(lost_fields), sorted(lost_values)))


def main(output_dir=None, raw_dir=None):
    """Run one crawl; serialize invocations because request recording is shared."""
    global RAW_DIR
    previous_raw_dir = RAW_DIR
    RAW_DIR = os.fspath(raw_dir) if raw_dir is not None else None
    try:
        return crawl_snapshot(OUT if output_dir is None else os.fspath(output_dir))
    finally:
        RAW_DIR = previous_raw_dir


def crawl_snapshot(output_dir):
    with FETCH_LOCK:
        FETCH_RECORDS.clear()
    service_names = discover_services(get(BASE + '.html'))
    services = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for res in pool.map(parse_service, service_names):
            services.append(res)
            print("%-26s %3d ops" % (res["service"], len(res["operations"])))
    services.sort(key=lambda s: s['service'])
    services, models = normalize_services(services)
    previous_path = os.path.join(output_dir, 'services.json')
    if os.path.exists(previous_path):
        with open(previous_path, encoding='utf-8') as stream:
            previous = json.load(stream)
        previous, _ = normalize_services(previous)
        validate_snapshot(previous, services)
    metadata = {'kind': 'live_crawl', 'fetched_at': datetime.now(timezone.utc).isoformat(),
                'emby_version': None, 'source': BASE + '.html',
                'requests': sorted(FETCH_RECORDS, key=lambda r: r['url']),
                'incomplete_policy': 'Only three known BackupApi HTTP 404 details are allowed',
                'service_directory': service_names}
    publish_snapshot({'services.json': services, 'models.json': models,
                      'metadata.json': metadata}, output_dir=output_dir)
    total = sum(len(s['operations']) for s in services)
    print('TOTAL services=%d operations=%d models=%d' % (len(services), total, len(models)))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', default=OUT, help='Snapshot output directory (default: tools/_data)')
    parser.add_argument('--raw-dir', help='Save raw HTTP response bytes under their SHA-256 filenames')
    args = parser.parse_args()
    sys.exit(main(output_dir=args.output_dir, raw_dir=args.raw_dir))
