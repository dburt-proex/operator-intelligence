# Operator Intelligence DecisionLedger Record Template

Use this template for every material decision affecting scoring, confidence, unknown handling, findings, recommendations, package routing, roadmap sequencing, publication, approval, exception, halt, or supersession.

The ledger records the decision and its traceability. It does not replace evidence, scoring logic, quality control, publication approval, or implementation authorization.

## Record metadata

```yaml
ledger_id: OI-DL-YYYY-NNN
assessment_id: ""
score_run_id: ""
methodology_version: ""
status: draft
created_at: ""
updated_at: ""
```

**Allowed status values:** `draft`, `review_required`, `approved`, `rejected`, `superseded`, `closed`

## Governed decision

```yaml
decision_type: ""
subject_type: ""
subject_id: ""
decision: ""
rationale: ""
control_gate: REVIEW
```

**Allowed decision types:** `scoring`, `confidence`, `unknown_handling`, `finding`, `recommendation`, `package_routing`, `roadmap`, `publication`, `exception`, `approval`, `halt`, `supersession`

**Allowed control gates:** `ALLOW`, `REVIEW`, `HALT`

Use `ALLOW` only when evidence, authority, dependencies, and applicable standards support proceeding. Use `REVIEW` when qualified judgment or validation is required. Use `HALT` when proceeding would violate an evidence, authorization, dependency, methodology, publication, or client-safety gate.

## Traceability references

```yaml
evidence_refs: []
criterion_refs: []
finding_refs: []
recommendation_refs: []
prior_ledger_ref: null
supersedes: null
```

All upstream material references must remain resolvable. A decision without evidence must document why evidence is unavailable and what validation is required.

## Evidence interpretation

### Observation

[State only what was directly observed or supplied.]

### Interpretation

[Explain what the evidence supports without exceeding its scope.]

```yaml
confidence: unknown
unknown_state: none
limitations: []
assumptions: []
validation_required: []
```

**Allowed confidence values:** `high`, `medium`, `low`, `unknown`

**Allowed unknown states:** `none`, `unknown`, `blocked`, `not_applicable`

Unknown and blocked conditions remain unscored. Missing access is not negative evidence, and public absence cannot prove that an internal capability does not exist.

## Finding decision

Complete when the record creates, revises, suppresses, or closes a finding.

```yaml
finding_action: null
business_relevance: ""
weighted_owner: null
reference_only_uses: []
```

**Finding action values:** `create`, `revise`, `suppress`, `close`, or `null`

A finding requires evidence, business relevance, confidence, and a governed subject. Suppressed findings remain traceable with the suppression reason. Duplicate signals must identify one weighted owner; all other uses are reference-only.

## Recommendation and package routing

Complete when the record affects a recommendation or delivery route.

```yaml
recommendation_class: null
primary_package: null
secondary_packages: []
dependency_refs: []
roadmap_phase: null
implementation_authorization: not_requested
acceptance_evidence_required: []
```

Every implementation recommendation requires exactly one primary package. Secondary packages may represent prerequisite, dependency, downstream, or reference relationships only. Validation recommendations may precede package selection when evidence is insufficient.

**Implementation authorization values:** `not_requested`, `pending`, `authorized`, `declined`, `blocked`

Roadmap phase must follow the canonical roadmap standard. Priority alone cannot bypass prerequisites. Undefined workflows cannot advance into automation, and AI work cannot advance without required workflow, data, privacy, review, escalation, logging, and QA controls.

## Publication effect

```yaml
publication_effect: none
publication_state_ref: null
weighted_evidence_coverage: null
report_version: null
```

**Allowed publication effects:** `none`, `official`, `provisional`, `range_only`, `blocked`, `internal_only`

Published scores must disclose evidence coverage and limitations. Publication approval does not authorize implementation.

## Ownership and approval

```yaml
decided_by: ""
decided_at: ""
reviewed_by: ""
reviewed_at: null
approved_by: ""
approved_at: null
```

Package routing, roadmap changes, publication, exceptions, approvals, `HALT`, and supersession require review and approval. Record names or accountable roles; do not use unassigned placeholders in a released ledger.

## Change control

Complete when correcting or replacing a prior decision.

```yaml
change_reason: null
new_or_corrected_evidence_refs: []
dependent_records_updated: []
```

Approved records must not be silently overwritten. Corrections create a new record that references and supersedes the prior record while preserving the original history.

## Client-safe summary

```yaml
client_safe_summary: ""
```

Use plain executive language that distinguishes observation from interpretation, discloses material limitations, avoids certainty beyond the evidence, and does not imply publication or implementation authority. Do not state unsupported ROI, revenue, lead-loss, conversion, ranking, market-share, competitor-performance, or timeline claims.

## Pre-approval validation

- [ ] `ledger_id` is unique and immutable.
- [ ] Assessment or score-run reference is present.
- [ ] Decision type, subject, decision, and rationale are explicit.
- [ ] Evidence references are present, or the evidence limitation is documented.
- [ ] Confidence does not exceed the supporting evidence chain.
- [ ] Unknown or blocked conditions remain unscored.
- [ ] Control gate matches the unresolved risk and authority state.
- [ ] Findings identify governed evidence and business relevance.
- [ ] Duplicate signals have one weighted owner.
- [ ] Each implementation recommendation has exactly one primary package.
- [ ] Roadmap phase respects dependencies and entry gates.
- [ ] Publication effect matches the publication standard.
- [ ] Publication approval and implementation authorization remain separate.
- [ ] Material decisions include required reviewer and approver records.
- [ ] Supersession preserves prior history and updates dependent records.
- [ ] Client-safe summary avoids unsupported claims.

## Release decision

```yaml
quality_control_result: REVIEW
release_blockers: []
final_status: review_required
```

Any failed blocking check requires `HALT` until a superseding record resolves the condition.