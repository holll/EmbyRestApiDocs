"""All crawler tests are mocked/offline; no production snapshots are written."""
import hashlib
import io
import json
from pathlib import Path
import ssl
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import crawl_emby_api as crawl


def table(rows):
    return '<table><tbody>' + ''.join('<tr>' + ''.join('<td>' + cell + '</td>' for cell in row)
                                      + '</tr>' for row in rows) + '</tbody></table>'


class CrawlTests(unittest.TestCase):
    def test_explicit_output_directory_is_used_for_read_and_publish(self):
        with tempfile.TemporaryDirectory() as output, tempfile.TemporaryDirectory() as default:
            (Path(default) / 'services.json').write_text('invalid default must not be read')
            with patch.object(crawl, 'OUT', default), \
                    patch.object(crawl, 'get', return_value='directory'), \
                    patch.object(crawl, 'discover_services', return_value=[]):
                self.assertEqual(crawl.main(output_dir=Path(output)), 0)
                self.assertEqual(json.loads((Path(output) / 'services.json').read_text()), [])
                self.assertEqual((Path(default) / 'services.json').read_text(), 'invalid default must not be read')
                (Path(output) / 'services.json').write_text(json.dumps([
                    {'service': 'Example', 'operations': [{'method': 'get', 'path': '/Old'}]}]))
                with patch.object(crawl, 'publish_snapshot') as publish:
                    with self.assertRaisesRegex(crawl.CrawlError, 'disappeared'):
                        crawl.main(output_dir=output)
                    publish.assert_not_called()

    def test_raw_bytes_hash_and_metadata_match_without_decoding_loss(self):
        payload = b'<html>raw \\xff\\x00 bytes</html>'
        response = io.BytesIO(payload)
        response.geturl = lambda: 'https://example.com/final'
        response.status = 200
        response.headers = {'ETag': 'example'}
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as output, \
                patch.object(crawl.OPENER, 'open', return_value=response), \
                patch.object(crawl, 'discover_services', return_value=[]):
            self.assertEqual(crawl.main(output_dir=output, raw_dir=raw), 0)
            metadata = json.loads((Path(output) / 'metadata.json').read_text())
            record = metadata['requests'][0]
            digest = hashlib.sha256(payload).hexdigest()
            self.assertEqual(record['sha256'], digest)
            self.assertEqual(record['raw_file'], digest)
            self.assertEqual((Path(raw) / digest).read_bytes(), payload)
            self.assertEqual(record['final_url'], 'https://example.com/final')
            self.assertEqual(record['etag'], 'example')
            self.assertIsNone(crawl.RAW_DIR)

    def test_raw_write_failure_stops_publication_without_retry(self):
        response = io.BytesIO(b'directory')
        response.geturl = lambda: crawl.BASE + '.html'
        response.status = 200
        response.headers = {}
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(crawl.OPENER, 'open', return_value=response) as opener, \
                patch.object(crawl.os, 'replace', side_effect=OSError('raw disk full')), \
                patch.object(crawl, 'publish_snapshot') as publish:
            with self.assertRaisesRegex(crawl.RawWriteError, 'raw disk full'):
                crawl.main(output_dir=directory, raw_dir=directory)
            publish.assert_not_called()
            self.assertEqual(opener.call_count, 1)
            self.assertEqual(list(Path(directory).iterdir()), [])
            self.assertIsNone(crawl.RAW_DIR)

    def test_http_error_raw_body_saved_but_non_allowlisted_404_still_fails(self):
        payload = b'missing page'
        error = urllib.error.HTTPError('https://example.com/missing', 404, 'missing', {}, io.BytesIO(payload))
        with tempfile.TemporaryDirectory() as raw, \
                patch.object(crawl, 'RAW_DIR', raw), \
                patch.object(crawl.OPENER, 'open', side_effect=error):
            with self.assertRaises(crawl.FetchError) as raised:
                crawl.get('https://example.com/missing', tries=1)
            self.assertEqual(raised.exception.status, 404)
            digest = hashlib.sha256(payload).hexdigest()
            self.assertEqual((Path(raw) / digest).read_bytes(), payload)
            self.assertEqual(crawl.FETCH_RECORDS[-1]['raw_file'], digest)
            self.assertEqual(crawl.FETCH_RECORDS[-1]['status'], 404)

    def test_parameter_required_evidence(self):
        html = '<h5>Parameters</h5>' + table([
            ['*ConnectUserId', 'query', 'string', '', ''],
            ['Unknown', 'query', 'string', '', 'No constraint'],
            ['Optional', 'query', 'string', '', 'Optional.'],
            ['Required', 'query', 'string', '', 'Required identifier'],
        ])
        params = crawl.parse_params(html)
        self.assertEqual([(p['required'], p['required_source']) for p in params],
                         [('required', 'name_marker'), ('unknown', 'unspecified'),
                          ('optional', 'notes'), ('required', 'notes')])

    def test_scalar_and_array_types_preserved(self):
        html = '<div id="definitions"><h3 id="A" class="text-capitalize">A</h3>' + table([
            ['One', '<a href="#Child">Child</a>', ''],
            ['Many', '<a href="#Child">Child</a>[]', ''],
        ])
        self.assertEqual([f['type'] for f in crawl.parse_definitions(html)[0]['fields']], ['Child', 'Child[]'])

    def test_tls_verification_enabled(self):
        self.assertTrue(crawl.CTX.check_hostname)
        self.assertEqual(crawl.CTX.verify_mode, ssl.CERT_REQUIRED)
        with self.assertRaises(crawl.CrawlError):
            crawl.get('http://dev.emby.media/')

    def test_http_redirect_rejected(self):
        handler = crawl.HTTPSOnlyRedirect()
        with self.assertRaises(crawl.CrawlError):
            handler.redirect_request(None, None, 301, '', {}, 'http://example.com/')

    def test_failed_request_raises_not_empty(self):
        with patch.object(crawl.OPENER, 'open', side_effect=OSError('offline')):
            with self.assertRaises(crawl.FetchError):
                crawl.get('https://example.com/', tries=1)

    def test_directory_discovers_new_services(self):
        with patch.object(crawl, 'SERVICES', ['OldService']):
            self.assertEqual(crawl.discover_services('<a href="RestAPI/OldService.html">Old</a>'
                             '<a href="RestAPI/NewService.html">New</a>'), ['NewService', 'OldService'])
            with self.assertRaises(crawl.CrawlError):
                crawl.discover_services('<a href="RestAPI/NewService.html">New</a>')

    def test_service_markup_failure_stops_crawl(self):
        with patch.object(crawl, 'get', return_value='<html>Unexpected format</html>'):
            with self.assertRaises(crawl.CrawlError):
                crawl.parse_service('AnyService')
            with self.assertRaises(crawl.CrawlError):
                crawl.parse_operation('https://example.com/operation')

    def test_operation_response_markup_required(self):
        html = '<span class="opspan opspan-get">GET</span>/Example</code>'
        with patch.object(crawl, 'get', return_value=html):
            with self.assertRaisesRegex(crawl.CrawlError, 'no parsed responses'):
                crawl.parse_operation('https://example.com/operation')

    def test_only_known_backup_404_is_allowed(self):
        html = ('<a class="xref" href="BackupApi/getBackup.html"><h3>Backup</h3>'
                '<span class="opspan opspan-get">GET</span>/BackupRestore/BackupInfo</code>')
        error = crawl.FetchError('https://example.com/',
                                 urllib.error.HTTPError('https://example.com/', 404, 'missing', {}, None))
        with patch.object(crawl, 'get', return_value=html), \
                patch.object(crawl, 'parse_operation', side_effect=error):
            result = crawl.parse_service('BackupApi')
            self.assertEqual(result['operations'][0]['incomplete_reason'], 'http_404_allowlisted')
            with self.assertRaises(crawl.FetchError):
                crawl.parse_service('OtherApi')
        error.status = 503
        with patch.object(crawl, 'get', return_value=html), \
                patch.object(crawl, 'parse_operation', side_effect=error):
            with self.assertRaises(crawl.FetchError):
                crawl.parse_service('BackupApi')

    def test_endpoint_disappearance_stops_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / 'services.json').write_text(json.dumps([
                {'service': 'Example', 'operations': [{'method': 'get', 'path': '/Old'}]}]))
            with patch.object(crawl, 'OUT', directory), \
                    patch.object(crawl, 'get', return_value='directory'), \
                    patch.object(crawl, 'discover_services', return_value=['Example']), \
                    patch.object(crawl, 'parse_service', return_value={
                        'service': 'Example', 'operations': [{'method': 'get', 'path': '/New'}]}), \
                    patch.object(crawl, 'publish_snapshot') as publish:
                with self.assertRaisesRegex(crawl.CrawlError, 'disappeared'):
                    crawl.main()
                publish.assert_not_called()

    def test_parameter_and_model_loss_blocked(self):
        def snapshot(params, fields, enum):
            return [{'service': 'Example', 'operations': [{'method': 'get', 'path': '/Example',
                     'params': params, 'definitions': [{'name': 'A', 'description': 'X.A',
                     'fields': fields, 'enum': enum}]}]}]
        parameter = {'name': 'UserId', 'in': 'query'}
        field = {'name': 'Id', 'type': 'string'}
        previous = snapshot([parameter], [field], ['One'])
        for current, message in [(snapshot([], [field], ['One']), 'Parameters disappeared'),
                                 (snapshot([parameter], [], ['One']), 'Model fields/enum disappeared'),
                                 (snapshot([parameter], [field], []), 'Model fields/enum disappeared')]:
            with self.subTest(message=message, current=current):
                with self.assertRaisesRegex(crawl.CrawlError, message):
                    crawl.validate_snapshot(previous, current)
        current = snapshot([parameter, {'name': 'Limit', 'in': 'query'}],
                           [field, {'name': 'Name', 'type': 'string'}], ['One', 'Two'])
        crawl.validate_snapshot(previous, current)

    def test_parameter_parse_loss_stops_main_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            old = [{'service': 'Example', 'operations': [{'method': 'get', 'path': '/Example',
                    'params': [{'name': 'Id', 'in': 'query'}], 'definitions': []}]}]
            (Path(directory) / 'services.json').write_text(json.dumps(old))
            with patch.object(crawl, 'OUT', directory), \
                    patch.object(crawl, 'get', return_value='directory'), \
                    patch.object(crawl, 'discover_services', return_value=['Example']), \
                    patch.object(crawl, 'parse_service', return_value={'service': 'Example', 'operations': [
                        {'method': 'get', 'path': '/Example', 'params': [], 'definitions': []}]}), \
                    patch.object(crawl, 'publish_snapshot') as publish:
                with self.assertRaisesRegex(crawl.CrawlError, 'Parameters disappeared'):
                    crawl.main()
                publish.assert_not_called()

    def test_service_detail_mismatch_rejected(self):
        html = ('<a class="xref" href="Example/getExample.html"><h3>Example</h3>'
                '<span class="opspan opspan-get">GET</span>/Example</code>')
        for detail in [{'method': 'post', 'path': '/Example'}, {'method': 'get', 'path': '/Wrong'}]:
            with self.subTest(detail=detail), patch.object(crawl, 'get', return_value=html), \
                    patch.object(crawl, 'parse_operation', return_value=detail):
                with self.assertRaisesRegex(crawl.CrawlError, 'does not match service listing'):
                    crawl.parse_service('Example')

    def test_publication_success(self):
        with tempfile.TemporaryDirectory() as directory:
            crawl.publish_snapshot({'services.json': [1], 'models.json': {'A': 2}}, directory)
            self.assertEqual(json.loads((Path(directory) / 'models.json').read_text()), {'A': 2})
            self.assertEqual(sorted(p.name for p in Path(directory).iterdir()), ['models.json', 'services.json'])

    def test_stage_failure_keeps_original(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'services.json'
            target.write_bytes(b'original')
            with self.assertRaises(TypeError):
                crawl.publish_snapshot({'services.json': [], 'models.json': object()}, directory)
            self.assertEqual(target.read_bytes(), b'original')
            self.assertEqual([p.name for p in Path(directory).iterdir()], ['services.json'])

    def test_replace_failure_rolls_back(self):
        with tempfile.TemporaryDirectory() as directory:
            first, second = Path(directory) / 'services.json', Path(directory) / 'models.json'
            first.write_bytes(b'old services')
            second.write_bytes(b'old models')
            actual_replace = crawl.os.replace
            calls = []
            def replace(source, destination):
                calls.append(destination)
                if len(calls) == 2:
                    raise OSError('publication fault')
                return actual_replace(source, destination)
            with patch.object(crawl.os, 'replace', side_effect=replace):
                with self.assertRaisesRegex(OSError, 'publication fault'):
                    crawl.publish_snapshot({'services.json': [], 'models.json': {}}, directory)
            self.assertEqual(first.read_bytes(), b'old services')
            self.assertEqual(second.read_bytes(), b'old models')
            self.assertEqual(len(list(Path(directory).iterdir())), 2)

    def test_no_publication_on_fetch_failure(self):
        with patch.object(crawl, 'get', side_effect=crawl.CrawlError('network failed')), \
                patch.object(crawl, 'publish_snapshot') as publish:
            with self.assertRaises(crawl.CrawlError):
                crawl.main()
            publish.assert_not_called()

    def test_filename_escape_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                crawl.publish_snapshot({'../outside.json': []}, directory)


if __name__ == '__main__':
    unittest.main()
