# Northstar Painting Co. — Synthetic Quality-Control Record

Version: v1.0 sample QC record  
Stage alignment: Stage 7 — `examples/`  
Status: ALLOW provisional demonstration release

## 1. Review identity

```yaml
qc_id: OI-QC-2026-EX001
assessment_id: OI-ASSESS-2026-EX001
artifact_type: sample_engagement_set
artifact_id: examples/sample-painting-contractor
artifact_version: "1.0"
methodology_version: commercial-v1.0
evidence_snapshot_date: 2026-07-20
reviewed_by: Sample QC Reviewer
decision_authority: Example Folder Gate
reviewed_at: "2026-07-20T18:00:00Z"
ledger_ref: OI-DL-2026-EX022
```

## 2. Artifact scope reviewed

- engagement brief
- evidence register
- scorecard
- finding ledger
- recommendation map
- roadmap
- executive report
- proposal
- DecisionLedger

## 3. Ordered checks

| Review area | Result | Notes |
|---|---|---|
| Scope/version | PASS | Fictional client, synthetic data, exclusions, method, version, and snapshot are explicit |
| Evidence | PASS with limitations | 13 accepted and 4 limited synthetic records; no real-client claims |
| Scoring | PASS | Weight 100%; coverage 86.5%; score 49.789 displayed 50; confidence 0.779; range 34–67 |
| Unknown handling | PASS | Social remains unknown; not zero and no social finding |
| Confidence | PASS | Confidence does not modify maturity or priority |
| Findings | PASS | Five governed findings; unsupported candidates suppressed |
| Duplicate control | PASS | Estimate form, cabinet page, project proof, lead workflow, and AI controls have one weighted owner |
| Recommendations | PASS | Canonical priority formula reproduces; five actions are proportional |
| Package routing | PASS | Three eligible routes have one primary package; two validation routes have none |
| Roadmap | PASS | Phase 0 and phases 1–5 used; priority does not bypass validation |
| AI controls | PASS as HALT | No AI recommendation or package assignment; blockers explicit |
| Executive report | PASS provisional | Coverage, confidence, range, limitations, and synthetic notice shown |
| Proposal | PASS internal example | Only bounded Website package; fee/timeline/authorization not invented |
| Authorization | PASS | Publication, proposal acceptance, and implementation authorization remain separate |
| Completion/value | PASS | No delivery or outcome result is claimed |
| DecisionLedger | PASS | Material states and boundaries are recorded |
| Language | PASS | No unsupported lead, ranking, conversion, revenue, savings, ROI, competitor, or timeline claims |

## 4. Validation messages

| Code | Type | Condition | Disposition |
|---|---|---|---|
| `QC-SAMPLE-001` | warning | Internal workflow sample is narrow | Retained in confidence and report limitations |
| `QC-SAMPLE-002` | warning | Competitive fixture is synthetic and limited | Restricted to visible comparative context |
| `QC-UNKNOWN-EX001` | warning | Social evidence unavailable | Category unknown; no finding/recommendation |
| `QC-AI-EX001` | blocking for AI implementation | Privacy, retention, escalation, logging, review, and QA controls incomplete | AI route HALT; does not block non-AI sample release |
| `QC-COMM-EX001` | warning | Proposal has no real price or timeline | Intentional; prevents invented commercial facts |

## 5. Recalculation record

```yaml
active_weight_total: 100
weighted_evidence_coverage: 0.865
observed_score_raw: 49.7894736842
observed_score_display: 50
operator_confidence_index: 0.7789017341
operator_lower_bound_raw: 34.3825
operator_upper_bound_raw: 67.0075
operator_range_display: "34-67"
recalculation_passed: true
```

## 6. QC decision

```yaml
recalculation_passed: true
duplicate_check_passed: true
routing_check_passed: true
authorization_separation_passed: true
language_review_passed: true
ledger_check_passed: true
blocking_errors_for_sample_release: []
warnings:
  - narrow synthetic internal samples
  - social unknown
  - AI implementation HALT
  - no real commercial terms
review_state: ALLOW
publication_effect: provisional
publication_decision_required: true
implementation_authorized: false
```

## 7. Publication recommendation

ALLOW the example folder for repository publication as a **synthetic provisional demonstration** under these conditions:

- retain fictional/synthetic labels
- retain score range, coverage, confidence, and limitations
- retain social unknown state
- retain AI HALT state
- do not represent the proposal as accepted or priced
- do not represent any work as implemented or measured

## 8. Corrective-action rule

Any material change to evidence, score arithmetic, findings, priority, package route, phase, publication state, proposal scope, or authorization requires affected artifacts and this QC record to be superseded and re-reviewed.

## 9. Commercial v1.0 connection

This record demonstrates that an end-to-end engagement can pass controlled review while preserving material uncertainty and implementation blocks.