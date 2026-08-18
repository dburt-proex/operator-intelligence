#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED = {"CORE", "CONSUMER", "REFERENCE", "EXPERIMENT", "LEGACY", "ARCHIVED"}
NON_AUTHORITY = {"CONSUMER", "REFERENCE", "EXPERIMENT", "LEGACY", "ARCHIVED"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    path = Path(__file__).with_name("registry.json")
    data = json.loads(path.read_text(encoding="utf-8"))

    repos = data.get("repositories", [])
    primitives = data.get("primitives", [])

    repo_names = [r["repo"] for r in repos]
    if len(repo_names) != len(set(repo_names)):
        fail("duplicate repository entry")

    primitive_ids = [p["id"] for p in primitives]
    if len(primitive_ids) != len(set(primitive_ids)):
        fail("duplicate primitive id")

    repo_by_name = {r["repo"]: r for r in repos}
    primitive_by_id = {p["id"]: p for p in primitives}

    for repo in repos:
        classification = repo.get("classification")
        if classification not in ALLOWED:
            fail(f"{repo['repo']}: invalid classification {classification}")
        authority_for = repo.get("authority_for", [])
        if classification in NON_AUTHORITY and authority_for:
            fail(f"{repo['repo']}: {classification} repositories cannot own primitives")
        if classification != "CORE" and repo.get("may_define_new_primitives"):
            fail(f"{repo['repo']}: only CORE repositories may define new primitives")
        if classification in {"LEGACY", "ARCHIVED"} and repo.get("status") == "ACTIVE":
            fail(f"{repo['repo']}: {classification} repository cannot be ACTIVE")
        for primitive in authority_for:
            if primitive not in primitive_by_id:
                fail(f"{repo['repo']}: owns unknown primitive {primitive}")
        for primitive in repo.get("consumes", []):
            if primitive not in primitive_by_id:
                fail(f"{repo['repo']}: consumes unknown primitive {primitive}")

    claims = {}
    for repo in repos:
        for primitive in repo.get("authority_for", []):
            claims.setdefault(primitive, []).append(repo["repo"])

    for primitive in primitive_ids:
        owners = claims.get(primitive, [])
        if len(owners) != 1:
            fail(f"{primitive}: expected exactly one repository authority, found {owners}")
        declared = primitive_by_id[primitive]["authority"]
        if owners[0] != declared:
            fail(f"{primitive}: primitive authority {declared} disagrees with repository claim {owners[0]}")
        owner = repo_by_name.get(declared)
        if owner is None:
            fail(f"{primitive}: authority repository {declared} is absent from registry")
        if owner["classification"] != "CORE":
            fail(f"{primitive}: authority repository must be CORE")

    for repo in repos:
        replacement = repo.get("superseded_by")
        if replacement and replacement not in repo_by_name:
            fail(f"{repo['repo']}: superseded_by target {replacement} is absent")
        for old in repo.get("supersedes", []):
            if old not in repo_by_name:
                fail(f"{repo['repo']}: supersedes target {old} is absent")

    print(
        f"PASS: ecosystem registry v{data['registry_version']} — "
        f"{len(repos)} repositories, {len(primitives)} primitives, exclusive authority preserved"
    )


if __name__ == "__main__":
    main()
