# -*- coding: utf-8 -*-
"""离线校验：生成一致性、快照结构完整性；不等于官方全覆盖或服务器实测。

validate() 不修改工作树，不共享错误列表。临时渲染用于检查生成漂移，另外逐表格、
端点、模型字段/枚举检查语义，避免仅有标题/数量正确的空壳文档通过。
"""
import argparse
from contextlib import contextmanager
from dataclasses import dataclass, field
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))
import build_docs
import build_ai_index
from zh_services import SVC


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    counts: dict = field(default_factory=dict)

    @property
    def ok(self):
        return not self.errors


@contextmanager
def module_root(module, root):
    """现有生成器保留文件输出接口；仅指向临时目录并保证还原。"""
    old = module.ROOT
    old_data = getattr(module, "DATA", None)
    module.ROOT = str(root)
    if old_data is not None:
        module.DATA = str(Path(root) / "tools/_data")
    try:
        yield
    finally:
        module.ROOT = old
        if old_data is not None:
            module.DATA = old_data


def load_json(path, report):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        report.errors.append("无法读取 JSON %s：%s" % (path.name, exc))
        return None


def read_text(path, report):
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        report.errors.append("缺少或无法读取文档 %s：%s" % (path, exc))
        return None


def sections(text):
    """保留小节顺序及重名，不用字典静默吞掉重复小节。"""
    matches = list(re.finditer(r"^## (.+)$", text, re.M))
    return [(m.group(1), text[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)]


def table_rows(text):
    """读取全部表格，支持生成器的转义竖线；顺序与重复项均有意义。"""
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and line.endswith("|"):
            rows.append(tuple(cell.strip().replace("\\|", "|")
                              for cell in re.split(r"(?<!\\)\|", line[1:-1])))
    return rows


def service_semantics(text):
    result = []
    for title, body in sections(text):
        if title == "接口一览" or re.match(r"\d+\. ", title):
            route = re.findall(r"^`(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)` `([^`]+)`$", body, re.M)
            auth = re.findall(r"^- \*\*权限\*\*：(.+)$", body, re.M)
            success = re.findall(r"^- \*\*成功响应\*\*：(.+)$", body, re.M)
            result.append((title, route, auth, success, table_rows(body)))
    return result


def model_semantics(text):
    return [(title, table_rows(body), re.findall(r"^\*\*枚举值\*\*：(.+)$", body, re.M))
            for title, body in sections(text)]


def validate_source(services, models, report):
    """只检查保存快照的结构，绝不据此声称实时官网全覆盖。"""
    names = set()
    incomplete = []
    for svc in services:
        name = svc["service"]
        if name in names:
            report.errors.append("源数据服务重复：" + name)
        names.add(name)
        if name not in SVC:
            report.errors.append("服务未登记中文信息：" + name)
        if not svc["operations"]:
            report.errors.append("源数据服务无接口（可能抓取失败）：" + name)
        routes = set()
        for op in svc["operations"]:
            route = (op["method"].upper(), op["path"])
            label = "%s %s %s" % (name, *route)
            if route in routes:
                report.errors.append("源数据端点重复：" + label)
            routes.add(route)
            if op.get("incomplete"):
                incomplete.append(label)
                continue
            if not op.get("responses"):
                report.errors.append("完整端点缺少响应定义：" + label)
            params = set()
            for p in op["params"]:
                key = (p["name"], p.get("in", ""))
                if key in params:
                    report.errors.append("源数据参数重复：%s %s" % (label, key))
                params.add(key)
    # 同名定义/枚举丢失由独立registry归并重建检测，不能只信任models.json。
    try:
        from model_registry import normalize_services
        _, rebuilt = normalize_services(services)
        if rebuilt != models:
            report.errors.append("源数据模型 registry 与接口定义重建结果不一致（字段/枚举/命名冲突）")
    except ImportError:
        report.warnings.append("未提供模型 registry，未执行接口定义与模型快照的独立一致性检查")
    if incomplete:
        report.warnings.append("源数据不完整：%d 个端点仅有清单信息，参数/响应未核验：%s" %
                               (len(incomplete), "；".join(incomplete)))
    report.counts.update(services=len(services), endpoints=sum(len(s["operations"]) for s in services),
                         params=sum(len(o["params"]) for s in services for o in s["operations"]),
                         models=len(models), model_fields=sum(len(m["fields"]) for m in models.values()),
                         incomplete=len(incomplete))


def compare_document(actual_path, expected_path, kind, report):
    actual = read_text(actual_path, report)
    if actual is None:
        return
    expected = expected_path.read_text(encoding="utf-8")
    parser = service_semantics if kind == "service" else model_semantics
    if parser(actual) != parser(expected):
        report.errors.append("内容语义不一致：%s（小节/方法路径/参数/响应/模型字段/枚举）" % actual_path.name)
    if actual != expected:
        report.errors.append("生成一致性不符：%s（请重新生成，不代表服务器实测失败）" % actual_path.name)


def heading_anchors(text):
    """GitHub 风格标题锚点，包括重复标题的 -1/-2 后缀；忽略 fenced code。"""
    anchors = set()
    seen = {}
    fenced = False
    fence_char = None
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            if not fenced:
                fenced, fence_char = True, fence.group(1)[0]
            elif fence.group(1)[0] == fence_char:
                fenced = False
            continue
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", title)
        # 中间的下划线是模型名的一部分，不是 Markdown 强调标记。
        title = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"\1", title)
        title = re.sub(r"[\[\]`*~]", "", title).lower()
        title = "".join(c for c in title if c.isalnum() or c in "_- ")
        anchor = title.replace(" ", "-")
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        anchors.add(anchor + ("-%d" % count if count else ""))
    return anchors


def validate_links(root, report):
    sources = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts and "_data" not in p.parts)
    if (root / "llms.txt").exists():
        sources.append(root / "llms.txt")
    cache = {}
    for source in sources:
        text = source.read_text(encoding="utf-8")
        # 排除 fenced code 中的示意链接，避免把教程代码视为导航。
        text = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            target = raw.strip()
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">")]
            else:
                target = target.split(' "', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            filename = unquote(parsed.path)
            if filename and not filename.endswith(".md"):
                continue
            path = (source.parent / filename).resolve() if filename else source.resolve()
            if not path.is_file():
                report.errors.append("断链：%s → %s" % (source.relative_to(root), raw))
                continue
            if parsed.fragment:
                if path not in cache:
                    cache[path] = heading_anchors(path.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in cache[path]:
                    report.errors.append("锚点不存在：%s → %s" % (source.relative_to(root), raw))
    report.counts["markdown"] = sum(p.suffix == ".md" for p in sources)


def validate(root=ROOT, services=None, models=None):
    root = Path(root).resolve()
    report = Report()
    if services is None and models is None:
        try:
            from dataset import load_dataset
            services, models = load_dataset(root / "tools/_data")
        except (OSError, ValueError, TypeError, KeyError) as exc:
            report.errors.append("源数据完整性校验失败：%s" % exc)
            return report
    else:
        if services is None:
            services = load_json(root / "tools/_data/services.json", report)
        if models is None:
            models = load_json(root / "tools/_data/models.json", report)
    if services is None or models is None:
        return report
    try:
        validate_source(services, models, report)
        with tempfile.TemporaryDirectory(prefix="emby-docs-check-") as tmp:
            expected_root = Path(tmp)
            (expected_root / build_docs.MODEL_DIR).mkdir()
            with module_root(build_docs, expected_root):
                models_map, _ = build_docs.render_models(models)
                for svc in services:
                    cat = build_docs.render_service(svc, models_map)
                    rel = Path(build_docs.API_DIR) / cat / (svc["service"] + ".md")
                    compare_document(root / rel, expected_root / rel, "service", report)
            for path in sorted((expected_root / build_docs.MODEL_DIR).glob("*.md")):
                compare_document(root / build_docs.MODEL_DIR / path.name, path, "model", report)
            expected_services = {s["service"] for s in services}
            actual_services = {p.stem for p in (root / build_docs.API_DIR).rglob("*.md") if p.name != "README.md"}
            if actual_services != expected_services:
                report.errors.append("服务文档集合不一致（缺失/多余）：%s" % sorted(actual_services ^ expected_services))
            with module_root(build_ai_index, root):
                expected_index = build_ai_index.build(services, models)
                expected_llms = build_ai_index.write_llms(expected_index)
            actual_index = load_json(root / "index.json", report)
            if actual_index is not None and actual_index != expected_index:
                report.errors.append("index.json 详细内容不一致（计数/服务/路径/小节/参数数/模型/约定）")
            actual_llms = read_text(root / "llms.txt", report)
            if actual_llms is not None and actual_llms != expected_llms:
                report.errors.append("llms.txt 生成一致性不符")
        validate_links(root, report)
    except (OSError, KeyError, TypeError, ValueError, AttributeError) as exc:
        report.errors.append("源数据结构或生成接口异常：%s: %s" % (type(exc).__name__, exc))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--strict-source", action="store_true", help="源快照含 incomplete 端点时也返回失败")
    args = parser.parse_args(argv)
    report = validate(args.root)
    for key, value in report.counts.items():
        print("%s: %s" % (key, value))
    for warning in report.warnings:
        print("[警告] " + warning)
    for error in report.errors:
        print("[错误] " + error)
    failed = not report.ok or (args.strict_source and report.counts.get("incomplete", 0) > 0)
    print("生成一致性/快照结构校验：%s（错误 %d，警告 %d）" %
          ("未通过" if failed else "通过", len(report.errors), len(report.warnings)))
    print("范围说明：本命令不证明实时官方全覆盖，也未进行 Emby 服务器实测。")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
