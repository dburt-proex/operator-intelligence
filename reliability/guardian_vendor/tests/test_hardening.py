"""Regression tests for execution, trust and durable audit boundaries."""
import copy
import io
import json
import multiprocessing
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from guardian import AuditError, ExecutionAuditError, GuardianAgent, Verdict
from guardian.adapter import GovernedToolRunner
from guardian.audit import AuditLedger, GENESIS, _hash
from guardian.cli import main
from guardian.engine import validate
from guardian.models import Action
from guardian.vil import Signal, evaluate


SIGNAL = {"content": "x" * 130, "source": "ops", "signal_score": 9,
          "source_pointers": ["a", "b", "c"],
          "metadata": {str(i): i for i in range(5)}}


def envelope():
    return {"signal": copy.deepcopy(SIGNAL),
            "action": {"id": "request-1", "type": "read_file", "params": {"target": "safe"}}}


def append_worker(path):
    for i in range(5):
        AuditLedger(path).append({"i": i})


class HardeningTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "audit.jsonl"
        self.agent = GuardianAgent(self.path)

    def test_malformed_inputs_never_execute(self):
        bad = [None, [], "read", {}, {"action": []}, {"signal": []}]
        for field, value in [("params", []), ("type", None), ("id", ""),
                             ("payload", {}), ("extra", True)]:
            e = envelope()
            e["action"][field] = value
            bad.append(e)
        for score in [float("nan"), float("inf"), -1, 11, "9", True]:
            e = envelope()
            e["signal"]["signal_score"] = score
            bad.append(e)
        for key, value in [("risk_flags", "unsafe_action"), ("metadata", []),
                           ("source_pointers", [None]), ("content", {})]:
            e = envelope()
            e["signal"][key] = value
            bad.append(e)
        for e in bad:
            with self.subTest(e=repr(e)):
                calls = []
                d = self.agent.govern_and_execute(e, lambda a, calls=calls: calls.append(a))
                self.assertIs(d.verdict, Verdict.HALT)
                self.assertFalse(calls)

    def test_large_deep_and_cyclic_inputs_halt(self):
        e = envelope()
        e["action"]["payload"] = "a" * 1_048_577
        self.assertIs(self.agent.govern(e).verdict, Verdict.HALT)
        e = envelope()
        nested = {}
        for _ in range(34):
            nested = {"a": nested}
        e["action"]["params"] = nested
        self.assertIs(self.agent.govern(e).verdict, Verdict.HALT)
        e["action"]["params"] = e
        self.assertIs(self.agent.govern(e).verdict, Verdict.HALT)

    def test_evidence_verification_required(self):
        agent = GuardianAgent(self.path, require_verified_evidence=True)
        self.assertIs(agent.govern(envelope()).verdict, Verdict.HALT)
        for value in [False, None, 1, "true"]:
            agent = GuardianAgent(self.path, evidence_verifier=lambda e, value=value: value)
            self.assertIs(agent.govern(envelope()).verdict, Verdict.HALT)
        agent = GuardianAgent(self.path, evidence_verifier=lambda e: True)
        self.assertIs(agent.govern(envelope()).verdict, Verdict.ALLOW)

    def test_verifier_failure_halts(self):
        def fail(e):
            raise RuntimeError("sensitive exception")
        d = GuardianAgent(self.path, evidence_verifier=fail).govern(envelope())
        self.assertIs(d.verdict, Verdict.HALT)
        self.assertNotIn("sensitive exception", self.path.read_text())

    def test_snapshot_prevents_reparse_after_audit(self):
        e = envelope()
        original = self.agent.ledger.append
        def mutate(record):
            entry = original(record)
            e["action"]["type"] = "wire_transfer"
            e["action"]["params"]["target"] = "changed"
            return entry
        with patch.object(self.agent.ledger, "append", side_effect=mutate):
            d = self.agent.govern_and_execute(e, lambda a: a.type + a.params["target"])
        self.assertEqual(d.execution_result, "read_filesafe")

    def test_verifier_cannot_mutate_governed_action(self):
        def mutate(e):
            e["action"]["type"] = "wire_transfer"
            return True
        d = GuardianAgent(self.path, evidence_verifier=mutate).govern_and_execute(
            envelope(), lambda a: a.type)
        self.assertEqual(d.execution_result, "read_file")

    def test_executor_failure_is_error_not_secret(self):
        def fail(**kwargs):
            raise ValueError("private-tool-exception")
        runner = GovernedToolRunner({"read_file": fail}, self.agent)
        r = runner.handle_tool_use_block({"type": "tool_use", "id": "t1",
            "name": "read_file", "input": {}}, signal=SIGNAL)
        self.assertTrue(r["is_error"])
        self.assertNotIn("private-tool-exception", self.path.read_text() + r["content"])
        out = json.loads(r["content"])
        self.assertTrue(out["attempted"])
        self.assertFalse(out["executed"])

    def test_outputs_not_logged(self):
        d = self.agent.govern_and_execute(envelope(), lambda a: "confidential-output")
        self.assertEqual(d.execution_result, "confidential-output")
        self.assertNotIn("confidential-output", self.path.read_text())
        entries = self.agent.ledger.entries()
        self.assertEqual(entries[1]["record"]["decision_hash"], entries[0]["entry_hash"])
        self.assertEqual(d.to_dict()["entry_hash"], entries[1]["entry_hash"])

    def test_pre_execution_audit_failure_blocks(self):
        calls = []
        with patch.object(self.agent.ledger, "append", side_effect=AuditError("failed")):
            with self.assertRaises(AuditError):
                self.agent.govern_and_execute(envelope(), lambda a: calls.append(a))
        self.assertFalse(calls)

    def test_post_execution_audit_failure_reports_attempt(self):
        original = self.agent.ledger.append
        def append(record):
            if record.get("event") == "execution":
                raise AuditError("failure")
            return original(record)
        with patch.object(self.agent.ledger, "append", side_effect=append):
            with self.assertRaises(ExecutionAuditError) as ctx:
                self.agent.govern_and_execute(envelope(), lambda a: "done")
        self.assertTrue(ctx.exception.decision.executed)
        self.assertTrue(ctx.exception.decision.attempted)

    def test_corruption_blocks_append(self):
        for raw in ["not json\n", "{}\n", "[]\n", "\n", '{"ts":1}',
                    '{"ts":1,"record":{}}\n']:
            with self.subTest(raw=raw):
                self.path.write_text(raw)
                self.assertFalse(self.agent.ledger.verify()[0])
                with self.assertRaises(AuditError):
                    self.agent.govern(envelope())
                self.assertEqual(self.path.read_text(), raw)

    def test_timestamp_tampering_and_anchor_truncation(self):
        ledger = self.agent.ledger
        first = ledger.append({"a": 1})
        last = ledger.append({"a": 2})
        self.assertTrue(ledger.verify(last["entry_hash"])[0])
        self.path.write_text(json.dumps(first) + "\n")
        self.assertTrue(ledger.verify()[0])
        self.assertFalse(ledger.verify(last["entry_hash"])[0])
        first["ts"] = "edited"
        self.path.write_text(json.dumps(first) + "\n")
        self.assertFalse(ledger.verify()[0])

    def test_legacy_ledger_can_be_extended(self):
        old = {"ts": "legacy", "record": {"a": 1}, "prev_hash": GENESIS}
        old["entry_hash"] = _hash(GENESIS, old["record"])
        self.path.write_text(json.dumps(old) + "\n")
        self.agent.ledger.append({"a": 2})
        self.assertTrue(self.agent.ledger.verify()[0])

    def test_threads_share_chain(self):
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(lambda i: AuditLedger(self.path).append({"i": i}), range(30)))
        self.assertTrue(self.agent.ledger.verify()[0])
        self.assertEqual(len(self.agent.ledger.entries()), 30)

    def test_processes_share_chain(self):
        ctx = multiprocessing.get_context("spawn")
        processes = [ctx.Process(target=append_worker, args=(str(self.path),)) for _ in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join(20)
            if p.is_alive():
                p.terminate()
                p.join()
                self.fail("Audit worker timed out")
            self.assertEqual(p.exitcode, 0)
        self.assertTrue(self.agent.ledger.verify()[0])
        self.assertEqual(len(self.agent.ledger.entries()), 15)

    def test_secret_json_fields_halt_without_logging_payload(self):
        e = envelope()
        e["action"]["params"] = {"password": "fixture-credential"}
        d = self.agent.govern(e)
        self.assertIs(d.verdict, Verdict.HALT)
        self.assertNotIn("fixture-credential", self.path.read_text())

    def test_destructive_command_variants_halt(self):
        for command in ["rm -fr /tmp/x", "rm -r -f /tmp/x", "Remove-Item C:\\data -Recurse -Force", "rmdir /s /q data"]:
            self.assertIs(validate(Action("a", "read_file", payload=command)).verdict, Verdict.HALT)

    def test_ambiguous_and_mutating_queries_never_allow(self):
        for kind, payload in [("query", "select 1"), ("fetch", ""), ("get", ""),
                              ("read_file", "UPDATE users SET active=0")]:
            self.assertIsNot(validate(Action("a", kind, payload=payload)).verdict, Verdict.ALLOW)

    def test_adapter_empty_signal_does_not_inherit_default(self):
        runner = GovernedToolRunner({"read_file": lambda: "ok"}, self.agent, default_signal=SIGNAL)
        self.assertEqual(runner.run("read_file", {}, signal={})["verdict"], "HALT")

    def test_registered_policy_cannot_be_downgraded(self):
        for name in ["wire_transfer", "delete_database", "send_email", "db_write", "query"]:
            with self.assertRaises(ValueError):
                GovernedToolRunner({name: lambda: "bad"}, self.agent,
                                   type_map={name: "read_file"})

    def test_custom_tool_mapping_is_supported(self):
        runner = GovernedToolRunner({"read_kpi": lambda: "ok"}, self.agent,
                                   type_map={"read_kpi": "read_file"})
        self.assertTrue(runner.run("read_kpi", {}, SIGNAL)["executed"])

    def test_async_execution_is_not_reported_as_success(self):
        async def async_tool():
            return "ok"
        with self.assertRaises(ValueError):
            GovernedToolRunner({"read_file": async_tool}, self.agent)
        d = self.agent.govern_and_execute(envelope(), lambda a: async_tool())
        self.assertFalse(d.executed)
        self.assertTrue(d.execution_error)

    def test_disk_sync_failure_prevents_execution(self):
        calls = []
        with patch("guardian.audit.os.fsync", side_effect=OSError("disk error")):
            with self.assertRaises(AuditError):
                self.agent.govern_and_execute(envelope(), lambda a: calls.append(a))
        self.assertFalse(calls)

    def test_secret_identifiers_are_redacted(self):
        e = envelope()
        e["action"]["id"] = "sk-" + "a" * 25
        self.assertIs(self.agent.govern(e).verdict, Verdict.HALT)
        self.assertNotIn(e["action"]["id"], self.path.read_text())

    def test_duplicate_ledger_keys_fail_verification(self):
        entry = self.agent.ledger.append({"a": 1})
        raw = json.dumps(entry).replace('"record":', '"record": {}, "record":', 1)
        self.path.write_text(raw + "\n")
        self.assertFalse(self.agent.ledger.verify()[0])

    def test_lock_contention_prevents_execution(self):
        calls = []
        self.agent.ledger.lock_timeout = 0.02
        with self.agent.ledger._locked(write=True):
            with self.assertRaises(AuditError):
                self.agent.govern_and_execute(envelope(), lambda a: calls.append(a))
        self.assertFalse(calls)

    def test_verification_status_and_runtime_are_audited(self):
        d = GuardianAgent(self.path, evidence_verifier=lambda e: True).govern(envelope())
        self.assertTrue(d.evidence_verified)
        record = self.agent.ledger.entries()[0]["record"]
        self.assertTrue(record["evidence_verified"])
        self.assertEqual(record["runtime_version"], "1.1.0")
        self.assertEqual(record["event"], "decision")

    def test_long_identifiers_and_invalid_mode_halt(self):
        for field, value in [("id", "x" * 129), ("type", "x" * 65)]:
            e = envelope()
            e["action"][field] = value
            self.assertIs(self.agent.govern(e).verdict, Verdict.HALT)
        with self.assertRaises(ValueError):
            GuardianAgent(self.path, require_verified_evidence="false")

    def test_deterministic_decision_fields(self):
        first = self.agent.govern(envelope()).to_dict()
        second = self.agent.govern(envelope()).to_dict()
        for data in [first, second]:
            data.pop("entry_hash")
            data.pop("decision_hash")
        self.assertEqual(first, second)

    def test_adapter_invalid_inputs_and_unregistered_read_tool(self):
        runner = GovernedToolRunner({}, self.agent)
        for value in [None, [], "input", {"a": float("nan")}]:
            self.assertEqual(runner.run("read_file", value, SIGNAL)["verdict"], "HALT")
        out = runner.run("read_file", {}, SIGNAL)
        self.assertEqual(out["verdict"], "REVIEW")
        self.assertFalse(out["executed"])

    def test_invalid_thresholds_and_normalized_flags(self):
        self.assertEqual(evaluate(Signal(risk_flags=[" UNSAFE_ACTION "])).route.value, "HALT")
        for thresholds in [{}, {"pass": 4, "review": 8, "clarify": 3},
                           {"pass": float("nan"), "review": 5, "clarify": 3}]:
            with self.assertRaises(ValueError):
                evaluate(Signal(), thresholds)

    def test_cli_invalid_duplicate_json_and_corrupt_audit(self):
        request = Path(self.temp.name) / "request.json"
        request.write_text('{"action":{},"action":{}}')
        with redirect_stdout(io.StringIO()):
            self.assertEqual(main(["check", str(request), "--ledger", str(self.path)]), 2)
        self.path.write_text("corrupt\n")
        request.write_text(json.dumps(envelope()))
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(main(["check", str(request), "--ledger", str(self.path)]), 2)
        self.assertIn("audit unavailable", output.getvalue())


if __name__ == "__main__":
    unittest.main()
