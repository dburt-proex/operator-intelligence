#!/usr/bin/env python3
"""Fail-closed Operator Intelligence artifact-registry validator."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "artifacts.yaml"
VALID_STATES = {"canonical", "approved_extension", "proposed", "experimental", "generated", "deprecated", "superseded", "archived"}
REQUIRED = {"artifact_id", "path", "title", "artifact_type", "authority_state", "version", "release_scope", "status", "generated"}
IGNORE_NAMES = {".git", "__pycache__", ".pytest_cache"}
IGNORE_SUFFIXES = {".pyc", ".pyo"}


def load_registry() -> dict:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"registry cannot be loaded: {exc}") from exc
    if data.get("schema_version") != "oi-artifact-registry-v1":
        raise ValueError("unsupported registry schema_version")
    return data


def repository_files() -> set[str]:
    files: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in IGNORE_NAMES for part in relative.parts) or path.suffix in IGNORE_SUFFIXES:
            continue
        files.add(relative.as_posix())
    return files


def classify(path: str, data: dict, explicit: dict[str, dict]) -> dict | None:
    if path in explicit:
        return explicit[path]
    matches = []
    for root in data.get("governed_roots", []):
        prefix = root["path"].rstrip("/")
        if path == prefix or path.startswith(prefix + "/"):
            matches.append((len(prefix), root))
    return max(matches, default=(0, None), key=lambda item: item[0])[1]


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    states = set(data.get("authority_states", []))
    if states != VALID_STATES:
        errors.append("authority_states must match the governed state set")

    artifacts = data.get("artifacts", [])
    ids: set[str] = set()
    paths: set[str] = set()
    explicit: dict[str, dict] = {}
    for index, artifact in enumerate(artifacts):
        missing = REQUIRED - set(artifact)
        if missing:
            errors.append(f"artifact[{index}] missing fields: {sorted(missing)}")
            continue
        artifact_id = artifact["artifact_id"]
        path = artifact["path"]
        if not re.fullmatch(r"OI-ART-\d{4}", artifact_id):
            errors.append(f"invalid artifact_id: {artifact_id}")
        if artifact_id in ids:
            errors.append(f"duplicate artifact_id: {artifact_id}")
        if path in paths:
            errors.append(f"duplicate explicit path: {path}")
        ids.add(artifact_id)
        paths.add(path)
        explicit[path] = artifact
        if artifact["authority_state"] not in VALID_STATES:
            errors.append(f"{path}: invalid authority_state")
        if artifact["generated"] != (artifact["authority_state"] == "generated"):
            errors.append(f"{path}: generated flag and authority_state disagree")
        if not (ROOT / path).exists():
            errors.append(f"registered path does not exist: {path}")
        for dependency in artifact.get("depends_on", []):
            if not (ROOT / dependency).exists():
                errors.append(f"{path}: missing dependency {dependency}")
        if artifact["authority_state"] == "proposed" and artifact.get("status") in {"approved", "canonical"}:
            errors.append(f"{path}: proposed artifact cannot have approved status")

    files = repository_files()
    root_files = {"README.md", "ROADMAP.md", "CHANGELOG.md", "COMMERCIAL_V1_COMPLETION.md", "RELEASE_NOTES_v1.0.0.md"}
    for path in sorted(files):
        if path in root_files:
            continue
        if classify(path, data, explicit) is None:
            errors.append(f"unclassified governed file: {path}")

    for root in data.get("governed_roots", []):
        if root.get("authority_state") not in VALID_STATES:
            errors.append(f"governed root {root.get('path')}: invalid authority state")
        if not (ROOT / root.get("path", "")).exists():
            errors.append(f"governed root does not exist: {root.get('path')}")

    return errors


def main() -> int:
    try:
        data = load_registry()
        errors = validate(data)
    except ValueError as exc:
        errors = [str(exc)]
    result = {"schema_version": "oi-registry-validation-v1", "decision": "HALT" if errors else "ALLOW", "error_count": len(errors), "errors": errors}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
