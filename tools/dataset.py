"""Shared, deterministic loading and provenance for the checked-in API snapshot."""
import hashlib
import json
from pathlib import Path

from model_registry import normalize_services


def load_dataset(data_dir):
    """Return normalized services/models; reject a stale or hand-corrupted registry."""
    data_dir = Path(data_dir)
    services = json.loads((data_dir / "services.json").read_text(encoding="utf-8"))
    stored_models = json.loads((data_dir / "models.json").read_text(encoding="utf-8"))
    services, models = normalize_services(services)
    if stored_models != models:
        raise ValueError("models.json 与 services.json 的规范化定义不一致；请先运行 python3 tools/rebuild_snapshot.py")
    return services, models


def snapshot_metadata(data_dir):
    """Content hashes are reproducible; unknown historical dates stay unknown."""
    data_dir = Path(data_dir)
    files = {name: hashlib.sha256((data_dir / name).read_bytes()).hexdigest()
             for name in ("services.json", "models.json")}
    metadata_path = data_dir / "metadata.json"
    provenance = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {
        "kind": "legacy_snapshot", "fetched_at": None, "emby_version": None,
        "note": "遗留快照未记录抓取时间和服务器版本；不能据示例版本推定适用版本。",
    }
    return {"sha256": files, "provenance": provenance}
