"""Explicit inference policy remains constrained by every baseline rule."""
import copy
import tempfile
from pathlib import Path
import unittest

from guardian.inference import AuthorizedInferenceGuardian
from guardian.models import Verdict
from guardian.pipeline import GuardianAgent


class InferenceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = str(Path(self.directory.name) / "audit.jsonl")
        self.action = {"id": "run-001", "type": "external_model_execution",
            "target": "https://api.openai.com/v1/responses", "payload": "",
            "params": {"argv": ["python3", "harness.py", "--execute"],
                "scope": "AR-001", "data_class": "SYNTHETIC_EXPERIMENT_EVIDENCE",
                "network": "api.openai.com", "credential": "OPENAI_API_KEY",
                "mutation": False, "authorization": "ALLOW_TO_RUN_PILOT",
                "evaluated_agent_tool_count": 0, "automatic_inference_retries": 0,
                "store": False}}
        self.signal = {"content": "Verified exact synthetic inference authorization and frozen command checked by host code before execution. No tools or retries are permitted.",
                       "source": "host", "signal_score": 9,
                       "source_pointers": ["auth", "hash", "scope"],
                       "metadata": {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}}

    def tearDown(self):
        self.directory.cleanup()

    def agent(self, verifier=lambda envelope: True):
        return AuthorizedInferenceGuardian(self.path, authorized_action=self.action,
                                           evidence_verifier=verifier)

    def envelope(self):
        return {"action": copy.deepcopy(self.action), "signal": self.signal}

    def test_generic_runtime_still_reviews_inference(self):
        self.assertIs(GuardianAgent(self.path).govern(self.envelope()).verdict, Verdict.REVIEW)

    def test_exact_verified_request_allows(self):
        decision = self.agent().govern(self.envelope())
        self.assertIs(decision.verdict, Verdict.ALLOW)
        self.assertTrue(decision.evidence_verified)
        self.assertEqual(decision.casa["triggered_by"], ["R7_AUTHORIZED_INFERENCE"])

    def test_contract_drift_halts(self):
        agent = self.agent()
        for key, value in (("network", "example.com"), ("store", True), ("argv", ["other"]), ("mutation", True)):
            envelope = self.envelope()
            envelope["action"]["params"][key] = value
            self.assertIs(agent.govern(envelope).verdict, Verdict.HALT)

    def test_missing_or_false_verification_blocks(self):
        with self.assertRaises(ValueError):
            self.agent(None)
        self.assertIs(self.agent(lambda envelope: False).govern(self.envelope()).verdict, Verdict.HALT)

    def test_baseline_destruction_rule_is_never_overridden(self):
        self.action["payload"] = "rm -rf /important"
        decision = self.agent().govern(self.envelope())
        self.assertIs(decision.verdict, Verdict.HALT)
        self.assertIn("R1_IRREVERSIBLE_DESTRUCTION", decision.casa["triggered_by"])

    def test_weak_signal_never_overridden(self):
        agent = self.agent()
        envelope = self.envelope()
        envelope["signal"] = {}
        self.assertIs(agent.govern(envelope).verdict, Verdict.HALT)
