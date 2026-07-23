#!/usr/bin/env python3
"""Fail-closed validator for the Agentic Control Platform Readiness Sprint."""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
REQUIRED_FILES = {
    "readiness-protocol.md",
    "assessment-questionnaire.md",
    "evidence-requirements.md",
    "control-mapping.md",
    "scoring-profile.md",
    "gap-register.md",
    "prioritized-roadmap.md",
    "executive-decision-brief.md",
    "diffwall-demonstration.md",
    "export-schema.json",
}
DOMAINS = {f"AIGR-D{index}" for index in range(1, 8)}
EXPECTED_WEIGHTS = {
    "AIGR-D1": 10,
    "AIGR-D2": 15,
    "AIGR-D3": 15,
    "AIGR-D4": 15,
    "AIGR-D5": 15,
    "AIGR-D6": 15,
    "AIGR-D7": 15,
}
FINDING_STATES = {"VERIFIED_GAP", "PARTIAL_CONTROL", "CONTROLLED", "UNKNOWN", "NOT_APPLICABLE"}
MATERIAL_STATES = {"VERIFIED_GAP", "PARTIAL_CONTROL", "CONTROLLED"}
PLANES = {"governance", "change_time", "runtime", "assurance"}
DECISION_GATES = {
    "READY": "ALLOW",
    "CONDITIONAL": "REVIEW",
    "NOT_READY": "HALT",
    "BLOCKED": "HALT",
}
VENDOR_TERMS = {
    "servicenow",
    "salesforce",
    "microsoft purview",
    "azure ai foundry",
    "ibm watsonx",
    "google vertex",
    "aws bedrock",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(PACKAGE)} cannot be loaded: {exc}") from exc


def validate_package() -> list[str]:
    errors: list[str] = []
    missing = sorted(name for name in REQUIRED_FILES if not (PACKAGE / name).is_file())
    if missing:
        errors.append(f"missing required artifacts: {missing}")

    try:
        schema = load_json(PACKAGE / "export-schema.json")
    except ValueError as exc:
        errors.append(str(exc))
        schema = {}
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("export-schema.json must declare JSON Schema draft 2020-12")
    required = set(schema.get("required", []))
    expected = {
        "schema_version",
        "assessment",
        "scope",
        "evidence_summary",
        "domain_results",
        "control_results",
        "findings",
        "roadmap",
        "decision",
        "authorization",
        "ledger_refs",
    }
    if required != expected:
        errors.append("export schema top-level required fields do not match the handoff contract")

    markdown = "\n".join(
        (PACKAGE / name).read_text(encoding="utf-8").lower()
        for name in REQUIRED_FILES
        if name.endswith(".md") and (PACKAGE / name).is_file()
    )
    for term in sorted(VENDOR_TERMS):
        if term in markdown:
            errors.append(f"vendor-neutrality violation: {term}")
    for required_phrase in (
        "implementation authorization",
        "change-time",
        "runtime",
        "unknown",
        "evidence",
        "owner",
        "allow",
        "review",
        "halt",
    ):
        if required_phrase not in markdown:
            errors.append(f"required governance concept missing: {required_phrase}")
    return errors


def validate_export(data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != "oi-acpr-export-v0.1":
        errors.append("unsupported schema_version")

    domain_results = data.get("domain_results", [])
    domain_ids = [item.get("domain_id") for item in domain_results]
    if len(domain_results) != 7 or set(domain_ids) != DOMAINS or len(domain_ids) != len(set(domain_ids)):
        errors.append("domain_results must contain each canonical domain exactly once")
    weights = {item.get("domain_id"): item.get("weight") for item in domain_results}
    if weights != EXPECTED_WEIGHTS or sum(value for value in weights.values() if isinstance(value, (int, float))) != 100:
        errors.append("domain weights must match the governed seven-domain profile and total 100")

    planes = set()
    for index, control in enumerate(data.get("control_results", [])):
        plane = control.get("control_plane")
        planes.add(plane)
        if plane not in PLANES:
            errors.append(f"control_results[{index}] has invalid control_plane")
        if control.get("domain_id") not in DOMAINS:
            errors.append(f"control_results[{index}] has invalid domain_id")
        if control.get("state") not in FINDING_STATES:
            errors.append(f"control_results[{index}] has invalid state")
        if not control.get("owner"):
            errors.append(f"control_results[{index}] requires an owner")
    if "change_time" not in planes or "runtime" not in planes:
        errors.append("control_results must represent change_time and runtime separately")

    for index, finding in enumerate(data.get("findings", [])):
        state = finding.get("state")
        if state not in FINDING_STATES:
            errors.append(f"findings[{index}] has invalid state")
        evidence_refs = finding.get("evidence_refs", [])
        if state in MATERIAL_STATES and not evidence_refs:
            errors.append(f"findings[{index}] material state requires admitted evidence_refs")
        if state == "UNKNOWN" and finding.get("confidence") != "unknown":
            errors.append(f"findings[{index}] UNKNOWN requires unknown confidence")
        if finding.get("severity") in {"critical", "high"}:
            for field in ("owner", "target_gate", "acceptance_criteria", "ledger_refs"):
                if not finding.get(field):
                    errors.append(f"findings[{index}] {field} is required for material severity")

    for index, item in enumerate(data.get("roadmap", [])):
        for field in ("owner", "decision_authority", "acceptance_criteria", "acceptance_evidence", "ledger_refs"):
            if not item.get(field):
                errors.append(f"roadmap[{index}] {field} is required")
        if item.get("implementation_authorized") is not False:
            errors.append(f"roadmap[{index}] cannot authorize implementation")

    decision = data.get("decision", {})
    outcome = decision.get("outcome")
    expected_gate = DECISION_GATES.get(outcome)
    if expected_gate is None or decision.get("control_gate") != expected_gate:
        errors.append("decision outcome and control_gate disagree")

    authorization = data.get("authorization", {})
    if authorization.get("assessment_authorized") is not True:
        errors.append("assessment authority must be explicit")
    if authorization.get("implementation_authorized") is not False:
        errors.append("readiness export cannot authorize implementation")
    if authorization.get("production_authorized") is not False:
        errors.append("readiness export cannot authorize production")

    evidence_summary = data.get("evidence_summary", {})
    coverage = evidence_summary.get("coverage_percent")
    if not isinstance(coverage, (int, float)) or not 0 <= coverage <= 100:
        errors.append("evidence coverage must be between 0 and 100")
    if outcome == "READY":
        score = decision.get("readiness_score")
        if not isinstance(score, (int, float)) or score < 75:
            errors.append("READY requires readiness_score >= 75")
        if not isinstance(coverage, (int, float)) or coverage < 80:
            errors.append("READY requires evidence coverage >= 80")
        if evidence_summary.get("confidence") not in {"high", "medium"}:
            errors.append("READY requires high or medium confidence")
        if evidence_summary.get("blocked_conditions"):
            errors.append("READY cannot contain blocked conditions")

    if not data.get("ledger_refs"):
        errors.append("at least one DecisionLedger reference is required")
    return errors


def self_test() -> list[str]:
    errors = validate_package()
    try:
        valid = load_json(PACKAGE / "fixtures" / "valid-ready.json")
    except ValueError as exc:
        return errors + [str(exc)]
    valid_errors = validate_export(valid)
    if valid_errors:
        errors.append(f"valid fixture failed: {valid_errors}")

    mutations = []

    missing_runtime = copy.deepcopy(valid)
    missing_runtime["control_results"] = [
        item for item in missing_runtime["control_results"] if item["control_plane"] != "runtime"
    ]
    mutations.append(("missing runtime plane", missing_runtime))

    bad_weights = copy.deepcopy(valid)
    bad_weights["domain_results"][0]["weight"] = 9
    mutations.append(("invalid weight total", bad_weights))

    missing_evidence = copy.deepcopy(valid)
    missing_evidence["findings"][0]["evidence_refs"] = []
    mutations.append(("material finding without evidence", missing_evidence))

    unauthorized = copy.deepcopy(valid)
    unauthorized["authorization"]["implementation_authorized"] = True
    mutations.append(("implicit implementation authorization", unauthorized))

    mismatched_gate = copy.deepcopy(valid)
    mismatched_gate["decision"]["control_gate"] = "HALT"
    mutations.append(("decision gate mismatch", mismatched_gate))

    for name, payload in mutations:
        if not validate_export(payload):
            errors.append(f"negative fixture was not rejected: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--export", type=Path)
    args = parser.parse_args()

    errors = self_test() if args.self_test else validate_package()
    if args.export:
        try:
            errors.extend(validate_export(load_json(args.export.resolve())))
        except ValueError as exc:
            errors.append(str(exc))
    result = {
        "schema_version": "oi-acpr-validation-v0.1",
        "decision": "HALT" if errors else "ALLOW",
        "error_count": len(errors),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
