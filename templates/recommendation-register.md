# Recommendation Register

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed commercial v1.0 working template

## 1. Purpose

Use this register to convert governed findings into controlled recommendations that remain traceable through priority, package eligibility, package routing, roadmap placement, publication, implementation authorization, acceptance, and DecisionLedger review.

A recommendation may advance only when its evidence-to-action chain is complete and its scope does not exceed the verified condition.

## 2. Register controls

| Field | Value |
|---|---|
| Assessment ID | |
| Client | |
| Register version | |
| Methodology version | |
| Evidence snapshot date | |
| Publication state | `internal_only` / `provisional` / `range_only` / `official` / `blocked` |
| Register owner | |
| Reviewer | |
| QC reference | |
| DecisionLedger register ref | |

## 3. Controlled values

- **Class:** `implementation`, `validation`, `monitoring`, `defer`, `halt`
- **Status:** `proposed`, `validation_required`, `accepted`, `deferred`, `blocked`, `authorized`, `in_progress`, `complete`, `monitoring`, `rejected`, `cancelled`, `superseded`
- **Confidence:** `high`, `medium`, `low`, `unknown`
- **Package eligibility:** `eligible`, `validation_required`, `blocked`, `not_applicable`
- **Roadmap phase:** `0`, `1`, `2`, `3`, `4`, `5`
- **Review state:** `ALLOW`, `REVIEW`, `HALT`

## 4. Recommendation register

| Recommendation ID | Class | Finding refs | Evidence refs | Action | Confidence | Impact | Evidence strength | Effort inverse | Strategic fit | Priority | Package eligibility | Primary package | Phase | Owner | Status | Review state | Ledger ref |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|---|---|---|
| OI-REC-YYYY-NNN | | | | | | | | | | | | | | | | | |

## 5. Recommendation record

### 5.1 Identity and source chain

```yaml
recommendation_id: OI-REC-YYYY-NNN
recommendation_version: "1.0"
supersedes: null
assessment_id: ""
recommendation_class: implementation|validation|monitoring|defer|halt
status: proposed|validation_required|accepted|deferred|blocked|authorized|in_progress|complete|monitoring|rejected|cancelled|superseded
finding_refs: []
evidence_refs: []
criterion_refs: []
category_refs: []
ledger_refs: []
```

### 5.2 Decision basis

**Observation**  
[State only what was directly observed or supplied.]

**Interpretation**  
[State what the evidence supports and its limits.]

**Business impact**  
[Describe the supported operational, buyer-path, trust, visibility, measurement, or governance effect.]

```yaml
confidence: high|medium|low|unknown
confidence_basis: ""
assumptions: []
limitations: []
unknowns: []
blocked_conditions: []
```

### 5.3 Priority inputs

```yaml
impact_score: 1-5
evidence_strength_score: 1-5
effort_inverse: 1-5
strategic_fit_score: 1-5
priority_score: 0-100
priority_band: critical|high|medium|low
priority_formula_ref: standards/recommendation-standard.md
```

Rules:

- Import `impact_score` and `evidence_strength_score` from `framework/risk-impact-model.md`.
- Import `effort_inverse` from `framework/effort-model.md`.
- Import or reproduce `strategic_fit_score` under `framework/opportunity-model.md`.
- Confidence is a separate gate and does not modify priority.
- Priority does not bypass evidence, authority, package, dependency, or roadmap gates.

### 5.4 Recommended action

**Recommendation statement**  
[Specific, bounded, implementation-ready or validation-ready action.]

**Included scope**

- 

**Excluded scope**

- 

**Acceptance criteria**

1. 
2. 

**Required acceptance evidence**

- 

### 5.5 Package eligibility and routing

```yaml
package_eligibility: eligible|validation_required|blocked|not_applicable
primary_package_id: null
prerequisite_package_ids: []
dependent_package_ids: []
reference_only_package_ids: []
routing_reason: ""
routing_ref: null
```

Rules:

- Assign exactly one primary package only when `package_eligibility: eligible`.
- Validation recommendations may remain unrouted in Phase 0.
- Route by verified root condition, not commercial preference.
- Secondary relationships cannot duplicate ownership, deliverables, or billing.
- When no canonical package fits, record a methodology gap rather than inventing a package.

### 5.6 Roadmap placement

```yaml
roadmap_phase: 0|1|2|3|4|5
phase_eligibility: validation_required|eligible|blocked|complete
roadmap_item_ref: null
sequence_rank: null
prerequisites: []
dependencies: []
owner: ""
decision_authority: ""
target_window: ""
```

- Phase 0 is validation and access, not implementation.
- Phase 4 requires workflow, data, privacy, human review, escalation, logging, QA, and failure controls.
- Phase 5 requires measured implementation/adoption evidence and a renewal, optimization, maintenance, or closure decision.

### 5.7 Publication and authorization

```yaml
publication_state: internal_only|provisional|range_only|official|blocked
qc_ref: null
implementation_authorized: false
implementation_authorization_ref: null
review_state: ALLOW|REVIEW|HALT
review_reason: ""
reviewed_by: ""
reviewed_at: ""
approved_by: null
approved_at: null
```

Publication, roadmap approval, and proposal acceptance do not authorize implementation. Work may enter `in_progress` only when the separate authorization reference resolves.

### 5.8 Completion and measurement

```yaml
completion_state: not_started|in_progress|complete|accepted|rejected|cancelled
completion_evidence_refs: []
realized_value_evidence_refs: []
measurement_plan: []
```

Implementation completion confirms acceptance criteria. It does not prove traffic, ranking, lead, conversion, savings, revenue, ROI, or other business outcomes.

### 5.9 Change control

| Change date | Prior version | Material change | Reason | Evidence/finding effect | Routing/phase effect | Ledger ref | Reviewer |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Material changes require versioning, supersession, and dependent-record review.

## 6. Release validation

- [ ] Source findings and evidence refs resolve.
- [ ] Observation, interpretation, impact, assumptions, and limitations are separated.
- [ ] Confidence matches the weakest material evidence dependency.
- [ ] Priority inputs use canonical authorities and reproduce.
- [ ] Unknown confidence routes to validation, monitoring, defer, or halt rather than implementation.
- [ ] Scope is proportional to the verified condition.
- [ ] Package eligibility is explicit.
- [ ] Exactly one primary package exists only for eligible work.
- [ ] Phase 0, phases 1–5, prerequisites, and dependencies are valid.
- [ ] Acceptance criteria and evidence are observable.
- [ ] QC, publication, roadmap approval, and implementation authorization remain separate.
- [ ] Completion evidence and realized-value evidence remain separate.
- [ ] DecisionLedger traceability is complete.
- [ ] Client language avoids unsupported outcome certainty.

Any failed evidence, priority, routing, authority, traceability, or unresolved `HALT` check requires `HALT`.

## 7. Commercial v1.0 connection

This register is the operational bridge from findings to governed delivery decisions. It supports repeatable report generation, package routing, roadmap construction, proposal scope, implementation control, and quality review.

## 8. Canonical references

- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
- `framework/recommendation-index.md`
- `scoring/recommendation-map.md`
- `templates/finding-register.md`
- `templates/evidence-register.md`
- `templates/roadmap.md`
- `templates/decision-ledger.md`