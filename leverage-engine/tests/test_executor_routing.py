import json
import unittest
from copy import deepcopy

from leverage_engine.executor_routing import build_executor_profiles, route_executor
from leverage_engine.experience import load_validated_receipts
from leverage_engine.io import load_json
from leverage_engine.paths import ROOT, SCHEMA_DIR
from leverage_engine.schema_validation import load_and_validate, validate_schema_document


class ExecutorRoutingTests(unittest.TestCase):
    def sample(self):
        return load_json(ROOT / "fixtures" / "performance-routing-sample" / "receipts.json")

    def test_routing_schema_is_canonical_and_sample_decision_validates(self):
        schema_path = SCHEMA_DIR / "routing-decision.schema.json"
        validate_schema_document(load_json(schema_path), "routing-decision")
        sample = self.sample()
        decision = route_executor(
            sample["receipts"],
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=sample["min_samples"],
            tie_tolerance=sample["tie_tolerance"],
        )
        load_and_validate(decision, schema_path)

    def test_stronger_sample_candidate_routes_without_claiming_real_benchmark(self):
        sample = self.sample()
        self.assertTrue(sample["sample_data"])
        decision = route_executor(
            sample["receipts"],
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        self.assertEqual(decision["decision"], "ROUTE")
        selected = next(
            item for item in decision["profiles"] if item["candidate_id"] == decision["selected_candidate_id"]
        )
        self.assertEqual(selected["agent"], "sample-agent-a")
        self.assertEqual(selected["completion_rate"], 1.0)
        self.assertEqual(selected["validation_pass_rate"], 1.0)
        self.assertFalse(decision["execution_authorized"])

    def test_every_profile_metric_traces_source_executions(self):
        sample = self.sample()
        profiles = build_executor_profiles(
            sample["receipts"],
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        self.assertEqual(len(profiles), 2)
        for profile in profiles:
            self.assertEqual(profile["sample_count"], len(profile["source_execution_ids"]))
            self.assertTrue(profile["source_execution_ids"])

    def test_routing_is_deterministic(self):
        sample = self.sample()
        first = route_executor(
            sample["receipts"],
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        second = route_executor(
            list(reversed(sample["receipts"])),
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        self.assertEqual(
            json.dumps(first, sort_keys=True, separators=(",", ":")),
            json.dumps(second, sort_keys=True, separators=(",", ":")),
        )

    def test_insufficient_live_history_abstains_instead_of_guessing(self):
        decision = route_executor(
            load_validated_receipts(),
            as_of="2026-08-18T15:05:00Z",
            project_id="dburt-proex/operator-intelligence:leverage-engine",
            min_samples=3,
        )
        self.assertIn(decision["decision"], {"REVIEW", "NO_EVIDENCE"})
        self.assertIsNone(decision["selected_candidate_id"])
        self.assertFalse(decision["execution_authorized"])

    def test_material_tie_requires_review(self):
        sample = self.sample()
        tied = deepcopy(sample["receipts"])
        for receipt in tied:
            if receipt["executor"]["agent"] == "sample-agent-b":
                receipt["completion_status"] = "completed"
                receipt["validation"] = [{"result": "pass"}]
                receipt["failures"] = []
                receipt["friction"] = []
        for receipt in tied:
            if receipt["executor"]["agent"] == "sample-agent-a":
                receipt["friction"] = []
        decision = route_executor(
            tied,
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        self.assertEqual(decision["decision"], "REVIEW")
        self.assertIsNone(decision["selected_candidate_id"])

    def test_future_and_halt_evidence_cannot_improve_profile(self):
        sample = self.sample()
        receipts = deepcopy(sample["receipts"])
        template = deepcopy(receipts[0])
        for index in range(3):
            future = deepcopy(template)
            future["execution_id"] = f"LE-EXEC-2099-30{index + 1:02d}"
            future["recorded_at"] = "2026-08-19T10:00:00Z"
            future["executor"] = {"agent": "sample-agent-future", "model": "sample-model-future"}
            receipts.append(future)

            halted = deepcopy(template)
            halted["execution_id"] = f"LE-EXEC-2099-40{index + 1:02d}"
            halted["recorded_at"] = "2026-08-18T09:00:00Z"
            halted["gate_result"] = "HALT"
            halted["executor"] = {"agent": "sample-agent-halt", "model": "sample-model-halt"}
            receipts.append(halted)

        profiles = build_executor_profiles(
            receipts,
            as_of=sample["as_of"],
            project_id=sample["project_id"],
            min_samples=3,
        )
        agents = {profile["agent"] for profile in profiles}
        self.assertNotIn("sample-agent-future", agents)
        self.assertNotIn("sample-agent-halt", agents)


if __name__ == "__main__":
    unittest.main()
