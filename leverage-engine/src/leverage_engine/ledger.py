import hashlib
import json
from pathlib import Path
from typing import Any

from .io import canonical_json


class LedgerError(RuntimeError):
    pass


def append_idempotent(path: Path | None, record: dict[str, Any]) -> dict[str, Any]:
    digest = hashlib.sha256(canonical_json(record).encode()).hexdigest()
    receipt = {"record_id": record["record_id"], "sha256": digest, "appended": False}
    if path is None:
        return receipt

    path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict[str, Any]] = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.append(json.loads(line))
    for item in existing:
        if item.get("record_id") == record["record_id"]:
            existing_digest = hashlib.sha256(canonical_json(item).encode()).hexdigest()
            if existing_digest != digest:
                raise LedgerError("record ID collision with different content")
            return receipt
    with path.open("a", encoding="utf-8") as handle:
        handle.write(canonical_json(record) + "\n")
    receipt["appended"] = True
    return receipt
