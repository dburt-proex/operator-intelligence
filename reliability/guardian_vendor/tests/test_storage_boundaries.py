"""Storage regressions: successful writes must be readable and verifiable."""
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from guardian import GuardianAgent
from guardian.audit import AuditError, AuditLedger
from guardian.validation import MAX_BYTES, snapshot


class StorageBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "audit.jsonl"
        self.ledger = AuditLedger(self.path)

    def test_record_size_cannot_create_unverifiable_entry(self):
        self.ledger.append({"seed": True})
        before = self.path.read_bytes()
        record = {"data": "a" * (MAX_BYTES - 20)}
        snapshot(record)  # Fits the raw record limit, but not a sealed entry.
        with self.assertRaises(AuditError):
            self.ledger.append(record)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertTrue(self.ledger.verify()[0])

    def test_record_depth_cannot_create_unverifiable_entry(self):
        self.ledger.append({"seed": True})
        before = self.path.read_bytes()
        record = {"value": True}
        for _ in range(31):
            record = {"nested": record}
        snapshot(record)
        with self.assertRaises(AuditError):
            self.ledger.append(record)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertTrue(self.ledger.verify()[0])

    def test_near_limit_valid_record_round_trips(self):
        record = {"data": "a" * (MAX_BYTES - 1024)}
        sealed = self.ledger.append(record)
        self.assertTrue(self.ledger.verify(sealed["entry_hash"])[0])
        self.assertEqual(self.ledger.entries()[0]["record"], record)

    def test_oversized_line_is_read_with_a_limit(self):
        class BoundedStream(io.BytesIO):
            def readline(self, size=-1):
                if not 0 < size <= MAX_BYTES + 2:
                    raise AssertionError("Unbounded audit line read")
                return super().readline(size)

            def __iter__(self):
                raise AssertionError("Unbounded line iteration")

        stream = BoundedStream(b"a" * (MAX_BYTES + 100))
        with self.assertRaises(AuditError):
            AuditLedger._read(stream)
        self.assertLessEqual(stream.tell(), MAX_BYTES + 2)

    def test_invalid_timeout_is_rejected_before_io(self):
        for value in [float("nan"), float("inf"), -1, True, "1", None]:
            with self.subTest(timeout=value), self.assertRaises(ValueError):
                AuditLedger(self.path, lock_timeout=value)
        self.assertFalse(self.path.exists())
        with self.assertRaises(ValueError):
            self.ledger.lock_timeout = float("nan")

    def test_close_failure_is_a_sanitized_audit_error(self):
        real_open = open

        class CloseFailure:
            def __init__(self, *args, **kwargs):
                self.stream = real_open(*args, **kwargs)

            def __getattr__(self, name):
                return getattr(self.stream, name)

            def close(self):
                self.stream.close()
                raise OSError("private-close-failure")

        with patch("guardian.audit.open", side_effect=CloseFailure):
            with self.assertRaises(AuditError) as caught:
                self.ledger.append({"valid": True})
        self.assertNotIn("private-close-failure", str(caught.exception))
        self.assertTrue(self.ledger.verify()[0])

    def test_unlock_failure_blocks_invocation(self):
        if os.name == "nt":
            import msvcrt
            original = msvcrt.locking

            def release_failure(fd, mode, count):
                if mode == msvcrt.LK_UNLCK:
                    raise OSError("private-unlock-failure")
                return original(fd, mode, count)

            target = "msvcrt.locking"
        else:
            import fcntl
            original = fcntl.flock

            def release_failure(fd, mode):
                if mode == fcntl.LOCK_UN:
                    raise OSError("private-unlock-failure")
                return original(fd, mode)

            target = "fcntl.flock"
        signal = {"content": "x" * 130, "source": "ops", "signal_score": 9,
                  "source_pointers": ["a", "b", "c"],
                  "metadata": {str(i): i for i in range(5)}}
        request = {"signal": signal, "action": {"id": "a", "type": "read_file"}}
        calls = []
        with patch(target, side_effect=release_failure), self.assertRaises(AuditError) as caught:
            GuardianAgent(self.path).govern_and_execute(request, lambda a: calls.append(a))
        self.assertFalse(calls)
        self.assertNotIn("private-unlock-failure", str(caught.exception))
        self.assertTrue(self.ledger.verify()[0])

    def test_large_strings_are_rejected_before_serialization(self):
        with patch("guardian.validation.json.dumps", side_effect=AssertionError("serialization started")):
            with self.assertRaises(ValueError):
                snapshot({"input": "x" * (MAX_BYTES + 1)})

    def test_large_collections_are_rejected_before_serialization(self):
        with patch("guardian.validation.json.dumps", side_effect=AssertionError("serialization started")):
            with self.assertRaises(ValueError):
                snapshot(["abcdefgh"] * (MAX_BYTES // 8 + 1))

    def test_large_integer_is_rejected_before_decimal_conversion(self):
        number = 1 << (MAX_BYTES * 4 + 4)
        with patch("guardian.validation.json.dumps", side_effect=AssertionError("serialization started")):
            with self.assertRaises(ValueError):
                snapshot({"input": number})

    def test_unicode_budget_remains_encoded_json_budget(self):
        value = {"input": "\u2603" * 100}
        self.assertEqual(snapshot(value), value)
        with self.assertRaises(ValueError):
            snapshot({"input": "\u2603" * (MAX_BYTES // 6 + 1)})

    def test_corrupt_oversized_line_remains_unchanged(self):
        raw = json.dumps({"data": "a" * (MAX_BYTES + 100)}) + "\n"
        self.path.write_text(raw, encoding="utf-8")
        self.assertFalse(self.ledger.verify()[0])
        with self.assertRaises(AuditError):
            self.ledger.append({"valid": True})
        self.assertEqual(self.path.read_text(encoding="utf-8"), raw)


if __name__ == "__main__":
    unittest.main()
