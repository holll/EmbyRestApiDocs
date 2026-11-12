# -*- coding: utf-8 -*-
"""为「机器/AI 阅读」生成两个入口文件：

- llms.txt   ：llmstxt.org 约定的纯文本索引，一屏内交代清楚项目结构、约定与每个服务的入口
- index.json ：完整的机器可读目录（服务 → 文件路径 + 逐接口 method/path/标题/权限 + 模型）

README.md 面向人类读者，这两个文件面向 AI 与脚本。重新生成：
    python tools\\build_ai_index.py
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from zh_ops import OP_TITLE, PATH_TITLE, SUM  # noqa: E402
from zh_services import SVC  # noqa: E402

DATA = os.path.join(ROOT, "tools", "_data")
API_DIR = "01-接口参考"
MODEL_DIR = "02-数据模型"
MODEL_FILES = ["01-通用结构.md", "02-媒体条目.md", "03-用户与账号.md",
               "04-播放与转码.md", "05-直播电视.md", "06-系统与配置.md"]
BASE_DOCS = [
    ("00-基础/01-快速开始.md", "快速开始：找到服务器、登录、拉列表、取播放地址"),
    ("00-基础/02-认证与鉴权.md", "认证头 X-Emby-Authorization、令牌传递、API Key、UserPolicy"),
    ("00-基础/03-通用约定与响应格式.md", "tick、QueryResult 分页、Fields 白名单、图片 URL、BaseItemDto"),
    ("00-基础/04-错误与排查.md", "400/401/403/404/500 对照表与播放类问题排查"),
    ("00-基础/05-常用接口速查表.md", "按「要做什么」组织的接口清单，最省的查法"),
]
DEMOS = [
    ("03-实战示例/01-从登录到播放.md", "完整链路代码：登录 → 视图 → 列表 → 详情 → 播放 → 进度上报"),
    ("03-实战示例/02-图片与列表页优化.md", "图片 URL 拼法、尺寸阶梯、缓存与分页策略"),
    ("03-实战示例/03-远程控制与投屏.md", "会话发现、Capabilities 上报、下发播放命令、投屏"),
]
CONVENTIONS = {
    "base_url": "http://<host>:8096 (HTTPS 8920)",
    "auth_header": "X-Emby-Authorization: Emby Client=\"…\", Device=\"…\", DeviceId=\"…\", Version=\"…\" [, UserId=\"…\", Token=\"…\"]",
    "token_header": "X-Emby-Token: <AccessToken>",
    "login": "POST /Users/AuthenticateByName  body {Username, Pw} → {AccessToken, User, SessionInfo, ServerId}",
    "tick": "1 秒 = 10,000,000 ticks；所有 *Ticks 字段（RunTimeTicks / PositionTicks / StartTimeTicks）均为此单位",
    "paging": "QueryResult {Items, TotalRecordCount, StartIndex}；参数 StartIndex + Limit",
    "fields": "列表接口默认不返回 MediaSources/MediaStreams/People/Overview，需要时用 Fields 显式索取",
    "image": "GET /Items/{Id}/Images/{Type}?tag={Tag}&maxHeight={h}；无 PrimaryImageTag 时不要拼 URL",
    "case": "JSON 字段名 PascalCase，按原样大小写匹配",
    "missing_type": "参数表类型列为官方缺失时按命名惯例推断，仅供参考",
}


def zh_title(service, op):
    key = (service, op["method"], op["path"])
    if key in PATH_TITLE:
        return PATH_TITLE[key]
    s = (op["summary"] or "").strip()
    if s and s in SUM:
        return SUM[s]
    if s:
        return s
    if key in OP_TITLE:
        return OP_TITLE[key]
    return op["name"]


def short_auth(op):
    a = (op.get("auth") or "").lower()
    if "admin" in a:
        return "管理员"
    if a:
        return "用户"
    return "未标注"


def build(services, models):
    # 服务 → 分类 / 中文名
    svc_meta = {}
    for svc in services:
        name = svc["service"]
        cat, zh, intro = SVC[name]
        svc_meta[name] = {
            "service": name,
            "zh": zh,
            "category": cat,
            "file": "%s/%s/%s.md" % (API_DIR, cat, name),
            "endpoint_count": len(svc["operations"]),
            "doc": svc["url"],
            "intro": intro,
            "endpoints": [
                {
                    "section": i,
                    "method": op["method"].upper(),
                    "path": op["path"],
                    "title": zh_title(name, op),
                    "auth": short_auth(op),
                    "params": len(op["params"]),
                }
                for i, op in enumerate(svc["operations"], 1)
            ],
        }

    model_meta = {}
    for fn in MODEL_FILES:
        p = os.path.join(ROOT, MODEL_DIR, fn)
        if not os.path.exists(p):
            continue
        text = io.open(p, encoding="utf-8").read()
        import re
        names = re.findall(r"^## ([\w\-\.]+)$", text, re.M)
        for n in names:
            m = models.get(n, {})
            model_meta[n] = {
                "file": "%s/%s" % (MODEL_DIR, fn),
                "fields": len(m.get("fields", [])),
                "enum": len(m.get("enum", [])),
            }

    index = {
        "meta": {
            "project": "EmbyRestApiDocs",
            "source": "https://dev.emby.media/reference/RestAPI.html",
            "counts": {
                "services": len(services),
                "endpoints": sum(len(s["operations"]) for s in services),
                "params": sum(len(op["params"]) for s in services for op in s["operations"]),
                "models": len(models),
                "model_fields": sum(len(m.get("fields", [])) for m in models.values()),
            },
            "conventions": CONVENTIONS,
            "usage": "按 path 或 method 在 services[].endpoints 中检索可定位服务文件与 section 序号；"
                     "打开对应 md 后搜索「## <section>. 」即可命中该接口的完整参数表。",
        },
        "services": [svc_meta[n] for n in sorted(svc_meta)],
        "models": {n: model_meta[n] for n in sorted(model_meta)},
    }
    return index


def write_llms(index):
    lines = []
    lines.append("# Emby REST API 中文速查手册")
    lines.append("")
    lines.append("> 官方 Emby Server REST API（https://dev.emby.media/reference/RestAPI.html）的中文逐接口参考，"
                 "面向要自己写 Emby 第三方客户端的开发者。")
    lines.append("")
    lines.append("覆盖 %d 个服务（Controller）、%d 个接口、%d 个参数条目、%d 个数据模型（%d 个字段）。"
                 "README.md 是给人看的总目录；本文件与 index.json 是给 AI / 脚本用的入口。" %
                 (index["meta"]["counts"]["services"], index["meta"]["counts"]["endpoints"],
                  index["meta"]["counts"]["params"], index["meta"]["counts"]["models"],
                  index["meta"]["counts"]["model_fields"]))
    lines.append("")
    lines.append("怎么查最省事：")
    lines.append("1. 先看「速查表」，按任务找到要调哪几个接口；")
    lines.append("2. 需要精确字段时读对应服务页，每个接口都有独立小节（方法 / 路径 / 权限 / 参数表 / 响应码 / 涉及模型）；")
    lines.append("3. 参数结构与字段含义查「模型索引」；")
    lines.append("4. 需要程序化定位接口，用 index.json（services[].endpoints 里有 method / path / title / section）。")
    lines.append("")
    lines.append("## 关键约定（读接口前必看）")
    lines.append("")
    for k in ("base_url", "auth_header", "token_header", "login", "tick", "paging", "fields", "image", "case", "missing_type"):
        lines.append("- %s：%s" % (k, index["meta"]["conventions"][k]))
    lines.append("")
    lines.append("## 入门（先读这 5 篇）")
    lines.append("")
    for p, d in BASE_DOCS:
        lines.append("- [%s](%s)：%s" % (os.path.basename(p)[:-3], p, d))
    lines.append("")
    lines.append("## 实战示例")
    lines.append("")
    for p, d in DEMOS:
        lines.append("- [%s](%s)：%s" % (os.path.basename(p)[:-3], p, d))
    lines.append("")
    lines.append("## 接口参考（按分类 → 服务）")
    lines.append("")
    cats = {}
    for s in index["services"]:
        cats.setdefault(s["category"], []).append(s)
    for cat in sorted(cats):
        lines.append("### %s" % cat.split("-", 1)[-1])
        lines.append("")
        for s in cats[cat]:
            intro = s["intro"]
            if len(intro) > 42:
                intro = intro[:42].rstrip("，。；") + "…"
            lines.append("- [%s](%s)：%s（%d 个接口）" % (s["zh"], s["file"], intro, s["endpoint_count"]))
        lines.append("")
    lines.append("## 数据模型")
    lines.append("")
    lines.append("- [模型索引](%s/00-模型索引.md)：全部 %d 个模型（含枚举）的总索引，按分类给出文件与锚点"
                 % (MODEL_DIR, index["meta"]["counts"]["models"]))
    lines.append("")
    lines.append("## 机器可读索引")
    lines.append("")
    lines.append("- [index.json](index.json)：服务 → 文档路径 + 逐接口 method/path/标题/权限/小节序号；"
                 "附 321 个模型的文件位置与字段数，可直接程序化检索。")
    lines.append("")
    lines.append("## 再生成与校验")
    lines.append("")
    lines.append("```text")
    lines.append("python tools\\build_ai_index.py   # 生成本文件与 index.json")
    lines.append("python tools\\build_docs.py       # 重新生成接口/模型/README/进度清单")
    lines.append("python tools\\check_docs.py       # 校验覆盖率、参数表、断链、未打钩项")
    lines.append("```")
    lines.append("")
    lines.append("## 已知边界")
    lines.append("")
    lines.append("- BackupApi 的 3 个接口官方站无详情页，参数以服务器实际实现为准（文档内已标注）。")
    lines.append("- 模型表说明列的 `—` 表示官方未提供该字段说明；`（原文）` 开头为保留的官方英文原文。")
    lines.append("- 接口行为随 Emby 版本变化，以实际请求结果为准；本文档为社区整理，非官方发布。")
    return "\n".join(lines).rstrip() + "\n"


def main():
    services = json.load(io.open(os.path.join(DATA, "services.json"), encoding="utf-8"))
    models = json.load(io.open(os.path.join(DATA, "models.json"), encoding="utf-8"))
    index = build(services, models)

    with io.open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

    with io.open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(write_llms(index))

    print("index.json：%d 服务 / %d 接口" % (len(index["services"]),
                                        sum(len(s["endpoints"]) for s in index["services"])))
    print("llms.txt：%d 行" % len(write_llms(index).splitlines()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
