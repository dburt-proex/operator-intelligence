# Realized Value Register

Version: v0.1 post-v1 reliability extension  
Stage alignment: Post-v1 field learning and outcome verification  
Folder alignment: `templates/`  
Status: Governed working template; downstream registration pending

## 1. Purpose

Use this register to distinguish implementation completion from verified business outcomes and to record what changed, what did not change, what remains unknown, and what the evidence supports after an approved recommendation or package enters monitoring.

The register connects baseline evidence, implementation completion, outcome evidence, attribution confidence, realized-value state, renewal or closure decisions, and methodology feedback without changing the original assessment score or overstating causation, savings, revenue, ROI, ranking, lead, conversion, or operational effects.

## 2. Trigger and prerequisites

Open a realized-value record only when:

- a governed recommendation, roadmap item, or package has a stable identifier;
- implementation completion, monitoring, or a no-action decision has been recorded;
- the baseline, intended effect, measurement owner, and review window are known or explicitly marked unknown;
- outcome evidence can be handled under the engagement's authority, privacy, retention, and evidence rules; and
- no unresolved `HALT` condition prohibits measurement or downstream use.

Completion is not evidence of realized value. A record may remain `not_measured`, `measurement_planned`, `measurement_active`, or `insufficient_evidence` without being treated as a negative result.

## 3. Register controls

| Field | Value |
|---|---|
| Engagement ID | |
| Assessment ID | |
| Client | |
| Register version | |
| Methodology version | |
| Evidence snapshot date | |
| Measurement owner | |
| Reviewer | |
| Decision authority | |
| QC reference | |
| DecisionLedger register ref | |

## 4. Controlled values

### 4.1 Realized-value state

`not_measured`, `measurement_planned`, `measurement_active`, `insufficient_evidence`, `no_material_change`, `positive_signal`, `negative_signal`, `mixed_result`, `validated_value`, `disputed`, `closed`

### 4.2 Attribution confidence

`high`, `medium`, `low`, `unknown`

### 4.3 Review state

`ALLOW`, `REVIEW`, `HALT`

### 4.4 Renewal decision

`not_due`, `continue_monitoring`, `optimize`, `maintain`, `renew`, `expand_scope`, `close`, `declined`, `blocked`

## 5. Register summary

| Realized Value ID | Recommendation ref | Package ref | Measurement window | Realized-value state | Attribution confidence | Renewal decision | Review state | Ledger ref |
|---|---|---|---|---|---|---|---|---|
| OI-RV-YYYY-NNN | | | | | | | | |

## 6. Realized-value record

### 6.1 Identity and source chain

```yaml
realized_value_id: OI-RV-YYYY-NNN
record_version: "1.0"
supersedes: null
engagement_id: ""
assessment_id: ""
recommendation_id: ""
package_id: null
roadmap_item_ref: null
implementation_record_ref: null
completion_evidence_refs: []
baseline_evidence_refs: []
outcome_evidence_refs: []
ledger_refs: []
```

### 6.2 Intended effect and measurement question

**Approved recommendation or package objective**  
[Restate the governed objective without adding new promises.]

**Measurement question**  
[State the bounded decision this review should support.]

**Expected effect**  
[Describe the direction or operational condition expected if the implementation works as intended.]

```yaml
expected_effect_type: visibility|conversion|trust|response_time|workflow_quality|data_quality|cost_control|risk_reduction|adoption|other
expected_effect_statement: ""
expected_effect_source_ref: null
unsupported_guarantee_present: false
```

Expected effect is not a forecast guarantee. If the source recommendation did not define a measurable effect, record a methodology or planning gap rather than inventing one.

### 6.3 Baseline

```yaml
baseline_period_start: null
baseline_period_end: null
baseline_metric_definition: ""
baseline_value: null
baseline_unit: null
baseline_scope: ""
baseline_evidence_refs: []
baseline_confidence: high|medium|low|unknown
baseline_limitations: []
```

Baseline evidence must use the same material metric definition, scope, attribution boundary, and unit as the outcome comparison unless the change is documented and reviewed.

### 6.4 Implementation and adoption context

```yaml
implementation_state: not_started|in_progress|complete|accepted|rejected|cancelled|superseded
implementation_completed_at: null
implementation_scope: ""
implementation_exceptions: []
adoption_state: unknown|limited|partial|substantial|sustained
adoption_evidence_refs: []
residual_risks: []
```

Implementation completion confirms that approved acceptance criteria were met. Adoption and continued use require separate evidence.

### 6.5 Measurement window and observed result

```yaml
measurement_period_start: null
measurement_period_end: null
reviewed_at: null
observed_metric_definition: ""
observed_value: null
observed_unit: null
observed_change_absolute: null
observed_change_percent: null
observed_effect_statement: ""
outcome_evidence_refs: []
```

Do not calculate percentage change when the baseline is missing, zero, incomparable, or outside the approved scope. Record the limitation instead.

### 6.6 Attribution assessment

```yaml
attribution_confidence: high|medium|low|unknown
attribution_basis: ""
material_confounders: []
external_changes: []
parallel_interventions: []
data_quality_limitations: []
seasonality_or_timing_effects: []
alternative_explanations: []
validation_required: []
```

Attribution confidence reflects whether the observed result can reasonably be connected to the governed implementation. It does not modify the original recommendation priority, assessment maturity score, or evidence confidence assigned during the assessment.

### 6.7 Realized-value decision

```yaml
realized_value_state: not_measured|measurement_planned|measurement_active|insufficient_evidence|no_material_change|positive_signal|negative_signal|mixed_result|validated_value|disputed|closed
realized_value_summary: ""
financial_value_asserted: false
financial_value_method_ref: null
client_position: accepted|partially_accepted|disputed|not_reviewed
review_state: ALLOW|REVIEW|HALT
review_reason: ""
reviewed_by: ""
reviewed_at: ""
approved_by: null
approved_at: null
```

Rules:

- `validated_value` requires attributable, in-scope, sufficiently complete outcome evidence and a passed review gate.
- `positive_signal` or `negative_signal` may describe direction without establishing causation.
- `mixed_result` preserves conflicting effects rather than averaging them into a single conclusion.
- `insufficient_evidence` is not automatically negative.
- Financial value may be stated only when the governing ROI method, assumptions, evidence, scope, and limitations are recorded.
- Disputed outcomes remain visible and cannot be overwritten by a preferred narrative.

### 6.8 Unintended effects and residual conditions

```yaml
positive_unintended_effects: []
negative_unintended_effects: []
new_risks: []
open_unknowns: []
corrective_actions: []
escalation_refs: []
```

Any safety, privacy, legal, customer-harm, financial-commitment, unauthorized-access, or irreversible-action concern routes to the applicable G4 boundary and may require `HALT`.

### 6.9 Renewal, optimization, maintenance, or closure

```yaml
renewal_decision: not_due|continue_monitoring|optimize|maintain|renew|expand_scope|close|declined|blocked
renewal_decision_reason: ""
next_review_date: null
next_owner: ""
next_evidence_required: []
new_recommendation_required: false
new_recommendation_refs: []
closure_state: open|monitoring|renewed|closed|blocked
```

A realized-value record may inform a new recommendation, but it cannot silently expand scope, authorize implementation, or reuse the original authorization for new work.

### 6.10 Methodology and package feedback

```yaml
methodology_feedback_state: none|candidate|validation_required|approved_for_review
criterion_feedback: []
anchor_ambiguities: []
finding_feedback: []
priority_feedback: []
package_scope_feedback: []
measurement_design_feedback: []
reliability_study_refs: []
methodology_change_authorized: false
methodology_change_ledger_ref: null
```

Field outcomes may generate calibration evidence. They do not directly modify scoring criteria, anchors, findings, package scope, or publication rules. Any methodology change requires aggregated evidence, reliability review, versioning, and a separate DecisionLedger approval.

## 7. Evidence and claim rules

1. Separate baseline, completion, adoption, outcome, attribution, and client-position evidence.
2. Record source, owner, date, scope, method, limitations, and integrity reference for every material evidence item.
3. Preserve unknowns, contradictions, disputes, and missing access.
4. Do not treat a before-and-after difference as causation without an attribution assessment.
5. Do not convert client opinion into verified performance without corroboration.
6. Do not compare unlike periods, populations, locations, services, channels, or metric definitions without disclosure and review.
7. Do not claim realized ROI from modeled opportunity alone.
8. Supersede approved records; do not overwrite history.
9. Record every material state, interpretation, renewal, escalation, or closure decision in the DecisionLedger.

## 8. Report-use rules

### Client-safe language

Use:

> The implementation was completed and the available monitoring evidence indicates a positive directional change during the reviewed period. Attribution remains medium because seasonality and a parallel campaign cannot be fully isolated.

Avoid:

> The package increased revenue.

unless direct evidence, scope, attribution, and the approved financial method support that conclusion.

### Publication boundaries

- Internal monitoring notes may remain unpublished.
- A client-facing realized-value statement requires QC and a separate publication decision.
- `positive_signal`, `negative_signal`, and `mixed_result` must disclose attribution confidence and material limitations.
- `validated_value` must identify the measurement window and supporting evidence.
- Outcome publication never authorizes new implementation work.

## 9. Change control

| Change date | Prior version | Material change | Reason | Evidence effect | Decision effect | Ledger ref | Reviewer |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Material changes require versioning, supersession, dependent-record review, and DecisionLedger traceability.

## 10. Release validation

- [ ] Recommendation, package, roadmap, implementation, and completion references resolve.
- [ ] Expected effect matches the approved source objective.
- [ ] Baseline and outcome definitions are materially comparable.
- [ ] Completion, adoption, outcome, and realized value remain separate.
- [ ] Outcome evidence includes scope, period, source, owner, and limitations.
- [ ] Attribution confidence is supported and alternative explanations are visible.
- [ ] Unknown or insufficient evidence is not treated as failure.
- [ ] Percentage and financial calculations are reproducible and governed.
- [ ] No unsupported causation, revenue, savings, ranking, lead, conversion, or ROI claim appears.
- [ ] Disputes and contradictory evidence remain visible.
- [ ] Renewal or closure does not silently authorize new work.
- [ ] Methodology feedback does not alter canonical controls without separate approval.
- [ ] QC, publication, renewal, proposal, and implementation authorization remain separate.
- [ ] DecisionLedger traceability is complete.

Any failed evidence, attribution, claim, authority, privacy, traceability, or unresolved `HALT` check requires `HALT` or removal of the unsupported assertion.

## 11. Usage instructions

1. Create the record when implementation enters monitoring or when a no-action outcome requires later review.
2. Resolve source recommendation, package, roadmap, completion, and evidence IDs.
3. Freeze the baseline definition before interpreting outcomes.
4. Record the measurement window, observed result, confounders, and attribution confidence.
5. Assign the realized-value state conservatively.
6. Complete QC before any client-facing outcome statement.
7. Record renewal, optimization, maintenance, closure, or validation decisions separately.
8. Route methodology observations into reliability review rather than changing the method in place.

## 12. Commercial v1.0 and post-v1 connection

Commercial v1.0 already separates completion evidence from realized-value evidence and places monitoring, optimization, renewal, maintenance, and closure in Phase 5. This register closes the missing record layer between delivery completion and evidence-backed field learning.

It supports post-v1 recommendation calibration, package evaluation, renewal decisions, case-study evidence, defensible outcome language, and future automation while preserving the approved commercial-v1 methodology.

## 13. Canonical references

- `framework/assessment-lifecycle.md`
- `framework/lifecycle-roadmap-map.md`
- `framework/roi-framework.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
- `templates/evidence-register.md`
- `templates/recommendation-register.md`
- `templates/roadmap.md`
- `templates/decision-ledger.md`
- `templates/delivery-checklist.md`
