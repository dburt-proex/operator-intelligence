import json
import unittest

from leverage_engine.context import compile_context_package, load_context_relations
from leverage_engine.experience import load_validated_receipts
from leverage_engine.io import load_json
from leverage_engine.paths import ROOT, SCHEMA_DIR
from leverage_engine.runner import run_fixture
from leverage_engine.schema_validation import load_and_validate, validate_schema_document


PROJECT = "dburt-proex/operator-intelligence:leverage-engine"


def synthetic_receipt(execution_id, recorded_at, statement, scope=None, project_id=PROJECT):
    return {
        "execution_id": execution_id,
        "directive_id": "LD-2026-08-18-099",
        "project_id": project_id,
        "recorded_at": recorded_at,
        "reusable_learnings": [
            {
                "learning": statement,
                "evidence_refs": [f"evidence:{execution_id}"],
                "reuse_scope": scope or ["leverage-engine"],
            }
        ],
        "next_improvement": None,
    }


class ContextCompilerTests(unittest.TestCase):
    def request(self):
        return load_json(ROOT / "fixtures" / "context-compiler-valid" / "request.json")

    def compile_request(self):
        request = self.request()
        return compile_context_package(
            load_validated_receipts(),
            run_timestamp=request["run_timestamp"],
            project_id=request["project_id"],
            reuse_scope=request["reuse_scope"],
            relations=load_context_relations(),
            max_items=request["max_items"],
            max_chars=request["max_chars"],
            max_age_days=request["max_age_days"],
        )

    def test_context_schemas_are_canonical_and_live_package_validates(self):
        for name in ("context-package", "context-relations"):
            path = SCHEMA_DIR / f"{name}.schema.json"
            validate_schema_document(load_json(path), name)
        package = self.compile_request()
        load_and_validate(package, SCHEMA_DIR / "context-package.schema.json")
        self.assertTrue(package["included"])
        self.assertTrue(package["authority_neutral"])

    def test_compilation_is_deterministic(self):
        first = self.compile_request()
        second = self.compile_request()
        canonical_first = json.dumps(first, sort_keys=True, separators=(",", ":"))
        canonical_second = json.dumps(second, sort_keys=True, separators=(",", ":"))
        self.assertEqual(canonical_first, canonical_second)
        self.assertEqual(first["context_id"], second["context_id"])

    def test_future_stale_and_unrelated_items_are_excluded(self):
        receipts = [
            synthetic_receipt("LE-EXEC-2026-0101", "2026-08-19T00:00:00Z", "future"),
            synthetic_receipt("LE-EXEC-2026-0102", "2026-01-01T00:00:00Z", "stale"),
            synthetic_receipt("LE-EXEC-2026-0103", "2026-08-18T10:00:00Z", "unrelated", ["other"]),
        ]
        package = compile_context_package(
            receipts,
            run_timestamp="2026-08-18T15:00:00Z",
            project_id=PROJECT,
            reuse_scope=["leverage-engine"],
            relations=[],
            max_age_days=30,
        )
        self.assertEqual(package["included"], [])
        reasons = {item["reason"] for item in package["excluded"]}
        self.assertEqual(reasons, {"future", "stale", "unrelated"})

    def test_superseded_learning_is_excluded(self):
        old = synthetic_receipt("LE-EXEC-2026-0201", "2026-08-18T10:00:00Z", "old rule")
        new = synthetic_receipt("LE-EXEC-2026-0202", "2026-08-18T11:00:00Z", "replacement rule")
        relations = [
            {
                "relation_id": "CTX-REL-001",
                "relation_type": "supersedes",
                "source_item_id": "LE-EXEC-2026-0202:learning:1",
                "target_item_id": "LE-EXEC-2026-0201:learning:1",
                "recorded_at": "2026-08-18T11:05:00Z",
                "evidence_refs": ["evidence:supersession"],
            }
        ]
        package = compile_context_package(
            [old, new],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["leverage-engine"],
            relations=relations,
        )
        self.assertEqual([item["statement"] for item in package["included"]], ["replacement rule"])
        excluded = {item["item_id"]: item for item in package["excluded"]}
        self.assertEqual(excluded["LE-EXEC-2026-0201:learning:1"]["reason"], "superseded")

    def test_unresolved_contradiction_excludes_both_items(self):
        first = synthetic_receipt("LE-EXEC-2026-0301", "2026-08-18T10:00:00Z", "rule A")
        second = synthetic_receipt("LE-EXEC-2026-0302", "2026-08-18T10:30:00Z", "rule B")
        relations = [
            {
                "relation_id": "CTX-REL-002",
                "relation_type": "contradicts",
                "source_item_id": "LE-EXEC-2026-0301:learning:1",
                "target_item_id": "LE-EXEC-2026-0302:learning:1",
                "recorded_at": "2026-08-18T10:40:00Z",
                "evidence_refs": ["evidence:contradiction"],
            }
        ]
        package = compile_context_package(
            [first, second],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["leverage-engine"],
            relations=relations,
        )
        self.assertEqual(package["included"], [])
        self.assertEqual(
            {item["reason"] for item in package["excluded"]},
            {"unresolved_contradiction"},
        )

    def test_context_budget_never_silently_overflows(self):
        receipts = [
            synthetic_receipt("LE-EXEC-2026-0401", "2026-08-18T10:00:00Z", "first"),
            synthetic_receipt("LE-EXEC-2026-0402", "2026-08-18T11:00:00Z", "second"),
        ]
        item_limited = compile_context_package(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["leverage-engine"],
            relations=[],
            max_items=1,
            max_chars=5000,
        )
        self.assertEqual(item_limited["budget"]["used_items"], 1)
        self.assertIn("item_budget", {item["reason"] for item in item_limited["excluded"]})

        char_limited = compile_context_package(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["leverage-engine"],
            relations=[],
            max_items=10,
            max_chars=1,
        )
        self.assertEqual(char_limited["included"], [])
        self.assertEqual(char_limited["budget"]["used_chars"], 0)
        self.assertIn("character_budget", {item["reason"] for item in char_limited["excluded"]})

    def test_compiled_context_cannot_project_authority(self):
        package = self.compile_request()
        prohibited = {
            "gate_result",
            "gate_reasons",
            "review_events",
            "decision_refs",
            "permissions",
            "approval_state",
            "allowed_actions",
        }
        for item in package["included"]:
            self.assertTrue(prohibited.isdisjoint(item))
        self.assertTrue(package["authority_neutral"])

    def test_runner_exposes_compiled_context_without_authorizing_execution(self):
        result = run_fixture(ROOT / "fixtures" / "experience-reuse-valid" / "run.json")
        self.assertIn("compiled_context", result)
        self.assertTrue(result["compiled_context"]["context_id"].startswith("LE-CTX-"))
        self.assertEqual(result["reused_experience"], result["compiled_context"]["included"])
        self.assertFalse(result["execution_authorized"])


if __name__ == "__main__":
    unittest.main()
