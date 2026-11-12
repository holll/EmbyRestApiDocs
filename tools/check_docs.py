# -*- coding: utf-8 -*-
"""核对生成结果：文档是否覆盖全部服务/接口/模型，是否存在未打钩项与断链。"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from zh_services import SVC  # noqa: E402

API_DIR = "01-接口参考"
MODEL_DIR = "02-数据模型"
MODEL_FILES = ["01-通用结构.md", "02-媒体条目.md", "03-用户与账号.md",
               "04-播放与转码.md", "05-直播电视.md", "06-系统与配置.md"]

errors = []
warns = []


def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def main():
    services = json.load(io.open(os.path.join(ROOT, "tools", "_data", "services.json"), encoding="utf-8"))
    models = json.load(io.open(os.path.join(ROOT, "tools", "_data", "models.json"), encoding="utf-8"))

    total_ops = 0
    total_params = 0
    for svc in services:
        name = svc["service"]
        total_ops += len(svc["operations"])
        total_params += sum(len(op["params"]) for op in svc["operations"])
        if name not in SVC:
            errors.append("服务未登记中文信息：%s" % name)
            continue
        cat = SVC[name][0]
        path = os.path.join(ROOT, API_DIR, cat, "%s.md" % name)
        if not os.path.exists(path):
            errors.append("缺少服务文档：%s" % path)
            continue
        text = read(path)
        n_heading = len(re.findall(r"^## \d+\. ", text, re.M))
        if n_heading != len(svc["operations"]):
            errors.append("%s：文档小节 %d 个，官方接口 %d 个" % (name, n_heading, len(svc["operations"])))
        n_params = text.count("**请求参数**")
        n_ops_with_params = sum(1 for op in svc["operations"] if op["params"])
        if n_params != n_ops_with_params:
            warns.append("%s：参数表 %d 个，有参数的接口 %d 个" % (name, n_params, n_ops_with_params))
        # 路径一致性：文档中出现的反引号路径应都能在官方数据里找到
        doc_paths = set(re.findall(r"^\| \d+ \| `(GET|POST|DELETE|PUT|HEAD|PATCH)` \| `([^`]+)`", text, re.M))
        official = {(op["method"].upper(), op["path"]) for op in svc["operations"]}
        for m, p in doc_paths:
            if (m, p) not in official:
                errors.append("%s：一览表出现非官方端点 %s %s" % (name, m, p))

    # 模型
    all_model_names = []
    for fn in MODEL_FILES:
        p = os.path.join(ROOT, MODEL_DIR, fn)
        if not os.path.exists(p):
            errors.append("缺少模型文件：%s" % fn)
            continue
        all_model_names += re.findall(r"^## ([\w\-\.]+)$", read(p), re.M)
    missing = set(models) - set(all_model_names)
    if missing:
        errors.append("模型未写入文档：%d 个，例如 %s" % (len(missing), sorted(missing)[:5]))
    extra = set(all_model_names) - set(models)
    if extra:
        warns.append("文档中出现了数据文件里没有的模型名：%s" % sorted(extra)[:5])

    idx = os.path.join(ROOT, MODEL_DIR, "00-模型索引.md")
    if os.path.exists(idx):
        for fn in MODEL_FILES:
            if fn[:-3] not in read(idx):
                warns.append("模型索引未链接分类：%s" % fn)

    # AI / 脚本入口
    llms = os.path.join(ROOT, "llms.txt")
    idx_json = os.path.join(ROOT, "index.json")
    if not os.path.exists(llms):
        errors.append("缺少 llms.txt（AI 入口索引）")
    else:
        for link in re.findall(r"\]\(([^)#\s]+\.md)", read(llms)):
            if not os.path.exists(os.path.normpath(os.path.join(ROOT, link))):
                errors.append("llms.txt 链接失效：%s" % link)
        for svc in services:
            if SVC[svc["service"]][0] and ("%s.md" % svc["service"]) not in read(llms):
                errors.append("llms.txt 未列出服务：%s" % svc["service"])
    if not os.path.exists(idx_json):
        errors.append("缺少 index.json（机器可读目录）")
    else:
        data = json.load(io.open(idx_json, encoding="utf-8"))
        c = data["meta"]["counts"]
        if c["services"] != len(services) or c["endpoints"] != total_ops:
            errors.append("index.json 计数与官方数据不一致")
        if len(data["services"]) != len(services):
            errors.append("index.json 服务条目数不符：%d" % len(data["services"]))
        for s in data["services"]:
            if not os.path.exists(os.path.join(ROOT, s["file"])):
                errors.append("index.json 指向的文件不存在：%s" % s["file"])
        if len(data.get("models", {})) != len(models):
            errors.append("index.json 模型条目数不符：%d" % len(data.get("models", {})))

    # 进度清单
    prog = os.path.join(ROOT, "进度清单.md")
    if os.path.exists(prog):
        undone = read(prog).count("- [ ]")
        if undone:
            errors.append("进度清单仍有 %d 项未打钩" % undone)

    # 链接可达性（只查站内相对链接）
    md_files = []
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath or "_data" in dirpath:
            continue
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(dirpath, f))
    broken = 0
    for p in md_files:
        for link in re.findall(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)", read(p)):
            if link.startswith("http"):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(p), link))
            if not os.path.exists(target):
                broken += 1
                if broken <= 10:
                    errors.append("断链：%s → %s" % (os.path.relpath(p, ROOT), link))

    print("服务 %d / 接口 %d / 参数条目 %d / 模型 %d" % (
        len(services), total_ops, total_params, len(models)))
    print("Markdown 文件 %d 个" % len(md_files))
    for w in warns:
        print("[警告] " + w)
    for e in errors:
        print("[错误] " + e)
    print("结果：%s（错误 %d，警告 %d）" % ("通过" if not errors else "未通过", len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
