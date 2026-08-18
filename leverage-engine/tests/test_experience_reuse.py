import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from leverage_engine.experience import compile_experience_context, load_validated_receipts
from leverage_engine.io import load_json
from leverage_engine.paths import RECEIPT_DIR, ROOT
from leverage_engine.runner import run_fixture


class ExperienceReuseTests(unittest.TestCase):
    def fixture(self) -> Path:
        return ROOT / "fixtures" / "experience-reuse-valid" / "run.json"

    def test_retained_receipts_are_loaded_through_canonical_validation(self):
        receipts = load_validated_receipts()
        self.assertTrue(receipts)
        self.assertIn("LE-EXEC-2026-0001", {item["execution_id"] for item in receipts})

    def test_run_n_plus_one_consumes_phase_one_experience(self):
        result = run_fixture(self.fixture())
        self.assertEqual(result["selection"]["result"], "DIRECTIVE")
        reused = result["reused_experience"]
        self.assertTrue(reused)
        self.assertTrue(all(item["source_execution_id"] == "LE-EXEC-2026-0001" for item in reused))
        self.assertTrue(any(item["kind"] == "learning" for item in reused))
        self.assertIn("experience:LE-EXEC-2026-0001", result["evidence_refs"])
        self.assertIn(
            "experience:LE-EXEC-2026-0001",
            result["selection"]["directive"]["evidence_refs"],
        )
        self.assertFalse(result["execution_authorized"])

    def test_unrelated_scope_is_excluded_from_compiled_context(self):
        fixture = load_json(self.fixture())
        fixture["run_id"] = "LE-RUN-2026-0043"
        fixture["experience_scope"] = ["unrelated-domain"]
        fixture["experience_project_id"] = "unrelated/project"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "run.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            result = run_fixture(path)
        self.assertEqual(result["reused_experience"], [])
        self.assertNotIn("experience:LE-EXEC-2026-0001", result["evidence_refs"])
        if result["selection"]["directive"] is not None:
            self.assertNotIn(
                "experience:LE-EXEC-2026-0001",
                result["selection"]["directive"]["evidence_refs"],
            )

    def test_future_receipts_cannot_leak_into_historical_replay(self):
        receipt = deepcopy(load_json(RECEIPT_DIR / "LE-EXEC-2026-0001.json"))
        receipt["recorded_at"] = "2026-08-18T15:00:00Z"
        projected = compile_experience_context(
            [receipt],
            run_timestamp="2026-08-18T14:20:00Z",
            project_id="dburt-proex/operator-intelligence:leverage-engine",
            reuse_scope=["leverage-engine"],
        )
        self.assertEqual(projected, [])

    def test_prior_authority_state_is_not_projected_into_new_run(self):
        projected = compile_experience_context(
            load_validated_receipts(),
            run_timestamp="2026-08-18T14:20:00Z",
            project_id="dburt-proex/operator-intelligence:leverage-engine",
            reuse_scope=["leverage-engine"],
        )
        self.assertTrue(projected)
        prohibited = {"gate_result", "gate_reasons", "review_events", "decision_refs", "permissions"}
        for item in projected:
            self.assertTrue(prohibited.isdisjoint(item))


if __name__ == "__main__":
    unittest.main()
