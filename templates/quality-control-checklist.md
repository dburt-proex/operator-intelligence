# Operator Intelligence Quality-Control Checklist

Version: v0.1 commercial v1.0 checklist  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed release-control template

## 1. Purpose

Use this checklist to execute and record the ordered quality-control review required before a score, finding set, recommendation set, roadmap, report, proposal, package scope, implementation completion, or renewal record advances.

The checklist produces a bounded `ALLOW`, `REVIEW`, or `HALT`. It does not publish an artifact or authorize implementation.

## 2. Review identity

```yaml
qc_id: OI-QC-YYYY-NNN
assessment_id: ""
artifact_type: score_run|finding_set|recommendation_set|roadmap|report|proposal|package|implementation_completion|renewal_record
artifact_id: ""
artifact_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
reviewed_by: ""
decision_authority: ""
reviewed_at: "YYYY-MM-DDThh:mm:ssZ"
supersedes_qc_id: null
ledger_ref: OI-DL-YYYY-NNN
```

## 3. Ordered review checks

### 3.1 Scope control

- [ ] Artifact ID, version, purpose, audience, and release target are fixed.
- [ ] Assessment boundary, applicable categories, systems, locations, date range, and exclusions are explicit.
- [ ] Access restrictions and testing boundaries are recorded.
- [ ] Material conflicts of interest are disclosed.

Validation codes: `QC-SCOPE-001`

### 3.2 Evidence control

- [ ] Every material claim cites a resolvable Evidence ID.
- [ ] Source, owner, date, scope, capture method, integrity, and authorization are recorded.
- [ ] Evidence admission state is accepted or limited with explicit effects.
- [ ] Client statements remain reported until corroborated.
- [ ] Public absence is not treated as internal nonexistence.
- [ ] Conflicting, stale, rejected, and superseded evidence remains visible.

Validation codes: `QC-EVID-001`, `QC-RECENCY-001`, `QC-SAMPLE-001`

### 3.3 Scoring control

- [ ] Active category weights total 100%.
- [ ] Criterion and category applicability decisions are valid.
- [ ] Unknown and blocked criteria remain in applicable coverage.
- [ ] Unknown is never scored as zero.
- [ ] Confidence does not multiply maturity.
- [ ] Category scores, bounds, evidence coverage, confidence index, and Operator Score reproduce.
- [ ] Publication state and score display satisfy canonical gates.
- [ ] Rounding occurs only at the approved display stage.

Validation codes: `QC-SCORE-001`, `QC-UNKNOWN-001`

### 3.4 Finding control

- [ ] Observation, evidence, interpretation, impact, confidence, limitations, and validation needs are separated.
- [ ] Finding ID and finding-library mapping are valid.
- [ ] Duplicate weighted ownership is absent.
- [ ] Unknown conditions have not been converted into negative findings.
- [ ] Report language follows the governed finding library.

Validation codes: `QC-FIND-001`, `QC-DUP-001`

### 3.5 Recommendation control

- [ ] Recommendation traces to governed findings and evidence.
- [ ] Impact, evidence-strength score, effort inverse, and strategic fit use canonical authorities.
- [ ] Priority calculation reproduces.
- [ ] Confidence remains a separate gate.
- [ ] Scope is proportional to the verified root condition.
- [ ] Acceptance criteria and evidence are observable.

Validation codes: `QC-PRIORITY-001`

### 3.6 Package and roadmap control

- [ ] Package eligibility is explicit.
- [ ] Exactly one primary package exists only when eligible.
- [ ] Dependencies, exclusions, and ownership are non-duplicative.
- [ ] Phase 0 represents validation only.
- [ ] Phases 1–5 follow root condition and prerequisites.
- [ ] Owners, authority, sequence, start gates, and completion evidence are explicit.
- [ ] AI work remains blocked until all readiness controls pass.

Validation codes: `QC-ROUTE-001`, `QC-PHASE0-001`, `QC-AI-001`

### 3.7 Publication and language control

- [ ] Publication state matches evidence, coverage, confidence, limitations, QC, and version state.
- [ ] Provisional and range-only outputs remain explicit.
- [ ] Unknowns and blockers are disclosed.
- [ ] Executive language is bounded and blame-free.
- [ ] Unsupported outcome, competitor, financial, ranking, conversion, or timeline claims are absent.

Validation codes: `QC-PUB-001`, `QC-LANGUAGE-001`

### 3.8 Authorization and completion control

- [ ] QC, publication, roadmap approval, proposal acceptance, and implementation authorization are separate.
- [ ] No work is in progress without a resolvable authorization reference.
- [ ] Authorized scope, exclusions, access, owner, prerequisites, and rollback/escalation are recorded.
- [ ] Completion is supported by acceptance evidence.
- [ ] Realized-value evidence remains separate from completion evidence.

Validation codes: `QC-AUTH-001`, `QC-COMPLETE-001`, `QC-MEASURE-001`

### 3.9 DecisionLedger control

- [ ] Material decisions, exceptions, approvals, authorizations, blocks, changes, completions, and supersessions have ledger events.
- [ ] Upstream and downstream references resolve.
- [ ] Approved or published history is not overwritten.
- [ ] Client-safe summaries match the reviewed decision.

Validation codes: `QC-LEDGER-001`

## 4. Error and warning register

| Code | Type | Condition | Affected object | Owner | Corrective action | State | Ledger ref |
|---|---|---|---|---|---|---|---|
| | blocking / warning | | | | | open / resolved / accepted | |

## 5. QC result

```yaml
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
release_blockers: []
next_governed_decision: ""
```

## 6. Decision rules

- `ALLOW`: all blocking checks pass; warnings are resolved or accepted with rationale.
- `REVIEW`: qualified judgment or a bounded exception is required before advancement.
- `HALT`: a blocking evidence, scoring, routing, authority, language, traceability, or completion failure exists.

The result applies only to the reviewed artifact version and evidence snapshot.

## 7. Usage instructions

1. Freeze artifact and evidence versions.
2. Run sections in order.
3. Record codes and corrective actions.
4. Recalculate quantitative outputs independently.
5. Issue and ledger the bounded result.
6. Re-run affected checks after material corrections.
7. Store the completed checklist with the released artifact.

## 8. Commercial v1.0 connection

This checklist turns the quality-control standard into an executable release gate for consistent, defensible client delivery.

## 9. References

- `standards/quality-control-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/decision-ledger.md`