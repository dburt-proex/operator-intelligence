"""Internal local/runner profile: verified requests and scoped file access.

The operator/host owns the evidence verifier and executor. This profile performs
no credential changes, deployment, approval override or arbitrary shell execution.
"""
from __future__ import annotations

import os
import stat
from pathlib import Path

from .models import Action
from .pipeline import GuardianAgent
from .rules import r3_exposed_secret
from .validation import MAX_BYTES

_FILE_ACTIONS = frozenset({"read_file", "file_write", "config_change"})
_PROCESS_ACTIONS = frozenset({"shell", "shell_command", "git", "git_operation", "tool_call"})
_CREDENTIAL_COMPONENTS = frozenset({".ssh", ".aws", "credentials", "id_rsa", "id_ed25519"})
MAX_READ_BYTES = 65_536


class WorkstationGuardian(GuardianAgent):
    """Guardian v1 local profile for Drew/DAXXER internal repositories.

    Required verification binds the full envelope to trusted operator/CI input.
    Only read_file can automatically execute; writes, configs, shell and Git
    remain REVIEW/HALT. The host must route every executor through this object.
    """
    def __init__(self, workspace_root, ledger_path, *, evidence_verifier,
                 max_read_bytes=MAX_READ_BYTES):
        root = Path(workspace_root).resolve(strict=True)
        if not root.is_dir():
            raise ValueError("workspace_root must be an existing directory")
        if not callable(evidence_verifier):
            raise ValueError("A trusted host evidence verifier is required")
        if type(max_read_bytes) is not int or not 1 <= max_read_bytes <= MAX_BYTES:
            raise ValueError("max_read_bytes must be an integer from 1 to 1048576")
        self.workspace_root = root
        self.max_read_bytes = max_read_bytes
        self._host_verifier = evidence_verifier
        super().__init__(ledger_path, evidence_verifier=self._verify_scoped_request,
                         require_verified_evidence=True)

    def _file_path(self, target, *, must_exist):
        if type(target) is not str or not target.strip() or "\x00" in target or ":" in target:
            raise ValueError("Invalid relative file target")
        relative = Path(target.replace("\\", "/"))
        if relative.is_absolute() or relative.drive or ".." in relative.parts:
            raise ValueError("File target must remain inside the workspace")
        for part in relative.parts:
            lower = part.lower()
            if (lower in _CREDENTIAL_COMPONENTS or lower == ".env" or lower.startswith(".env.") or
                    lower.endswith((".pem", ".key", ".p12", ".pfx"))):
                raise ValueError("Credential file targets are excluded")
        path = self.workspace_root
        for part in relative.parts:
            path = path / part
            try:
                info = path.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                raise ValueError("Symlink and reparse targets are excluded")
        resolved = path.resolve(strict=must_exist)
        if not resolved.is_relative_to(self.workspace_root):
            raise ValueError("File target leaves the workspace")
        if must_exist and not resolved.is_file():
            raise ValueError("Read target must be a regular file")
        if resolved == Path(self.ledger.path).resolve():
            raise ValueError("The active audit ledger is not a tool target")
        return resolved

    def _verify_scoped_request(self, envelope):
        action = Action.from_dict(envelope["action"])
        if action.type in _FILE_ACTIONS:
            self._file_path(action.target, must_exist=action.type == "read_file")
            allowed_params = {"path", "target"}
            if action.type != "read_file":
                allowed_params.add("content")
            if set(action.params) - allowed_params:
                return False
            for key in ("path", "target"):
                if key in action.params and action.params[key] != action.target:
                    return False
            if "cwd" in action.params:
                return False
        elif action.type in _PROCESS_ACTIONS:
            if action.target != "." or action.params.get("cwd", ".") != ".":
                return False
            if "argv" in action.params:
                argv = action.params["argv"]
                if type(argv) is not list or not argv or any(type(arg) is not str or not arg for arg in argv):
                    return False
        else:
            return False
        return self._host_verifier(envelope) is True

    def read_file(self, action):
        """Scoped UTF-8 read executor, limited to 64 KiB and non-secret output.

        Call through govern_and_execute(envelope, guardian.read_file).
        This helper is not a replacement for the governance admission call.
        """
        if action.type != "read_file":
            raise ValueError("Executor only supports read_file")
        path = self._file_path(action.target, must_exist=True)
        with open(path, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ValueError("Read target must remain a regular file")
            data = stream.read(self.max_read_bytes + 1)
        if len(data) > self.max_read_bytes:
            raise ValueError("File output exceeds the read limit")
        result = data.decode("utf-8")
        if r3_exposed_secret(Action(id=action.id, type="read_file", payload=result)).matched:
            raise ValueError("File output contains a recognized credential pattern")
        return result
