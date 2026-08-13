# Field Reliability Protocol

Version: `field-reliability-v1.0.1`
Stage alignment: v1.1 — Field Reliability Program  
Folder alignment: `reliability/`  
Status: FR-001 governed protocol and input contract

## 1. Purpose and boundary

This protocol defines how Operator Intelligence collects and admits blinded multi-evaluator rating records for reliability analysis. It measures evaluator agreement; it does not alter approved assessment scores, accept a methodology change, authorize publication, authorize implementation, or prove business outcomes.

FR-001 establishes the protocol, manifest, CSV admission checks, structural fixtures, and deterministic analysis surface. FR-002 begins only after independent evaluators produce authorized human-study records under this protocol.

## 2. Required study conditions

Before a human field study starts:

1. Freeze one assessment cohort, scope, evidence snapshot, methodology version, criteria version, calculator version, and weight profile.
2. Assign at least two evaluators through a separately controlled authority record.
3. Assign pseudonymous evaluator IDs. Do not put names, emails, client identifiers, raw evidence, or evaluator-to-identity mappings in the ratings CSV or repository.
4. Keep each evaluator blind to peer ratings, rationales, aggregates, threshold results, and calibration discussion until their rating submission is frozen.
5. Record the authority, evaluator-independence/conflict attestation reference, data classification, retention rule, and reviewer-owned threshold profile in the manifest.
6. Preserve source ratings as read-only after the manifest's `ratings_sha256` is recorded. Any material correction creates a new study record and superseding DecisionLedger event when the study is real and material.

The validator checks record structure and references. It does not prove that an attestation, identity separation, or external authority is genuine. Those are FR-002 evidence responsibilities.

## 3. Records and ownership

| Record | Owner | Purpose | Prohibited use |
|---|---|---|---|
| Ratings CSV | Study custodian | One evaluator state per criterion | Identity map, client PII, evidence narrative, score mutation |
| Study manifest | Study owner and reviewer | Version, scope, integrity, blinding, authority, retention, threshold references | Evidence of human independence by itself |
| Analysis output | Validator | Deterministic agreement metrics and `ALLOW`/`REVIEW`/`HALT` analysis gate | Publication or implementation authorization |
| DecisionLedger event | Named decision authority | Real material study admission, analysis, supersession, or methodology decision | Replacement for underlying source records |

Synthetic structural fixtures are repository test artifacts only. They may demonstrate parser and gate behavior but must never be cited as evaluator, calibration, scoring, or commercial evidence.

## 4. Ratings CSV contract

The CSV header must be exactly, in this order:

```csv
criterion_id,category,evaluator_id,state,score
```

| Field | Rule |
|---|---|
| `criterion_id` | Existing canonical ID from `scoring/criteria-library.md`. |
| `category` | Canonical category matching the criterion prefix. `OI-MSG-*` and `OI-OFFER-*` both use `messaging_offer`. |
| `evaluator_id` | Opaque pseudonymous ID listed exactly once in the manifest. |
| `state` | `scored`, `unknown`, `blocked`, or `not_applicable`. |
| `score` | Blank unless `state=scored`; then exactly `0`, `25`, `50`, `75`, or `100`. |

The row identity is `(study_id, criterion_id, evaluator_id)`. `study_id` is carried by the manifest; duplicate `(criterion_id, evaluator_id)` rows halt admission. Unknown, blocked, and not-applicable are never numeric zeroes and do not become score pairs. They remain visible in state-agreement analysis.

## 5. Study-manifest contract

The manifest is strict JSON with `schema_version: oi-field-reliability-study-v1`. Unknown or missing durable fields halt admission.

```json
{
  "schema_version": "oi-field-reliability-study-v1",
  "study_id": "OI-FR-YYYY-NNN",
  "record_class": "synthetic_contract_fixture | human_field_study",
  "protocol_version": "field-reliability-v1.0.1",
  "methodology_version": "",
  "criteria_version": "",
  "calculator_version": "",
  "weight_profile": "",
  "scope_ref": "",
  "evidence_snapshot_ref": "",
  "evidence_snapshot_sha256": "lowercase SHA-256",
  "ratings_sha256": "lowercase SHA-256",
  "blinding_status": "blinded | not_blinded",
  "evaluator_count": 2,
  "evaluator_ids": ["opaque-ID-1", "opaque-ID-2"],
  "independence_attestation_ref": "",
  "authority_ref": "",
  "retention_class": "",
  "retention_rule_ref": "",
  "threshold_profile": {
    "profile_id": "",
    "version": "",
    "approved_by": "",
    "decision_authority": "",
    "metrics": {"exact_agreement": 0.0}
  },
  "reviewer_id": "",
  "decision_authority": "",
  "created_at": "YYYY-MM-DDThh:mm:ssZ"
}
```

Human-study records require `blinding_status: blinded`, two or more unique evaluator IDs exactly matching the CSV, a non-empty approved threshold profile, and an `exact_agreement` or `adjacent_agreement` threshold. Threshold values must be between `0` and `1`; this protocol deliberately sets no numeric target. Target selection needs separate reviewer authority and is retained in the manifest.

The manifest binds the supplied CSV through `ratings_sha256`. A changed or substituted CSV halts before analysis. `evidence_snapshot_sha256` records the frozen assessment source snapshot; resolving and retaining that source remains the study owner's responsibility.

## 6. Gates and handling

| Condition | Gate | Required handling |
|---|---|---|
| Malformed manifest, header, ID, category, hash, evaluator set, score state, blinding, authority, retention, or threshold profile | `HALT` | Do not analyze or claim a field result. Correct through a new manifest/source record. |
| Synthetic fixture | `REVIEW` | Validates the contract only. No field-reliability conclusion or ledger claim. |
| Human record with no scored pairs or threshold miss | `REVIEW` | Preserve metrics and disagreements; route to qualified review. |
| Human record meeting its reviewer-approved thresholds | `ALLOW` | Allows only the bounded analysis result to advance to its separate QC/DecisionLedger gate. |

`ALLOW` does not authorize score replacement, scoring-method change, report publication, package routing, implementation, or a public reliability claim.

## 7. Required analysis and later handoff

The validator reports exact score agreement, adjacent score agreement, state agreement, quadratic weighted kappa, category mean absolute delta, and disagreement records. It deterministically sorts criteria and evaluator IDs.

For a real study, the later immutable analysis/ledger record must reference the study ID, protocol and methodology versions, criteria/calculator/weight profile, scope and evidence snapshot refs/hashes, pseudonymous evaluator IDs, blinding/attestation/authority/retention refs, threshold profile, input hash, output hash, gate, reason codes, reviewer, and DecisionLedger ID. It must not contain the identity map or raw evidence.

## 8. Usage

```bash
python reliability/field_reliability_validator.py --self-test

python reliability/field_reliability_validator.py \
  reliability/fixtures/field-reliability-contract-valid.csv \
  --study-manifest reliability/fixtures/field-reliability-contract-valid.manifest.json
```

The valid repository fixture exits `1` with `REVIEW` by design. It is structurally valid but synthetic. A malformed input exits `2` with `HALT`.

## 9. Acceptance criteria

- [x] Versioned protocol and strict manifest contract exist.
- [x] CSV header, canonical criterion/category pairing, evaluator identity set, score states, and SHA-256 binding fail closed.
- [x] Unknown, blocked, and not-applicable carry no numeric score.
- [x] Synthetic fixtures are visibly synthetic and cannot return field-reliability `ALLOW`.
- [x] Human-study admission requires blinding, authority, retention, independence-attestation, version, and reviewer threshold references.
- [x] The validator does not mutate scores, create a publication decision, or authorize implementation.

## 10. Cross references

- `ROADMAP.md`
- `scoring/criteria-library.md`
- `scoring/calculator-spec.md`
- `scoring/unknown-data-handling.md`
- `standards/evidence-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
