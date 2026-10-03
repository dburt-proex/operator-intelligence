"""No-network Guardian integration regressions; ALLOW uses trusted mocks only."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from reliability import guardian_ar_001 as gate
from guardian.audit import AuditError, AuditLedger


class TestGuardianAR001(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.calls = []

    def tearDown(self):
        self.directory.cleanup()

    def execute(self, action, root):
        self.assertEqual(root, self.root)
        ledger = AuditLedger(str(self.root / "ar001-guardian-ledger.jsonl"))
        self.assertEqual(ledger.entries()[-1]["record"]["verdict"], "ALLOW")
        self.calls.append(action.params["argv"])
        return "mock harness success"

    def run_gate(self, verifier=lambda envelope: True, executor=None):
        return gate.execute_run("AR001-PILOT-RUN-001", "AR001-PILOT-TRACE-001",
                                root=self.root, verifier=verifier,
                                execute=self.execute if executor is None else executor)

    def test_allow_audited_before_exact_command(self):
        self.assertEqual(self.run_gate(), 0)
        self.assertEqual(self.calls, [gate.action_for("AR001-PILOT-RUN-001", "AR001-PILOT-TRACE-001")["params"]["argv"]])
        ledger = AuditLedger(str(self.root / "ar001-guardian-ledger.jsonl"))
        self.assertTrue(ledger.verify()[0])
        self.assertEqual(len(ledger.entries()), 2)

    def test_denied_and_throwing_verifiers_never_invoke(self):
        def fail(envelope):
            raise RuntimeError("sensitive verifier detail")
        for verifier in (lambda envelope: False, fail):
            self.assertEqual(self.run_gate(verifier), 3)
        self.assertEqual(self.calls, [])
        self.assertNotIn("sensitive", (self.root / "ar001-guardian-ledger.jsonl").read_text())

    def test_duplicate_not_reexecuted(self):
        self.assertEqual(self.run_gate(), 0)
        self.assertEqual(self.run_gate(), 3)
        self.assertEqual(len(self.calls), 1)

    def test_harness_failure_is_execution_failure(self):
        def fail(action, root):
            raise gate.HarnessExecutionError(2)
        self.assertEqual(self.run_gate(executor=fail), 3)
        receipt = json.loads((self.root / "ar001-guardian-AR001-PILOT-RUN-001.json").read_text())
        self.assertTrue(receipt["attempted"])
        self.assertFalse(receipt["executed"])
        self.assertEqual(receipt["harness_exit_code"], 2)

    def test_corrupt_ledger_prevents_execution(self):
        (self.root / "ar001-guardian-ledger.jsonl").write_text("corrupt\n")
        with self.assertRaises(AuditError):
            self.run_gate()
        self.assertEqual(self.calls, [])

    def test_current_closeout_blocks_consumed_authorization(self):
        env = {"GITHUB_REPOSITORY": "dburt-proex/operator-intelligence",
               "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/main",
               "GITHUB_RUN_ATTEMPT": "1", "OPENAI_API_KEY": "test-only"}
        envelope = {"action": gate.action_for("AR001-PILOT-RUN-001", "AR001-PILOT-TRACE-001")}
        # Source checkout line endings differ on Windows; isolate the closeout
        # check from already-tested harness integrity and authorization checks.
        with patch.object(gate, "PINS", {}), patch.object(gate.harness, "validate_execution_authorization", return_value={
            "authorized_runs": 2, "evaluated_agent_tool_count": 0,
            "automatic_inference_retries": 0, "automatic_semantic_retries": 0,
            "store": False, "cohort_execution_authorized": False,
            "thirty_run_cohort_authorized": False}):
            self.assertFalse(gate.verify_authority(envelope, environment=env))

    def test_pr_and_rerun_contexts_blocked(self):
        action = {"action": gate.action_for("AR001-PILOT-RUN-001", "AR001-PILOT-TRACE-001")}
        for event, attempt in (("pull_request", "1"), ("workflow_dispatch", "2")):
            self.assertFalse(gate.verify_authority(action, environment={
                "GITHUB_REPOSITORY": "dburt-proex/operator-intelligence",
                "GITHUB_EVENT_NAME": event, "GITHUB_REF": "refs/heads/main",
                "GITHUB_RUN_ATTEMPT": attempt, "OPENAI_API_KEY": "test-only"}))

    def test_historical_authorization_cannot_be_revived(self):
        envelope = {"action": gate.action_for("AR001-PILOT-RUN-001", "AR001-PILOT-TRACE-001")}
        env = {"GITHUB_REPOSITORY": "dburt-proex/operator-intelligence",
               "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/main",
               "GITHUB_RUN_ATTEMPT": "1", "OPENAI_API_KEY": "test-only"}
        with patch.object(gate, "PINS", {}), patch.object(gate.harness, "verify_frozen_artifacts") as frozen:
            self.assertFalse(gate.verify_authority(envelope, environment=env))
            frozen.assert_not_called()
