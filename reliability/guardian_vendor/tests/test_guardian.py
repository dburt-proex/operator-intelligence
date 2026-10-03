import json
import os
import tempfile
import unittest
from pathlib import Path

from guardian import GuardianAgent, Verdict
from guardian.audit import AuditLedger
from guardian.engine import validate
from guardian.models import Action, most_restrictive
from guardian import vil


def env(action, signal=None):
    return {"action": action, "signal": signal or {
        "content": "Verified operational request from the internal ops queue with full ticket reference, requester identity, and approved runbook step attached." ,
        "source": "ops_queue", "source_pointers": ["TICKET-42", "RUNBOOK-7", "REQ-9"],
        "metadata": {"ticket": "42", "requester": "db", "runbook": "7", "env": "prod", "step": "read"},
        "signal_score": 9.0}}


class TestCasaRules(unittest.TestCase):
    def test_r1_destruction_halts(self):
        r = validate(Action(id="a", type="delete_database", target="prod"))
        self.assertIs(r.verdict, Verdict.HALT)
        self.assertIn("R1_IRREVERSIBLE_DESTRUCTION", r.triggered_by)

    def test_r1_pattern_rm_rf(self):
        r = validate(Action(id="a", type="shell", payload="rm -rf /var/data"))
        self.assertIs(r.verdict, Verdict.HALT)

    def test_r2_financial_halts(self):
        r = validate(Action(id="a", type="wire_transfer", payload="$5000"))
        self.assertIs(r.verdict, Verdict.HALT)

    def test_r3_secret_halts(self):
        r = validate(Action(id="a", type="log", payload="api_key=sk-abcdefghijklmnopqrstu"))
        self.assertIs(r.verdict, Verdict.HALT)

    def test_r4_broadcast_reviews(self):
        r = validate(Action(id="a", type="send_email", target="all@list"))
        self.assertIs(r.verdict, Verdict.REVIEW)

    def test_r5_mutation_reviews(self):
        r = validate(Action(id="a", type="db_write", target="users"))
        self.assertIs(r.verdict, Verdict.REVIEW)

    def test_r6_readonly_allows(self):
        r = validate(Action(id="a", type="read_file", target="report.txt"))
        self.assertIs(r.verdict, Verdict.ALLOW)

    def test_unknown_fails_safe_to_review(self):
        r = validate(Action(id="a", type="teleport"))
        self.assertIs(r.verdict, Verdict.REVIEW)
        self.assertEqual(r.triggered_by, ["DEFAULT_FAIL_SAFE"])

    def test_most_restrictive_merge(self):
        self.assertIs(most_restrictive([Verdict.ALLOW, Verdict.HALT]), Verdict.HALT)
        self.assertIs(most_restrictive([]), Verdict.REVIEW)


class TestVil(unittest.TestCase):
    def test_verification_cap(self):
        s = vil.Signal(content="short", signal_score=10.0)
        self.assertLess(vil.vil_score(s), 5.0)  # weak evidence caps high claim

    def test_pass_route(self):
        s = vil.Signal(content="x" * 130, source="crm",
                       source_pointers=["a", "b", "c"],
                       metadata={str(i): i for i in range(5)},
                       signal_score=9.5)
        self.assertIs(vil.evaluate(s).route, vil.Route.PASS)

    def test_speculative_penalty(self):
        base = vil.Signal(content="a" * 50, source="crm")
        spec = vil.Signal(content="a" * 44 + " rumor", source="crm")
        self.assertGreater(vil.verifiability_score(base),
                           vil.verifiability_score(spec))

    def test_halt_flag_overrides_score(self):
        s = vil.Signal(content="x" * 130, source="crm", signal_score=10.0,
                       source_pointers=["a"], metadata={"k": 1},
                       risk_flags=["secrets"])
        self.assertIs(vil.evaluate(s).route, vil.Route.HALT)

    def test_archive_route(self):
        self.assertIs(vil.evaluate(vil.Signal(content="", signal_score=0.5)).route,
                      vil.Route.ARCHIVE)


class TestAuditLedger(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.dir.name, "audit.jsonl")

    def tearDown(self):
        self.dir.cleanup()

    def test_chain_intact(self):
        led = AuditLedger(self.path)
        led.append({"a": 1})
        led.append({"a": 2})
        ok, msg = led.verify()
        self.assertTrue(ok, msg)

    def test_tamper_detected(self):
        led = AuditLedger(self.path)
        led.append({"a": 1})
        led.append({"a": 2})
        lines = Path(self.path).read_text(encoding="utf-8").splitlines()
        e = json.loads(lines[0])
        e["record"]["a"] = 999
        lines[0] = json.dumps(e, sort_keys=True)
        Path(self.path).write_text("\n".join(lines) + "\n", encoding="utf-8")
        ok, msg = led.verify()
        self.assertFalse(ok)
        self.assertIn("tamper", msg)

    def test_deletion_detected(self):
        led = AuditLedger(self.path)
        led.append({"a": 1})
        led.append({"a": 2})
        lines = Path(self.path).read_text(encoding="utf-8").splitlines()
        Path(self.path).write_text(lines[1] + "\n", encoding="utf-8")
        self.assertFalse(led.verify()[0])


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.agent = GuardianAgent(os.path.join(self.dir.name, "audit.jsonl"))

    def tearDown(self):
        self.dir.cleanup()

    def test_allow_executes(self):
        d = self.agent.govern_and_execute(
            env({"id": "1", "type": "read_file", "target": "kpi.csv"}),
            lambda a: f"read {a.target}")
        self.assertIs(d.verdict, Verdict.ALLOW)
        self.assertTrue(d.executed)
        self.assertEqual(d.execution_result, "read kpi.csv")

    def test_halt_never_executes(self):
        ran = []
        d = self.agent.govern_and_execute(
            env({"id": "2", "type": "wire_transfer", "payload": "$9,000 usd"}),
            lambda a: ran.append(1))
        self.assertIs(d.verdict, Verdict.HALT)
        self.assertFalse(d.executed)
        self.assertEqual(ran, [])

    def test_weak_signal_blocks_readonly_action(self):
        # Read-only action (policy ALLOW) but no supporting evidence → HALT.
        d = self.agent.govern({"action": {"id": "3", "type": "read_file"},
                               "signal": {"content": "", "signal_score": 1.0}})
        self.assertIs(d.verdict, Verdict.HALT)

    def test_vil_review_upgrades_allow(self):
        d = self.agent.govern({"action": {"id": "4", "type": "read_file"},
                               "signal": {"content": "x" * 130, "source": "crm",
                                          "signal_score": 6.0}})
        self.assertIs(d.verdict, Verdict.REVIEW)

    def test_malformed_envelope_fails_safe(self):
        d = self.agent.govern({"action": {"type": []}})  # type coerces; still governed
        self.assertIn(d.verdict, (Verdict.REVIEW, Verdict.HALT))

    def test_every_decision_ledgered_and_chained(self):
        self.agent.govern(env({"id": "5", "type": "read_file"}))
        self.agent.govern(env({"id": "6", "type": "drop_table", "payload": "drop table users"}))
        ok, msg = self.agent.ledger.verify()
        self.assertTrue(ok, msg)
        self.assertEqual(len(self.agent.ledger.entries()), 2)


if __name__ == "__main__":
    unittest.main()
