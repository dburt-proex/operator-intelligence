# Quality Control Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Reconciled commercial v1.0 control standard; pending folder approval

## 1. Purpose

This standard defines the minimum quality-control process required before an Operator Intelligence score, finding set, recommendation set, roadmap, report, proposal, implementation package, or completion record may advance to its next governed state.

Quality control verifies that outputs are reproducible, evidence-grounded, internally consistent, traceable through the DecisionLedger, and safe for executive use. It does not replace evidence collection, scoring, package eligibility, roadmap approval, publication approval, implementation authorization, client acceptance, or realized-value validation.

## 2. Governance principles

1. Every client-facing assessment release requires a documented quality-control record.
2. Quality control follows the source chain in order; downstream polish cannot cure an upstream evidence or scoring failure.
3. Unknown, blocked, and not-applicable states remain distinct. Unknown is never zero.
4. Confidence remains separate from maturity and priority.
5. Every material output must trace to admissible evidence and a DecisionLedger event.
6. Exactly one primary package is required only for package-eligible recommendations.
7. Phase 0 validation may remain unrouted and cannot authorize implementation.
8. QC `ALLOW`, publication approval, roadmap approval, implementation authorization, completion, and realized-value validation are separate decisions.
9. Unsupported ROI, revenue, conversion, ranking, savings, lead-loss, market-share, competitor-performance, or timeline certainty is prohibited.
10. A blocking failure routes the affected output to `HALT` until corrected or superseded.
11. QC records are retained with the exact artifact and evidence snapshot reviewed.

## 3. Review scope

| Review area | Required verification |
|---|---|
| Scope | Assessment boundary, applicable categories, systems, criteria, exclusions, access, and evidence windows are defined. |
| Evidence | Evidence is admissible, attributable, current enough, scoped, reviewable, and conflicts are resolved or disclosed. |
| Scoring | Approved anchors, applicability, weights, coverage, bounds, confidence handling, rounding, and publication gates reproduce. |
| Unknowns | Unknown, blocked, and not-applicable states are correctly distinguished and preserved. |
| Findings | Observation, evidence, interpretation, impact, confidence, limitation, and report-use state are complete. |
| Duplicate control | Each weighted signal and implementation responsibility has one owner. |
| Recommendations | Each recommendation traces to a finding, uses canonical priority inputs, and has proportional scope. |
| Package routing | Eligibility is explicit; one primary package exists only when eligible; dependencies and exclusions are visible. |
| Roadmap | Validation state, phase, sequence, prerequisites, owner, authority, and acceptance evidence are valid. |
| AI controls | Workflow, data, privacy, human review, escalation, logging, QA, and failure controls pass before AI implementation. |
| Publication | Publication state matches coverage, confidence, limitations, QC state, and artifact version. |
| Authorization | Roadmap and publication decisions are not treated as implementation authorization. |
| Completion | Acceptance criteria and completion evidence prove delivery; realized value remains separately measured. |
| Language | Client claims are bounded, accurate, executive-safe, and free of unsupported outcomes. |
| DecisionLedger | Material decisions, reviews, approvals, exceptions, authorizations, blocks, and supersessions resolve. |

## 4. Review sequence

Quality control runs in this order:

1. **Scope control** — confirm boundary, applicability, exclusions, access, and version.
2. **Evidence control** — verify admissibility, attribution, recency, scope, integrity, authorization, and conflicts.
3. **Scoring control** — independently recalculate criterion, category, coverage, bounds, confidence index, and Operator Score outputs.
4. **Unknown-state control** — verify missing evidence is not converted to failure or silently removed.
5. **Finding control** — verify complete evidence-to-interpretation chains and bounded business impact.
6. **Recommendation control** — verify priority inputs, confidence gate, scope, status, and acceptance logic.
7. **Routing control** — verify package eligibility, primary ownership, dependencies, exclusions, and Phase 0 handling.
8. **Roadmap control** — verify phases, sequence, owners, authority, start gates, acceptance criteria, and authorization separation.
9. **Publication control** — verify publication state, score display, limitations, artifact version, and evidence snapshot.
10. **Language control** — remove unsupported certainty, blame, and outcome claims.
11. **Ledger control** — verify every material state and exception has a resolvable event.
12. **Release decision** — issue `ALLOW`, `REVIEW`, or `HALT` for the bounded artifact and version.

A later step cannot cure an earlier failure without correction and re-running every affected downstream check.

## 5. Review outcomes

| State | Meaning | Required action |
|---|---|---|
| `ALLOW` | Blocking checks pass and warnings are resolved or accepted with rationale. | May advance to the next separate governed decision. |
| `REVIEW` | No uncontrolled blocking error remains, but qualified judgment or a bounded exception is required. | Correct, disclose, limit, or formally accept before advancement. |
| `HALT` | A blocking error, unsupported claim, authority gap, traceability break, or material control failure exists. | Do not publish, authorize, start, or complete dependent work. |

`ALLOW` applies only to the reviewed artifact, scope, version, and evidence snapshot.

## 6. Reviewer independence and authority

- The primary author performs a documented self-check.
- Official client publication requires a qualified independent reviewer when available.
- Without an independent reviewer, publication remains `provisional` unless an authorized exception is ledgered.
- The reviewer must be independent from unresolved commercial pressure to sell a package or overstate impact.
- Reviewer edits that change material meaning require a superseding source or ledger event.
- Conflicts of interest, disagreements, and exceptions must be recorded.
- The reviewer may issue QC state but cannot assume publication or implementation authority unless that role is separately assigned.

## 7. Recalculation contract

The reviewer independently verifies:

```yaml
score_run_id: OI-SCORE-YYYY-NNN
methodology_version: ""
applicable_weight_total: 100
known_weight_total: 0-100
weighted_evidence_coverage: 0-1
operator_confidence_index: 0-1
category_scores: {}
category_bounds: {}
observed_operator_score: 0-100|null
operator_lower_bound: 0-100
operator_upper_bound: 0-100
published_score_type: official|observed_indicator|range|null
publication_state: official|provisional|range_only|blocked|internal_only
validation_messages: []
```

Rules:

- Active category weights reconcile to 100%.
- Approved not-applicable criteria are removed before normalization only under the approved category rule.
- Unknown and blocked criteria remain inside applicable coverage.
- Unknown is never scored as zero.
- Confidence does not multiply maturity.
- Bounds and confidence factors follow the canonical scoring specifications.
- Rounding occurs only at the approved display stage.
- Recalculation differences must be resolved before `ALLOW`.

## 8. Finding and recommendation checks

Each published finding must pass:

- admissible evidence refs resolve
- observation is separated from interpretation
- criterion and category ownership are valid
- business impact is bounded and material
- confidence matches the evidence chain
- limitations, unknowns, and validation needs are visible
- report wording follows the finding library
- DecisionLedger reference exists

Each recommendation must additionally pass:

- valid finding linkage
- canonical impact, evidence-strength, effort-inverse, and strategic-fit inputs
- confidence remains a separate gate
- priority calculation reproduces
- package eligibility is explicit
- exactly one primary package only when eligible
- no duplicate implementation ownership
- prerequisites, dependencies, exclusions, and acceptance criteria are explicit
- Phase 0 or roadmap phase is valid
- implementation authorization remains separate

## 9. Package, roadmap, and authorization checks

Before roadmap publication:

- package eligibility and routing resolve
- validation requirements are not disguised as implementation
- Phase 0 items carry no implementation authorization
- phase and sequence respect root condition and dependencies
- owner and decision authority are named
- roadmap approval is distinct from start authorization
- AI work remains blocked until required controls pass

Before work enters `in_progress`:

- `implementation_authorized: true`
- authorization reference resolves
- authorized scope and exclusions are recorded
- prerequisites and access pass
- implementation owner accepts responsibility
- rollback, recovery, or escalation requirements are defined
- no unresolved `HALT` affects the work

## 10. Publication checks

A client-facing artifact may advance only when:

- QC scope exactly matches the artifact version
- evidence snapshot and methodology version are recorded
- publication state matches score and evidence conditions
- official publication gates pass or an allowed lower state is used
- provisional and range-only outputs remain explicit
- limitations and material unknowns are visible
- report, proposal, and roadmap do not imply unauthorized implementation
- every material claim traces to evidence or is labeled as assumption/interpretation

## 11. Executive-safe language review

Approved patterns include:

- `verified across the reviewed scope`
- `supported by the available evidence`
- `not visible on the tested public surfaces`
- `partially confirmed`
- `requires internal validation`
- `the evidence supports a provisional interpretation`
- `this creates a revenue leakage risk` when the mechanism is stated and no unsupported amount is claimed

Prohibited without validated support:

- guaranteed lead, revenue, conversion, ranking, savings, or ROI outcomes
- public absence presented as proof of internal nonexistence
- competitor-performance or market-share claims inferred from appearance alone
- definitive failure language when evidence is incomplete
- timeline certainty where access, capacity, approvals, or dependencies are unverified
- blame-oriented language

## 12. Quality-control record

```yaml
qc_id: OI-QC-YYYY-NNN
assessment_id: ""
artifact_type: score_run|finding_set|recommendation_set|roadmap|report|proposal|package|implementation_completion|renewal_record
artifact_id: ""
artifact_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
reviewed_scope: []
checks_run: []
blocking_errors: []
warnings: []
accepted_exceptions: []
recalculation_passed: false
duplicate_check_passed: false
routing_check_passed: false
authorization_separation_passed: false
language_review_passed: false
ledger_check_passed: false
review_state: ALLOW|REVIEW|HALT
publication_effect: none|official|provisional|range_only|blocked|internal_only
reviewed_by: ""
reviewed_at: "YYYY-MM-DDThh:mm:ssZ"
decision_authority: ""
ledger_ref: OI-DL-YYYY-NNN
supersedes_qc_id: null
```

Material corrections require a new QC record or a superseding review event. Reusing a QC decision against a changed artifact or evidence snapshot is prohibited.

## 13. Validation codes

### Blocking errors

| Code | Condition |
|---|---|
| `QC-SCOPE-001` | Required scope, applicability, exclusion, access, or artifact version is unresolved. |
| `QC-EVID-001` | Material output lacks admissible, attributable, or scoped evidence. |
| `QC-SCORE-001` | Score, weight, coverage, bounds, confidence, or rounding cannot be reproduced. |
| `QC-UNKNOWN-001` | Unknown or blocked data is hidden, dropped, or scored as zero. |
| `QC-DUP-001` | Weighted signal or implementation responsibility has duplicate primary ownership. |
| `QC-FIND-001` | Finding lacks a complete evidence-to-interpretation chain. |
| `QC-PRIORITY-001` | Recommendation priority uses missing or noncanonical inputs. |
| `QC-ROUTE-001` | Package eligibility, primary ownership, dependency, or phase routing is invalid. |
| `QC-PHASE0-001` | Validation work is represented as authorized implementation. |
| `QC-AI-001` | AI implementation advances without required workflow, data, privacy, review, escalation, logging, QA, or failure controls. |
| `QC-LEDGER-001` | Material decision lacks DecisionLedger traceability. |
| `QC-PUB-001` | Publication state conflicts with coverage, confidence, limitations, QC, or version state. |
| `QC-LANGUAGE-001` | Client language contains unsupported certainty, blame, or outcome claims. |
| `QC-AUTH-001` | QC, roadmap, or publication approval is treated as implementation authorization. |
| `QC-COMPLETE-001` | Work is marked complete without acceptance evidence. |

### Warnings

| Code | Condition |
|---|---|
| `QC-REVIEW-001` | No independent reviewer is available for intended official publication. |
| `QC-RECENCY-001` | Evidence remains admissible but is near its freshness limit. |
| `QC-SAMPLE-001` | Evidence sample is narrow but disclosed and non-blocking. |
| `QC-OWNER-001` | Accountable owner exists but acceptance authority is pending. |
| `QC-MEASURE-001` | Delivery acceptance exists but realized-value evidence is not yet available. |
| `QC-INTEGRITY-001` | Integrity reference is recommended but not required for the bounded artifact. |

Unresolved blocking errors require `HALT`. Warnings require disposition and may require `REVIEW`.

## 14. Release checklist

- [ ] reviewed scope, artifact ID, version, and methodology version are fixed
- [ ] applicability, access, exclusions, and evidence windows are complete
- [ ] evidence refs resolve and conflicts are resolved or disclosed
- [ ] scores, coverage, bounds, confidence, and publication gates reproduce
- [ ] unknown, blocked, and not-applicable states are correct
- [ ] findings are complete, bounded, and traceable
- [ ] duplicate ownership checks pass
- [ ] recommendation priority and status reproduce
- [ ] package eligibility and routing pass
- [ ] Phase 0, roadmap phases, dependencies, and owner controls pass
- [ ] AI prerequisites pass where applicable
- [ ] publication and implementation authorization remain separate
- [ ] executive-safe language review passes
- [ ] DecisionLedger records resolve
- [ ] reviewer state and warning/error dispositions are recorded
- [ ] QC record is stored with the released artifact version

## 15. Usage instructions

1. Freeze the artifact version and evidence snapshot.
2. Run the review sequence in order.
3. Record validation codes and dispositions.
4. Recalculate quantitative outputs independently.
5. Issue a bounded `ALLOW`, `REVIEW`, or `HALT` decision.
6. Store the QC record and ledger event with the artifact.
7. Re-run affected checks after any material correction.

## 16. Commercial v1.0 connection

This standard creates the reproducibility and release discipline required to sell Operator Intelligence as a dependable assessment product. It supports evaluator consistency, defensible reporting, controlled implementation, client trust, and repeatable delivery quality.

## 17. Cross references

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
- `standards/decision-ledger-standard.md`
- `standards/ai-readiness-standard.md`
- `scoring/calculator-spec.md`
- `scoring/completion-status.md`
- `templates/quality-control-checklist.md`