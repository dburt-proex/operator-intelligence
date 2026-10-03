import os
import json
import tempfile
import unittest
from unittest.mock import patch

from guardian import GuardianAgent
from guardian.adapter import GovernedToolRunner
from guardian.audit import AuditError

VERIFIED = {
    "content": "Ops ticket approved: pull weekly KPI report per standing "
               "runbook step 3 for client dashboard refresh, requester DB.",
    "source": "ops_queue",
    "source_pointers": ["TICKET-88", "RUNBOOK-3", "APPROVAL-DB"],
    "metadata": {"ticket": "88", "requester": "db", "runbook": "3",
                 "client": "acme", "step": "read"},
    "signal_score": 9.0,
}


class TestAdapter(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.agent = GuardianAgent(os.path.join(self.dir.name, "audit.jsonl"))
        self.calls = []
        self.runner = GovernedToolRunner(
            tools={
                "read_file": lambda target="": self.calls.append(target) or f"data:{target}",
                "wire_transfer": lambda **kw: self.calls.append("WIRE") or "sent",
                "send_email": lambda **kw: self.calls.append("MAIL") or "sent",
            },
            agent=self.agent,
        )

    def tearDown(self):
        self.dir.cleanup()

    def test_allow_executes(self):
        r = self.runner.run("read_file", {"target": "kpi.csv"}, signal=VERIFIED)
        self.assertEqual(r["verdict"], "ALLOW")
        self.assertTrue(r["executed"])
        self.assertEqual(r["output"], "data:kpi.csv")
        self.assertEqual(self.calls, ["kpi.csv"])

    def test_halt_never_calls_tool(self):
        r = self.runner.run("wire_transfer",
                            {"amount": "$12,000 usd", "to": "acct 4471"},
                            signal=VERIFIED)
        self.assertEqual(r["verdict"], "HALT")
        self.assertTrue(r["blocked"])
        self.assertNotIn("WIRE", self.calls)

    def test_review_pends_no_execution(self):
        r = self.runner.run("send_email", {"to": "all@list"}, signal=VERIFIED)
        self.assertEqual(r["verdict"], "REVIEW")
        self.assertTrue(r["pending_review"])
        self.assertNotIn("MAIL", self.calls)

    def test_no_signal_fails_safe(self):
        # Read-only tool, but zero grounding context -> blocked at VIL.
        r = self.runner.run("read_file", {"target": "kpi.csv"})
        self.assertEqual(r["verdict"], "HALT")
        self.assertFalse(r["executed"])

    def test_unknown_tool_governed_not_executed(self):
        r = self.runner.run("teleport", {}, signal=VERIFIED)
        self.assertEqual(r["verdict"], "REVIEW")  # unknown type fail-safe
        self.assertFalse(r["executed"])
        self.assertIn("unknown tool", r["error"])

    def test_anthropic_block_shape(self):
        block = {"type": "tool_use", "id": "toolu_01", "name": "wire_transfer",
                 "input": {"amount": "$500 usd"}}
        res = self.runner.handle_tool_use_block(block, signal=VERIFIED)
        self.assertEqual(res["type"], "tool_result")
        self.assertEqual(res["tool_use_id"], "toolu_01")
        self.assertTrue(res["is_error"])
        self.assertIn('"verdict": "HALT"', res["content"])

    def test_every_call_ledgered(self):
        self.runner.run("read_file", {"target": "a"}, signal=VERIFIED)
        self.runner.run("wire_transfer", {"amount": "$1 usd"}, signal=VERIFIED)
        ok, msg = self.agent.ledger.verify()
        self.assertTrue(ok, msg)
        self.assertGreaterEqual(len(self.agent.ledger.entries()), 3)  # 2 govern + 1 exec

    def test_malformed_blocks_are_audited_before_rejection(self):
        valid = {"type": "tool_use", "id": "call-1", "name": "read_file", "input": {"target": "a"}}
        malformed = [None, [], {}, {**valid, "type": "text"},
                     {**valid, "id": ""}, {**valid, "id": "x" * 129},
                     {**valid, "name": None}, {**valid, "name": "x" * 65},
                     {**valid, "input": []}, {**valid, "extra": "secret-detail"},
                     {k: v for k, v in valid.items() if k != "input"},
                     {**valid, "input": {"sensitive": "x" * 1_048_577}}]
        for block in malformed:
            with self.subTest(block_type=type(block).__name__):
                previous = len(self.agent.ledger.entries())
                with self.assertRaisesRegex(ValueError, "Invalid tool_use block"):
                    self.runner.handle_tool_use_block(block, signal=VERIFIED)
                entries = self.agent.ledger.entries()
                self.assertEqual(len(entries), previous + 1)
                self.assertEqual(entries[-1]["record"]["verdict"], "HALT")
        self.assertEqual(self.calls, [])
        with open(self.agent.ledger.path, encoding="utf-8") as stream:
            self.assertNotIn("secret-detail", stream.read())

    def test_rejected_block_audit_failure_propagates(self):
        with patch.object(self.agent.ledger, "append", side_effect=AuditError("audit unavailable")):
            with self.assertRaises(AuditError):
                self.runner.handle_tool_use_block(None)
        self.assertEqual(self.calls, [])

    def test_block_snapshot_preserves_correlation_and_inputs(self):
        block = {"type": "tool_use", "id": "call-1", "name": "read_file", "input": {"target": "a"}}
        def verifier(envelope):
            block["id"] = "changed"
            block["input"]["target"] = "changed"
            return True
        self.agent.evidence_verifier = verifier
        result = self.runner.handle_tool_use_block(block, signal=VERIFIED)
        self.assertEqual(result["tool_use_id"], "call-1")
        self.assertEqual(json.loads(result["content"])["call_id"], "call-1")
        self.assertEqual(self.calls, ["a"])

    def test_target_values_are_not_coerced(self):
        for target in (None, [], {}, True, 42):
            with self.subTest(target=target):
                result = self.runner.run("read_file", {"target": target}, signal=VERIFIED)
                self.assertEqual(result["verdict"], "HALT")
                self.assertFalse(result["attempted"])
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
