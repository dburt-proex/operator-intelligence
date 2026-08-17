# AR-001 — Pre-Code Gate Decision Receipt

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Receipt version:** 0.1  
**Gate:** `ALLOW_TO_WRITE_HARNESS`  
**Decision:** `REVIEW`  
**Recorded:** 2026-08-17  
**Scope:** Pre-code readiness only; no experiment execution authority.

## Purpose

Record the current governed decision after freezing the AR-001 implementation-readiness specification, control evidence packet, input manifest, and permission/configuration contract. This receipt prevents incomplete evidence from being mistaken for authorization to implement or execute the experiment.

## Evidence reviewed

| Artifact | Version/state | Evidence status |
|---|---|---|
| `agent-reliability-ar-001-implementation-readiness.md` | v0.2 / FROZEN | present |
| `agent-reliability-ar-001-control-evidence-packet.md` | v0.1 / REVIEW | present |
| `agent-reliability-ar-001-frozen-input-manifest.md` | v0.1 / FROZEN FOR HARNESS DESIGN | present |
| `agent-reliability-ar-001-permission-configuration-manifest.md` | v0.1 / FROZEN CONTROL CONTRACT | present |
| representative synthetic fixture | fixture v1.0.0 | repository object identified |
| canonical fixture SHA-256 receipt | required | `validation_required` |
| final repository commit binding | required | `validation_required` |
| provider/model/version record | required | `validation_required` |
| provider approved-use decision | required | `validation_required` |
| PromptBP/instruction artifact + SHA-256 | required | `validation_required` |
| exact execution budget | required | `validation_required` |
| final least-privilege permission verification | required before pilot | not yet executable |
| security-boundary test evidence | required before pilot | not yet executable |
| recovery/integrity test evidence | required before pilot | not yet executable |
| risk treatment/residual-risk owner acceptance | required | `validation_required` |
| retention/deletion owner decision | required | `validation_required` |
| incident/recovery owner designation | required | `validation_required` |

## Decision logic

### FACT

The experimental scope, synthetic evidence identity, contradiction invariant, oracle separation, agent authority boundary, prohibited actions, network policy, isolation requirements, control applicability, and staged authorization gates are defined and frozen sufficiently to prevent scope drift.

### OPEN EVIDENCE

The exact inference configuration and several owner-controlled records cannot be truthfully completed from repository evidence currently available. In particular, no provider/model/version, PromptBP artifact hash, execution budget, provider approval, risk acceptance, retention decision, or owner designation is asserted by this receipt.

### RISK

Writing executable harness code before those fields are resolved would cause implementation choices to become de facto experimental parameters. That would weaken reproducibility and make the later freeze partly retrospective.

## Gate decision

`REVIEW`

`ALLOW_TO_WRITE_HARNESS` is **not issued**.

The design is ready for final parameter selection, but implementation remains blocked until the minimum pre-code fields below are resolved and bound into a superseding receipt.

## Minimum remaining pre-code closure set

1. select and record the exact provider/model/version and reasoning/sampling configuration;
2. select the immutable PromptBP/instruction artifact and compute its canonical SHA-256;
3. define identical maximum input/output/turn/time budgets;
4. compute the canonical SHA-256 and byte length of the frozen fixture bytes;
5. bind all frozen artifacts to the repository commit used for implementation;
6. complete supplier/provider approved-use review for the synthetic packet;
7. record owner acceptance/treatment of the bounded AR-001 risk register;
8. record retention/deletion rule and incident/recovery ownership;
9. issue a new human/operator pre-code decision receipt.

## Explicit non-blockers for the pre-code gate

Security-boundary execution tests, permission-denial execution tests, and receipt recovery tests require an executable harness and therefore are **not** prerequisites to writing the harness. They remain mandatory prerequisites to `ALLOW_TO_RUN_PILOT`.

This distinction prevents a circular gate while preserving fail-closed execution governance.

## Authorization boundaries

This `REVIEW` decision authorizes only further specification/evidence completion. It does not authorize:

- harness implementation;
- inference calls for AR-001;
- pilot runs;
- cohort runs;
- client/production data;
- network/tool expansion;
- changing frozen experimental outcomes or thresholds.

## Machine-readable receipt

```json
{
  "experiment_id": "AR-001",
  "gate": "ALLOW_TO_WRITE_HARNESS",
  "receipt_version": "0.1",
  "decision": "REVIEW",
  "recorded_date": "2026-08-17",
  "specification_version": "0.2",
  "control_packet_version": "0.1",
  "input_manifest_version": "0.1",
  "permission_configuration_manifest_version": "0.1",
  "experiment_execution_authorized": false,
  "harness_implementation_authorized": false,
  "remaining_precode_requirements": [
    "canonical_fixture_sha256",
    "repository_commit_binding",
    "provider_model_version_configuration",
    "provider_approved_use",
    "promptbp_instruction_artifact_sha256",
    "execution_budget",
    "risk_treatment_owner_acceptance",
    "data_retention_deletion_decision",
    "incident_recovery_owner_designation",
    "human_operator_allow_receipt"
  ],
  "pilot_only_requirements": [
    "permission_boundary_execution_tests",
    "security_boundary_execution_tests",
    "receipt_integrity_recovery_test"
  ],
  "next_gate": "resolve pre-code closure set and supersede this receipt with an evidence-backed ALLOW, REVIEW, or HALT decision"
}
```

## Governance rule

Unknown values remain unknown. Repository agents may prepare evidence and validate records, but may not invent owner authority or self-issue the final human/operator `ALLOW_TO_WRITE_HARNESS` decision.

## v1.0 connection

This receipt provides a durable separation between design completion and implementation authorization, making AR-001 reproducibility evidence auditable rather than dependent on conversational intent or retrospective parameter choices.
