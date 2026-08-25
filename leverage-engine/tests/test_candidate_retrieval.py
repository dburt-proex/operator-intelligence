import json
import unittest

from leverage_engine.context import compile_context_package
from leverage_engine.experience import load_validated_receipts
from leverage_engine.io import load_json
from leverage_engine.paths import ROOT, SCHEMA_DIR
from leverage_engine.retrieval import retrieve_candidates
from leverage_engine.runner import run_fixture
from leverage_engine.schema_validation import load_and_validate, validate_schema_document


PROJECT = "dburt-proex/operator-intelligence:leverage-engine"


def receipt(execution_id, recorded_at, statement, scope=None):
    return {
        "execution_id": execution_id,
        "directive_id": "LD-2026-08-18-099",
        "project_id": PROJECT,
        "recorded_at": recorded_at,
        "reusable_learnings": [
            {
                "learning": statement,
                "evidence_refs": [f"evidence:{execution_id}"],
                "reuse_scope": scope or ["not-the-requested-scope"],
            }
        ],
        "next_improvement": None,
        "failures": [],
        "friction": [],
        "residual_risks": [],
        "evidence_refs": [],
        "decision_refs": [],
    }


class CandidateRetrievalTests(unittest.TestCase):
    def test_schema_is_canonical_and_live_retrieval_validates(self):
        schema_path = SCHEMA_DIR / "candidate-retrieval.schema.json"
        validate_schema_document(load_json(schema_path), "candidate-retrieval")
        result = retrieve_candidates(
            load_validated_receipts(),
            run_timestamp="2026-08-18T14:20:00Z",
            project_id=PROJECT,
            query="parallel backend control infrastructure",
            relations=[],
            max_candidates=5,
        )
        load_and_validate(result, schema_path)
        self.assertTrue(result["candidates"])
        self.assertTrue(result["authority_neutral"])
        self.assertFalse(result["execution_authorized"])

    def test_retrieval_improves_recall_without_exact_scope_and_compiler_admits(self):
        receipts = [
            receipt(
                "LE-EXEC-2026-6101",
                "2026-08-18T10:00:00Z",
                "Bounded candidate retrieval improves context recall.",
            )
        ]
        retrieval = retrieve_candidates(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="candidate retrieval context recall",
            relations=[],
            max_candidates=5,
        )
        ids = {item["item_id"] for item in retrieval["candidates"]}
        package = compile_context_package(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["different-scope"],
            relations=[],
            retrieved_item_ids=ids,
        )
        self.assertEqual(len(package["included"]), 1)
        admitted = package["included"][0]
        self.assertEqual(admitted["matched_scope"], [])
        self.assertEqual(admitted["relevance_basis"], ["retrieval"])
        self.assertTrue(package["authority_neutral"])

    def test_future_receipt_is_not_even_proposed(self):
        receipts = [
            receipt(
                "LE-EXEC-2026-6102",
                "2026-08-19T10:00:00Z",
                "candidate retrieval future leak",
            )
        ]
        result = retrieve_candidates(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="candidate retrieval future leak",
            relations=[],
        )
        self.assertEqual(result["candidates"], [])

    def test_zero_overlap_is_not_proposed_and_candidate_budget_is_hard(self):
        receipts = [
            receipt("LE-EXEC-2026-6103", "2026-08-18T10:00:00Z", "alpha retrieval context"),
            receipt("LE-EXEC-2026-6104", "2026-08-18T11:00:00Z", "alpha retrieval evidence"),
        ]
        none = retrieve_candidates(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="totally different vocabulary",
            relations=[],
            max_candidates=5,
        )
        self.assertEqual(none["candidates"], [])

        bounded = retrieve_candidates(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="alpha retrieval",
            relations=[],
            max_candidates=1,
        )
        self.assertEqual(len(bounded["candidates"]), 1)

    def test_graph_neighbor_can_be_proposed_but_supersession_still_wins_in_compiler(self):
        old = receipt(
            "LE-EXEC-2026-6201",
            "2026-08-18T10:00:00Z",
            "lexical retrieval seed",
        )
        new = receipt(
            "LE-EXEC-2026-6202",
            "2026-08-18T11:00:00Z",
            "replacement control rule",
        )
        relation = {
            "relation_id": "CTX-REL-6201",
            "relation_type": "supersedes",
            "source_item_id": "LE-EXEC-2026-6202:learning:1",
            "target_item_id": "LE-EXEC-2026-6201:learning:1",
            "recorded_at": "2026-08-18T11:05:00Z",
            "evidence_refs": ["evidence:supersession"],
        }
        retrieval = retrieve_candidates(
            [old, new],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="lexical retrieval seed",
            relations=[relation],
            max_candidates=5,
        )
        by_id = {item["item_id"]: item for item in retrieval["candidates"]}
        self.assertEqual(by_id["LE-EXEC-2026-6202:learning:1"]["match_type"], "graph_neighbor")

        package = compile_context_package(
            [old, new],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=["different-scope"],
            relations=[relation],
            retrieved_item_ids=set(by_id),
        )
        self.assertEqual([item["statement"] for item in package["included"]], ["replacement control rule"])
        excluded = {item["item_id"]: item for item in package["excluded"]}
        self.assertEqual(excluded["LE-EXEC-2026-6201:learning:1"]["reason"], "superseded")

    def test_retrieved_stale_contradicted_and_over_budget_items_still_lose(self):
        stale = receipt(
            "LE-EXEC-2026-6301",
            "2026-01-01T00:00:00Z",
            "retrieval stale candidate",
        )
        stale_retrieval = retrieve_candidates(
            [stale],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="retrieval stale candidate",
            relations=[],
        )
        stale_package = compile_context_package(
            [stale],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=[],
            relations=[],
            retrieved_item_ids={item["item_id"] for item in stale_retrieval["candidates"]},
            max_age_days=30,
        )
        self.assertEqual(stale_package["included"], [])
        self.assertIn("stale", {item["reason"] for item in stale_package["excluded"]})

        first = receipt("LE-EXEC-2026-6302", "2026-08-18T10:00:00Z", "retrieval conflict alpha")
        second = receipt("LE-EXEC-2026-6303", "2026-08-18T10:30:00Z", "retrieval conflict beta")
        contradiction = {
            "relation_id": "CTX-REL-6301",
            "relation_type": "contradicts",
            "source_item_id": "LE-EXEC-2026-6302:learning:1",
            "target_item_id": "LE-EXEC-2026-6303:learning:1",
            "recorded_at": "2026-08-18T10:40:00Z",
            "evidence_refs": ["evidence:conflict"],
        }
        retrieval = retrieve_candidates(
            [first, second],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="retrieval conflict",
            relations=[contradiction],
        )
        ids = {item["item_id"] for item in retrieval["candidates"]}
        conflict_package = compile_context_package(
            [first, second],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=[],
            relations=[contradiction],
            retrieved_item_ids=ids,
        )
        self.assertEqual(conflict_package["included"], [])
        self.assertEqual(
            {item["reason"] for item in conflict_package["excluded"]},
            {"unresolved_contradiction"},
        )

        budget_package = compile_context_package(
            [first, second],
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            reuse_scope=[],
            relations=[],
            retrieved_item_ids=ids,
            max_items=1,
            max_chars=5000,
        )
        self.assertEqual(budget_package["budget"]["used_items"], 1)
        self.assertIn("item_budget", {item["reason"] for item in budget_package["excluded"]})

    def test_retrieval_is_deterministic_and_carries_no_authority_fields(self):
        receipts = [
            receipt("LE-EXEC-2026-6401", "2026-08-18T10:00:00Z", "candidate retrieval deterministic"),
            receipt("LE-EXEC-2026-6402", "2026-08-18T11:00:00Z", "candidate retrieval deterministic replay"),
        ]
        first = retrieve_candidates(
            receipts,
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="candidate retrieval deterministic",
            relations=[],
        )
        second = retrieve_candidates(
            list(reversed(receipts)),
            run_timestamp="2026-08-18T12:00:00Z",
            project_id=PROJECT,
            query="candidate retrieval deterministic",
            relations=[],
        )
        self.assertEqual(
            json.dumps(first, sort_keys=True, separators=(",", ":")),
            json.dumps(second, sort_keys=True, separators=(",", ":")),
        )
        prohibited = {"gate_result", "review_events", "permissions", "approval_state", "allowed_actions"}
        for item in first["candidates"]:
            self.assertTrue(prohibited.isdisjoint(item))
        self.assertFalse(first["execution_authorized"])

    def test_runner_places_retrieval_before_compiler_and_does_not_authorize(self):
        result = run_fixture(ROOT / "fixtures" / "candidate-retrieval-valid" / "run.json")
        self.assertIsNotNone(result["candidate_retrieval"])
        self.assertTrue(result["candidate_retrieval"]["candidates"])
        retrieved_ids = {item["item_id"] for item in result["candidate_retrieval"]["candidates"]}
        admitted = [
            item for item in result["compiled_context"]["included"]
            if item["item_id"] in retrieved_ids
        ]
        self.assertTrue(admitted)
        self.assertTrue(any(item["relevance_basis"] == ["retrieval"] for item in admitted))
        self.assertFalse(result["execution_authorized"])
        self.assertFalse(result["candidate_retrieval"]["execution_authorized"])


if __name__ == "__main__":
    unittest.main()
