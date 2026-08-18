import json
import unittest
from copy import deepcopy

from leverage_engine.experience import load_validated_receipts
from leverage_engine.improvement import generate_improvement_analysis, load_improvement_patterns
from leverage_engine.io import load_json
from leverage_engine.paths import ROOT, SCHEMA_DIR
from leverage_engine.schema_validation import load_and_validate, validate_schema_document


PROJECT = "dburt-proex/operator-intelligence:leverage-engine"
AS_OF = "2026-08-18T15:13:00Z"


def minimal_receipt(execution_id, recorded_at, friction):
    return {
        "execution_id": execution_id,
        "project_id": PROJECT,
        "recorded_at": recorded_at,
        "friction": friction,
        "failures": [],
        "residual_risks": [],
    }


class ImprovementLoopTests(unittest.TestCase):
    def registry(self):
        return load_improvement_patterns()

    def real_analysis(self, minimum=2):
        return generate_improvement_analysis(
            load_validated_receipts(),
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=self.registry(),
            min_distinct_executions=minimum,
        )

    def test_schemas_are_canonical_and_real_analysis_validates(self):
        for name in ("improvement-patterns", "improvement-analysis"):
            path = SCHEMA_DIR / f"{name}.schema.json"
            validate_schema_document(load_json(path), name)
        analysis = self.real_analysis()
        load_and_validate(analysis, SCHEMA_DIR / "improvement-analysis.schema.json")
        self.assertIn(analysis["decision"], {"PROPOSE", "NO_ACTION"})
        self.assertFalse(analysis["execution_authorized"])

    def test_real_history_produces_evidence_backed_review_proposal(self):
        analysis = self.real_analysis()
        self.assertEqual(analysis["decision"], "PROPOSE")
        proposal = analysis["selected_proposal"]
        self.assertIsNotNone(proposal)
        self.assertGreaterEqual(proposal["distinct_execution_count"], 2)
        self.assertEqual(proposal["required_gate"], "REVIEW")
        self.assertFalse(proposal["execution_authorized"])
        self.assertTrue(proposal["source_execution_ids"])
        self.assertTrue(proposal["evidence_refs"])
        self.assertEqual(proposal["pattern_id"], "IMP-CONTEXT-RELEVANCE")

    def test_retained_live_analysis_is_exactly_reproducible(self):
        retained = load_json(ROOT / "analyses" / "LE-IMPROVEMENT-2026-0001.json")
        generated = self.real_analysis()
        self.assertEqual(
            json.dumps(retained, sort_keys=True, separators=(",", ":")),
            json.dumps(generated, sort_keys=True, separators=(",", ":")),
        )
        load_and_validate(retained, SCHEMA_DIR / "improvement-analysis.schema.json")

    def test_analysis_is_deterministic_even_if_receipt_order_changes(self):
        receipts = load_validated_receipts()
        registry = self.registry()
        first = generate_improvement_analysis(
            receipts,
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=registry,
            min_distinct_executions=2,
        )
        second = generate_improvement_analysis(
            list(reversed(receipts)),
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=deepcopy(registry),
            min_distinct_executions=2,
        )
        self.assertEqual(
            json.dumps(first, sort_keys=True, separators=(",", ":")),
            json.dumps(second, sort_keys=True, separators=(",", ":")),
        )

    def test_insufficient_recurrence_returns_no_action(self):
        analysis = self.real_analysis(minimum=99)
        self.assertEqual(analysis["decision"], "NO_ACTION")
        self.assertIsNone(analysis["selected_proposal"])
        self.assertFalse(analysis["execution_authorized"])

    def test_future_receipt_cannot_satisfy_recurrence_threshold(self):
        receipts = [
            minimal_receipt(
                "LE-EXEC-2026-9101",
                "2026-08-18T10:00:00Z",
                ["Context relevance is still deterministic exact scope/project matching rather than semantic retrieval."],
            ),
            minimal_receipt(
                "LE-EXEC-2026-9102",
                "2026-08-19T10:00:00Z",
                ["Context relevance is still deterministic exact scope/project matching rather than semantic retrieval."],
            ),
        ]
        analysis = generate_improvement_analysis(
            receipts,
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=self.registry(),
            min_distinct_executions=2,
        )
        self.assertEqual(analysis["decision"], "NO_ACTION")
        candidate = next(
            item for item in analysis["candidates"] if item["pattern_id"] == "IMP-CONTEXT-RELEVANCE"
        )
        self.assertEqual(candidate["distinct_execution_count"], 1)
        self.assertFalse(candidate["eligible"])

    def test_unmatched_text_is_not_semantically_guessed_into_a_pattern(self):
        receipts = [
            minimal_receipt("LE-EXEC-2026-9201", "2026-08-18T10:00:00Z", ["Embedding similarity quality is weak."]),
            minimal_receipt("LE-EXEC-2026-9202", "2026-08-18T11:00:00Z", ["Embedding similarity quality is weak."]),
        ]
        analysis = generate_improvement_analysis(
            receipts,
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=self.registry(),
            min_distinct_executions=2,
        )
        self.assertEqual(analysis["decision"], "NO_ACTION")
        self.assertEqual(analysis["candidates"], [])

    def test_proposal_generation_never_self_authorizes(self):
        analysis = self.real_analysis()
        self.assertFalse(analysis["execution_authorized"])
        proposal = analysis["selected_proposal"]
        self.assertEqual(proposal["required_gate"], "REVIEW")
        self.assertFalse(proposal["execution_authorized"])
        prohibited = {
            "approval_state",
            "allowed_actions",
            "permissions",
            "policy_changes",
            "implemented",
            "completion_status",
        }
        self.assertTrue(prohibited.isdisjoint(proposal))

    def test_only_explicit_friction_failures_and_residual_risks_are_mined(self):
        receipt = minimal_receipt("LE-EXEC-2026-9301", "2026-08-18T10:00:00Z", [])
        receipt["reusable_learnings"] = [
            {
                "learning": "Context relevance is still deterministic exact scope/project matching rather than semantic retrieval.",
                "evidence_refs": ["sample"],
                "reuse_scope": ["leverage-engine"],
            }
        ]
        receipt["next_improvement"] = {
            "objective": "Context relevance is still deterministic exact scope/project matching rather than semantic retrieval."
        }
        analysis = generate_improvement_analysis(
            [receipt, deepcopy(receipt)],
            generated_at=AS_OF,
            project_id=PROJECT,
            pattern_document=self.registry(),
            min_distinct_executions=1,
        )
        self.assertEqual(analysis["decision"], "NO_ACTION")
        self.assertEqual(analysis["candidates"], [])


if __name__ == "__main__":
    unittest.main()
