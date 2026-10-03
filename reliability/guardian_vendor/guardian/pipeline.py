"""Guardian Agent runtime.

Deterministic governance pipeline sitting between an AI reasoning layer and
real-world execution:

    envelope { signal, action }
        │
        ▼
    [1] VIL signal gate      — evidence-capped scoring; weak signals never
        │                      reach the policy layer (CLARIFY/ARCHIVE/HALT)
        ▼
    [2] CASA policy gate     — six deterministic rules (Diffwall engine),
        │                      most-restrictive merge, fail-safe REVIEW
        ▼
    [3] Audit ledger         — hash-chained record BEFORE any execution
        │
        ▼
    [4] Gated executor       — runs only on ALLOW; REVIEW pends; HALT blocks

Guardian does not reason or generate. It governs.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional

from . import vil
from .audit import AuditLedger
from .engine import validate
from .models import Action, Verdict
from .validation import fields, snapshot
from .audit import AuditError
import hashlib
import json
import inspect

# VIL route -> contribution to the final governance verdict.
# PASS imposes nothing; CLARIFY/ARCHIVE and VIL-HALT block execution outright;
# VIL-REVIEW forces at least human review even if policy says ALLOW.
_VIL_TO_VERDICT = {
    vil.Route.PASS: Verdict.ALLOW,
    vil.Route.REVIEW: Verdict.REVIEW,
    vil.Route.CLARIFY: Verdict.HALT,
    vil.Route.ARCHIVE: Verdict.HALT,
    vil.Route.HALT: Verdict.HALT,
}

_RANK = {Verdict.ALLOW: 0, Verdict.REVIEW: 1, Verdict.HALT: 2}


@dataclass
class Decision:
    action_id: str
    verdict: Verdict
    vil: vil.VilResult
    casa: dict                      # policy Report as dict
    executed: bool = False
    execution_result: Optional[str] = None
    entry_hash: str = ""
    reasons: list = field(default_factory=list)
    action_hash: str = ""
    execution_error: str = ""
    attempted: bool = False
    decision_hash: str = ""
    evidence_verified: bool = False

    def to_dict(self) -> dict:
        return {
            "action_id": self.action_id,
            "verdict": self.verdict.value,
            "vil": self.vil.to_dict(),
            "casa": self.casa,
            "executed": self.executed,
            "execution_result": self.execution_result,
            "reasons": self.reasons,
            "entry_hash": self.entry_hash,
            "decision_hash": self.decision_hash,
            "action_hash": self.action_hash,
            "attempted": self.attempted,
            "execution_error": self.execution_error,
            "evidence_verified": self.evidence_verified,
        }


class GuardianAgent:
    def __init__(self, ledger_path: str = "guardian_audit.jsonl", *,
                 evidence_verifier=None, require_verified_evidence=False):
        self.ledger = AuditLedger(ledger_path)
        if type(require_verified_evidence) is not bool:
            raise ValueError("require_verified_evidence must be a boolean")
        if evidence_verifier is not None and not callable(evidence_verifier):
            raise ValueError("evidence_verifier must be callable")
        self.evidence_verifier = evidence_verifier
        self.require_verified_evidence = require_verified_evidence

    def govern(self, envelope: dict) -> Decision:
        """Malformed envelopes halt; audit failures raise before invocation."""
        return self._govern(envelope)[0]

    def _policy_report(self, action):
        """Trusted profiles may add rules while preserving baseline restrictions."""
        return validate(action)

    def _govern(self, envelope):
        invalid = False
        verified = False
        try:
            envelope = snapshot(envelope)
            fields(envelope, {"signal", "action"})
            signal = vil.Signal.from_dict(envelope.get("signal", {}))
            action = Action.from_dict(envelope.get("action", {}))
        except (ValueError, TypeError, OverflowError, RecursionError):
            signal, action = vil.Signal(), Action(id="malformed", type="unknown")
            invalid = True

        # [1] VIL signal gate
        vres = vil.evaluate(signal)
        reasons = [f"VIL:{vres.route.value} — {vres.reason}"]

        # [2] CASA policy gate (always run: full rule trace in every record)
        report = self._policy_report(action)
        reasons.append(
            f"CASA:{report.verdict.value} — triggered_by {report.triggered_by}")

        # Most-restrictive merge across stages
        final = max([_VIL_TO_VERDICT[vres.route], report.verdict],
                    key=lambda v: _RANK[v])
        if invalid:
            final = Verdict.HALT
            reasons.append("INVALID_INPUT: malformed envelope")
        if not invalid and (self.require_verified_evidence or self.evidence_verifier is not None):
            verified = False
            if self.evidence_verifier is not None:
                try:
                    verified = self.evidence_verifier(snapshot(envelope)) is True
                except Exception:
                    pass
            if not verified:
                final = Verdict.HALT
                reasons.append("EVIDENCE_UNVERIFIED: trusted verification required")

        decision = Decision(action_id=action.id or "unset", verdict=final,
                            vil=vres, casa=report.to_dict(), reasons=reasons,
                            evidence_verified=verified)
        if any(r.rule == "R3_EXPOSED_SECRET" and r.matched for r in report.results):
            decision.action_id = "redacted"
            decision.casa["action_id"] = "redacted"
            decision.casa["action_type"] = "redacted"
        decision.action_hash = hashlib.sha256(json.dumps(vars(action), sort_keys=True,
            separators=(",", ":"), allow_nan=False).encode()).hexdigest()

        # [3] Audit record precedes any execution
        from . import __version__
        record = decision.to_dict()
        record.update(event="decision", runtime_version=__version__,
                      require_verified_evidence=self.require_verified_evidence)
        entry = self.ledger.append(record)
        decision.entry_hash = entry["entry_hash"]
        decision.decision_hash = decision.entry_hash
        return decision, action

    def govern_and_execute(self, envelope: dict,
                           executor: Callable[[Action], str]) -> Decision:
        """Execute only on ALLOW. REVIEW returns pending; HALT never calls
        the executor. Execution outcome is appended as its own ledger entry."""
        decision, action = self._govern(envelope)
        if decision.verdict is Verdict.ALLOW:
            if not callable(executor):
                raise ValueError("executor must be callable")
            decision.attempted = True
            try:
                result = executor(action)
                if inspect.isawaitable(result) or inspect.isgenerator(result) or inspect.isasyncgen(result):
                    if inspect.iscoroutine(result) or inspect.isgenerator(result):
                        result.close()
                    raise TypeError("Executor must return a synchronous result")
                decision.execution_result = str(result)
                decision.executed = True
            except Exception:
                decision.execution_error = "executor failed; side effects may have occurred"
            try:
                entry = self.ledger.append({
                    "action_id": decision.action_id, "event": "execution",
                    "decision_hash": decision.decision_hash,
                    "action_hash": decision.action_hash,
                    "attempted": True, "executed": decision.executed,
                    "error": decision.execution_error,
                })
            except AuditError:
                raise ExecutionAuditError(decision) from None
            decision.entry_hash = entry["entry_hash"]
        return decision


class ExecutionAuditError(AuditError):
    """Outcome audit failed after invocation. Reconcile before any retry."""
    def __init__(self, decision):
        super().__init__("Execution attempted but outcome audit failed; reconcile before retry")
        self.decision = decision
