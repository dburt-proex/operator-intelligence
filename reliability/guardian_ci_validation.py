"""Deterministic exact-head validation; fake credentials, forbidden executors.

This validates a denied production gate. It never grants inference authority.
"""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import platform
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from reliability import guardian_ar_001 as gate
from guardian.audit import AuditLedger

DIRECTIVE = "DAXXER-GUARDIAN-AR001-CI-INTEGRATION-001"


def main():
    root = gate.ROOT
    evidence = root / "guardian-ci-evidence"
    evidence.mkdir(exist_ok=True)
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    expected = os.environ.get("EXPECTED_HEAD_SHA", sha)
    receipt = {"directive_id": DIRECTIVE, "tested_sha": sha, "expected_sha": expected,
               "python": platform.python_version(), "platform": platform.platform(),
               "workflow_run_id": os.environ.get("GITHUB_RUN_ID"), "gate": "HALT",
               "provider_calls": 0, "network_attempts": 0, "executor_calls": 0,
               "inference_authorization_created": False, "validation_only": True,
               "publication_actions": 0, "test_results": {}, "guardian_gate": [],
               "provider_monitor_scope": "production_gate_probes",
               "network_monitor_scope": "all_suites_and_gate_probes"}
    def forbidden_executor(*args, **kwargs):
        receipt["executor_calls"] += 1
        raise AssertionError("CI must never invoke the harness executor")
    def forbidden_provider(*args, **kwargs):
        receipt["provider_calls"] += 1
        raise AssertionError("CI must never invoke the provider")
    def forbidden_network(*args, **kwargs):
        receipt["network_attempts"] += 1
        raise AssertionError("CI validation forbids network access")
    try:
        if sha != expected:
            raise AssertionError("Checkout does not match the requested exact head")
        if os.environ.get("OPENAI_API_KEY"):
            raise AssertionError("Deterministic validation must not receive a provider credential")
        # All suites and gate probes use fail-fast transport sentinels. A caught
        # transport failure still increments a counter and fails final admission.
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(socket, "create_connection", forbidden_network))
            stack.enter_context(patch.object(socket, "socket", forbidden_network))
            for name, directory, count in (
                    ("ar001", root / "reliability", 37),
                    ("guardian", root / "reliability/guardian_vendor/tests", 111)):
                suite = unittest.TestLoader().discover(str(directory), pattern="test_*.py")
                result = unittest.TextTestRunner(verbosity=2).run(suite)
                receipt["test_results"][name] = {
                    "count": result.testsRun, "expected_count": count,
                    "failures": len(result.failures), "errors": len(result.errors),
                    "skipped": len(result.skipped), "passed": result.wasSuccessful()}
                if not result.wasSuccessful() or result.testsRun != count:
                    raise AssertionError("Regression suite failed or baseline count changed")
            stack.enter_context(patch.object(gate.harness, "call_openai", forbidden_provider))
            for relative, digest in gate.PINS.items():
                if hashlib.sha256((root / relative).read_bytes()).hexdigest() != digest:
                    raise AssertionError("Frozen source or authorization pin mismatch")
            authorization = json.loads((root / gate.AUTH).read_text(encoding="utf-8"))
            closeout = json.loads((root / gate.CLOSEOUT).read_text(encoding="utf-8"))
            if (authorization.get("authorization_version") != "1.0.0" or
                    closeout.get("next_inference_authorized") is not False):
                raise AssertionError("Historical consumed authority unexpectedly changed")
            receipt["authority_state"] = "CONSUMED_V1_NEXT_INFERENCE_BLOCKED"
            # Synthetic eligible host context exercises consumed authorization,
            # rather than merely rejecting the surrounding pull_request event.
            # This string is a dummy and never goes to the network or executor.
            context = {"GITHUB_REPOSITORY": "dburt-proex/operator-intelligence",
                       "GITHUB_EVENT_NAME": "workflow_dispatch", "GITHUB_REF": "refs/heads/main",
                       "GITHUB_RUN_ATTEMPT": "1", "OPENAI_API_KEY": "test-only"}
            case = Path(tempfile.mkdtemp(prefix="consumed-authority-", dir=evidence))
            receipt["gate_evidence_directory"] = str(case.relative_to(root))
            for number in (1, 2):
                run_id, trace_id = f"AR001-PILOT-RUN-00{number}", f"AR001-PILOT-TRACE-00{number}"
                status = gate.execute_run(run_id, trace_id, root=case,
                    verifier=lambda envelope: gate.verify_authority(envelope, root=root, environment=context),
                    execute=forbidden_executor)
                decision = json.loads((case / f"ar001-guardian-{run_id}.json").read_text())
                if status != 3 or decision["verdict"] != "HALT" or decision["attempted"] or decision["executed"]:
                    raise AssertionError("Consumed authorization failed to block execution")
                receipt["guardian_gate"].append({
                    "run_id": run_id, "exit_code": status, "verdict": decision["verdict"],
                    "attempted": decision["attempted"], "executed": decision["executed"],
                    "decision_hash": decision["decision_hash"], "action_hash": decision["action_hash"]})
            ledger = AuditLedger(str(case / "ar001-guardian-ledger.jsonl"))
            entries = ledger.entries()
            if len(entries) != 2 or not ledger.verify(expected_head=entries[-1]["entry_hash"])[0]:
                raise AssertionError("Guardian decision ledger failed verification")
            receipt["ledger_head"] = entries[-1]["entry_hash"]
        if receipt["provider_calls"] or receipt["network_attempts"] or receipt["executor_calls"]:
            raise AssertionError("Forbidden invocation attempted during validation")
        receipt["gate"] = "ALLOW"
        receipt["next_decision"] = "REVIEW_FOR_FRESH_BOUNDED_AR001_PILOT_AUTHORIZATION"
        return 0
    except Exception as error:
        receipt["failure"] = type(error).__name__ + ": validation failed; inspect CI logs"
        return 1
    finally:
        (evidence / "integration-validation.json").write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    sys.exit(main())
