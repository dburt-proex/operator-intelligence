"""VIL — Verifiable Intelligence Layer (signal gate).

Stdlib port of the VIL deterministic scoring engine's core law:

    vil_score = min(signal_score, verifiability_score)     # verification cap

A signal can never route higher than its evidence supports. Runs BEFORE the
CASA policy gate: low-confidence signals are clarified or blocked before an
action is ever considered for execution.

Routes: PASS >= 8.0 | REVIEW >= 5.0 | CLARIFY >= 3.0 | ARCHIVE < 3.0
Critical risk flags force HALT regardless of score.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Iterable
import math
from types import MappingProxyType
from .validation import fields, snapshot, strings, text


class Route(str, Enum):
    PASS = "PASS"
    REVIEW = "REVIEW"
    CLARIFY = "CLARIFY"
    ARCHIVE = "ARCHIVE"
    HALT = "HALT"


DEFAULT_THRESHOLDS = MappingProxyType({"pass": 8.0, "review": 5.0, "clarify": 3.0})

DEFAULT_HALT_FLAGS = frozenset({
    "secrets", "prod_data_destruction", "policy_violation", "unsafe_action",
    "irreversible_external_action", "regulated_decision", "private_data_exposure",
})

_SPECULATIVE = ["maybe", "possibly", "guess", "heard", "rumor", "unverified"]


@dataclass
class Signal:
    """The context/instruction a proposed action is based on."""
    content: str = ""
    source: str = "unknown"
    metadata: dict = field(default_factory=dict)
    source_pointers: list = field(default_factory=list)
    signal_score: float = 5.0          # caller-supplied value estimate, 0-10
    risk_flags: list = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: dict) -> "Signal":
        d = snapshot(d)
        fields(d, {"content", "source", "metadata", "source_pointers",
                   "signal_score", "risk_flags"})
        score = d.get("signal_score", 5.0)
        if type(score) not in (int, float) or not 0 <= score <= 10 or not math.isfinite(score):
            raise ValueError("signal_score must be a finite number from 0 to 10")
        metadata = d.get("metadata", {})
        if type(metadata) is not dict:
            raise ValueError("metadata must be an object")
        return cls(
            content=text(d.get("content", ""), "content"),
            source=text(d.get("source", "unknown"), "source"),
            metadata=metadata,
            source_pointers=strings(d.get("source_pointers", []), "source_pointers"),
            signal_score=float(score),
            risk_flags=strings(d.get("risk_flags", []), "risk_flags"),
        )


def clamp(v: float, lo: float = 0.0, hi: float = 10.0) -> float:
    if not math.isfinite(v):
        raise ValueError("Score must be finite")
    return max(lo, min(hi, v))


def verifiability_score(s: Signal) -> float:
    """Deterministic evidence score. Rewards concrete content, source pointers,
    structured metadata; penalizes speculative language."""
    score = 2.0
    content = s.content.strip()
    if len(content) >= 40:
        score += 1.5
    if len(content) >= 120:
        score += 1.0
    if s.metadata:
        score += min(2.0, len(s.metadata) * 0.4)
    if s.source_pointers:
        score += min(2.0, len(s.source_pointers) * 0.75)
    if s.source and s.source.lower() not in {"unknown", "n/a", "none"}:
        score += 1.0
    if any(m in content.lower() for m in _SPECULATIVE):
        score -= 1.0
    return round(clamp(score), 2)


def vil_score(s: Signal) -> float:
    """Verification cap: value claim can never exceed evidence."""
    return round(clamp(min(clamp(s.signal_score), verifiability_score(s))), 2)


def has_halt_flag(flags: Iterable[str], halt_flags: Iterable[str] | None = None) -> bool:
    halt = {f.strip().lower() for f in (DEFAULT_HALT_FLAGS if halt_flags is None else halt_flags)}
    return any(str(f).strip().lower() in halt for f in flags)


@dataclass
class VilResult:
    route: Route
    score: float
    verifiability: float
    reason: str

    def to_dict(self) -> dict:
        return {"route": self.route.value, "score": self.score,
                "verifiability": self.verifiability, "reason": self.reason}


def evaluate(s: Signal, thresholds: Dict[str, float] | None = None,
             halt_flags: Iterable[str] | None = None) -> VilResult:
    s = Signal.from_dict(vars(s))
    t = DEFAULT_THRESHOLDS if thresholds is None else thresholds
    if (set(t) != {"pass", "review", "clarify"} or
            any(type(v) not in (int, float) or not math.isfinite(v) for v in t.values()) or
            not 0 <= t["clarify"] <= t["review"] <= t["pass"] <= 10):
        raise ValueError("Invalid VIL thresholds")
    v = verifiability_score(s)
    score = vil_score(s)
    if has_halt_flag(s.risk_flags, halt_flags):
        return VilResult(Route.HALT, score, v,
                         "HALT: critical risk flag present.")
    if score >= t["pass"]:
        return VilResult(Route.PASS, score, v, f"Score {score}: high-confidence signal.")
    if score >= t["review"]:
        return VilResult(Route.REVIEW, score, v, f"Score {score}: human judgment required.")
    if score >= t["clarify"]:
        return VilResult(Route.CLARIFY, score, v, f"Score {score}: insufficient evidence; clarify.")
    return VilResult(Route.ARCHIVE, score, v, f"Score {score}: low-confidence noise.")
