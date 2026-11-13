"""AI-facing prose is English; official summaries are not translated."""
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import build_ai_index as ai


class AIIndexTests(unittest.TestCase):
    def make_index(self):
        services = [{'service': 'UserService', 'url': 'https://example.test/UserService.html',
                     'operations': [{'method': 'post', 'path': '/Example', 'auth': 'administrator',
                                     'summary': 'Official summary stays unchanged.', 'params': [],
                                     'doc_url': 'https://example.test/postExample.html'}]}]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'services.json').write_text(json.dumps(services))
            (root / 'models.json').write_text('{}')
            with patch.object(ai, 'DATA', root):
                return ai.build(services, {})

    def test_original_summary_and_english_metadata(self):
        index = self.make_index()
        endpoint = index['services'][0]['endpoints'][0]
        self.assertEqual(endpoint['title'], 'Official summary stays unchanged.')
        self.assertEqual(endpoint['auth'], 'administrator')
        self.assertEqual(endpoint['doc'], 'https://example.test/postExample.html')
        self.assertEqual(index['meta']['language'], 'en')
        self.assertEqual(index['meta']['source_data']['services'], 'tools/_data/services.json')

    def test_llms_english_except_existing_document_paths(self):
        text = ai.write_llms(self.make_index())
        prose = re.sub(r'\]\([^\n)]*\)', '](path)', text)
        self.assertNotRegex(prose, r'[\u4e00-\u9fff]')
        self.assertIn('untranslated', text)
        self.assertIn('unknown', text)
        self.assertIn('services.json', text)

    def test_unmarked_auth_is_not_claimed_anonymous(self):
        self.assertEqual(ai.short_auth({}), 'unspecified')
        self.assertEqual(ai.short_auth({'auth': 'user'}), 'user')


if __name__ == '__main__':
    unittest.main()
