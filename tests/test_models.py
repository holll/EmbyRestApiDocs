"""Offline regression tests for lossless model identity normalization."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from model_registry import ModelConflictError, normalize_services


def definition(name, identity, fields=(), enum=()):
    return {'name': name, 'description': identity, 'fields': list(fields), 'enum': list(enum)}


def service(definitions):
    return [{'service': 'Example', 'operations': [{'method': 'get', 'path': '/Example',
            'definitions': definitions, 'params': [], 'responses': []}]}]


class ModelTests(unittest.TestCase):
    def test_empty_enum_cannot_hide_rich_definition(self):
        services = service([definition('DayOfWeek', 'System.DayOfWeek'),
                            definition('DayOfWeek', 'System.DayOfWeek', enum=['Sunday', 'Monday'])])
        original = copy.deepcopy(services)
        normalized, models = normalize_services(services)
        self.assertEqual(services, original)
        self.assertEqual(models['DayOfWeek']['enum'], ['Sunday', 'Monday'])
        self.assertEqual(normalized, normalize_services(normalized)[0])

    def test_wrapper_is_not_entity(self):
        services = service([
            definition('DeviceInfo', 'QueryResult_Devices.DeviceInfo',
                       [{'name': 'Items', 'type': 'DeviceInfo[]'}]),
            definition('DeviceInfo', 'see also MediaBrowser.Model.Devices.DeviceInfo',
                       [{'name': 'Id', 'type': 'string'}]),
        ])
        services[0]['operations'][0]['responses'] = [{'type': 'QueryResult_Devices.DeviceInfo'}]
        normalized, models = normalize_services(services)
        self.assertEqual(set(models), {'DeviceInfo', 'QueryResult_DeviceInfo'})
        self.assertEqual(models['DeviceInfo']['fields'][0]['name'], 'Id')
        self.assertEqual(models['QueryResult_DeviceInfo']['fields'][0]['type'], 'DeviceInfo[]')
        self.assertEqual(normalized[0]['operations'][0]['responses'][0]['type'], 'QueryResult_DeviceInfo')
        self.assertEqual((normalized, models), normalize_services(normalized))

    def test_namespace_collisions_remain_separate(self):
        normalized, models = normalize_services(service([
            definition('TagItem', 'One.TagItem', [{'name': 'Id', 'type': 'string'}]),
        ]) + [{'service': 'Other', 'operations': [{'definitions': [
            definition('TagItem', 'Two.TagItem', [{'name': 'Name', 'type': 'string'}])]}]}])
        self.assertEqual(set(models), {'One_TagItem', 'Two_TagItem'})
        self.assertEqual(models['One_TagItem']['fields'][0]['name'], 'Id')

    def test_array_conflict_explicit_and_idempotent(self):
        data = service([definition('Parent', 'A.Parent', [{'name': 'Child', 'type': 'Child[]'}]),
                        definition('Parent', 'A.Parent', [{'name': 'Child', 'type': 'Child'}])])
        normalized, models = normalize_services(data)
        field = models['Parent']['fields'][0]
        self.assertEqual(field['type_candidates'], ['Child', 'Child[]'])
        self.assertEqual(field['type_status'], 'source_conflict')
        self.assertEqual((normalized, models), normalize_services(normalized))

    def test_incompatible_field_sets_fail(self):
        with self.assertRaises(ModelConflictError):
            normalize_services(service([definition('A', 'X.A', [{'name': 'One', 'type': 'string'}]),
                                        definition('A', 'X.A', [{'name': 'Two', 'type': 'string'}])]))

    def test_incompatible_enum_sets_fail(self):
        with self.assertRaises(ModelConflictError):
            normalize_services(service([definition('A', 'X.A', enum=['One']),
                                        definition('A', 'X.A', enum=['Two'])]))

    def test_existing_wrapper_name_not_doubled(self):
        _, models = normalize_services(service([definition('QueryResult_String', 'QueryResult_String')]))
        self.assertIn('QueryResult_String', models)

    def test_legacy_snapshot_offline_regressions(self):
        source = Path(__file__).resolve().parents[1] / 'tools/_data/services.json'
        services = json.loads(source.read_text(encoding='utf-8'))
        normalized, models = normalize_services(services)
        self.assertEqual(len(models['DeviceInfo']['fields']), 10)
        self.assertEqual(len(models['DayOfWeek']['enum']), 7)
        self.assertIn('QueryResult_DeviceInfo', models)
        self.assertEqual((normalized, models), normalize_services(normalized))
        self.assertTrue(models['DeviceInfo']['sources'])


if __name__ == '__main__':
    unittest.main()
