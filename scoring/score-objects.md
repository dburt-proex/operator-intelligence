# Operator Intelligence Score Objects

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines the canonical data objects used to record, calculate, validate, audit, and report Operator Intelligence scores.

The objects create a stable contract between evidence collection, criterion scoring, category aggregation, Operator Score calculation, findings, reports, roadmaps, and future software implementations.

## v1.0 connection

Commercial v1.0 requires scoring records that can be reproduced and reviewed without relying on evaluator memory.

This file strengthens v1.0 readiness by providing:

- stable score object identifiers
- required and optional fields
- controlled state vocabularies
- version and provenance requirements
- criterion, category, and Operator Score schemas
- validation-error structures
- audit and approval fields
- report-safe output rules

## Object hierarchy

```text
Score Run
├── Evidence References
├── Criterion Score Objects
├── Category Score Objects
├── Operator Score Object
├── Validation Errors and Warnings
└── Review and Approval Record
```

A client-facing score must be reproducible from this hierarchy.

## Identifier conventions

| Object | ID pattern |
|---|---|
| Score run | `OI-SCORE-YYYY-NNN` |
| Criterion score | `OI-CS-YYYY-NNNN` |
| Category score | `OI-CAT-YYYY-NNN` |
| Operator Score | `OI-OS-YYYY-NNN` |
| Evidence reference | `OI-EV-YYYY-NNNN` |
| Validation message | `OI-VAL-YYYY-NNNN` |
| DecisionLedger record | `OI-DL-YYYY-NNN` |

IDs are immutable after creation. Corrections create a new version or superseding object rather than silently rewriting history.

## Controlled vocabularies

### Evaluation state

- `scored`
- `unknown`
- `not_applicable`
- `blocked`

### Validation state

- `verified`
- `partial`
- `validation_required`
- `conflicting`
- `not_observed`

### Confidence

- `high`
- `medium`
- `low`
- `unknown`

### Publication state

- `official`
- `provisional`
- `range_only`
- `blocked`

### Message severity

- `error`
- `warning`
- `advisory`

### Review state

- `draft`
- `review_required`
- `approved`
- `superseded`
- `rejected`

## Evidence reference object

```yaml
evidence_ref: OI-EV-YYYY-NNNN
evidence_type: screenshot
source_class: A
source_location: ""
captured_at: ""
captured_by: ""
summary: ""
related_criteria: []
access_state: available
integrity_notes: []
limitations: []
client_provided: false
verified: false
```

### Required fields

- `evidence_ref`
- `evidence_type`
- `source_class`
- `source_location` or an approved internal record reference
- `captured_at`
- `summary`
- `limitations`

Evidence objects do not contain conclusions. They record what was observed or supplied.

## Criterion score object

```yaml
criterion_score_id: OI-CS-YYYY-NNNN
score_run_id: OI-SCORE-YYYY-NNN
criterion_id: OI-CONV-001
category_key: conversion
criterion_version: ""
applicability_state: applicable
evaluation_state: scored
unknown_reason: null
not_applicable_reason: null
score_anchor: 75
raw_score: 75
criterion_weight: 0.0714
evidence_refs: []
evidence_classes: []
observation: ""
scoring_rationale: ""
confidence: high
confidence_factor: 1.0
lower_bound: 75
upper_bound: 75
validation_state: verified
duplicate_group: null
dependent_criteria: []
finding_refs: []
flags: []
review_state: draft
reviewer: ""
approver: ""
created_at: ""
updated_at: ""
ledger_ref: OI-DL-YYYY-NNN
```

### Criterion object rules

1. `score_anchor` is required only when `evaluation_state` is `scored`.
2. `score_anchor` must be `0`, `25`, `50`, `75`, or `100` unless an approved category sheet permits interpolation.
3. `unknown` and `blocked` criteria must not contain a numeric performance score.
4. `not_applicable` requires a reason and approval record.
5. Evidence references and scoring rationale are required for a scored criterion.
6. Confidence must reflect evidence quality, not evaluator certainty alone.
7. Duplicate groups must be recorded when several criteria use the same underlying signal.
8. Finding references are downstream outputs and may be empty during initial scoring.

## Unknown-reason vocabulary

- `not_provided`
- `access_unavailable`
- `not_tested`
- `insufficient_sample`
- `conflicting_evidence`
- `internal_process_unverified`
- `policy_restricted`
- `system_error`
- `methodology_gap`
- `other_documented`

The reason must be paired with a validation owner or a statement that validation is not currently planned.

## Category score object

```yaml
category_score_id: OI-CAT-YYYY-NNN
score_run_id: OI-SCORE-YYYY-NNN
category_key: conversion
category_name: Conversion infrastructure
category_version: ""
weight_profile: default
category_weight: 0.15
criterion_score_refs: []
applicable_criterion_count: 0
scored_criterion_count: 0
unknown_criterion_count: 0
not_applicable_criterion_count: 0
blocked_criterion_count: 0
known_criterion_weight: 0
unknown_criterion_weight: 0
applicable_criterion_weight: 0
observed_score: null
minimum_score: 0
maximum_score: 100
coverage_percent: 0
confidence_index: 0
confidence: unknown
publication_state: range_only
maturity_interpretation: unresolved
material_unknowns: []
validation_errors: []
warnings: []
primary_findings: []
review_state: draft
reviewer: ""
approver: ""
ledger_ref: OI-DL-YYYY-NNN
```

### Category object rules

1. `category_weight` must match the active weight profile.
2. Criterion score references must map to the category according to the approved category map.
3. `observed_score` is null when no criterion can be scored.
4. Minimum and maximum must include unresolved criterion weight.
5. Coverage must be calculated from weight, not criterion count, when non-equal weights exist.
6. Publication state must follow `scoring/calculator-spec.md`.
7. A category with a material unresolved G4 issue cannot be `reportable`.
8. Client-facing category language must disclose provisional or range-only status.

## Operator Score object

```yaml
operator_score_id: OI-OS-YYYY-NNN
score_run_id: OI-SCORE-YYYY-NNN
client_ref: ""
assessment_date: ""
calculator_version: "0.1"
criteria_version: ""
category_map_version: "0.1"
weight_profile: default
weight_profile_version: ""
category_score_refs: []
active_category_weight: 1.0
weighted_evidence_coverage: 0
observed_normalized_score: null
operator_minimum: 0
operator_maximum: 100
published_score: null
publication_state: range_only
maturity_tier: unresolved
confidence_index: 0
confidence: unknown
material_unknowns: []
control_boundary_flags: []
validation_errors: []
warnings: []
report_language: ""
review_state: draft
reviewer: ""
approver: ""
created_at: ""
supersedes: null
ledger_ref: OI-DL-YYYY-NNN
```

### Operator Score object rules

1. `published_score` is permitted only when publication-state gates allow a point estimate.
2. `observed_normalized_score` must disclose included active weight and cannot be silently presented as the official score.
3. `operator_minimum` and `operator_maximum` must use all active categories.
4. Maturity tier is unresolved when a point estimate is prohibited or the range crosses material tier boundaries.
5. Confidence is separate from maturity score.
6. A blocked score object may still retain internal calculations for audit, but no client-facing score may be published.
7. Any superseding score object must reference the prior object.

## Score run object

```yaml
score_run_id: OI-SCORE-YYYY-NNN
client_ref: ""
engagement_ref: ""
lifecycle_state: OI-LC-05
run_type: initial
calculator_version: "0.1"
criteria_version: ""
grading_rubric_version: ""
evidence_threshold_version: ""
confidence_model_version: ""
unknown_handling_version: "0.1"
confidence_adjustment_version: "0.1"
category_map_version: "0.1"
weight_profile: default
weight_profile_version: ""
started_at: ""
completed_at: ""
evaluator: ""
reviewer: ""
approver: ""
evidence_refs: []
criterion_score_refs: []
category_score_refs: []
operator_score_ref: ""
validation_message_refs: []
assumptions: []
unknowns: []
methodology_exceptions: []
status: in_progress
ledger_ref: OI-DL-YYYY-NNN
```

### Run types

- `initial`
- `evidence_update`
- `review_correction`
- `weight_profile_change`
- `post_implementation`
- `renewal`

A run must not mix evidence from materially different assessment periods without recording the date boundary and rationale.

## Validation message object

```yaml
validation_message_id: OI-VAL-YYYY-NNNN
score_run_id: OI-SCORE-YYYY-NNN
severity: error
code: WEIGHT_TOTAL_INVALID
object_ref: ""
message: ""
blocking: true
required_action: ""
owner: ""
status: open
resolved_at: null
resolution_notes: ""
```

## Standard validation codes

### Weight and mapping

- `WEIGHT_TOTAL_INVALID`
- `CATEGORY_MAPPING_MISSING`
- `CRITERION_DUPLICATE_MAPPING`
- `CRITERION_WEIGHT_INVALID`
- `WEIGHT_PROFILE_UNAPPROVED`

### Evidence and score

- `EVIDENCE_MISSING`
- `EVIDENCE_THRESHOLD_FAILED`
- `SCORE_WITHOUT_CONFIDENCE`
- `UNKNOWN_WITH_NUMERIC_SCORE`
- `INVALID_SCORE_ANCHOR`
- `CONFLICTING_EVIDENCE`
- `DUPLICATE_SIGNAL_RISK`

### Applicability and coverage

- `NOT_APPLICABLE_UNJUSTIFIED`
- `CATEGORY_COVERAGE_LOW`
- `OPERATOR_COVERAGE_LOW`
- `MATERIAL_UNKNOWN_UNRESOLVED`
- `SCORE_RANGE_CROSSES_TIERS`

### Governance and publication

- `CONTROL_BOUNDARY_OPEN`
- `PUBLICATION_STATE_INVALID`
- `APPROVAL_MISSING`
- `VERSION_MISSING`
- `LEDGER_REFERENCE_MISSING`
- `SOCIAL_FINDING_ROUTE_UNAVAILABLE`

## Review and approval rules

| Object | Minimum review requirement |
|---|---|
| Evidence reference | Capturer or evaluator verification |
| Criterion score | Evaluator; reviewer for low confidence, conflicts, or interpolation |
| Category score | Reviewer when provisional, range-only, or category weight is 10% or more |
| Operator Score | Named reviewer and approver before client publication |
| Methodology exception | Methodology owner approval |

The same person may evaluate and review in a small engagement only when the report discloses the single-reviewer condition and no G3 or G4 issue is present.

## Immutability and correction

1. Client-published score objects are immutable.
2. Corrections create a superseding object and preserve the original.
3. Evidence may be appended, but prior evidence references must not be silently removed.
4. Score-run versions must identify the exact methodology inputs used.
5. Recalculation after new evidence requires a new run or documented run version.
6. The reason for score change must be recorded.

## Client-facing output object

```yaml
category: Conversion infrastructure
score_display: "63"
score_state: provisional
range_display: "55–75"
coverage_display: "72%"
confidence_display: medium
summary: ""
material_unknowns: []
next_validation_action: ""
```

Do not expose internal precision, hidden assumptions, or normalized-score substitutions without explanation.

## DecisionLedger integration

Every Operator Score publication record must include:

```yaml
score_run_id: OI-SCORE-YYYY-NNN
operator_score_ref: OI-OS-YYYY-NNN
methodology_versions: {}
publication_state: provisional
published_score: null
score_range: [0, 100]
coverage_percent: 0
confidence: unknown
material_unknowns: []
validation_errors: []
approval: ""
publication_decision: validate
reason: ""
```

## Usage instructions

1. Create the score run before creating score objects.
2. Register evidence references without interpretation.
3. Create one criterion score object per applicable criterion.
4. Resolve unknown and not-applicable states explicitly.
5. Calculate category objects from criterion references.
6. Calculate the Operator Score object from category references.
7. Generate validation objects.
8. Complete review and approval.
9. Publish only the approved client-facing fields.
10. Preserve all objects for audit and future recalculation.

## Completion check

Before closing a score run, confirm:

- all objects have stable IDs
- methodology versions are present
- evidence and score rationale are linked
- criterion states are valid
- unknowns contain no numeric score
- exclusions are approved
- category and Operator Score calculations reconcile
- validation messages are resolved or disclosed
- publication state is correct
- reviewer and approver are recorded
- DecisionLedger traceability exists
