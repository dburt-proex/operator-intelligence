# Quality Control Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard defines the minimum quality-control process required before an Operator Intelligence assessment, score, finding set, roadmap, recommendation, or client report may advance to publication.

Quality control verifies that the assessment is reproducible, evidence-grounded, internally consistent, traceable through the DecisionLedger, and safe for executive use. It does not replace evidence collection, scoring, confidence assignment, package routing, roadmap approval, publication approval, or implementation authorization.

## 2. Core rules

1. Every client-facing assessment requires a documented quality-control review.
2. The reviewer must verify evidence admissibility, scoring consistency, confidence assignment, unknown handling, duplicate-signal ownership, finding construction, package routing, roadmap sequencing, publication state, and executive-safe language.
3. Unknown and blocked conditions must remain visible and may not be converted to zero.
4. Confidence must remain separate from maturity.
5. Every material output must trace to evidence and a DecisionLedger record.
6. Every recommendation must have exactly one primary package and an approved roadmap phase.
7. Publication approval and implementation authorization remain separate decisions.
8. Unsupported ROI, revenue, conversion, ranking, lead-loss, market-share, competitor-performance, or timeline certainty is prohibited.
9. A failed blocking check requires `HALT` until corrected or formally superseded.
10. Quality-control records must be retained with the released report version.

## 3. Review scope

The quality-control review must cover:

| Review area | Required verification |
|---|---|
| Scope | Required categories, criteria, systems, and evidence windows are identified |
| Evidence | Evidence is admissible, dated, attributable, and sufficient for the claimed condition |
| Scoring | Approved anchors, weights, applicability, rounding, and coverage calculations are followed |
| Confidence | Confidence reflects evidence strength and does not alter maturity |
| Unknowns | Unknown, blocked, and not-applicable states are correctly distinguished |
| Findings | Each finding has observation, evidence, interpretation, impact, confidence, and limitations |
| Duplicate control | Each signal has one weighted owner and no duplicated implementation ownership |
| Recommendations | Each recommendation traces to a finding and uses proportional scope |
| Package routing | Exactly one primary package is assigned and prerequisites are explicit |
| Roadmap | Dependencies, phase gates, owners, and acceptance evidence are defined |
| Publication | Publication state matches coverage, confidence, and unresolved limitations |
| Language | Client-facing claims are bounded, accurate, and executive-safe |
| DecisionLedger | Material decisions, approvals, exceptions, and supersessions are recorded |

## 4. Review sequence

Quality control must follow this order:

1. **Scope review** — confirm the assessment boundary and applicable criteria.
2. **Evidence review** — verify admissibility, attribution, recency, and conflicts.
3. **Scoring review** — recalculate category scores, weights, coverage, and Operator Score.
4. **Confidence review** — confirm evidence-to-confidence mapping.
5. **Unknown-state review** — confirm missing access is not treated as failure.
6. **Finding review** — verify every finding is supported and proportionate.
7. **Routing review** — verify one primary package, dependencies, and roadmap phase.
8. **Publication review** — verify state, limitations, versioning, and release fields.
9. **Language review** — remove unsupported certainty and outcome claims.
10. **Ledger review** — confirm DecisionLedger completeness and reviewer decision.

A later review step cannot cure a failure in an earlier step without correcting and re-running the affected checks.

## 5. Review outcomes

| State | Meaning | Required action |
|---|---|---|
| `ALLOW` | All blocking checks pass; warnings are resolved or accepted with rationale | May proceed to the separate publication decision |
| `REVIEW` | No blocking error exists, but a bounded issue requires documented reviewer judgment | Correct, disclose, or formally accept the limitation before publication |
| `HALT` | A blocking error, unsupported claim, traceability break, or material control failure exists | Do not publish or authorize dependent work |

`ALLOW` from quality control does not itself authorize publication or implementation.

## 6. Independence and reviewer controls

- The primary author may perform an initial self-check.
- A second-person review is required for `official` client publication when available.
- If a second reviewer is unavailable, the report must remain `provisional` unless an approved exception is recorded.
- Reviewers must not silently edit material decisions without creating a superseding DecisionLedger event.
- Reviewer conflicts of interest, unresolved disagreements, or scope exceptions must be documented.

## 7. Recalculation requirements

The reviewer must independently verify:

```yaml
applicable_weight_total: 0-100
scored_applicable_weight: 0-100
coverage_percent: 0-100
category_scores: {}
weighted_operator_score: 0-100|null
published_score_type: official|observed_indicator|range|null
publication_state: official|provisional|range_only|blocked|internal_only
```

Rules:

- Applicable weight must reconcile to the approved weight profile.
- Approved `not_applicable` criteria may be removed only before weight normalization.
- Unknown and blocked criteria remain inside applicable weight.
- Unknown is never scored as zero.
- Rounding must occur only at the approved display stage.
- Recalculation differences must be resolved before `ALLOW`.

## 8. Finding and routing checks

Each reported finding must pass all of the following:

- evidence references exist and are admissible
- observation is separated from interpretation
- business impact is bounded and not overstated
- confidence is supported by the evidence chain
- limitations and unknowns are visible
- one criterion or category owns the weighted signal
- DecisionLedger reference exists

Each recommendation must additionally pass:

- valid finding linkage
- exactly one primary package
- no duplicate implementation ownership
- prerequisite and dependency checks
- roadmap phase assignment
- acceptance evidence definition
- implementation authorization state recorded separately

## 9. Executive-safe language review

Approved language includes:

- `verified across the reviewed scope`
- `supported by the available evidence`
- `not visible on the tested public surfaces`
- `partially confirmed`
- `requires internal validation`
- `the evidence supports a provisional interpretation`

Prohibited without validated support:

- guaranteed lead, revenue, conversion, ranking, savings, or ROI outcomes
- claims that public absence proves internal nonexistence
- competitor-performance or market-share conclusions derived from appearance alone
- definitive failure language when evidence is incomplete
- timeline certainty where dependencies or capacity are unverified

## 10. Quality-control record

Every completed review must retain:

```yaml
qc_id: OI-QC-YYYY-NNN
report_id: OI-REPORT-YYYY-NNN|null
report_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
reviewed_scope: []
blocking_errors: []
warnings: []
accepted_exceptions: []
recalculation_passed: false
duplicate_check_passed: false
language_review_passed: false
ledger_check_passed: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
reviewed_at: YYYY-MM-DD
ledger_ref: OI-DL-YYYY-NNN
```

Material corrections after review require a new quality-control record or a superseding review event.

## 11. Validation rules

### Blocking errors

- `QC-SCOPE-001`: required assessment scope or applicability decision is unresolved
- `QC-EVID-001`: material output lacks admissible evidence
- `QC-SCORE-001`: score, weight, coverage, or rounding cannot be reproduced
- `QC-CONF-001`: confidence is unsupported or used to alter maturity
- `QC-UNKNOWN-001`: unknown or blocked data is hidden, dropped, or scored as zero
- `QC-DUP-001`: a signal or implementation responsibility has duplicate primary ownership
- `QC-FIND-001`: a published finding lacks a complete evidence-to-interpretation chain
- `QC-ROUTE-001`: recommendation lacks valid package, prerequisite, or roadmap routing
- `QC-LEDGER-001`: material decision lacks DecisionLedger traceability
- `QC-PUB-001`: publication state conflicts with evidence coverage or unresolved limitations
- `QC-LANGUAGE-001`: client language contains unsupported certainty or outcome claims
- `QC-AUTH-001`: quality-control or publication approval is treated as implementation authorization

### Warnings

- `QC-REVIEW-001`: no independent reviewer is available for an intended official release
- `QC-RECENCY-001`: evidence remains admissible but is near its freshness limit
- `QC-SAMPLE-001`: evidence sample is narrow but disclosed and non-blocking
- `QC-OWNER-001`: accountable owner is identified but acceptance authority remains pending
- `QC-MEASURE-001`: implementation acceptance is defined but outcome measurement is not yet available

Warnings require disposition but do not automatically permit publication.

## 12. Release checklist

A report may advance from quality control only when:

- [ ] required scope and applicability decisions are complete
- [ ] evidence references are valid and conflicts are resolved or disclosed
- [ ] scoring and coverage calculations reproduce exactly
- [ ] confidence assignments match evidence strength
- [ ] unknown, blocked, and not-applicable states are correctly handled
- [ ] findings are complete, bounded, and traceable
- [ ] duplicate-signal and duplicate-package checks pass
- [ ] recommendations use one primary package and valid roadmap phases
- [ ] executive-safe language review passes
- [ ] publication state is defensible
- [ ] report version and evidence snapshot are recorded
- [ ] DecisionLedger records are complete
- [ ] reviewer state is recorded as `ALLOW`, `REVIEW`, or `HALT`

## 13. Cross references

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/decision-ledger-standard.md`
- `scoring/category-sheets/`
- `framework/findings/`
