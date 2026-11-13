"""Offline migration of the legacy snapshot. Does not fetch or infer missing evidence."""
import json
from pathlib import Path

from crawl_emby_api import publish_snapshot
from model_registry import normalize_services

DATA = Path(__file__).resolve().parent / "_data"


def apply_corrections(services, corrections):
    for correction in corrections:
        matches = [p for svc in services if svc["service"] == correction["service"]
                   for op in svc["operations"]
                   if op["method"].upper() == correction["method"] and op["path"] == correction["path"]
                   for p in op["params"]
                   if p["name"] == correction["parameter"] and p["in"] == correction["location"]]
        if len(matches) != 1:
            raise ValueError("Correction must match exactly one parameter: %r" % correction)
        # A fresh explicit source marker supersedes a legacy repair; do not erase it.
        if matches[0].get("required_source") in ("name_marker", "notes"):
            if matches[0].get("required") != correction["required"]:
                raise ValueError("Correction conflicts with explicit upstream evidence: %r" % correction)
            continue
        matches[0].update({key: correction[key] for key in ("required", "required_source")})
        matches[0]["required_evidence"] = correction["source_url"]
    return services


def main():
    services = json.loads((DATA / "services.json").read_text(encoding="utf-8"))
    corrections = json.loads((DATA / "corrections.json").read_text(encoding="utf-8"))
    # Preserve only trustworthy provenance, not the old crawler's default-to-required heuristic.
    for svc in services:
        for op in svc["operations"]:
            for p in op["params"]:
                if p.get("required_source"):
                    continue
                note = p.get("notes", "").strip().lower()
                if p.get("in") == "path":
                    p.update(required="required", required_source="path")
                elif note.startswith("required") or note.startswith("optional"):
                    p.update(required="required" if note.startswith("required") else "optional", required_source="notes")
                else:
                    p.update(required="unknown", required_source="legacy_unspecified")
    apply_corrections(services, corrections)
    services, models = normalize_services(services)
    metadata_path = DATA / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {
        "kind": "legacy_snapshot", "source": "https://dev.emby.media/reference/RestAPI.html",
        "fetched_at": None, "emby_version": None,
        "note": "遗留快照缺少抓取日期、原始HTML与服务器版本；离线规范化不是重新抓取。",
        "normalization": "namespace-aware models; source conflicts retained; explicit parameter corrections",
    }
    publish_snapshot({"services.json": services, "models.json": models, "metadata.json": metadata}, DATA)
    print("离线快照：%d 服务 / %d 端点 / %d 模型" %
          (len(services), sum(len(s["operations"]) for s in services), len(models)))


if __name__ == "__main__":
    main()
