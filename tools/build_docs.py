# -*- coding: utf-8 -*-
"""根据抓取结果 + 中文词表生成整本手册。

运行: python tools/build_docs.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "_data")
sys.path.insert(0, HERE)

from zh_notes import NOTE, PNOTE_EMPTY, PNOTE_OVERRIDE  # noqa: E402
from zh_ops import OP_TITLE, PATH_TITLE, SUM  # noqa: E402
from zh_services import SVC  # noqa: E402
from zh_model import tr_field  # noqa: E402
from dataset import load_dataset, snapshot_metadata  # noqa: E402

API_DIR = "01-接口参考"
MODEL_DIR = "02-数据模型"

STATUS = {
    "400": "请求无法被服务器处理",
    "401": "未认证，或令牌已失效",
    "403": "已认证但无权限执行该操作",
    "404": "资源不存在或不可用",
    "500": "服务器内部错误",
}

PATH_NOTE = {
    "Id": "条目 ID",
    "UserId": "用户 ID",
    "ItemId": "条目 ID",
    "Name": "名称（需 URL 编码）",
    "Type": "图片类型（Primary / Backdrop / Logo / Thumb / Banner / Art / Disc / Box / Screenshot 等）",
    "Index": "序号，从 0 开始",
    "Tag": "缓存标记，取图片信息中的 Tag 值",
    "Format": "图片格式（original / gif / jpg / png）",
    "MaxWidth": "最大宽度",
    "MaxHeight": "最大高度",
    "PercentPlayed": "已播放百分比",
    "UnPlayedCount": "未播放集数",
    "PlaylistId": "播放列表 ID",
    "SegmentId": "分片序号",
    "SegmentContainer": "分片封装格式",
    "Language": "语言代码（如 chi、eng）",
    "SubtitleId": "字幕 ID",
    "Key": "API 密钥",
    "SeriesId": "剧集（series）ID",
    "SeasonId": "季 ID",
    "TimerId": "定时器 ID",
    "ChannelId": "频道 ID",
    "ProviderId": "提供方 ID",
    "SectionId": "首页分区 ID",
    "Command": "命令名，如 PlayPause / Pause / Unpause / Stop / Seek / NextTrack / VolumeUp",
    "TrackType": "轨道类型（Audio / Subtitle）",
    "SearchProviderName": "元数据提供方名称",
    "TargetId": "同步目标（设备）ID",
    "MediaSourceId": "媒体源 ID（不确定时可用 - 占位）",
    "DeviceId": "设备 ID",
    "CollectionType": "媒体库类型（movies / tvshows / music / books / photos）",
    "Id_": "标识",
}

MODEL_FILES = {
    "general": ("01-通用结构.md", "通用结构"),
    "media": ("02-媒体条目.md", "媒体条目"),
    "user": ("03-用户与账号.md", "用户与账号"),
    "play": ("04-播放与转码.md", "播放与转码"),
    "live": ("05-直播电视.md", "直播电视"),
    "system": ("06-系统与配置.md", "系统与配置"),
}


def anchor(name):
    s = re.sub(r"[^\w\s-]", "", name)
    return s.strip().lower().replace(" ", "-")


def classify(name):
    if name.startswith("QueryResult"):
        return "general"
    keys = {
        "live": ["LiveTv", "Timer", "Channel", "Tuner", "Listing", "Guide",
                 "Recording", "Program", "SeriesTimer", "Epg"],
        "user": ["User", "Session", "Auth", "Connect", "Device",
                 "DisplayPreferences", "Notification", "Activity", "Log"],
        "play": ["Sync", "Playback", "Player", "Play", "Transcod", "Encoding",
                 "Profile", "Subtitle", "Audio", "Video", "Stream", "Hls",
                 "Codec", "ToneMap", "Ffmpeg", "Bitrate"],
        "media": ["Item", "Media", "Person", "Studio", "Genre", "Collection",
                  "Playlist", "Chapter", "Image", "Thumbnail", "Provider",
                  "Editor", "Condition", "Content", "Query", "Search",
                  "Metadata", "External", "Marker", "Book", "Music", "Album",
                  "Artist", "Folder", "Trailer", "Tag", "Task"],
    }
    for bucket in ("live", "user", "play", "media"):
        for k in keys[bucket]:
            if k in name:
                return bucket
    return "system"


def zh_note(note, pname=""):
    if pname and pname in PNOTE_OVERRIDE:
        return PNOTE_OVERRIDE[pname]
    if note and note in NOTE:
        return NOTE[note]
    if pname and pname in PNOTE_EMPTY:
        return PNOTE_EMPTY[pname]
    if note:
        if re.match(r"^[\w`\.]+\:$", note):
            return "请求体：`%s` 对象。" % note[:-1]
        if re.match(r"^[A-Z][A-Za-z0-9]+$", note):
            return "请求体：`%s` 对象。" % note
        return "（原文）" + note
    return "—"


def zh_title(service, op):
    key = (service, op["method"], op["path"])
    if key in PATH_TITLE:
        return PATH_TITLE[key]
    s = op["summary"].strip()
    if s and s in SUM:
        return SUM[s]
    if s:
        return "（原文）" + s
    key = (service, op["method"], op["path"])
    if key in OP_TITLE:
        return OP_TITLE[key]
    return op["name"]


def uniq_titles(service_ops):
    """同一服务内摘要重名时，用路径末段做区分，避免一览表里多行同名。"""
    base = [zh_title("", o) for o in service_ops]
    out = []
    seen = {}
    for o, t in zip(service_ops, base):
        seg = [p for p in o["path"].split("/") if p and not p.startswith("{")]
        hint = seg[-1] if seg else o["method"].upper()
        out.append(t)
        seen[t] = seen.get(t, 0) + 1
    final = []
    for o, t in zip(service_ops, base):
        if seen[t] > 1:
            seg = [p for p in o["path"].split("/") if p and not p.startswith("{")]
            hint = seg[-1] if seg else o["method"].upper()
            final.append("%s（%s）" % (t, hint))
        else:
            final.append(t)
    return final


def zh_resp(op, r):
    if r["status"] == "200":
        if "Empty response" in r["description"]:
            return "成功，无返回内容"
        t = clean_type(r["type"])
        if t:
            return "成功，返回 `%s`" % t
        return "成功"
    d = r["description"].strip()
    if r["status"] in STATUS:
        extra = ""
        if d and d not in ("Bad Request. Server cannot process request.",
                           "Unauthorized. Client needs to authenticate.",
                           "Forbidden. No permission for the reqested operation.",
                           "Resource not found or unavailable.",
                           "Server error."):
            extra = "（%s）" % d
        return STATUS[r["status"]] + extra
    return d or "—"


def clean_type(t):
    t = (t or "").strip()
    t = re.sub(r"\s+", " ", t)
    return t


def auth_text(op, short=False):
    a = (op.get("auth") or "").lower()
    if "admin" in a:
        return "管理员" if short else "管理员令牌"
    if a:
        return "用户" if short else "用户令牌"
    return "未标注" if short else "未标注（按接口语义判断）"


def guess_type(name, loc):
    """官方文档未给出类型时按命名惯例推断（仅用于展示，避免整列空白）。"""
    if re.match(r"^(Is|Has|Enable|Disable|Supports|Can|Allow|Recursive|Static|Auto)", name):
        return "boolean"
    if re.search(r"(Limit|StartIndex|Index|Count|Year|Width|Height|BitRate|Channels|Number|Ticks|Position|Percent|Volume|Quality|Size|Level)", name):
        return "integer"
    return "string"


def required_flag(p):
    loc = (p.get("in") or "").lower()
    note = (p.get("notes") or "").strip()
    if loc == "path":
        return "是"
    if note.lower().startswith("required"):
        return "是"
    if note.lower().startswith("optional"):
        return "否"
    # 旧抓取器把所有未注明 Optional 的参数都判成 required，不能据此宣称必填。
    if p.get("required_source") in ("name_marker", "notes", "verified"):
        return {"required": "是", "optional": "否"}.get(p.get("required"), "未标注")
    return "未标注"


def path_note(path, name):
    """按路径上下文补全路径参数的中文含义。"""
    if name == "Id":
        if "/Users/" in path:
            return "用户 ID"
        if "/Sessions/" in path:
            return "会话 ID"
        return "条目 ID"
    if name == "Name":
        for seg, label in (("/Artists/", "艺术家名称"), ("/MusicGenres/", "音乐类型名称"),
                           ("/GameGenres/", "游戏类型名称"), ("/Genres/", "类型名称"),
                           ("/Persons/", "人物名称"), ("/Studios/", "工作室名称")):
            if seg in path:
                return label + "（需 URL 编码）"
        return "名称（需 URL 编码）"
    return PATH_NOTE.get(name, "路径参数")


def path_params(op):
    """补齐路径中的占位参数。"""
    have = {p["name"] for p in op["params"] if (p.get("in") or "").lower() == "path"}
    extra = []
    for name in re.findall(r"\{([^}]+)\}", op["path"]):
        if name in have:
            continue
        extra.append({
            "name": name,
            "in": "path",
            "type": "string",
            "required": "required",
            "default": "",
            "notes": "",
            "_zh": path_note(op["path"], name),
        })
    return extra


def esc(t):
    return t.replace("|", "\\|")


def render_service(svc, models_map):
    s = svc["service"]
    cat, cname, intro = SVC.get(s, ("08-系统与运维", s, "（暂无概述）"))
    ops = svc["operations"]
    lines = []
    lines.append("# %s %s\n" % (s, cname))
    lines.append("> 官方文档：<%s> ｜ 上级目录：[%s](README.md) ｜ [返回总目录](../../README.md)\n" % (
        svc["url"], cname))
    lines.append("## 概述\n")
    lines.append(intro + "\n")
    lines.append("- 接口数量：**%d**" % len(ops))
    lines.append("- 收录范围：当前官方文档快照中的 %d 个端点；不代表已逐接口实机验证。" % len(ops))
    lines.append("")
    lines.append("## 接口一览\n")
    lines.append("| # | 方法 | 路径 | 说明 | 权限 |")
    lines.append("|---:|---|---|---|---|")
    titles = [zh_title(s, op) for op in ops]
    for i, op in enumerate(ops, 1):
        lines.append("| %d | `%s` | `%s` | %s | %s |" % (
            i, op["method"].upper(), esc(op["path"]), esc(titles[i - 1]), auth_text(op, True)))
    lines.append("")

    for i, op in enumerate(ops, 1):
        lines.append("---\n")
        lines.append("## %d. %s\n" % (i, titles[i - 1]))
        lines.append("`%s` `%s`\n" % (op["method"].upper(), op["path"]))
        lines.append("- **权限**：%s" % auth_text(op))
        ok = [r for r in op["responses"] if r["status"] == "200"]
        if ok:
            t = clean_type(ok[0]["type"])
            if t:
                lines.append("- **成功响应**：`200` → `%s`" % t)
            elif "Empty" in ok[0]["description"]:
                lines.append("- **成功响应**：`200`（无返回内容）")
            elif op["method"].upper() in ("GET", "HEAD"):
                lines.append("- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）")
            else:
                lines.append("- **成功响应**：`200`（无返回内容，动作类接口）")
        if op.get("incomplete"):
            lines.append("- **注意**：本次快照未取得可解析的详情，可能是上游缺页、网络或解析失败；参数和响应未知，不可据此认定无参数。")
        lines.append("")

        desc = op.get("description") or ""
        desc = re.sub(r"Requires authentication as \w+", "", desc).strip()
        if desc:
            lines.append("> %s\n" % desc)

        params = op["params"] + path_params(op)
        if params:
            lines.append("**请求参数**\n")
            lines.append("| 参数 | 位置 | 类型 | 必填 | 说明 |")
            lines.append("|---|---|---|---|---|")
            for p in params:
                t = clean_type(p["type"]) or guess_type(p["name"], p.get("in", ""))
                req = required_flag(p)
                if p.get("in") == "path" and not (p.get("notes") or "").strip():
                    zh = path_note(op["path"], p["name"])
                else:
                    zh = p.get("_zh") or zh_note(p.get("notes", ""), p["name"])
                defv = p.get("default", "")
                if defv and defv.lower() not in ("optional", "required"):
                    zh += "（默认 `%s`）" % defv
                lines.append("| `%s` | %s | %s | %s | %s |" % (
                    esc(p["name"]), p.get("in", ""), esc(t), req, esc(zh)))
            lines.append("")
        elif op.get("incomplete"):
            lines.append("请求参数未知：当前快照未取得详情。\n")
        else:
            lines.append("该接口无请求参数。\n")

        if op["responses"]:
            lines.append("**响应**\n")
            lines.append("| 状态码 | 说明 |")
            lines.append("|---|---|")
            for r in op["responses"]:
                lines.append("| %s | %s |" % (r["status"], esc(zh_resp(op, r))))
            lines.append("")

        defs = [d["name"] for d in op["definitions"] if d["name"]]
        # 只保留与本次调用直接相关的模型：响应类型 + 请求体类型
        keep = []
        for r in op["responses"]:
            t = clean_type(r["type"])
            if t and t in defs and t not in keep:
                keep.append(t)
        for p in op["params"]:
            t = clean_type(p["type"])
            if (p.get("in") in ("body", "form")) and t and t in defs and t not in keep:
                keep.append(t)
        if not keep:
            keep = defs[:2]
        if keep:
            lines.append("**涉及的数据模型**\n")
            parts = []
            for d in keep:
                if d in models_map:
                    fn = models_map[d]
                    parts.append("[`%s`](../../%s/%s#%s)" % (d, MODEL_DIR, fn, anchor(d)))
                else:
                    parts.append("`%s`" % d)
            lines.append("、".join(parts) + "\n")
            rest = len(defs) - len(keep)
            if rest > 0:
                lines.append("> 该接口在官方文档中还引用了 %d 个辅助模型，可在 [模型索引](../../%s/00-模型索引.md) 中按名称查找。\n" % (rest, MODEL_DIR))

    out_dir = os.path.join(ROOT, API_DIR, cat)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, s + ".md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    return cat


def render_models(models):
    models_map = {}
    buckets = {k: [] for k in MODEL_FILES}
    for name in sorted(models):
        buckets[classify(name)].append(name)
    for k, names in buckets.items():
        fn, title = MODEL_FILES[k]
        for n in names:
            models_map[n] = fn

    index = []
    index.append("# 数据模型索引\n")
    index.append("> [返回总目录](../README.md)\n")
    index.append("本索引收录当前快照中的 **%d** 个数据模型（含枚举）；同名不同身份已消歧，冲突类型保留候选并标注。" % len(models))
    index.append("服务文档中的“涉及的数据模型”一节点击即跳到对应条目。\n")
    for k in MODEL_FILES:
        fn, title = MODEL_FILES[k]
        index.append("## %s（%d 个）\n" % (title, len(buckets[k])))
        index.append("| 模型 | 字段/枚举值 | 文档 |")
        index.append("|---|---|---|")
        for n in buckets[k]:
            m = models[n]
            cnt = "%d 字段" % len(m["fields"]) if m["fields"] else (
                "%d 枚举值" % len(m["enum"]) if m["enum"] else "—")
            index.append("| `%s` | %s | [查看](%s#%s) |" % (n, cnt, fn, anchor(n)))
        index.append("")
    with open(os.path.join(ROOT, MODEL_DIR, "00-模型索引.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index).rstrip() + "\n")

    for k, names in buckets.items():
        fn, title = MODEL_FILES[k]
        lines = ["# %s\n" % title,
                 "> [返回模型索引](00-模型索引.md) ｜ [返回总目录](../README.md)\n",
                 "共 %d 个模型。字段名保持与 Emby 返回的 JSON 一致（PascalCase），说明为中文。\n" % len(names),
                 "> 说明列的约定：`—` 表示官方文档未提供该字段说明（Emby 约三分之一的字段本身无说明），"
                 "`（原文）` 开头表示官方英文原文无法用规则稳定翻译、直接保留以便对照。\n"]
        for n in names:
            m = models[n]
            lines.append("## %s\n" % n)
            if m.get("description") and "see also" not in m["description"]:
                lines.append("%s\n" % m["description"])
            if m["enum"]:
                lines.append("**枚举值**：%s\n" % "、".join("`%s`" % x for x in m["enum"]))
            if m["fields"]:
                lines.append("| 字段 | 类型 | 说明 |")
                lines.append("|---|---|---|")
                for f in m["fields"]:
                    t = clean_type(f["type"]) or "—"
                    note = tr_field(f["notes"], f["name"])
                    if f.get("type_status") == "source_conflict":
                        note += "（官方快照不同位置的类型冲突，候选均保留，待按服务器版本核验）"
                    lines.append("| `%s` | %s | %s |" % (
                        f["name"], esc(t), esc(note)))
                lines.append("")
            if not m["enum"] and not m["fields"]:
                lines.append("（该模型在官方文档中无字段明细。）\n")
        with open(os.path.join(ROOT, MODEL_DIR, fn), "w", encoding="utf-8") as f:
            f.write("\n".join(lines).rstrip() + "\n")
    return models_map, buckets


def render_category_readme(cats, services):
    for cat in sorted(cats):
        names = [s["service"] for s in services if SVC.get(s["service"], ("",))[0] == cat]
        title = SVC.get(names[0], ("", cat))[1] if names else cat
        lines = ["# %s\n" % cat.split("-", 1)[-1],
                 "> [返回总目录](../../README.md)\n",
                 "| 服务 | 中文名 | 接口数 | 说明 |",
                 "|---|---|---|---|"]
        for s in services:
            sv = s["service"]
            if SVC.get(sv, ("",))[0] != cat:
                continue
            _, cn, intro = SVC[sv]
            short = intro.split("：")[0][:40]
            lines.append("| [%s](%s.md) | %s | %d | %s |" % (sv, sv, cn, len(s["operations"]), short))
        with open(os.path.join(ROOT, API_DIR, cat, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines).rstrip() + "\n")


def render_readme(services, cats, models):
    total_ops = sum(len(s["operations"]) for s in services)
    total_params = sum(len(o["params"]) for s in services for o in s["operations"])
    lines = []
    lines.append("# Emby REST API 中文速查手册\n")
    lines.append("面向第三方客户端开发者的 Emby Server REST API 中文参考。内容依据官方文档 "
                 "<https://dev.emby.media/reference/RestAPI.html> 整理，按服务分组逐条编写，"
                 "收录仓库中的官方文档快照；不保证覆盖上游后续新增接口，也不代表逐接口实机核验。\n")
    lines.append("## 这份手册怎么用\n")
    lines.append("1. **第一次接入**：先读 [快速开始](00-基础/01-快速开始.md)，照着跑通登录与拉取媒体库。")
    lines.append("2. **写代码前**：查 [常用接口速查表](00-基础/05-常用接口速查表.md)，那里是按场景组织的“最短路径”。")
    lines.append("3. **查具体接口**：从下面的服务目录进入，每个接口都有方法、路径、权限、参数表与响应码。")
    lines.append("4. **对不上的字段**：去 [数据模型索引](02-数据模型/00-模型索引.md) 查字段含义。")
    lines.append("")
    lines.append("## 给 AI / 脚本的入口\n")
    lines.append("本 README 面向人类读者（目录 + 说明）。如果读者是 AI 助手或脚本，先读这两个文件，别从头啃目录：\n")
    lines.append("| 文件 | 用途 | 怎么用 |")
    lines.append("|---|---|---|")
    lines.append("| [llms.txt](llms.txt) | 一屏索引（约 18 KB）：关键约定 + 5 篇入门 + 3 篇实战 + 70 个服务入口 + 边界说明 | 直接整篇读入，按需打开对应服务页 |")
    lines.append("| [index.json](index.json) | 机器可读目录（约 190 KB）：服务 → 文件路径，逐接口 method / path / 标题 / 权限 / 参数数 / 小节序号 | 用脚本按 path 检索，再打开对应 md 搜索「## <小节序号>. 」 |")
    lines.append("")
    lines.append("> 单个服务页是「一个服务一篇」的自包含文档，按需读取即可，不必整库加载；"
                 "接口量大的服务（LiveTv 61、Image 49、Library 31）也只读其中一节。")
    lines.append("")
    lines.append("## 覆盖情况\n")
    lines.append("| 项目 | 数量 |")
    lines.append("|---|---|")
    lines.append("| 服务（Controller） | %d |" % len(services))
    lines.append("| 接口（端点） | %d |" % total_ops)
    lines.append("| 请求参数条目 | %d |" % total_params)
    lines.append("| 数据模型（含枚举） | %d |" % len(models))
    lines.append("| 模型字段 | %d |" % sum(len(m["fields"]) for m in models.values()))
    lines.append("")
    lines.append("## 约定\n")
    lines.append("- 所有接口前缀为 `http://<服务器地址>:8096`（HTTPS 默认 8920）。")
    lines.append("- 路径中的 `{Id}`、`{UserId}` 等为占位符，实际调用需替换为真实值。")
    lines.append("- 标注“管理员令牌”的接口需要管理员账号的 AccessToken；标注“用户令牌”的接口普通已登录用户即可。")
    lines.append("- 返回体均为 JSON（流媒体、图片类接口除外），字段名 PascalCase，解析时请按原样大小写匹配。")
    lines.append("- 布尔值用 `true` / `false`，时间为 ISO 8601 字符串，播放位置用 tick（1 毫秒 = 10000 ticks）。")
    lines.append("- 参数表“类型”列以官方文档为准；官方未给出类型时按命名惯例推断（`Is*`/`Has*`/`Can*` 判为布尔，`Limit`/`StartIndex` 等判为整数），仅供参考。")
    lines.append("- 参数表“必填”列：路径参数为“是”；官方名称星号、明确 Required/Optional 说明或带来源的核验记录决定“是/否”；旧快照无法恢复的标记显示“未标注”，不等于可省略。")
    lines.append("- 模型表“说明”列的 `—` 表示官方未提供该字段说明，`（原文）` 开头表示保留官方英文原文以便对照。")
    lines.append("")
    lines.append("## 目录\n")
    lines.append("### 00 基础\n")
    lines.append("| 文档 | 内容 |")
    lines.append("|---|---|")
    lines.append("| [快速开始](00-基础/01-快速开始.md) | 地址、认证头、第一个请求、最小可运行示例 |")
    lines.append("| [认证与鉴权](00-基础/02-认证与鉴权.md) | 登录流程、令牌传递、API Key、权限模型、常见踩坑 |")
    lines.append("| [通用约定与响应格式](00-基础/03-通用约定与响应格式.md) | 分页、排序、Fields、图片 URL、tick 与时间 |")
    lines.append("| [错误与排查](00-基础/04-错误与排查.md) | 状态码含义、典型报错对照表 |")
    lines.append("| [常用接口速查表](00-基础/05-常用接口速查表.md) | 按场景列出要调哪几个接口 |")
    lines.append("")
    lines.append("### 01 接口参考\n")
    for cat in sorted(cats):
        catname = cat.split("-", 1)[-1]
        lines.append("#### %s\n" % catname)
        lines.append("| 服务 | 中文名 | 接口数 |")
        lines.append("|---|---|---|")
        for s in services:
            if SVC.get(s["service"], ("",))[0] != cat:
                continue
            sv = s["service"]
            lines.append("| [%s](%s/%s/%s.md) | %s | %d |" % (
                sv, API_DIR, cat, sv, SVC[sv][1], len(s["operations"])))
        lines.append("")
    lines.append("### 02 数据模型\n")
    lines.append("| 文档 | 内容 |")
    lines.append("|---|---|")
    lines.append("| [模型索引](02-数据模型/00-模型索引.md) | 全部 %d 个模型的总索引 |" % len(models))
    for k in MODEL_FILES:
        fn, title = MODEL_FILES[k]
        lines.append("| [%s](%s/%s) | %s |" % (title, MODEL_DIR, fn, title))
    lines.append("")
    lines.append("### 03 实战示例\n")
    lines.append("| 文档 | 内容 |")
    lines.append("|---|---|")
    lines.append("| [从登录到播放](03-实战示例/01-从登录到播放.md) | 完整链路：认证 → 视图 → 列表 → 详情 → 播放地址 → 进度上报 |")
    lines.append("| [图片与列表页优化](03-实战示例/02-图片与列表页优化.md) | 图片 URL 拼装、尺寸与缓存策略 |")
    lines.append("| [远程控制与投屏](03-实战示例/03-远程控制与投屏.md) | 会话发现、下发播放命令、轮询状态 |")
    lines.append("")
    lines.append("## 生成与校验\n")
    lines.append("环境：Python 3.11+，核心工具无第三方依赖；维护流程和质量边界见 [维护指南](CONTRIBUTING.md)。\n")
    lines.append("接口清单由 `tools/crawl_emby_api.py` 从官方参考站抓取（结果落在 `tools/_data/`），"
                 "`tools/build_docs.py` 依据数据与中文词表生成全部 Markdown，`tools/check_docs.py` 做交付校验。\n")
    lines.append("```text")
    lines.append("python3 tools/crawl_emby_api.py       # 联网更新；失败不发布，保留旧快照")
    lines.append("python3 tools/rebuild_snapshot.py    # 离线规范化及应用有来源的修订")
    lines.append("python3 tools/build_docs.py          # 重生成接口、模型及目录（不覆盖手写教程）")
    lines.append("python3 tools/build_ai_index.py      # 重生成 AI / 脚本入口")
    lines.append("python3 tools/check_docs.py          # 内容、快照、链接与索引一致性校验")
    lines.append("python3 -m unittest discover -s tests -v  # 离线回归测试")
    lines.append("```\n")
    incomplete = sum(bool(op.get("incomplete")) for svc in services for op in svc["operations"])
    lines.append("当前快照：%d 个服务、%d 个端点，其中 %d 个端点详情不完整。生成统计不是校验结果。"
                 "校验仅证明快照与产物一致，不等于官方实时全覆盖或服务器实测通过。\n" %
                 (len(services), total_ops, incomplete))
    provenance = snapshot_metadata(DATA)
    lines.append("## 快照与质量边界\n")
    lines.append("- 输入哈希（SHA-256）：`services.json` 为 `%s`；`models.json` 为 `%s`。" %
                 (provenance["sha256"]["services.json"], provenance["sha256"]["models.json"]))
    source = provenance["provenance"]
    if source.get("kind") == "live_crawl" and source.get("fetched_at"):
        lines.append("- 本次官方站点抓取完成时间：`%s`；来源、页面哈希及归档关联见 [快照元数据](tools/_data/metadata.json)。官方参考站未提供可据以确认的 Emby Server 版本，不以抓取日期或示例版本代替。" % source["fetched_at"])
    else:
        lines.append("- 抓取来源及可追溯记录见 [快照元数据](tools/_data/metadata.json)；遗留数据的抓取日期和适用服务器版本未知，不以示例版本代替。")
    lines.append("- 已知详情缺失的端点必须单独报告；未知参数不应解释为无参数。")
    lines.append("- 同身份模型的冲突类型以 `A | A[]` 等候选形式保留，不代表两个类型都已实测支持。")
    lines.append("- 局部核验修订记录见 [修订记录](tools/_data/corrections.json)，不能据少量抽查推定所有参数已核对。\n")
    lines.append("> 手写文档（`00-基础/`、`03-实战示例/`）不会被 `build_docs.py` 覆盖；"
                 "`进度清单.md` 会在每次生成时按文件是否存在自动打钩。")
    lines.append("")
    lines.append("> 本手册为社区整理的中文参考资料，官方文档为唯一权威来源。接口行为随服务器版本变化，"
                 "以实际请求结果为准。")
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def render_progress(services, cats):
    lines = ["# 编写进度清单\n",
             "> [返回总目录](README.md)\n",
             "图例：`[x]` 文件已存在（自动生成或手写）；`[ ]` 文件缺失。勾选不代表人工核对、上游完整覆盖或实机验证。\n"]
    lines.append("## 基础篇\n")
    for n, t in [("01-快速开始.md", "快速开始"), ("02-认证与鉴权.md", "认证与鉴权"),
                 ("03-通用约定与响应格式.md", "通用约定与响应格式"),
                 ("04-错误与排查.md", "错误与排查"), ("05-常用接口速查表.md", "常用接口速查表")]:
        p = os.path.join(ROOT, "00-基础", n)
        mark = "x" if os.path.exists(p) else " "
        lines.append("- [%s] 00-基础 / %s" % (mark, t))
    lines.append("\n## 接口参考（按服务）\n")
    groups = {}
    for s in services:
        cat = SVC.get(s["service"], ("08-系统与运维",))[0]
        groups.setdefault(cat, []).append(s)
    for cat in sorted(groups):
        lines.append("### %s\n" % cat.split("-", 1)[-1])
        for s in groups[cat]:
            p = os.path.join(ROOT, API_DIR, cat, s["service"] + ".md")
            mark = "x" if os.path.exists(p) else " "
            lines.append("- [%s] %s（%s）— %d 个接口" % (
                mark, s["service"], SVC[s["service"]][1], len(s["operations"])))
        lines.append("")
    lines.append("## 数据模型\n")
    for k in MODEL_FILES:
        fn, title = MODEL_FILES[k]
        p = os.path.join(ROOT, MODEL_DIR, fn)
        mark = "x" if os.path.exists(p) else " "
        lines.append("- [%s] %s" % (mark, title))
    p = os.path.join(ROOT, MODEL_DIR, "00-模型索引.md")
    lines.append("- [%s] 模型索引" % ("x" if os.path.exists(p) else " "))
    lines.append("\n## 实战示例\n")
    for n, t in [("01-从登录到播放.md", "从登录到播放"), ("02-图片与列表页优化.md", "图片与列表页优化"),
                 ("03-远程控制与投屏.md", "远程控制与投屏")]:
        p = os.path.join(ROOT, "03-实战示例", n)
        mark = "x" if os.path.exists(p) else " "
        lines.append("- [%s] %s" % (mark, t))
    lines.append("\n## AI / 脚本入口\n")
    for fn, label in [("llms.txt", "llms.txt（一屏索引，给 AI 读）"),
                      ("index.json", "index.json（机器可读目录，给脚本查）")]:
        mark = "x" if os.path.exists(os.path.join(ROOT, fn)) else " "
        lines.append("- [%s] %s" % (mark, label))
    with open(os.path.join(ROOT, "进度清单.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def main():
    services, models = load_dataset(DATA)
    os.makedirs(os.path.join(ROOT, MODEL_DIR), exist_ok=True)

    models_map, buckets = render_models(models)
    cats = set()
    for s in services:
        cats.add(render_service(s, models_map))
    render_category_readme(cats, services)
    render_readme(services, cats, models)
    render_progress(services, cats)

    # ── 翻译缺口报告 ──────────────────────────────────────────────
    missing_notes, missing_sum = [], []
    for s in services:
        for o in s["operations"]:
            if o["summary"].strip() and o["summary"].strip() not in SUM:
                missing_sum.append(o["summary"].strip())
            for p in o["params"]:
                n = p["notes"].strip()
                rendered = zh_note(n, p["name"])
                if rendered.startswith("（原文）"):
                    missing_notes.append(n)
    print("未翻译摘要 %d 条，未翻译参数说明 %d 条" % (len(set(missing_sum)), len(set(missing_notes))))
    for x in sorted(set(missing_sum))[:10]:
        print("  SUM:", x[:90])
    for x in sorted(set(missing_notes))[:10]:
        print("  NOTE:", x[:90])
    print("模型桶:", {k: len(v) for k, v in buckets.items()})


if __name__ == "__main__":
    main()
