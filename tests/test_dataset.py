"""Offline regression coverage for legacy trust boundaries and generator helpers."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build_docs import required_flag
from dataset import load_dataset, snapshot_metadata
from model_registry import normalize_services
from rebuild_snapshot import apply_corrections
from crawl_emby_api import publish_snapshot


class DatasetTests(unittest.TestCase):
    def test_snapshot_publication_is_stable_for_mapping_key_order(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            publish_snapshot({'models.json': {'B': {'sources': [], 'identity': 'B'}}}, root)
            first = (root / 'models.json').read_bytes()
            publish_snapshot({'models.json': {'B': {'identity': 'B', 'sources': []}}}, root)
            self.assertEqual(first, (root / 'models.json').read_bytes())

    def test_legacy_required_is_not_evidence(self):
        self.assertEqual(required_flag({"name": "UserId", "in": "query", "required": "required", "notes": ""}), "未标注")
        self.assertEqual(required_flag({"name": "Id", "in": "path", "notes": ""}), "是")

    def test_explicit_marker_and_optional_notes(self):
        self.assertEqual(required_flag({"in": "query", "notes": "", "required": "required", "required_source": "name_marker"}), "是")
        self.assertEqual(required_flag({"in": "query", "notes": "Optional. Filter"}), "否")

    def test_correction_is_scoped_and_requires_unique_match(self):
        services = [{"service": "A", "operations": [{"method": "get", "path": "/X", "params": [{"name": "Id", "in": "query"}]}]}]
        corrections = [{"service": "A", "method": "GET", "path": "/X", "parameter": "Id", "location": "query", "required": "required", "required_source": "verified", "source_url": "https://example.test/doc"}]
        fixed = apply_corrections(copy.deepcopy(services), corrections)
        self.assertEqual(fixed[0]["operations"][0]["params"][0]["required_evidence"], corrections[0]["source_url"])
        with self.assertRaises(ValueError):
            apply_corrections([], corrections)

    def test_fresh_upstream_marker_is_preserved_over_legacy_correction(self):
        parameter = {'name': 'Id', 'in': 'query', 'required': 'required', 'required_source': 'name_marker'}
        services = [{'service': 'A', 'operations': [{'method': 'get', 'path': '/X', 'params': [parameter]}]}]
        correction = {'service': 'A', 'method': 'GET', 'path': '/X', 'parameter': 'Id', 'location': 'query',
                      'required': 'required', 'required_source': 'verified', 'source_url': 'https://example.test/doc'}
        apply_corrections(services, [correction])
        self.assertEqual(parameter['required_source'], 'name_marker')
        parameter.update(required='optional', required_source='notes')
        with self.assertRaises(ValueError):
            apply_corrections(services, [correction])

    def test_stale_registry_is_rejected_and_hash_is_deterministic(self):
        services, models = normalize_services([])
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "services.json").write_text(json.dumps(services))
            (root / "models.json").write_text(json.dumps(models))
            self.assertEqual(load_dataset(root), ([], {}))
            self.assertIsNone(snapshot_metadata(root)["provenance"]["fetched_at"])
            self.assertEqual(snapshot_metadata(root), snapshot_metadata(root))
            (root / "models.json").write_text('{"Stale": {}}')
            with self.assertRaises(ValueError):
                load_dataset(root)


if __name__ == "__main__":
    unittest.main()
