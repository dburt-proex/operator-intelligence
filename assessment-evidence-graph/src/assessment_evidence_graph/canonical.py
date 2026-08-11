"""Deterministic serialization and identifier helpers."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(canonical_json(value))


def stable_identifier(prefix: str, *parts: str) -> str:
    material = "\x1f".join(parts)
    return f"OI-{prefix.upper()}-{sha256_text(material)[:16].upper()}"
