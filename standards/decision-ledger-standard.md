# Operator Intelligence DecisionLedger Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Reconciled commercial v1.0 control standard; pending folder approval

## 1. Purpose

This standard defines the minimum record, control, and traceability requirements for every material Operator Intelligence decision.

The DecisionLedger preserves how admissible evidence became a criterion state, category score, Operator Score, finding, recommendation, package route, roadmap action, publication decision, implementation authorization, completion decision, or controlled halt.

The ledger is an immutable decision record. It does not replace evidence, scoring logic, review, publication approval, implementation authorization, or client authority.

## 2. Governance principles

1. Every material state change requires a resolvable ledger event.
2. Approved or published records are never silently overwritten.
3. Evidence, confidence, performance, priority, publication, and authorization remain separate fields.
4. Unknown and blocked conditions remain visible and are never converted to score `0`.
5. A decision may not claim stronger certainty than its supporting evidence chain.
6. Package eligibility is distinct from package assignment.
7. Roadmap approval is distinct from implementation authorization.
8. Quality-control `ALLOW` is distinct from publication approval.
9. Completion evidence is distinct from realized-value evidence.
10. Material changes create a superseding record and preserve prior history.

## 3. Scope

A DecisionLedger event is required when a material decision affects:

- assessment scope, applicability, or access state
- evidence admission, limitation, rejection, or supersession
- criterion score, category score, coverage, confidence, or publication state
- unknown, blocked, or not-applicable treatment
- finding creation, revision, suppression, validation, or closure
- risk, impact, opportunity, effort, or priority classification
- recommendation class, priority, status, or scope
- package eligibility, primary package assignment, dependency route, or rejection
- roadmap admission, phase, sequence, block, approval, start, completion, monitoring, renewal, or closure
- report or score publication
- implementation authorization, exception, escalation, or halt
- quality-control decision
- supersession of a prior decision

Routine working notes that do not alter governed state may remain outside the ledger.

## 4. Identifier and immutability rules

DecisionLedger IDs use:

```text
OI-DL-YYYY-NNN
```

Rules:

- `ledger_id` is immutable.
- Each event records one primary governed subject.
- Published, approved, authorized, completed, rejected, or halted records may not be edited in place.
- Corrections create a new record with `supersedes` and `prior_ledger_ref`.
- The superseded record remains retained and resolvable.
- Legal or contractual removal requires a controlled removal event that preserves the reason, authority, and affected references.

## 5. Canonical record

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

Required fields may not be replaced by narrative implication. Fields that are structurally inapplicable may be `null`; unresolved material fields must be represented as unknown, blocked, or validation required.

## 6. Controlled vocabularies

### 6.1 Control gate

| Gate | Use |
|---|---|
| `ALLOW` | Evidence, authority, dependencies, and applicable standards support the bounded decision. |
| `REVIEW` | Qualified judgment is required to resolve a material limitation, conflict, unknown, dependency, exception, or publication effect. |
| `HALT` | Proceeding would violate an evidence, authority, safety, privacy, scope, publication, dependency, or governance boundary. |

A gate records control state. It does not substitute for publication state, package eligibility, roadmap state, implementation authorization, or completion.

### 6.2 Status

- `draft`
- `review_required`
- `approved`
- `rejected`
- `blocked`
- `authorized`
- `in_progress`
- `complete`
- `monitoring`
- `cancelled`
- `superseded`
- `closed`

### 6.3 Publication state

- `internal_only`
- `official`
- `provisional`
- `range_only`
- `blocked`

### 6.4 Package eligibility

- `eligible`
- `validation_required`
- `blocked`
- `not_applicable`

## 7. Minimum required fields by decision class

| Decision class | Additional required fields |
|---|---|
| Evidence | evidence refs, admission state, scope, limitations, reviewer |
| Scoring | score-run ref, criterion/category refs, evidence refs, confidence, unknown treatment, methodology version |
| Finding | finding ref, observation/fact summary, interpretation, impact, confidence, limitations |
| Recommendation | recommendation ref, finding refs, impact, evidence strength, effort inverse, strategic fit, priority, status |
| Package routing | routing ref, package eligibility, one primary package only when eligible, dependencies, exclusions |
| Roadmap | roadmap ref, phase, sequence/dependencies, package eligibility, owner, acceptance criteria |
| Quality control | QC ref, checks, errors/warnings, reviewer, gate |
| Publication | publication state, artifact/version, evidence snapshot, QC ref, approver |
| Implementation authorization | authorized scope, package or validation scope, owner, authority, prerequisites, rollback/escalation |
| Completion | acceptance criteria, completion evidence, unresolved defects, owner acceptance |
| Monitoring/renewal | realized-value evidence, measurement window, next decision, renewal or closure authority |

## 8. Traceability chain

The canonical chain is:

```text
Evidence
→ Criterion evaluation
→ Category and Operator Score
→ Governed finding
→ Risk / impact / opportunity interpretation
→ Recommendation
→ Package eligibility and route
→ Phase 0 validation or roadmap phase
→ Quality-control decision
→ Publication decision
→ Separate implementation authorization
→ Completion evidence
→ Monitoring / realized-value evidence
→ Renewal or closure
→ DecisionLedger events
```

A record may reference only the portion relevant to its subject, but every upstream material reference must remain resolvable.

## 9. Evidence and confidence controls

1. Ledger records reference evidence objects; they do not replace them.
2. Evidence must pass `standards/evidence-standard.md` before supporting a governed decision.
3. Confidence follows `standards/confidence-standard.md` and never modifies maturity.
4. Public absence may support “not publicly visible within the reviewed scope,” not internal nonexistence.
5. Missing access is `unknown` or `blocked`, not negative evidence.
6. Conflicting evidence routes to `REVIEW` until resolved or explicitly accepted with limitations.
7. Class D or inferred evidence normally routes to validation and cannot independently justify a negative score or implementation route.
8. Evidence limitation changes confidence, uncertainty, assertion strength, and publication treatment as applicable.

## 10. Scoring and finding controls

- Score changes require the prior score reference, method version, reason, and evidence.
- Criterion, category, and Operator Score decisions must preserve applicability, coverage, bounds, and publication state.
- Unknown and blocked criteria remain in applicable-weight coverage unless formally not applicable.
- Duplicate signals identify one weighted owner and any reference-only uses.
- Findings require observation, evidence, interpretation, business impact, confidence, limitations, and report-use state.
- Suppressed or closed findings remain traceable with the reason and authority.

## 11. Recommendation and package controls

- Recommendations require observation, evidence, interpretation, impact, confidence, priority, package eligibility, roadmap phase or validation state, and action.
- Priority inputs must resolve to `framework/risk-impact-model.md`, `framework/effort-model.md`, and `framework/opportunity-model.md`.
- Confidence remains a separate gate and does not modify priority.
- Exactly one primary package is required only when `package_eligibility: eligible`.
- Validation requirements may remain unrouted in Phase 0.
- Dependent packages do not create duplicate primary ownership.
- Package-first selling, unsupported scope expansion, and unsupported ROI are prohibited.
- Material routing changes require a superseding ledger event.

## 12. Roadmap and implementation controls

- Roadmap phase follows `standards/roadmap-standard.md`.
- Phase 0 represents validation and access, not implementation.
- Dependencies cannot be bypassed by priority alone.
- Roadmap approval and publication do not authorize implementation.
- Work may enter `in_progress` only when `implementation_authorized: true` and the authorization reference resolves.
- AI work cannot advance without workflow, data, privacy, human review, escalation, logging, QA, and failure controls.
- Completion requires acceptance evidence; deliverable existence alone is insufficient.

## 13. Publication and quality-control controls

- Quality control follows `standards/quality-control-standard.md`.
- Publication follows `standards/publication-standard.md`.
- QC `ALLOW` permits advancement to a separate publication decision only.
- Published scores disclose coverage, confidence, uncertainty or bounds, limitations, and methodology version.
- `provisional` and `range_only` remain explicit.
- Unsupported revenue, lead-loss, conversion, ranking, savings, ROI, market-share, competitor-performance, or timeline certainty is prohibited.

## 14. Supersession and change control

A superseding event must:

1. reference the prior ledger record
2. identify the governed subject and prior state
3. state what changed and why
4. identify new, corrected, expired, or withdrawn evidence
5. preserve the prior record as `superseded`
6. record new review, approval, publication, and authorization effects
7. update dependent score, finding, recommendation, routing, roadmap, report, or implementation references
8. retain a client-safe summary when the change affects a published artifact

Silent resequencing, silent scope expansion, silent score correction, and silent publication-state changes are prohibited.

## 15. Executive-safe language

The `client_safe_summary` must:

- distinguish observation from interpretation
- state reviewed scope and material limitations
- avoid certainty beyond evidence
- avoid implying package eligibility, publication, or implementation authorization that has not been granted
- avoid unsupported financial, competitive, ranking, conversion, or timeline claims
- translate weaknesses into bounded business impact and a controlled next step

## 16. Validation codes

| Code | Condition | Severity |
|---|---|---|
| `DL-TRACE-001` | Material decision lacks resolvable upstream references. | error |
| `DL-EVID-001` | Decision lacks admissible evidence or a governed evidence limitation. | error |
| `DL-CONF-001` | Confidence exceeds supporting evidence or modifies performance. | error |
| `DL-UNKNOWN-001` | Unknown or blocked state is hidden, dropped, or converted to failure. | error |
| `DL-OWNER-001` | Owner, decision authority, or timestamp is missing. | error |
| `DL-APPROVAL-001` | Controlled decision lacks required review or approval. | error |
| `DL-PRIORITY-001` | Recommendation priority inputs are missing or use noncanonical authorities. | error |
| `DL-ROUTE-001` | Package eligibility is missing or primary-package ownership is invalid. | error |
| `DL-PHASE0-001` | Phase 0 validation is represented as authorized implementation. | error |
| `DL-IMPL-001` | Work starts without separate implementation authorization. | error |
| `DL-DEPEND-001` | Roadmap or implementation dependency is bypassed. | error |
| `DL-QC-001` | Client-facing artifact lacks a required QC decision. | error |
| `DL-PUB-001` | Publication state conflicts with publication rules or QC state. | error |
| `DL-SUPER-001` | Material change overwrites history without supersession. | error |
| `DL-LANG-001` | Client-safe summary contains unsupported certainty or outcome claims. | error |
| `DL-DUP-001` | Weighted-signal or implementation ownership is duplicated. | warning |
| `DL-INTEGRITY-001` | Integrity reference is required but missing or invalid. | warning/error by scope |

Unresolved errors route the affected decision to `HALT`. Warnings require disposition and may route to `REVIEW`.

## 17. Release checklist

Before a ledger-controlled decision advances:

- [ ] governed subject and decision type are valid
- [ ] upstream evidence and object references resolve
- [ ] fact, interpretation, assumption, and limitation are separated
- [ ] confidence is evidence-derived and separate from performance
- [ ] unknown and blocked states are preserved
- [ ] control gate is justified
- [ ] priority inputs use canonical authorities when applicable
- [ ] package eligibility and primary ownership are valid
- [ ] Phase 0 and roadmap dependencies are enforced
- [ ] implementation authorization is separate and resolvable
- [ ] QC and publication effects are valid
- [ ] owner, reviewer, approver, and authority are recorded where required
- [ ] methodology and record versions are recorded
- [ ] client-safe summary is bounded and supportable
- [ ] material changes supersede rather than overwrite
- [ ] completion and realized-value evidence remain distinct

## 18. Usage instructions

1. Create a ledger event when a material governed state changes.
2. Reference source objects instead of duplicating them.
3. Apply the narrowest valid decision type and subject.
4. Run the validation codes before approval or publication.
5. Create superseding events for corrections or material changes.
6. Store the ledger event with the assessment release record.

## 19. Commercial v1.0 connection

This standard makes assessment decisions auditable across scoring, findings, recommendations, package routing, roadmaps, reports, implementation, and renewal. It is required for evaluator consistency, client defensibility, quality control, and controlled commercial delivery.

## 20. Cross references

- `framework/governance-gate-index.md`
- `framework/risk-impact-model.md`
- `framework/effort-model.md`
- `framework/opportunity-model.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/quality-control-standard.md`
- `scoring/score-objects.md`
- `templates/decision-ledger.md`