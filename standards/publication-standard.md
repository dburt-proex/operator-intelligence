# Publication Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Reconciled commercial v1.0 control standard; pending folder approval

## 1. Purpose

This standard governs when an Operator Intelligence assessment, category result, Operator Score, finding set, roadmap, or recommendation may be released to a client or represented as an official deliverable.

Publication is a governed decision. It does not replace scoring, evidence review, confidence assignment, package routing, or implementation authorization.

## 2. Core rules

1. Publication state must reflect evidence coverage, confidence, unresolved unknowns, control boundaries, and DecisionLedger completeness.
2. A numeric score may not be published without its evidence coverage and applicable limitations.
3. Unknown and blocked conditions must remain visible.
4. Confidence remains separate from maturity.
5. A finding requires admissible evidence, interpretation, business impact, confidence, and DecisionLedger traceability.
6. A recommendation requires a valid finding, prerequisite review, approved package routing, and roadmap phase.
7. Publication does not authorize implementation.
8. Unsupported revenue, ROI, conversion, lead-loss, market-share, or competitor-performance claims are prohibited.
9. Report language may not imply internal failure from public absence alone.
10. Material publication decisions must be auditable and versioned.

## 3. Approved publication states

| State | Use when | Client treatment |
|---|---|---|
| `official` | Required scope is complete, evidence coverage meets threshold, material confidence is adequate, and no unresolved publication blocker exists | May publish category scores, Operator Score, findings, roadmap, and governed recommendations |
| `provisional` | The assessment is usable but one or more bounded evidence, confidence, or validation limitations remain | Publish with explicit limitations and validation requirements |
| `range_only` | Material unknowns, blocked criteria, or low-confidence conditions could materially change the result | Publish only defensible ranges, observed indicators, and validation priorities |
| `blocked` | Authorization, safety, evidence conflict, control failure, or missing critical scope prevents a defensible output | Do not publish scores or implementation recommendations |
| `internal_only` | Analysis is incomplete, under review, or not approved for client release | Restrict to internal quality control and DecisionLedger use |

`internal_only` is a distribution state, not a maturity or confidence value.

## 4. Publication eligibility and threshold precedence

Publication gates apply in this order:

1. Block integrity, authorization, policy, control-boundary, methodology, weight, duplicate, and traceability failures.
2. Determine whether the result is category-level or Operator-level.
3. Apply the correct coverage and confidence thresholds for that level.
4. Apply material-unknown, evidence-conflict, major-category, tier-range, and language overrides.
5. Complete quality control.
6. Record a separate publication decision and approver.

A stronger numeric threshold cannot override a blocking gate or material uncertainty.

### Category result

| Condition | Publication state |
|---|---|
| Coverage 80–100%, applicable confidence gates pass, and no material blocker exists | official may be considered |
| Coverage 60–79.99%, or a bounded confidence limitation requires qualification | provisional |
| Coverage below 60%, confidence is insufficient, or a material unknown prevents a precise value | range_only |
| Evidence, authorization, mapping, policy, or control-boundary integrity fails | blocked |

A category with coverage above 80% may still be range_only or blocked when a high-materiality unknown, unresolved conflict, G4 boundary, or broad range invalidates point precision.

### Operator Score

Official Operator Score publication requires all of the following:

- active category weights total 100%
- weighted evidence coverage is at least 80%
- Operator confidence index is at least 0.65
- no category weighted at 10% or more has coverage below 60%
- no high-materiality unknown invalidates the point estimate
- no unresolved G4 scoring boundary exists
- duplicate, category-mapping, methodology-version, and weight checks pass
- quality-control state is ALLOW
- a named publication approver records the release decision

Provisional Operator treatment may be used when no blocking failure exists and:

- weighted evidence coverage is 65–79.99%, or
- Operator confidence is at least 0.50 but below 0.65, or
- coverage and confidence clear official thresholds but a bounded, disclosed limitation prevents official treatment

The provisional point must be labeled, accompanied by its defensible range, and never presented as the official Operator Score.

Use range_only when:

- weighted evidence coverage is below 65%
- Operator confidence is below 0.50
- major categories remain unresolved
- material unknowns or conflicts could change the interpretation
- the range crosses multiple maturity tiers
- internal systems required for interpretation remain unavailable

Use blocked when:

- required authorization or approval is absent
- evidence integrity is materially uncertain
- scoring methodology or weight version is unresolved
- duplicate or category ownership cannot be reconciled
- a governance gate requires HALT
- privacy, safety, policy, access, or G4 control boundaries invalidate release
- required DecisionLedger traceability is missing

### Deliverable-level release

A report, finding set, roadmap, or recommendation set may be released only when every included component is permitted by its own publication state, limitations are carried forward, version and evidence snapshot are recorded, quality control is complete, and a separate publication approval exists.

Publication approval does not authorize implementation.

## 5. Coverage and score display

Every published numeric result must include:

```yaml
result_level: category|operator|finding_set|roadmap|report
score_type: official|provisional_point_with_range|observed_indicator|range|null
observed_indicator: 0-100|null
published_score: 0-100|null
score_range: [0-100, 0-100]|null
coverage_percent: 0-100
confidence_index: 0-1|null
publication_state: official|provisional|range_only|blocked|internal_only
confidence_summary: ""
material_unknowns: []
blocked_conditions: []
limitations: []
```

Rules:

- Unknown and blocked criteria remain inside applicable weight.
- Approved `not_applicable` criteria are removed before weight recalculation.
- Unknown is never converted to zero.
- Coverage must be computed from scored applicable weight divided by total applicable weight.
- Rounding must follow the approved calculator specification.
- Internal confidence-adjusted indicators may not replace the official maturity score.
- score_type official requires publication_state official and a non-null published_score.
- score_type provisional_point_with_range requires publication_state provisional, a labeled observed_indicator, and a non-null score_range.
- score_type observed_indicator is internal or explicitly non-official and cannot be represented as an official score.
- score_type range requires publication_state range_only or blocked and a non-null score_range when defensible.
- A blocked or internal-only result may retain calculations for audit while publishing no client-facing point value.

## 6. Findings and recommendations

A published finding must contain:

- finding ID
- criterion or category owner
- observation
- evidence references
- interpretation
- business impact stated without unsupported quantification
- confidence
- priority
- limitations
- DecisionLedger reference

A published recommendation must additionally contain:

- primary package
- dependent packages, if any
- prerequisite conditions
- roadmap phase
- validation required
- implementation authorization state

Prohibited:

- creating a recommendation directly from an unknown criterion
- package routing based only on a low category score
- using publication approval as implementation approval
- implying guaranteed business outcomes

## 7. Executive-safe language

Use bounded language such as:

- `verified across the reviewed scope`
- `supported by the available evidence`
- `not visible on tested public surfaces`
- `partially confirmed`
- `requires internal validation`
- `the available evidence supports a provisional interpretation`
- `the current evidence supports a range rather than a single official score`

Avoid:

- `definitely`, `always`, or `never` without complete proof
- `the business is losing leads` without direct evidence
- quantified revenue or ROI claims without validated data and approved methodology
- competitor performance claims derived from public appearance alone
- statements that convert missing access into operational failure

## 8. Versioning and supersession

Every client-facing release must include:

```yaml
report_id: OI-REPORT-YYYY-NNN
report_version: ""
assessment_date: YYYY-MM-DD
publication_date: YYYY-MM-DD
publication_state: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
reviewed_by: ""
supersedes_report_id: null
ledger_ref: OI-DL-YYYY-NNN
```

A revised report must not silently overwrite a prior released version. Material changes to score, confidence, findings, packages, roadmap phase, or publication state require a new version and DecisionLedger entry.

## 9. DecisionLedger requirements

Every publication decision must retain:

```yaml
publication_decision_id: OI-PUB-YYYY-NNN
result_level: category|operator|finding_set|roadmap|report
publication_state: official|provisional|range_only|blocked|internal_only
score_type: official|provisional_point_with_range|observed_indicator|range|null
observed_indicator: null
published_score: null
score_range: null
coverage_percent: 0-100
confidence_index: null
confidence_summary: ""
material_unknowns: []
blocked_conditions: []
reported_finding_ids: []
reported_package_ids: []
evidence_snapshot_date: YYYY-MM-DD
report_version: ""
duplicate_check_passed: false
language_review_passed: false
quality_control_ref: OI-QC-YYYY-NNN
implementation_authorized: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
publication_approver: ""
publication_date: YYYY-MM-DD|null
ledger_ref: OI-DL-YYYY-NNN
```

`implementation_authorized` defaults to `false` and requires a separate governed decision.

## 10. Validation rules

### Blocking errors

- `PUB-EVID-001`: published result lacks admissible evidence references
- `PUB-COVER-001`: publication state conflicts with the applicable category or Operator threshold
- `PUB-LEVEL-001`: result level is missing, so the correct threshold cannot be selected
- `PUB-SCORETYPE-001`: score type conflicts with publication state or permitted display form
- `PUB-CONF-001`: material confidence limitation is omitted or misrepresented
- `PUB-UNKNOWN-001`: unknown or blocked condition is hidden, dropped, or scored as zero
- `PUB-LEDGER-001`: material published output lacks DecisionLedger traceability
- `PUB-ROUTE-001`: recommendation lacks valid finding, package, prerequisite, or roadmap routing
- `PUB-LANGUAGE-001`: client language contains unsupported certainty or business-impact claims
- `PUB-VERSION-001`: released report lacks version or supersession controls
- `PUB-AUTH-001`: publication is treated as implementation authorization

### Warnings

- `PUB-SAMPLE-001`: reported interpretation depends on a narrow sample
- `PUB-STALE-001`: evidence recency may not support current-state language
- `PUB-RANGE-001`: observed indicator may be mistaken for an official score
- `PUB-PROV-001`: provisional limitations are not prominent in the executive summary
- `PUB-DUP-001`: one condition may be represented across multiple domains without clear ownership

## 11. Worked and regression examples

### Official Operator Score

~~~yaml
result_level: operator
score_type: official
observed_indicator: 54
published_score: 54
score_range: [51, 57]
coverage_percent: 100
confidence_index: 0.88
publication_state: official
confidence_summary: "Required scope and official Operator gates pass."
material_unknowns: []
review_state: ALLOW
implementation_authorized: false
~~~

### Provisional point with range

~~~yaml
result_level: category
score_type: provisional_point_with_range
observed_indicator: 61
published_score: null
score_range: [52, 69]
coverage_percent: 84
confidence_index: 0.70
publication_state: provisional
confidence_summary: "One bounded internal workflow limitation prevents official treatment."
material_unknowns:
  - "Missed-call recovery configuration was not directly inspected."
review_state: REVIEW
implementation_authorized: false
~~~

High coverage and confidence do not force official status when a material but bounded limitation remains.

### Range only

~~~yaml
result_level: category
score_type: range
observed_indicator: 56.25
published_score: null
score_range: [41.25, 68.75]
coverage_percent: 80
confidence_index: 0.9063
publication_state: range_only
confidence_summary: "Material unresolved criteria prevent a defensible point publication."
material_unknowns:
  - OI-COMP-006
  - OI-COMP-008
review_state: REVIEW
implementation_authorized: false
~~~

This matches scoring/examples/competitive-worked-example.md and demonstrates that threshold clearance cannot override material uncertainty.

### Blocked

~~~yaml
result_level: report
score_type: null
observed_indicator: null
published_score: null
score_range: null
coverage_percent: 41
confidence_index: null
publication_state: blocked
blocked_conditions:
  - "Required authorization for workflow testing was not provided."
review_state: HALT
implementation_authorized: false
~~~

### Canonical fixture checks

- scoring/examples/seo-worked-example.md must remain provisional_point_with_range with publication_state provisional.
- scoring/examples/website-worked-example.md must remain range with publication_state range_only because a material unknown overrides its high coverage.
- scoring/examples/competitive-worked-example.md must remain range with publication_state range_only.
- Every fixture must keep implementation_authorized false unless a separate implementation decision exists.

## 12. Publication checklist

Before release, confirm:

- required scope and evidence gates pass
- result level is identified and the correct threshold set is applied
- coverage and confidence are calculated correctly
- score type matches publication state and display permissions
- unknown, blocked, and not-applicable states are handled correctly
- confidence is separate from maturity
- material conflicts and limitations are disclosed
- findings trace to evidence and DecisionLedger records
- recommendations trace to approved packages and roadmap phases
- duplicate-signal ownership is clear
- executive-safe language review passes
- report version and evidence snapshot are recorded
- implementation authorization remains separate
- quality-control state and separate publication approval are recorded
- final review state matches the publication decision

## 13. Cross references

- scoring/calculator-spec.md
- scoring/confidence-adjusted-scoring.md
- scoring/unknown-data-handling.md
- scoring/score-objects.md
- scoring/examples/seo-worked-example.md
- scoring/examples/website-worked-example.md
- scoring/examples/competitive-worked-example.md
- framework/governance-gate-index.md
- standards/evidence-standard.md
- standards/confidence-standard.md
- standards/decision-ledger-standard.md
- standards/quality-control-standard.md

## 14. v1.0 connection

This standard establishes one controlled release model for Operator Intelligence deliverables. It prevents incomplete assessments from being represented as definitive, preserves traceability from evidence to client output, and makes commercial reporting repeatable, reviewable, and safe for v1.0 delivery.