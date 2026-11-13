# -*- coding: utf-8 -*-
"""Generate English AI entry points while preserving official source text.

README.md and linked Markdown pages remain Chinese human-facing documentation.
Run: python3 tools/build_ai_index.py
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from zh_services import SVC
from dataset import load_dataset, snapshot_metadata
from build_docs import classify, MODEL_FILES as MODEL_CATEGORIES

DATA = os.path.join(ROOT, "tools", "_data")
API_DIR = "01-接口参考"
MODEL_DIR = "02-数据模型"
CATEGORIES = {
    "01": "Users and authentication",
    "02": "Library browsing",
    "03": "Library maintenance",
    "04": "Playback and synchronization",
    "05": "Streaming protocols",
    "06": "Images and subtitles",
    "07": "Live TV",
    "08": "System and administration",
    "09": "DLNA",
}
BASE_DOCS = [
    ("00-基础/01-快速开始.md", "Quick start", "Server URL, login, item lists, and playback URLs"),
    ("00-基础/02-认证与鉴权.md", "Authentication", "Authorization headers, tokens, API keys, and user policies"),
    ("00-基础/03-通用约定与响应格式.md", "Conventions", "Ticks, pagination, Fields, image URLs, and BaseItemDto"),
    ("00-基础/04-错误与排查.md", "Troubleshooting", "HTTP errors and playback troubleshooting"),
    ("00-基础/05-常用接口速查表.md", "Task-based API lookup", "Find endpoints by task"),
]
DEMOS = [
    ("03-实战示例/01-从登录到播放.md", "Login to playback", "Browser integration snippets; not a server-tested complete player"),
    ("03-实战示例/02-图片与列表页优化.md", "Images and lists", "Image sizing, caching, and pagination"),
    ("03-实战示例/03-远程控制与投屏.md", "Remote control", "Sessions, capabilities, and playback commands"),
]
CONVENTIONS = {
    "base_url": "http://<host>:8096 (HTTPS commonly uses port 8920; deployments may differ)",
    "auth_header": 'X-Emby-Authorization: Emby Client="...", Device="...", DeviceId="...", Version="..." [, UserId="...", Token="..."]',
    "token_header": "X-Emby-Token: <AccessToken>",
    "login": "POST /Users/AuthenticateByName with {Username, Pw}; response includes AccessToken, User, SessionInfo, ServerId",
    "tick": "1 second = 10,000,000 ticks; *Ticks fields use this unit",
    "paging": "QueryResult commonly contains Items and TotalRecordCount; consult each endpoint for StartIndex and Limit",
    "fields": "Use Fields to request supported optional item fields; do not assume list responses contain full item details",
    "image": "GET /Items/{Id}/Images/{Type}?tag={Tag}&maxHeight={h}; use ImageTags[Type] when present, otherwise a placeholder",
    "case": "Preserve the exact case of JSON field names (usually PascalCase)",
    "missing_type": "An empty source type is unknown. Chinese parameter tables may show name-based hints, not verified source types",
    "required": "Trust name_marker, explicit notes, or sourced verification. Unknown/unspecified does not mean optional",
}


def short_auth(op):
    auth = (op.get("auth") or "").lower()
    if "admin" in auth:
        return "administrator"
    return "user" if auth else "unspecified"


def build(services, models):
    service_meta = []
    for svc in sorted(services, key=lambda item: item["service"]):
        name = svc["service"]
        category = SVC[name][0]
        service_meta.append({
            "service": name,
            "category": CATEGORIES.get(category.split("-", 1)[0], category),
            "file": "%s/%s/%s.md" % (API_DIR, category, name),
            "endpoint_count": len(svc["operations"]),
            "doc": svc["url"],
            "endpoints": [
                {
                    "section": i,
                    "method": op["method"].upper(),
                    "path": op["path"],
                    "title": op.get("summary") or "%s %s" % (op["method"].upper(), op["path"]),
                    "auth": short_auth(op),
                    "params": len(op["params"]),
                    "incomplete": bool(op.get("incomplete")),
                    "doc": op.get("doc_url", ""),
                }
                for i, op in enumerate(svc["operations"], 1)
            ],
        })
    return {
        "meta": {
            "project": "EmbyRestApiDocs",
            "language": "en",
            "human_docs_language": "zh-CN",
            "source": "https://dev.emby.media/reference/RestAPI.html",
            "counts": {
                "services": len(services),
                "endpoints": sum(len(s["operations"]) for s in services),
                "params": sum(len(op["params"]) for s in services for op in s["operations"]),
                "models": len(models),
                "model_fields": sum(len(m.get("fields", [])) for m in models.values()),
            },
            "conventions": CONVENTIONS,
            "snapshot": snapshot_metadata(DATA),
            "source_data": {"services": "tools/_data/services.json", "models": "tools/_data/models.json"},
            "usage": "Search services[].endpoints by path/method. Open file and find heading '## <section>. ' for the Chinese reference, or read source_data for untranslated parameter and model definitions. Endpoint titles retain official summaries when available.",
        },
        "services": service_meta,
        "models": {
            name: {"file": "%s/%s" % (MODEL_DIR, MODEL_CATEGORIES[classify(name)][0]),
                   "fields": len(model.get("fields", [])), "enum": len(model.get("enum", []))}
            for name, model in sorted(models.items())
        },
    }


def write_llms(index):
    counts = index["meta"]["counts"]
    lines = [
        "# Emby REST API reference", "",
        "> Community-maintained reference based on https://dev.emby.media/reference/RestAPI.html. "
        "This AI entry point is English; linked human-facing Markdown remains Chinese.", "",
        "Snapshot: {services} services, {endpoints} endpoints, {params} parameter entries, "
        "{models} models, and {model_fields} model fields.".format(**counts), "",
        "## Machine-readable source data", "",
        "- [index.json](index.json): endpoint navigation, official summaries, source URLs, model locations, and provenance.",
        "- [services.json](tools/_data/services.json): untranslated endpoint descriptions, parameter tables, responses, and model definitions. This is documentation data, not a server response or an OpenAPI schema.",
        "- [models.json](tools/_data/models.json): canonical model fields, enum values, source identities, and conflicting type candidates.",
        "- [metadata.json](tools/_data/metadata.json): crawl timestamp, source response hashes, and optional raw archive filenames.", "",
        "## How to look up an endpoint", "",
        "1. Search index.json services[].endpoints by method and path.",
        "2. Read services.json for original English text and exact parameter metadata. Keep unknown values unknown.",
        "3. For the Chinese reference, open the endpoint's service file and find heading '## <section>. '.",
        "4. Look up canonical model names in models.json; do not confuse QueryResult wrappers with entities.", "",
        "## Conventions", "",
    ]
    lines.extend("- %s: %s" % item for item in index["meta"]["conventions"].items())
    lines += ["", "## Getting started (Chinese pages)", ""]
    lines.extend("- [%s](%s): %s" % (label, path, description) for path, label, description in BASE_DOCS)
    lines += ["", "## Examples (Chinese pages)", ""]
    lines.extend("- [%s](%s): %s" % (label, path, description) for path, label, description in DEMOS)
    lines += ["", "## Service references (Chinese pages)", ""]
    categories = {}
    for service in index["services"]:
        categories.setdefault(service["category"], []).append(service)
    for category, services in sorted(categories.items()):
        lines += ["### " + category, ""]
        lines.extend("- [%s](%s): %d endpoints; [official source](%s)" %
                     (s["service"], s["file"], s["endpoint_count"], s["doc"]) for s in services)
        lines.append("")
    lines += [
        "## Models", "",
        "- [Model index](%s/00-模型索引.md): %d canonical models, including enums (Chinese page)." % (MODEL_DIR, counts["models"]), "",
        "## Regenerate and validate", "", "```text",
        "python3 tools/build_ai_index.py   # Generate llms.txt and index.json",
        "python3 tools/build_docs.py       # Generate Chinese service/model references and directories",
        "python3 tools/check_docs.py       # Check snapshot, tables, links, and indexes",
        "```", "", "## Known limitations", "",
        "- Endpoints marked incomplete have unknown parameters/responses, not necessarily no parameters. Current allowlisted BackupApi detail pages return HTTP 404.",
        "- Scalar/array type conflicts remain explicit candidates; neither interpretation is guaranteed for a target server version.",
        "- Crawl timestamps and response hashes identify the source snapshot, not the supported Emby Server version.",
        "- Offline consistency checks do not prove real-server behavior or exhaustive live coverage. This is not an official release.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def main():
    services, models = load_dataset(DATA)
    index = build(services, models)
    with io.open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    with io.open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8", newline="\n") as stream:
        stream.write(write_llms(index))
    print("index.json: %d services / %d endpoints" % (len(index["services"]), index["meta"]["counts"]["endpoints"]))
    print("llms.txt: %d lines" % len(write_llms(index).splitlines()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
