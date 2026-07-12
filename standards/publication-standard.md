# Publication Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

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

## 4. Publication eligibility

### Official

`official` requires all of the following:

- required evaluation scope is complete
- weighted evidence coverage is at least 80%
- no material category falls below its category-specific publication threshold
- no unresolved high-materiality unknown or blocked condition could materially change the interpretation
- no unresolved evidence conflict affects a reported score or finding
- all reported findings have valid evidence references and DecisionLedger records
- recommendations route to approved packages and roadmap phases
- duplicate-signal checks pass
- executive-safe language review passes
- reviewer state is `ALLOW`

Meeting the numeric coverage threshold alone does not guarantee `official` publication.

### Provisional

`provisional` may be used when:

- weighted evidence coverage is 60%–79.99%, or
- coverage is at least 80% but a bounded confidence or validation limitation remains, and
- the limitation does not prevent a useful, non-misleading interpretation, and
- all material limitations are disclosed, and
- reviewer state is `ALLOW` or documented `REVIEW`

### Range only

Use `range_only` when:

- weighted evidence coverage is below 60%, or
- a material unknown could change the Operator Score or category interpretation, or
- several low-confidence conditions create a wide defensible interval, or
- a score can be bounded but not defended as a single official value

Do not label an observed partial-data indicator as an official Operator Score.

### Blocked

Use `blocked` when:

- required authorization is absent
- safe testing cannot be completed and the missing evidence is material
- privacy, security, or access restrictions prevent defensible review
- evidence is materially conflicting and unresolved
- a governance gate requires `HALT`
- required DecisionLedger traceability is missing for a material output

## 5. Coverage and score display

Every published numeric result must include:

```yaml
score_value: 0-100|null
score_type: official|observed_indicator|range
coverage_percent: 0-100
publication_state: official|provisional|range_only|blocked|internal_only
confidence_summary: ""
material_unknowns: []
limitations: []
```

Rules:

- Unknown and blocked criteria remain inside applicable weight.
- Approved `not_applicable` criteria are removed before weight recalculation.
- Unknown is never converted to zero.
- Coverage must be computed from scored applicable weight divided by total applicable weight.
- Rounding must follow the approved calculator specification.
- Internal confidence-adjusted indicators may not replace the official maturity score.

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
publication_state: official|provisional|range_only|blocked|internal_only
coverage_percent: 0-100
confidence_summary: ""
material_unknowns: []
blocked_conditions: []
reported_finding_ids: []
reported_package_ids: []
duplicate_check_passed: false
language_review_passed: false
implementation_authorized: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

`implementation_authorized` defaults to `false` and requires a separate governed decision.

## 10. Validation rules

### Blocking errors

- `PUB-EVID-001`: published result lacks admissible evidence references
- `PUB-COVER-001`: publication state conflicts with evidence coverage or category thresholds
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

## 11. Worked examples

### Official

```yaml
score_value: 54
score_type: official
coverage_percent: 100
publication_state: official
confidence_summary: "Required scope is complete and material findings are supported by direct evidence."
material_unknowns: []
review_state: ALLOW
```

### Provisional

```yaml
score_value: 61
score_type: official
coverage_percent: 84
publication_state: provisional
confidence_summary: "Public evidence is strong; one internal workflow remains partially validated."
material_unknowns:
  - "Missed-call recovery configuration was not directly inspected."
review_state: REVIEW
```

### Range only

```yaml
score_value: null
score_type: range
score_range: [32, 73]
coverage_percent: 58.6
publication_state: range_only
confidence_summary: "Material internal evidence remains unavailable."
material_unknowns:
  - "Lead assignment rules"
  - "Estimate follow-up records"
review_state: REVIEW
```

### Blocked

```yaml
score_value: null
score_type: range
coverage_percent: 41
publication_state: blocked
blocked_conditions:
  - "Required authorization for workflow testing was not provided."
review_state: HALT
```

## 12. Publication checklist

Before release, confirm:

- required scope and evidence gates pass
- coverage is calculated correctly
- unknown, blocked, and not-applicable states are handled correctly
- confidence is separate from maturity
- material conflicts and limitations are disclosed
- findings trace to evidence and DecisionLedger records
- recommendations trace to approved packages and roadmap phases
- duplicate-signal ownership is clear
- executive-safe language review passes
- report version and evidence snapshot are recorded
- implementation authorization remains separate
- final review state matches the publication decision

## 13. v1.0 connection

This standard establishes one controlled release model for Operator Intelligence deliverables. It prevents incomplete assessments from being represented as definitive, preserves traceability from evidence to client output, and makes commercial reporting repeatable, reviewable, and safe for v1.0 delivery.