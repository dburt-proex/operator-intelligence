# Operator Intelligence DecisionLedger Record Template

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed commercial v1.0 working template

## 1. Purpose

Use this template for every material decision affecting evidence, scoring, confidence, unknown handling, findings, recommendations, package routing, roadmap state, quality control, publication, implementation authorization, completion, monitoring, renewal, closure, exception, halt, or supersession.

The record captures decision state and traceability. It does not replace source evidence, calculations, review, client authority, or implementation authorization.

## 2. Canonical record

```yaml
ledger_id: OI-DL-YYYY-NNN
assessment_id: ""
engagement_id: ""
score_run_id: null
methodology_version: ""
record_version: "1.0"
prior_ledger_ref: null
supersedes: null

decision_type: evidence|scoring|confidence|unknown_handling|finding|risk_impact|opportunity|recommendation|package_routing|roadmap|quality_control|publication|implementation_authorization|completion|monitoring|renewal|closure|exception|approval|halt|supersession
subject_type: ""
subject_id: ""
decision: ""
rationale: ""

fact_summary: ""
interpretation: ""
assumptions: []
limitations: []
unknowns: []
blocked_conditions: []

evidence_refs: []
criterion_refs: []
category_refs: []
finding_refs: []
recommendation_refs: []
routing_refs: []
roadmap_refs: []
qc_refs: []
publication_refs: []
authorization_refs: []

confidence: high|medium|low|unknown
impact_score: null
evidence_strength_score: null
effort_inverse: null
strategic_fit_score: null
priority_score: null

package_eligibility: eligible|validation_required|blocked|not_applicable|null
primary_package_id: null
dependent_package_ids: []
roadmap_phase: 0|1|2|3|4|5|null
publication_state: internal_only|official|provisional|range_only|blocked|null
implementation_authorized: false
implementation_authorization_ref: null

control_gate: ALLOW|REVIEW|HALT
status: draft|review_required|approved|rejected|blocked|authorized|in_progress|complete|monitoring|cancelled|superseded|closed
validation_required: []
acceptance_criteria: []
completion_evidence_refs: []
realized_value_evidence_refs: []

owner: ""
decision_authority: ""
decided_by: ""
reviewed_by: null
approved_by: null
decided_at: "YYYY-MM-DDThh:mm:ssZ"
reviewed_at: null
approved_at: null

client_safe_summary: ""
change_reason: null
integrity_ref: null
```

## 3. Decision construction

### Fact summary

[State only what was directly observed, tested, or supplied.]

### Interpretation

[State what the evidence supports, including scope and limits.]

### Decision and rationale

[Record the bounded decision, why it is justified, and what it does not authorize.]

### Assumptions, limitations, unknowns, and blockers

- Assumptions:
- Limitations:
- Unknowns:
- Blocked conditions:

## 4. Decision-class requirements

| Decision class | Required additions |
|---|---|
| Evidence | admission state, scope, limitations, reviewer |
| Scoring | score-run, criterion/category refs, coverage, confidence, publication effect |
| Finding | observation, interpretation, impact, confidence, report-use state |
| Recommendation | finding refs, canonical priority inputs, status, action |
| Package routing | eligibility, routing ref, one primary package only when eligible, dependencies |
| Roadmap | phase, dependencies, owner, acceptance criteria, authorization separation |
| Quality control | QC ref, checks, errors/warnings, reviewer, gate |
| Publication | artifact/version, state, evidence snapshot, QC ref, approver |
| Implementation authorization | authorized scope, owner, authority, prerequisites, rollback/escalation |
| Completion | acceptance criteria, completion evidence, unresolved defects |
| Monitoring/renewal | realized-value evidence, review window, next decision, renewal/closure authority |

## 5. Control rules

- Unknown and blocked are never score `0`.
- Confidence never modifies maturity or priority.
- Package eligibility precedes assignment.
- Phase 0 is validation, not implementation.
- QC `ALLOW`, publication approval, roadmap approval, proposal acceptance, and implementation authorization are separate.
- Work enters `in_progress` only with a resolvable authorization reference.
- Completion evidence and realized-value evidence are separate.
- Approved or published records are superseded, never silently overwritten.
- Unsupported outcome claims are prohibited.

## 6. Pre-approval validation

- [ ] ID, subject, decision type, owner, authority, and timestamp are present.
- [ ] Upstream references resolve.
- [ ] Fact, interpretation, assumptions, and limitations are separated.
- [ ] Confidence matches evidence and does not alter performance.
- [ ] Unknown and blocked states are preserved.
- [ ] Canonical priority inputs are present where applicable.
- [ ] Package eligibility and primary ownership are valid.
- [ ] Phase 0 and roadmap dependencies are valid.
- [ ] Publication and implementation authorization remain separate.
- [ ] QC and approval requirements are satisfied.
- [ ] Completion and realized value remain separate.
- [ ] Supersession preserves prior history.
- [ ] Client-safe summary is bounded and supportable.

## 7. Release decision

```yaml
quality_control_result: ALLOW|REVIEW|HALT
release_blockers: []
warning_dispositions: []
final_status: draft|review_required|approved|rejected|blocked|authorized|in_progress|complete|monitoring|cancelled|superseded|closed
```

Any failed blocking check requires `HALT` until a superseding record resolves the condition.

## 8. Commercial v1.0 connection

This template operationalizes the canonical DecisionLedger schema so assessments, reports, proposals, implementation decisions, and renewals remain auditable and reproducible.

## 9. References

- `standards/decision-ledger-standard.md`
- `standards/evidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/quality-control-standard.md`