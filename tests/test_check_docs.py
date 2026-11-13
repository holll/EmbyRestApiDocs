"""离线回归：文档即使计数不变，字段/端点/索引损坏也必须失败。"""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import build_docs
import build_ai_index
import check_docs


class CheckDocsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        model = {"name": "ExampleDto", "description": "ExampleDto", "enum": [],
                 "fields": [{"name": "Id", "type": "string", "notes": ""},
                            {"name": "Name", "type": "string", "notes": ""}]}
        enum = {"name": "ExampleEnum", "description": "ExampleEnum", "enum": ["One", "Two"], "fields": []}
        self.models = {m["name"]: m for m in (model, enum)}
        op = {"name": "getExample", "method": "get", "path": "/Examples/{Id}",
              "summary": "", "description": "", "auth": "user", "params": [
                  {"name": "Id", "in": "path", "type": "string", "notes": "", "default": "", "required": "required"},
                  {"name": "Limit", "in": "query", "type": "integer", "notes": "Optional", "default": "", "required": "optional"}],
              "responses": [{"status": "200", "type": "ExampleDto", "description": "Operation successful."},
                            {"status": "401", "type": "", "description": "Unauthorized."}],
              "definitions": [model, enum]}
        self.services = [{"service": "ActivityLogService", "url": "https://example.invalid/service", "operations": [op]}]
        from model_registry import normalize_services
        self.services, self.models = normalize_services(self.services)
        self.service_path = self.root / "01-接口参考/08-系统与运维/ActivityLogService.md"
        self.model_path = self.root / "02-数据模型/06-系统与配置.md"
        (self.root / "02-数据模型").mkdir()
        with check_docs.module_root(build_docs, self.root):
            mapping, _ = build_docs.render_models(self.models)
            build_docs.render_service(self.services[0], mapping)
        # 这些文件仅提供导航目标，不模拟服务器。
        targets = ["README.md", "01-接口参考/08-系统与运维/README.md"]
        targets += [entry[0] for entry in build_ai_index.BASE_DOCS + build_ai_index.DEMOS]
        for target in targets:
            path = self.root / target
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# 示例\n", encoding="utf-8")
        data = self.root / "tools/_data"
        data.mkdir(parents=True)
        (data / "services.json").write_text(json.dumps(self.services), encoding="utf-8")
        (data / "models.json").write_text(json.dumps(self.models), encoding="utf-8")
        (data / "metadata.json").write_text('{}', encoding="utf-8")
        with check_docs.module_root(build_ai_index, self.root):
            index = build_ai_index.build(self.services, self.models)
            (self.root / "llms.txt").write_text(build_ai_index.write_llms(index), encoding="utf-8")
        (self.root / "index.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")

    def validate(self):
        return check_docs.validate(self.root, self.services, self.models)

    def mutate(self, path, before, after):
        text = path.read_text(encoding="utf-8")
        self.assertIn(before, text)
        path.write_text(text.replace(before, after), encoding="utf-8")

    def assert_content_error(self):
        report = self.validate()
        self.assertFalse(report.ok, report)
        self.assertTrue(any("内容语义不一致" in e for e in report.errors), report.errors)

    def test_valid_fixture_and_no_shared_errors(self):
        self.assertTrue(self.validate().ok, self.validate().errors)
        self.mutate(self.service_path, "`GET` `/Examples/{Id}`", "`POST` `/Examples/{Id}`")
        self.assertFalse(self.validate().ok)
        self.mutate(self.service_path, "`POST` `/Examples/{Id}`", "`GET` `/Examples/{Id}`")
        self.assertTrue(self.validate().ok)

    def test_all_table_rows_deleted_cannot_pass(self):
        for directory in ("01-接口参考", "02-数据模型"):
            for path in (self.root / directory).rglob("*.md"):
                path.write_text("\n".join(line for line in path.read_text(encoding="utf-8").splitlines()
                                          if not line.startswith("|")) + "\n", encoding="utf-8")
        self.assert_content_error()

    def test_route_method_changed(self):
        self.mutate(self.service_path, "`GET` `/Examples/{Id}`", "`DELETE` `/Examples/{Id}`")
        self.assert_content_error()

    def test_overview_route_missing(self):
        self.mutate(self.service_path, "| 1 | `GET`", "| 1 | `POST`")
        self.assert_content_error()

    def test_parameter_name_type_position_required(self):
        original = self.service_path.read_text(encoding="utf-8")
        for old, new in [("`Limit`", "`Wrong`"), ("| query |", "| header |"),
                         ("| integer |", "| string |"), ("| 是 |", "| 否 |")]:
            with self.subTest(old=old):
                self.service_path.write_text(original, encoding="utf-8")
                self.mutate(self.service_path, old, new)
                self.assert_content_error()

    def test_response_changed(self):
        self.mutate(self.service_path, "| 401 |", "| 403 |")
        self.assert_content_error()

    def test_model_field_name_type_and_missing_field(self):
        original = self.model_path.read_text(encoding="utf-8")
        for old, new in [("`Id`", "`BadId`"), ("| string |", "| integer |"),
                         ("| `Name` | string | 名称 |\n", "")]:
            with self.subTest(old=old):
                self.model_path.write_text(original, encoding="utf-8")
                self.mutate(self.model_path, old, new)
                self.assert_content_error()

    def test_enum_value_changed(self):
        self.mutate(self.model_path, "`One`、`Two`", "`One`、`Three`")
        self.assert_content_error()

    def test_extra_model_rejected(self):
        with self.model_path.open("a", encoding="utf-8") as handle:
            handle.write("\n## ExtraModel\n")
        self.assert_content_error()

    def test_extra_service_rejected(self):
        self.service_path.with_name("UnexpectedService.md").write_text("# Extra\n", encoding="utf-8")
        self.assertTrue(any("服务文档集合" in e for e in self.validate().errors))

    def test_index_mutations_with_unchanged_counts(self):
        path = self.root / "index.json"
        original = json.loads(path.read_text(encoding="utf-8"))
        for key, value in [("section", 99), ("path", "/Wrong"), ("method", "POST"), ("params", 100)]:
            with self.subTest(key=key):
                data = copy.deepcopy(original)
                data["services"][0]["endpoints"][0][key] = value
                path.write_text(json.dumps(data), encoding="utf-8")
                self.assertTrue(any("index.json 详细内容" in e for e in self.validate().errors))

    def test_missing_document_and_invalid_json(self):
        self.service_path.unlink()
        (self.root / "index.json").write_text("{bad", encoding="utf-8")
        report = self.validate()
        self.assertFalse(report.ok)
        self.assertTrue(any("JSON" in e for e in report.errors))

    def test_missing_anchor_detected(self):
        (self.root / "README.md").write_text("# 示例\n[失效](02-数据模型/06-系统与配置.md#no-such-anchor)\n", encoding="utf-8")
        self.assertTrue(any("锚点不存在" in e for e in self.validate().errors))

    def test_source_incomplete_is_visible_and_strict_fails(self):
        services = copy.deepcopy(self.services)
        services[0]["operations"][0]["incomplete"] = True
        report = check_docs.Report()
        check_docs.validate_source(services, self.models, report)
        self.assertEqual(report.counts["incomplete"], 1)
        self.assertTrue(any("源数据不完整" in w for w in report.warnings))
        with patch.object(check_docs, "validate", return_value=report):
            self.assertEqual(check_docs.main(["--strict-source"]), 1)
            self.assertEqual(check_docs.main([]), int(not report.ok))

    def test_empty_source_service_is_error(self):
        services = copy.deepcopy(self.services)
        services[0]["operations"] = []
        report = check_docs.Report()
        check_docs.validate_source(services, {}, report)
        self.assertTrue(any("源数据服务无接口" in e for e in report.errors))

    def test_heading_anchors_unicode_duplicates_and_fences(self):
        self.assertEqual(check_docs.heading_anchors("# 中文 标题\n## Foo\n## Foo\n```md\n# Hidden\n```\n"),
                         {"中文-标题", "foo", "foo-1"})

    def test_heading_anchors_preserve_model_underscores(self):
        text = "## QueryResult_BaseItemDto\n## Emby_Api_UserLibrary_TagItem\n## Tuple_Double-Double\n## _Emphasis_\n## [A Link](README.md)\n"
        self.assertEqual(check_docs.heading_anchors(text),
                         {"queryresult_baseitemdto", "emby_api_userlibrary_tagitem", "tuple_double-double", "emphasis", "a-link"})

    def test_default_loader_accepts_normalized_fixture(self):
        report = check_docs.validate(self.root)
        self.assertTrue(report.ok, report.errors)

    def test_corrupt_source_model_registry_rejected(self):
        path = self.root / "tools/_data/models.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["ExampleDto"]["fields"] = []
        path.write_text(json.dumps(data), encoding="utf-8")
        report = check_docs.validate(self.root)
        self.assertFalse(report.ok)
        self.assertTrue(any("源数据完整性校验失败" in error for error in report.errors))

    def test_required_flag_does_not_trust_legacy_inference(self):
        self.assertEqual(build_docs.required_flag({"in": "path"}), "是")
        self.assertEqual(build_docs.required_flag({"in": "query", "required": "required"}), "未标注")
        self.assertEqual(build_docs.required_flag({"in": "query", "required": "required", "required_source": "name_marker"}), "是")
        self.assertEqual(build_docs.required_flag({"in": "query", "notes": "Optional"}), "否")
        self.assertEqual(build_docs.required_flag({"in": "query", "notes": "Required"}), "是")

    def test_llms_mismatch_rejected(self):
        path = self.root / "llms.txt"
        path.write_text(path.read_text(encoding="utf-8") + "\n额外陈旧内容\n", encoding="utf-8")
        self.assertTrue(any("llms.txt 生成一致性" in error for error in self.validate().errors))

    def test_render_roots_restored(self):
        docs_root, ai_root = build_docs.ROOT, build_ai_index.ROOT
        self.validate()
        self.assertEqual(build_docs.ROOT, docs_root)
        self.assertEqual(build_ai_index.ROOT, ai_root)


if __name__ == "__main__":
    unittest.main()
