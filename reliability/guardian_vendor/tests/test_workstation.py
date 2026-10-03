"""Internal v1 admission and execution acceptance for the workstation profile."""
import copy
import tempfile
import unittest
import stat
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from guardian import AuditError, Verdict
from guardian.workstation import MAX_READ_BYTES, WorkstationGuardian


def request(kind="read_file", target="source.txt", params=None):
    return {"signal": {"content": "x" * 130, "source": "internal-operator",
        "source_pointers": ["request", "scope", "evidence"], "signal_score": 9,
        "metadata": {str(i): i for i in range(5)}},
        "action": {"id": "internal-1", "type": kind, "target": target,
                   "params": {} if params is None else params}}


class WorkstationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "source.txt").write_bytes(b"internal fixture\n")
        self.ledger = self.root / "audit.jsonl"
        self.agent = WorkstationGuardian(self.root, self.ledger, evidence_verifier=lambda e: True)

    def test_scoped_read_executes_after_verified_admission(self):
        def read(action):
            entries = self.agent.ledger.entries()
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0]["record"]["verdict"], "ALLOW")
            self.assertTrue(entries[0]["record"]["evidence_verified"])
            return self.agent.read_file(action)
        d = self.agent.govern_and_execute(request(), read)
        self.assertTrue(d.executed)
        self.assertEqual(d.execution_result, "internal fixture\n")
        self.assertTrue(self.agent.ledger.verify(d.entry_hash)[0])

    def test_mutating_and_process_actions_remain_reviewed(self):
        for kind, target, params in [
            ("file_write", "new.txt", {"content": "draft"}),
            ("config_change", "settings.toml", {"content": "enabled=true"}),
            ("shell", ".", {"argv": ["python", "--version"]}),
            ("git", ".", {"argv": ["status", "--short"]}),
            ("tool_call", ".", {"name": "internal_tool"}),
        ]:
            calls = []
            d = self.agent.govern_and_execute(request(kind, target, params), lambda a, calls=calls: calls.append(a))
            self.assertIs(d.verdict, Verdict.REVIEW)
            self.assertFalse(calls)
        self.assertFalse((self.root / "new.txt").exists())
        self.assertEqual(len(self.agent.ledger.entries()), 5)

    def test_destructive_git_commands_halt(self):
        for argv in [["reset", "--hard"], ["git", "reset", "HEAD", "--hard"],
                     ["clean", "-fd"], ["git.exe", "clean", "--force"]]:
            self.assertIs(self.agent.govern(request("git", ".", {"argv": argv})).verdict, Verdict.HALT)

    def test_structured_destructive_shell_command_halts(self):
        d = self.agent.govern(request("shell", ".", {"argv": ["rm", "-rf", "data"]}))
        self.assertIs(d.verdict, Verdict.HALT)

    def test_host_verifier_failure_is_audited_without_its_message(self):
        def fail(envelope):
            raise RuntimeError("fixture-sensitive-verifier-message")
        agent = WorkstationGuardian(self.root, self.ledger, evidence_verifier=fail)
        d = agent.govern(request())
        self.assertIs(d.verdict, Verdict.HALT)
        self.assertEqual(len(agent.ledger.entries()), 1)
        self.assertNotIn("fixture-sensitive-verifier-message", self.ledger.read_text())

    def test_outside_and_sensitive_targets_halt_before_execution(self):
        targets = ["../outside", str(self.root / "source.txt"), ".env", ".env.local", ".ssh/id_rsa",
                   ".aws/credentials", "private.pem", "source.txt:private", "audit.jsonl", ""]
        for target in targets:
            calls = []
            d = self.agent.govern_and_execute(request(target=target), lambda a, calls=calls: calls.append(a))
            self.assertIs(d.verdict, Verdict.HALT)
            self.assertFalse(calls)

    def test_mismatched_path_or_cwd_halts(self):
        for params in [{"path": "other.txt"}, {"target": "other.txt"}, {"cwd": "../"},
                       {"filename": "other.txt"}, {"command": "ignored"}]:
            self.assertIs(self.agent.govern(request(params=params)).verdict, Verdict.HALT)
        self.assertIs(self.agent.govern(request("shell", ".", {"cwd": "../"})).verdict, Verdict.HALT)

    def test_symlink_and_reparse_targets_halt(self):
        for info in [SimpleNamespace(st_mode=stat.S_IFLNK),
                     SimpleNamespace(st_mode=stat.S_IFREG, st_file_attributes=0x400)]:
            with patch("pathlib.Path.lstat", return_value=info):
                self.assertIs(self.agent.govern(request()).verdict, Verdict.HALT)

    def test_read_limit_is_host_configured_and_validated(self):
        for value in [0, -1, True, "64", 1_048_577]:
            with self.assertRaises(ValueError):
                WorkstationGuardian(self.root, self.ledger, evidence_verifier=lambda e: True,
                                    max_read_bytes=value)
        agent = WorkstationGuardian(self.root, self.ledger, evidence_verifier=lambda e: True,
                                    max_read_bytes=4)
        d = agent.govern_and_execute(request(), agent.read_file)
        self.assertFalse(d.executed)
        self.assertIsNone(d.execution_result)

    def test_no_verifier_and_unknown_action_fail_closed(self):
        with self.assertRaises(ValueError):
            WorkstationGuardian(self.root, self.ledger, evidence_verifier=None)
        self.assertIs(self.agent.govern(request("unknown_tool", ".")).verdict, Verdict.HALT)
        other = WorkstationGuardian(self.root, self.ledger, evidence_verifier=lambda e: False)
        self.assertIs(other.govern(request()).verdict, Verdict.HALT)

    def test_host_verifier_binds_exact_request(self):
        approved = request()
        agent = WorkstationGuardian(self.root, self.ledger, evidence_verifier=lambda e: e == approved)
        altered = copy.deepcopy(approved)
        altered["signal"]["metadata"]["0"] = "different"
        self.assertIs(agent.govern(altered).verdict, Verdict.HALT)
        self.assertIs(agent.govern(approved).verdict, Verdict.ALLOW)

    def test_large_binary_and_credential_outputs_are_not_returned(self):
        for raw in [b"x" * (MAX_READ_BYTES + 1), b"\xff", b"password=fixture-private-value"]:
            (self.root / "source.txt").write_bytes(raw)
            d = self.agent.govern_and_execute(request(), self.agent.read_file)
            self.assertFalse(d.executed)
            self.assertIsNone(d.execution_result)
            self.assertTrue(d.execution_error)
            self.assertNotIn("fixture-private-value", self.ledger.read_text())

    def test_audit_failure_prevents_file_read(self):
        with patch.object(self.agent.ledger, "append", side_effect=AuditError("failure")), \
                patch.object(self.agent, "read_file", side_effect=AssertionError("read started")):
            with self.assertRaises(AuditError):
                self.agent.govern_and_execute(request(), self.agent.read_file)


if __name__ == "__main__":
    unittest.main()
