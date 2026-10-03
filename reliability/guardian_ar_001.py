"""Audited AR-001 in-process admission; no provider calls during verification.

Run as `python3 -m reliability.guardian_ar_001` from the repository root.
The committed v1 authorization is consumed: current closeout evidence HALTs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "guardian_vendor"))
from guardian.inference import AuthorizedInferenceGuardian
from guardian.models import Verdict
from guardian.audit import AuditError
from reliability import agent_reliability_ar_001_harness as harness

ROOT = Path(__file__).resolve().parents[1]
AUTH = "reliability/authorizations/ar-001-pilot-v1.json"
HARNESS = "reliability/agent_reliability_ar_001_harness.py"
PINS = {
    AUTH: "3065098db9710b1be54ea0ab4ed610db26fa0523d2f6b911febc62152ac63a79",
    HARNESS: "cac1fc79f6dbd2d8002f110338df705a5fc7b630d53edde79d58fdb416196778",
}
CLOSEOUT = "reliability/receipts/ar-001-stage-a-v2-closeout.json"


class HarnessExecutionError(RuntimeError):
    """Preserve the harness exit contract without spawning a child process."""

    def __init__(self, exit_code: int):
        super().__init__("AR-001 harness execution failed; reconcile receipt before retry")
        self.exit_code = exit_code


def action_for(run_id, trace_id):
    argv = [sys.executable, HARNESS, "--run-id", run_id, "--trace-id", trace_id,
            "--execute", "--pilot-authorization", AUTH]
    return {"id": run_id, "type": "external_model_execution",
            "target": "https://api.openai.com/v1/responses", "payload": "",
            "params": {"argv": argv, "scope": "AR-001",
                       "data_class": "SYNTHETIC_EXPERIMENT_EVIDENCE",
                       "network": "api.openai.com", "credential": "OPENAI_API_KEY",
                       "mutation": False, "authorization": "ALLOW_TO_RUN_PILOT",
                       "evaluated_agent_tool_count": 0, "automatic_inference_retries": 0,
                       "store": False}}


def verify_authority(envelope, root=ROOT, environment=None):
    """Host-owned authority check. A string claiming ALLOW is insufficient."""
    env = os.environ if environment is None else environment
    params = envelope["action"]["params"]
    run_id, trace_id = params["argv"][3], params["argv"][5]
    pairs = {f"AR001-PILOT-RUN-00{n}": f"AR001-PILOT-TRACE-00{n}" for n in (1, 2)}
    if pairs.get(run_id) != trace_id:
        return False
    if (env.get("GITHUB_REPOSITORY") != "dburt-proex/operator-intelligence" or
            env.get("GITHUB_EVENT_NAME") != "workflow_dispatch" or
            env.get("GITHUB_REF") != "refs/heads/main" or
            env.get("GITHUB_RUN_ATTEMPT") != "1" or not env.get("OPENAI_API_KEY")):
        return False
    for name, expected in PINS.items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            return False
    authorization = harness.validate_execution_authorization(root / AUTH)
    if authorization.get("authorization_version") == "1.0.0":
        # This exact authorization is already consumed. A closeout flag edit
        # cannot revive it; a future contract requires separate source review.
        return False
    for key, expected in {"authorized_runs": 2, "evaluated_agent_tool_count": 0,
                          "automatic_inference_retries": 0, "automatic_semantic_retries": 0,
                          "store": False, "cohort_execution_authorized": False,
                          "thirty_run_cohort_authorized": False}.items():
        if type(authorization.get(key)) is not type(expected) or authorization[key] != expected:
            return False
    # Fail closed on consumed authority, missing/malformed closeout, and any
    # unresolved historical stop. Reopening requires a separately reviewed
    # authorization and budget contract, never deletion of prior evidence.
    closeout = json.loads((root / CLOSEOUT).read_text(encoding="utf-8"))
    if (closeout.get("experiment_id") != "AR-001" or
            closeout.get("next_inference_authorized") is not True or
            closeout.get("decision") != "ALLOW"):
        return False
    harness.verify_frozen_artifacts()
    return True


def _run_harness_in_process(governed, root):
    """Invoke the pinned harness functions only after Guardian has ALLOWed."""
    params = governed.params
    run_id, trace_id = params["argv"][3], params["argv"][5]
    authorization_path = root / AUTH
    try:
        request_body = harness.build_request(run_id, trace_id)
        output, metadata = harness.call_openai(request_body, authorization_path)
        validation = harness.validate_output(output, run_id, trace_id)
        record = harness.RunRecord(run_id, trace_id, output, validation, metadata)
        payload = {"output": output, "receipt": harness.make_run_receipt(record)}
        print(json.dumps(payload, indent=2, sort_keys=True))
        if not validation.valid:
            raise HarnessExecutionError(2)
        return "AR-001 harness returned success; inspect its independent receipt"
    except HarnessExecutionError:
        raise
    except harness.HarnessError as exc:
        print(f"AR-001 HALT: {exc}", file=sys.stderr)
        raise HarnessExecutionError(3) from exc


def execute_run(run_id, trace_id, *, root=ROOT, verifier=verify_authority,
                execute=None):
    action = action_for(run_id, trace_id)
    ledger_path = root / "ar001-guardian-ledger.jsonl"
    # Admission is durable even when host validation fails. The verifier never
    # returns secrets or provider content to Guardian.
    def verify_once(envelope):
        if any(entry["record"].get("action_id") == run_id for entry in agent.ledger.entries()):
            return False
        return verifier(envelope) is True
    agent = AuthorizedInferenceGuardian(str(ledger_path), authorized_action=action,
                                        evidence_verifier=verify_once)
    envelope = {"action": action, "signal": {
        "content": "AR-001 bounded synthetic pilot inference requested under the frozen authorization contract; trusted host verification checks identity, integrity, budget and closeout before execution.",
        "source": "ar-001-host-verifier", "signal_score": 9,
        "source_pointers": [AUTH, HARNESS, CLOSEOUT],
        "metadata": {"scope": "AR-001", "gate": "ALLOW_TO_RUN_PILOT",
                     "data_class": "SYNTHETIC_EXPERIMENT_EVIDENCE", "tools": 0, "retries": 0}}}
    runner = _run_harness_in_process if execute is None else execute
    status = 3

    def invoke(governed):
        nonlocal status
        try:
            result = runner(governed, root)
            status = 0
            return result
        except HarnessExecutionError as exc:
            status = exc.exit_code
            raise
        except Exception:
            status = 3
            raise

    decision = agent.govern_and_execute(envelope, invoke)
    receipt = decision.to_dict()
    receipt.pop("execution_result")
    receipt["harness_exit_code"] = status if decision.attempted else None
    receipt_id = run_id if run_id in {"AR001-PILOT-RUN-001", "AR001-PILOT-RUN-002"} else "invalid"
    (root / f"ar001-guardian-{receipt_id}.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    if decision.verdict is not Verdict.ALLOW or not decision.executed:
        return 3
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True,
                        choices=["AR001-PILOT-RUN-001", "AR001-PILOT-RUN-002"])
    parser.add_argument("--trace-id", required=True,
                        choices=["AR001-PILOT-TRACE-001", "AR001-PILOT-TRACE-002"])
    args = parser.parse_args()
    try:
        return execute_run(args.run_id, args.trace_id)
    except (AuditError, OSError, ValueError):
        print("Guardian HALT: audit or receipt storage failed; reconcile before retry", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
