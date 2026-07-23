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
EXPECTED_MAP_OUTPUTS = {
    "generated/repository-map.md",
    "generated/repository-map.json",
    "generated/repository-map.mmd",
    "generated/repository-map.dot",
}


def load_registry() -> dict:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"registry cannot be loaded: {exc}") from exc
    if data.get("schema_version") != "oi-artifact-registry-v1":
        raise ValueError("unsupported registry schema_version")
    return data


def under_root(path: str, root: str) -> bool:
    prefix = root.rstrip("/")
    return path == prefix or path.startswith(prefix + "/")


def detect_cycles(graph: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in visiting:
            cycle = trail[trail.index(node):] + [node]
            errors.append("dependency cycle: " + " -> ".join(cycle))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            if dependency in graph:
                visit(dependency, trail + [dependency])
        visiting.remove(node)
        visited.add(node)

    for node in sorted(graph):
        visit(node, [node])
    return sorted(set(errors))


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if set(data.get("authority_states", [])) != VALID_STATES:
        errors.append("authority_states must match the governed state set")

    roots = data.get("governed_roots", [])
    root_paths: set[str] = set()
    for root in roots:
        path = root.get("path", "").rstrip("/")
        if not path:
            errors.append("governed root path is required")
            continue
        if path in root_paths:
            errors.append(f"duplicate governed root: {path}")
        root_paths.add(path)
        if root.get("authority_state") not in VALID_STATES:
            errors.append(f"governed root {path}: invalid authority state")
        if not (ROOT / path).exists():
            errors.append(f"governed root does not exist: {path}")

    artifacts = data.get("artifacts", [])
    ids: set[str] = set()
    paths: set[str] = set()
    explicit: dict[str, dict] = {}
    graph: dict[str, list[str]] = {}
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
        graph[path] = list(artifact.get("depends_on", []))

        state = artifact["authority_state"]
        if state not in VALID_STATES:
            errors.append(f"{path}: invalid authority_state")
        if artifact["generated"] != (state == "generated"):
            errors.append(f"{path}: generated flag and authority_state disagree")
        if not (ROOT / path).exists():
            errors.append(f"registered path does not exist: {path}")
        if "/" in path and not any(under_root(path, root) for root in root_paths):
            errors.append(f"{path}: explicit artifact is outside governed roots")
        if state == "proposed" and artifact.get("status") in {"approved", "canonical"}:
            errors.append(f"{path}: proposed artifact cannot have approved status")
        if path.startswith("generated/") and state != "generated":
            errors.append(f"{path}: generated path must use generated authority_state")

        for reference_type in ("depends_on", "downstream_consumers"):
            for reference in artifact.get(reference_type, []):
                if not (ROOT / reference).exists():
                    errors.append(f"{path}: missing {reference_type} reference {reference}")

    errors.extend(detect_cycles(graph))

    registered_generated = {path for path, artifact in explicit.items() if artifact["authority_state"] == "generated"}
    if registered_generated != EXPECTED_MAP_OUTPUTS:
        errors.append("generated repository-map registry entries do not match required outputs")

    map_config = data.get("map", {})
    if map_config.get("output_directory") != "generated":
        errors.append("map.output_directory must be generated")
    if set(map_config.get("formats", [])) != {"md", "json", "mmd", "dot"}:
        errors.append("map.formats must contain md, json, mmd, and dot")

    return errors


def main() -> int:
    try:
        data = load_registry()
        errors = validate(data)
    except ValueError as exc:
        errors = [str(exc)]
    result = {
        "schema_version": "oi-registry-validation-v1",
        "decision": "HALT" if errors else "ALLOW",
        "error_count": len(errors),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
