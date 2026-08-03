from typing import Any


class ProfileError(ValueError):
    pass


def validate_scoring_profile(profile: dict[str, Any]) -> None:
    for name in ("value_weights", "friction_weights", "risk_weights"):
        weights = profile.get(name)
        if not isinstance(weights, dict) or round(sum(weights.values()), 8) != 100:
            raise ProfileError(f"{name} must exist and total 100")
    if profile.get("allowed_anchors") != [0, 25, 50, 75, 100]:
        raise ProfileError("approved scoring anchors changed")
    expected_confidence = {"high": 1.0, "medium": 0.75, "low": 0.5, "unknown": 0.0}
    if profile.get("confidence_factors") != expected_confidence:
        raise ProfileError("confidence factors do not match the approved baseline")
    governance = profile.get("governance", {})
    if governance.get("self_adjustment") is not False or governance.get("operator_score_independent") is not True:
        raise ProfileError("scoring governance boundary is invalid")


def validate_policy_profile(profile: dict[str, Any]) -> None:
    mvp = profile.get("mvp", {})
    required_denials = ("dispatch_enabled", "network_enabled", "repository_writes_enabled", "external_actions_enabled")
    if any(mvp.get(key) is not False for key in required_denials):
        raise ProfileError("an advisory MVP prohibited capability is enabled")
    if mvp.get("human_approval_required") is not True:
        raise ProfileError("human approval must be required")
    if not profile.get("g4_rules"):
        raise ProfileError("G4 rules are required")
