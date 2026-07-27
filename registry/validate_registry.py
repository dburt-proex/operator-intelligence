#!/usr/bin/env python3
"""Fail-closed Operator Intelligence artifact-registry validator."""
from __future__ import annotations

import json
import re
import subprocess
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


def scan_tracked_files() -> set[str]:
    try:
        completed = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except FileNotFoundError as exc:
        raise ValueError("tracked file scan failed: git executable not found") from exc
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", errors="replace").strip()
        suffix = f": {detail}" if detail else ""
        raise ValueError(f"tracked file scan failed{suffix}") from exc

    try:
        tracked = {
            path
            for path in completed.stdout.decode("utf-8").split("\0")
            if path
        }
    except UnicodeDecodeError as exc:
        raise ValueError("tracked file scan failed: paths are not valid UTF-8") from exc
    if not tracked:
        raise ValueError("tracked file scan failed: git returned no tracked files")
    return tracked


def validate_documented_ignores(
    entries: object,
    tracked_files: set[str],
    root_paths: set[str],
    explicit_paths: set[str],
) -> tuple[set[str], list[str]]:
    errors: list[str] = []
    ignored_paths: set[str] = set()
    if not isinstance(entries, list):
        return ignored_paths, ["tracked_file_ignores must be an array"]

    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"tracked_file_ignores[{index}] must be an object")
            continue
        if set(entry) != {"path", "reason"}:
            errors.append(
                f"tracked_file_ignores[{index}] must contain only path and reason"
            )
            continue
        path = entry["path"]
        reason = entry["reason"]
        if not isinstance(path, str) or not path:
            errors.append(f"tracked_file_ignores[{index}]: path is required")
            continue
        if (
            path != path.strip()
            or path.startswith("/")
            or path.endswith("/")
            or "\\" in path
            or "//" in path
            or ".." in path.split("/")
            or any(token in path for token in ("*", "?", "["))
        ):
            errors.append(
                f"tracked_file_ignores[{index}]: path must be one exact repository-relative file"
            )
            continue
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"tracked_file_ignores[{index}]: reason is required")
        if path in ignored_paths:
            errors.append(f"duplicate tracked file ignore: {path}")
        ignored_paths.add(path)
        if path not in tracked_files:
            errors.append(f"documented ignore is not tracked: {path}")
        if path in explicit_paths or any(
            under_root(path, root) for root in root_paths
        ):
            errors.append(f"documented ignore overlaps governed classification: {path}")

    return ignored_paths, errors


def validate_tracked_paths(
    tracked_files: set[str],
    root_paths: set[str],
    explicit_paths: set[str],
    ignored_paths: set[str],
) -> list[str]:
    return [
        f"unclassified tracked path: {path}"
        for path in sorted(tracked_files)
        if path not in explicit_paths
        and path not in ignored_paths
        and not any(under_root(path, root) for root in root_paths)
    ]


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


def validate(data: dict, tracked_files: set[str] | None = None) -> list[str]:
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

    if tracked_files is None:
        tracked_files = scan_tracked_files()
    ignored_paths, ignore_errors = validate_documented_ignores(
        data.get("tracked_file_ignores", []),
        tracked_files,
        root_paths,
        paths,
    )
    errors.extend(ignore_errors)
    errors.extend(
        validate_tracked_paths(
            tracked_files,
            root_paths,
            paths,
            ignored_paths,
        )
    )

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
