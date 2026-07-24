#!/usr/bin/env python3
"""Regression tests for fail-closed repository conformance."""
from __future__ import annotations

import subprocess
import unittest
from unittest import mock

from registry import validate_registry


class TrackedPathRegressionTests(unittest.TestCase):
    def test_unclassified_tracked_path_halts(self) -> None:
        errors = validate_registry.validate_tracked_paths(
            {"README.md", "shadow/policy.md"},
            {"docs"},
            {"README.md"},
            set(),
        )
        self.assertEqual(
            ["unclassified tracked path: shadow/policy.md"],
            errors,
        )

    def test_governed_root_explicit_artifact_and_ignore_are_allowed(self) -> None:
        tracked = {"docs/usage.md", "README.md", "NOTICE.txt"}
        ignored, errors = validate_registry.validate_documented_ignores(
            [{"path": "NOTICE.txt", "reason": "Non-authoritative legal notice."}],
            tracked,
            {"docs"},
            {"README.md"},
        )
        self.assertEqual([], errors)
        self.assertEqual(
            [],
            validate_registry.validate_tracked_paths(
                tracked,
                {"docs"},
                {"README.md"},
                ignored,
            ),
        )

    def test_documented_ignore_cannot_be_a_glob(self) -> None:
        ignored, errors = validate_registry.validate_documented_ignores(
            [{"path": "*.md", "reason": "Too broad."}],
            {"README.md"},
            {"docs"},
            {"README.md"},
        )
        self.assertEqual(set(), ignored)
        self.assertIn(
            "tracked_file_ignores[0]: path must be one exact repository-relative file",
            errors,
        )

    def test_git_scan_failure_halts(self) -> None:
        failure = subprocess.CalledProcessError(
            128,
            ["git", "ls-files", "-z"],
            stderr=b"fatal: not a git repository",
        )
        with mock.patch.object(
            validate_registry.subprocess,
            "run",
            side_effect=failure,
        ):
            with self.assertRaisesRegex(ValueError, "tracked file scan failed"):
                validate_registry.scan_tracked_files()

    def test_current_checkout_is_fully_classified(self) -> None:
        data = validate_registry.load_registry()
        errors = validate_registry.validate(
            data,
            validate_registry.scan_tracked_files(),
        )
        self.assertEqual([], errors)


class WorkflowTriggerRegressionTests(unittest.TestCase):
    def test_conformance_workflow_has_no_path_filter(self) -> None:
        workflow = (
            validate_registry.ROOT
            / ".github"
            / "workflows"
            / "validate-registry-and-map.yml"
        ).read_text(encoding="utf-8")
        self.assertNotIn("paths:", workflow)


if __name__ == "__main__":
    unittest.main()
