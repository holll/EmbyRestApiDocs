# -*- coding: utf-8 -*-
"""抓取 dev.emby.media 的 Emby REST API 文档，输出结构化 JSON。

用法: python tools/crawl_emby_api.py
输出: tools/_data/services.json   每个服务的接口清单
      tools/_data/models.json     全局数据模型定义（按名称去重）
"""
import json
import os
import re
import ssl
import sys
import time
import html as htmllib
import urllib.request
from concurrent.futures import ThreadPoolExecutor

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
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def get(url, tries=5):
    last = None
    candidates = [url]
    if url.startswith("https://"):
        candidates.append("http://" + url[len("https://"):])
    for i in range(tries):
        for u in candidates:
            try:
                req = urllib.request.Request(u, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Accept": "text/html,application/xhtml+xml",
                    "Connection": "close",
                })
                with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
                    return r.read().decode("utf-8", "replace")
            except Exception as e:  # noqa: BLE001
                last = e
        time.sleep(1.5 * (i + 1))
    sys.stderr.write("FAIL %s %s\n" % (url, last))
    return ""


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
        required = name.startswith("*") or not c[4].lower().startswith("optional")
        out.append({
            "name": stripped,
            "in": c[1],
            "type": c[2],
            "required": "required" if required else "optional",
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
        return None
    i = page.find('class="refdoc"')
    body = page[i:] if i > 0 else page

    mm = re.search(
        r'(?is)<span class="opspan opspan-(\w+)">[^<]*</span>(.*?)</code>', body)
    if not mm:
        return None
    method = mm.group(1).lower()
    path = text(mm.group(2))

    sm = re.search(r'(?is)<div class="markdown level0 summary">(.*?)</div>', body)
    summary = text(sm.group(1)) if sm else ""
    dm = re.search(r'(?is)<div class="markdown level0 description">(.*?)</div>', body)
    description = text(dm.group(1)) if dm else ""
    dep = re.search(r"(?i)Requires authentication as (\w+)", description)
    auth = dep.group(1).lower() if dep else ""

    return {
        "method": method,
        "path": path,
        "summary": summary,
        "description": description,
        "auth": auth,
        "params": parse_params(body),
        "responses": parse_responses(body),
        "definitions": parse_definitions(body),
    }


def parse_service(name):
    url = "%s/%s.html" % (BASE, name)
    page = get(url)
    if not page:
        return {"service": name, "url": url, "operations": []}
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
        detail = parse_operation(op_url)
        if detail is None:
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
            }
        detail["name"] = text(h3.group(1)) if h3 else ""
        detail["doc_url"] = op_url
        ops.append(detail)
    return {"service": name, "url": url, "operations": ops}


def main():
    os.makedirs(OUT, exist_ok=True)
    models = {}
    services = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for res in pool.map(parse_service, SERVICES):
            services.append(res)
            for op in res["operations"]:
                for d in op["definitions"]:
                    if d["name"] not in models or (not models[d["name"]]["fields"] and d["fields"]):
                        models[d["name"]] = d
            print("%-26s %3d ops" % (res["service"], len(res["operations"])))
    services.sort(key=lambda s: s["service"])
    with open(os.path.join(OUT, "services.json"), "w", encoding="utf-8") as f:
        json.dump(services, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "models.json"), "w", encoding="utf-8") as f:
        json.dump(models, f, ensure_ascii=False, indent=1)
    total = sum(len(s["operations"]) for s in services)
    print("TOTAL services=%d operations=%d models=%d" % (len(services), total, len(models)))


if __name__ == "__main__":
    main()
