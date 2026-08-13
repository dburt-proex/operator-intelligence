# Field Reliability Study Initiation Packet

Version: `fr-002-initiation-v1.0`  
Stage alignment: v1.1 — Field Reliability Program  
Folder alignment: `reliability/`  
Status: controlled start packet; no human study is currently admitted

## 1. Purpose and boundary

This packet makes the FR-002 start gate executable for one real, authorized
Operator Intelligence assessment. It governs selection, frozen evidence,
blinded evaluator assignment, and pre-analysis admission. It does not create a
study, invent authority, identify an evaluator, establish independence, alter
a score, publish a result, or authorize implementation.

All completed control records, identity mappings, evidence files, ratings, and
study manifests remain in the separately access-controlled study system. Do
not commit real client, evaluator, assessment, evidence, or attestation data to
this repository.

## 2. FR-002 graph path

```text
authorized assessment selection
  -> frozen scope and evidence snapshot
  -> blinded evaluator assignment
  -> independent-rating submission freeze
  -> validator admission and analysis
  -> separate QC / DecisionLedger review
```

Only the first three states are in scope for this initiation packet. The next
state begins only after both assigned evaluators independently submit their
ratings against the same frozen source packet.

## 3. Start decision

The named study authority completes this record in the controlled study system.
It is a decision to begin data collection, not an analysis result or a
publication decision.

```yaml
decision_type: field_reliability_study_start
decision_state: ALLOW|REVIEW|HALT
study_id: OI-FR-YYYY-NNN
record_class: human_field_study
protocol_version: field-reliability-v1.0.1
assessment_id: ""
assessment_owner_ref: ""
scope_ref: ""
methodology_version: ""
criteria_version: ""
calculator_version: ""
weight_profile: ""
authority_ref: ""
authority_issued_at: ""
data_classification: ""
retention_class: ""
retention_rule_ref: ""
study_custodian_ref: ""
decision_authority_ref: ""
decision_recorded_at: ""
```

`ALLOW` requires every required reference to resolve in the controlled study
system. Any missing authorization, scope, retention, owner, or version binding
is `HALT`; uncertain access or unresolved authority is `REVIEW` pending
resolution.

## 4. Assessment selection and evidence freeze

The study owner selects exactly one completed or otherwise authorized real
assessment. The selection must not be synthetic, a repository fixture, or an
assessment used without its owner’s permission.

Before evaluator assignment, create a read-only evidence snapshot containing:

- an exact assessment and scope reference;
- every admissible evidence record available to both evaluators;
- evidence IDs, source locations, content hashes, capture dates, owners,
  authorization references, and limitations;
- the criteria in scope, category mapping, methodology, calculator, and weight
  profile versions;
- explicit exclusions, blocked access, and unknown evidence states;
- a single canonical manifest or index hash, recorded as
  `evidence_snapshot_sha256`.

Do not replace missing evidence with an assumed zero. Evaluators may record
`unknown` or `blocked` exactly as observed. Changes to the snapshot after
assignment invalidate the run: create a new snapshot and new study record.

## 5. Blinded evaluator assignment

The assignment authority maintains the identity map outside the repository.
The ratings and study manifest use only opaque IDs such as `FR-EV-001` and
`FR-EV-002`.

For each evaluator, the controlled authority record must establish:

```yaml
study_id: OI-FR-YYYY-NNN
evaluator_opaque_id: FR-EV-001
assignment_authority_ref: ""
independence_attestation_ref: ""
conflict_disclosure_ref: ""
blinding_acknowledgement_ref: ""
same_snapshot_acknowledgement_ref: ""
submission_deadline: ""
access_grant_ref: ""
identity_map_location_ref: "restricted; not in repository or ratings CSV"
```

The assignment authority must verify, before release of the source packet:

1. At least two distinct people are assigned.
2. Each evaluator has the same frozen evidence snapshot and version set.
3. Evaluators cannot see peer ratings, rationales, aggregates, calibration
   notes, or threshold results before submission freeze.
4. Evaluators do not self-approve their own independence or the study start.
5. Any commercial, delivery, family, employment, or assessment involvement
   conflict is disclosed and resolved by the named authority.
6. The evaluator identity map has restricted storage and a retention rule.

The validator can check opaque IDs and references only. It cannot establish
human identity or independence; that is evidence held by the assignment
authority.

## 6. Reviewer threshold profile

Before ratings begin, the reviewer supplies a versioned threshold profile in
the controlled study record. The profile must include either
`exact_agreement` or `adjacent_agreement`, identify its approver and decision
authority, and stay immutable for the run.

This packet deliberately does not set numeric targets. Threshold selection is
a reviewer decision, not an evaluator decision, and cannot be changed after
evaluator access begins without superseding the study.

## 7. Admission handoff

After both independent submissions are frozen, the study custodian produces:

1. A five-column ratings CSV with the exact header required by
   `field-reliability-protocol.md`.
2. A strict `human_field_study` manifest containing the frozen assessment,
   evidence, authority, retention, evaluator, and threshold references.
3. The CSV SHA-256 in `ratings_sha256` and the frozen source index SHA-256 in
   `evidence_snapshot_sha256`.

Then run:

```bash
python reliability/field_reliability_validator.py \
  /controlled-study/ratings.csv \
  --study-manifest /controlled-study/study-manifest.json
```

`ALLOW` from the validator advances only the bounded analysis result to
separate QC and DecisionLedger review. It never changes approved scores or
authorizes any client-facing claim.

## 8. Stop conditions

| Condition | Gate | Required action |
|---|---|---|
| No real assessment or owner authorization | `HALT` | Do not assign evaluators or create ratings. |
| Snapshot is incomplete, mutable, substituted, or differs by evaluator | `HALT` | Re-freeze a common source packet and issue a new study record. |
| Evaluator identities are not independently controlled or conflicts are unresolved | `HALT` | Resolve through the assignment authority. |
| Required authority, retention, reviewer, or threshold reference is unresolved | `REVIEW` | Do not collect ratings until the reference resolves. |
| A participant can see peer work before submission freeze | `HALT` | Invalidate the run and start a new blinded study. |
| No scored evaluator pairs or a threshold miss | `REVIEW` | Preserve the record; route analysis to qualified review. |

## 9. FR-002 start acceptance

FR-002 data collection may start only when the controlled study system has
evidence for all of the following:

- one real assessment selected under owner authority;
- a read-only, common evidence snapshot with a recorded content hash;
- two or more separately identified people assigned using opaque evaluator IDs;
- independence, conflict, blinding, and same-snapshot acknowledgements;
- restricted identity-map storage and retention controls;
- a reviewer-approved, versioned threshold profile;
- no evaluator ratings or raw evidence stored in this repository.

Until those records exist, FR-002 remains `REVIEW`; no claim of field
reliability is permitted.

## 10. Cross references

- `reliability/field-reliability-protocol.md`
- `standards/evidence-standard.md`
- `standards/quality-control-standard.md`
- `standards/decision-ledger-standard.md`
- `scoring/criteria-library.md`
- `scoring/calculator-spec.md`
