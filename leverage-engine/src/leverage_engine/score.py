from copy import deepcopy
from typing import Any


class ScoringError(ValueError):
    pass


def _weighted(inputs: dict[str, Any], weights: dict[str, float], anchors: set[int], label: str) -> float:
    if set(inputs) != set(weights):
        raise ScoringError(f"{label} factors must exactly match the approved profile")
    if any(value not in anchors for value in inputs.values()):
        raise ScoringError(f"{label} factor values must use approved anchors")
    return round(sum(inputs[key] * weights[key] for key in weights) / 100, 4)


def score_opportunity(opportunity: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(opportunity)
    inputs = result["score_inputs"]
    anchors = set(profile["allowed_anchors"])
    raw = _weighted(inputs["value"], profile["value_weights"], anchors, "value")
    friction = _weighted(inputs["friction"], profile["friction_weights"], anchors, "friction")
    risk = _weighted(inputs["risk"], profile["risk_weights"], anchors, "risk")
    confidence_factor = profile["confidence_factors"][result["confidence"]]
    urgency = result["urgency_bonus"]
    if urgency and not result["verified_deadline"]:
        raise ScoringError("urgency bonus requires a verified deadline")
    value = (raw * confidence_factor) - (friction * profile["penalties"]["friction"]) - (risk * profile["penalties"]["risk"]) + urgency
    result.update({
        "raw_value_score": raw,
        "friction_score": friction,
        "risk_score": risk,
        "confidence_factor": confidence_factor,
        "leverage_index": round(min(100, max(0, value)), 4),
        "state": "scored" if result["state"] != "duplicate" else "duplicate",
    })
    return result
