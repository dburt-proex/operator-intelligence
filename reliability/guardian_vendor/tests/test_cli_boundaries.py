"""CLI failure contracts and a scoped, fixture-only integration example."""
import importlib.util
import io
import json
import stat
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from threading import Barrier
from unittest.mock import patch

from guardian.audit import AuditError, AuditLedger, GENESIS
from guardian.cli import main


class CliBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.request = self.root / "request.json"
        self.request.write_text(json.dumps({"action": {"id": "a", "type": "read_file"}}))

    def invoke(self, arguments):
        with redirect_stdout(io.StringIO()) as output:
            code = main(arguments)
        return code, json.loads(output.getvalue())

    def test_invalid_ledger_path_never_claims_integrity(self):
        for path in ["", "\x00", "   "]:
            with self.subTest(path=repr(path)):
                code, out = self.invoke(["verify", "--ledger", path])
                self.assertEqual(code, 2)
                self.assertFalse(out["intact"])
                if path:
                    self.assertNotIn(path, out.get("detail", ""))

    def test_invalid_ledger_path_check_returns_sanitized_error(self):
        for path in ["", "\x00", "   "]:
            with self.subTest(path=repr(path)):
                code, out = self.invoke(["check", str(self.request), "--ledger", path])
                self.assertEqual(code, 2)
                self.assertEqual(out["error"], "audit unavailable; execution blocked")

    def test_invalid_paths_are_rejected_by_library(self):
        for path in ["", "\x00", "   ", None]:
            with self.subTest(path=repr(path)), self.assertRaises((ValueError, TypeError)):
                AuditLedger(path)

    def test_invalid_anchor_never_claims_integrity(self):
        ledger = self.root / "missing.jsonl"
        for anchor in ["", "0" * 63, "z" * 64, 1, True, [], GENESIS.upper() + "x"]:
            with self.subTest(anchor=repr(anchor)):
                self.assertFalse(AuditLedger(ledger).verify(expected_head=anchor)[0])
        self.assertTrue(AuditLedger(ledger).verify(expected_head=GENESIS)[0])

    def test_inspection_failure_is_not_an_empty_ledger(self):
        ledger = AuditLedger(self.root / "audit.jsonl")
        with patch("guardian.audit.os.stat", side_effect=PermissionError("private-inspection-error")):
            ok, detail = ledger.verify()
            self.assertFalse(ok)
            self.assertNotIn("private-inspection-error", detail)
            with self.assertRaises(AuditError):
                ledger.entries()

    def test_existing_directory_is_not_a_valid_ledger(self):
        code, out = self.invoke(["verify", "--ledger", str(self.root)])
        self.assertEqual(code, 2)
        self.assertFalse(out["intact"])

    def test_directory_append_fails_before_open(self):
        with patch("guardian.audit.open", side_effect=AssertionError("directory opened")):
            with self.assertRaises(AuditError):
                AuditLedger(self.root).append({"a": 1})

    def test_dangling_target_is_not_empty_history(self):
        ledger = AuditLedger(self.root / "dangling.jsonl")
        with patch("guardian.audit.os.stat", side_effect=FileNotFoundError), \
                patch("guardian.audit.os.lstat", return_value=SimpleNamespace(st_mode=stat.S_IFLNK)):
            self.assertFalse(ledger.verify()[0])
            with self.assertRaises(AuditError):
                ledger.entries()
            with self.assertRaises(AuditError):
                ledger.append({"a": 1})

    def test_concurrent_creation_is_not_misclassified_as_dangling(self):
        ledger = AuditLedger(self.root / "created.jsonl")
        with patch("guardian.audit.os.stat", side_effect=FileNotFoundError), \
                patch("guardian.audit.os.lstat", return_value=SimpleNamespace(st_mode=stat.S_IFREG)):
            self.assertTrue(ledger._exists())

    def test_simultaneous_first_writers_preserve_chain(self):
        for iteration in range(10):
            path = self.root / f"initial-{iteration}.jsonl"
            start = Barrier(4)

            def write(worker, path=path, start=start):
                start.wait(timeout=5)
                return AuditLedger(path).append({"worker": worker})

            with ThreadPoolExecutor(max_workers=4) as pool:
                entries = list(pool.map(write, range(4)))
            self.assertEqual(len({entry["entry_hash"] for entry in entries}), 4)
            self.assertEqual(len(AuditLedger(path).entries()), 4)
            self.assertTrue(AuditLedger(path).verify()[0])

    def test_invalid_path_assignment_preserves_valid_configuration(self):
        ledger = AuditLedger(self.root / "audit.jsonl")
        before = ledger.path
        with self.assertRaises(ValueError):
            ledger.path = "\x00"
        self.assertEqual(ledger.path, before)

    def test_envelope_read_is_bounded_in_bytes(self):
        class ByteBoundedInput(io.BytesIO):
            def read(self, size=-1):
                if size != 1_048_577:
                    raise AssertionError("Envelope read is not byte-bounded")
                return super().read(size)

        data = ByteBoundedInput(b"x" * 1_048_577)
        ledger = self.root / "audit.jsonl"
        with patch("guardian.cli.open", return_value=data):
            code, out = self.invoke(["check", "input.json", "--ledger", str(ledger)])
        self.assertEqual(code, 2)
        self.assertEqual(out["error"], "cannot read valid envelope")
        self.assertFalse(ledger.exists())

    def test_invalid_utf8_returns_error_without_audit_file(self):
        self.request.write_bytes(b"\xff\xfe\xff")
        ledger = self.root / "audit.jsonl"
        code, out = self.invoke(["check", str(self.request), "--ledger", str(ledger)])
        self.assertEqual(code, 2)
        self.assertEqual(out["error"], "cannot read valid envelope")
        self.assertFalse(ledger.exists())

    def test_readonly_example_runs_and_blocks_changed_request(self):
        script = Path(__file__).resolve().parents[1] / "scripts" / "readonly_integration.py"
        spec = importlib.util.spec_from_file_location("readonly_integration", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with redirect_stdout(io.StringIO()) as output:
            result = module.main()
        self.assertEqual(result["allowed"], "ALLOW")
        self.assertEqual(result["modified"], "HALT")
        self.assertEqual(result["calls"], 1)
        self.assertTrue(result["audit_intact"])
        self.assertIn("local fixture", output.getvalue())


if __name__ == "__main__":
    unittest.main()
