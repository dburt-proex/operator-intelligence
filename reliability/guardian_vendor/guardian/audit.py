"""Durable process-locked hash chain. Use a trusted local filesystem.

V2 seals timestamps; legacy V1 remains readable. Detecting suffix truncation
requires an independently retained head. Host administrators can rewrite files.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
import stat
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from .validation import MAX_BYTES, snapshot

GENESIS = "0" * 64


class AuditError(RuntimeError):
    """Audit unavailable or invalid: stop execution."""


def _canonical(record):
    return json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _hash(prev_hash, record):
    return hashlib.sha256((prev_hash + _canonical(record)).encode()).hexdigest()


def _entry_hash(entry):
    if entry.get("version") == 2:
        return _hash(entry["prev_hash"], {k: v for k, v in entry.items() if k != "entry_hash"})
    return _hash(entry["prev_hash"], entry["record"])


class AuditLedger:
    def __init__(self, path="guardian_audit.jsonl", lock_timeout=10.0):
        self.path = path
        self.lock_timeout = lock_timeout

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        path = os.fsdecode(os.fspath(value))
        if not path.strip() or "\x00" in path:
            raise ValueError("Audit path must be nonempty and contain no null characters")
        self._path = path

    def _exists(self):
        try:
            info = os.stat(self.path)
        except FileNotFoundError:
            # A dangling symlink is unavailable storage, not an empty history.
            try:
                info = os.lstat(self.path)
            except FileNotFoundError:
                return False
            except (OSError, ValueError):
                raise AuditError("Cannot inspect audit ledger") from None
            if stat.S_ISLNK(info.st_mode):
                raise AuditError("Audit ledger target is unavailable") from None
            # A cooperating writer may create a regular file between stat and
            # lstat. Continue with that actual metadata rather than rejecting it.
        except (OSError, ValueError):
            raise AuditError("Cannot inspect audit ledger") from None
        if not stat.S_ISREG(info.st_mode):
            raise AuditError("Audit ledger must be a regular file")
        return True

    @property
    def lock_timeout(self):
        return self._lock_timeout

    @lock_timeout.setter
    def lock_timeout(self, value):
        try:
            valid = type(value) in (int, float) and value >= 0 and math.isfinite(value)
        except OverflowError:
            valid = False
        if not valid:
            raise ValueError("lock_timeout must be a finite nonnegative number")
        self._lock_timeout = value

    @contextmanager
    def _locked(self, write=False):
        self._exists()
        try:
            stream = open(self.path, "a+b" if write else "rb")
        except OSError:
            raise AuditError("Cannot open audit ledger") from None
        acquired = False
        try:
            deadline = time.monotonic() + self.lock_timeout
            while not acquired:
                try:
                    stream.seek(0)
                    os.lseek(stream.fileno(), 0, os.SEEK_SET)
                    if os.name == "nt":
                        import msvcrt
                        msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    acquired = True
                except OSError:
                    if time.monotonic() >= deadline:
                        raise AuditError("Audit ledger lock timed out") from None
                    time.sleep(0.01)
            yield stream
        except (OSError, UnicodeError, ValueError, TypeError, KeyError, RecursionError):
            raise AuditError("Audit ledger read or write failed") from None
        finally:
            try:
                try:
                    if acquired:
                        stream.seek(0)
                        os.lseek(stream.fileno(), 0, os.SEEK_SET)
                        if os.name == "nt":
                            import msvcrt
                            msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                        else:
                            import fcntl
                            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
                finally:
                    stream.close()
            except OSError:
                raise AuditError("Cannot release audit ledger") from None

    @staticmethod
    def _read(stream, collect=True):
        stream.seek(0)
        prev, entries = GENESIS, []
        i = 0
        while True:
            line = stream.readline(MAX_BYTES + 2)
            if not line:
                break
            i += 1
            if len(line) > MAX_BYTES + 1:
                raise AuditError(f"Oversized audit entry {i}")
            if not line.endswith(b"\n") or not line.strip():
                raise AuditError(f"Incomplete or blank entry {i}")
            try:
                def unique_object(pairs):
                    obj = {}
                    for key, value in pairs:
                        if key in obj:
                            raise ValueError("Duplicate ledger key")
                        obj[key] = value
                    return obj
                entry = json.loads(line, object_pairs_hook=unique_object)
                expected = {"ts", "record", "prev_hash", "entry_hash"}
                if type(entry) is not dict:
                    raise ValueError()
                if "version" in entry:
                    if type(entry["version"]) is not int or entry["version"] != 2:
                        raise ValueError()
                    expected.add("version")
                if (set(entry) != expected or type(entry["record"]) is not dict or
                        type(entry["ts"]) is not str):
                    raise ValueError()
                snapshot(entry)
                if entry["prev_hash"] != prev:
                    raise AuditError(f"chain break at entry {i}: prev_hash mismatch")
                if _entry_hash(entry) != entry["entry_hash"]:
                    raise AuditError(f"tamper detected at entry {i}: hash mismatch")
            except (ValueError, TypeError, KeyError, RecursionError):
                raise AuditError(f"Malformed audit entry {i}") from None
            if collect:
                entries.append(entry)
            prev = entry["entry_hash"]
        return entries, prev

    def append(self, record):
        record = snapshot(record)
        if type(record) is not dict:
            raise ValueError("Audit record must be an object")
        with self._locked(write=True) as stream:
            _, prev = self._read(stream, collect=False)
            entry = {"version": 2, "ts": datetime.now(timezone.utc).isoformat(),
                     "record": record, "prev_hash": prev}
            entry["entry_hash"] = _entry_hash(entry)
            # Validate the sealed object, including metadata and added nesting,
            # before writing. Every successful append must pass its own reader.
            snapshot(entry)
            stream.seek(0, os.SEEK_END)
            stream.write((_canonical(entry) + "\n").encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
            return entry

    def verify(self, expected_head=None):
        if expected_head is not None and (type(expected_head) is not str or
                len(expected_head) != 64 or any(c not in "0123456789abcdef" for c in expected_head)):
            return False, "Invalid trusted ledger head"
        try:
            if not self._exists():
                if expected_head is not None and expected_head != GENESIS:
                    return False, "Missing anchored ledger"
                return True, "empty ledger"
            with self._locked() as stream:
                _, head = self._read(stream, collect=False)
            if expected_head is not None and head != expected_head:
                return False, "Ledger head does not match trusted anchor"
            return True, "chain intact"
        except AuditError as error:
            return False, str(error)

    def entries(self):
        if not self._exists():
            return []
        with self._locked() as stream:
            return self._read(stream)[0]
