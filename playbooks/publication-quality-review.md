# Publication Quality Review Playbook

Version: v0.1 execution foundation  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This playbook defines the required operational review before an Operator Intelligence assessment, score, finding set, recommendation set, roadmap, proposal, or executive report may be released to a client.

It converts `standards/quality-control-standard.md` and `standards/publication-standard.md` into an executable reviewer workflow.

Quality review does not authorize publication by itself and never authorizes implementation.

## 2. Inputs

Required inputs:

- approved assessment scope
- evidence register
- score run and category outputs
- finding register
- recommendation register
- roadmap
- executive report or client deliverable
- DecisionLedger records
- report version metadata
- quality-control and publication standards

Missing required inputs produce `HALT` unless the intended output is explicitly `internal_only`.

## 3. Preconditions

Before review begins, confirm:

- the assessment scope and evidence snapshot date are fixed
- the report version is identified
- all scored criteria have valid states
- findings and recommendations use approved identifiers
- the intended publication state is declared
- the reviewer has access to the referenced records
- no live testing is required during publication review

If the evidence base changes materially during review, stop and return the affected artifacts for recalculation or supersession.

## 4. Review sequence

Perform the review in this order:

```text
Scope
→ Evidence
→ Scoring
→ Confidence and unknowns
→ Findings
→ Recommendations and packages
→ Roadmap
→ DecisionLedger
→ Executive language
→ Version and distribution
→ Publication decision
```

A later step cannot cure an earlier failure without correction and re-review.

## 5. Step 1 — Scope review

Verify:

- included and excluded systems, channels, categories, and date ranges are explicit
- applicability and `not_applicable` decisions are approved
- public-only and internal-access limitations are visible
- the report does not imply review of surfaces outside the approved scope

Decision:

- `ALLOW` when scope is complete and represented accurately
- `REVIEW` when a bounded limitation can be disclosed without misleading the client
- `HALT` when the claimed assessment scope cannot be supported

## 6. Step 2 — Evidence review

Verify every material statement, score, and finding against the evidence register.

Required checks:

- stable evidence ID exists
- source, owner, collection date, and represented date range are recorded
- provenance and admissibility are valid
- client statements remain `reported` unless corroborated
- contradictory evidence remains visible
- stale or narrow samples are disclosed
- duplicate evidence use has distinct category ownership
- missing access is not treated as negative evidence

`HALT` when material provenance, integrity, authorization, or traceability is broken.

## 7. Step 3 — Scoring review

Independently reproduce:

```yaml
applicable_weight_total: 100
scored_applicable_weight: 0-100
coverage_percent: 0-100
category_scores: {}
operator_score: 0-100|null
score_type: official|observed_indicator|range|null
```

Confirm:

- approved anchors and category sheets were used
- unknown and blocked criteria remain inside applicable weight
- approved `not_applicable` criteria were removed before normalization
- confidence did not change maturity
- rounding occurred only at the display boundary
- duplicate weighted ownership is absent

Any unresolved recalculation difference requires `HALT`.

## 8. Step 4 — Confidence and unknown review

Verify:

- confidence is evidence-derived
- confidence does not exceed the weakest material evidence dependency
- `unknown` is not relabeled `low`
- blocked conditions remain explicit
- high-materiality unknowns are disclosed in the executive summary
- the proposed publication state reflects uncertainty

Unknown or blocked criteria never create automatic findings, zero scores, or implementation recommendations.

## 9. Step 5 — Finding review

Every published finding must include:

- finding ID
- observation
- criterion or category owner
- admissible evidence references
- interpretation
- bounded business impact
- confidence
- priority
- limitations and unknowns
- DecisionLedger reference

Confirm observation is separated from interpretation and that one signal has one weighted owner.

Use `HALT` when a material finding lacks evidence, overstates impact, hides uncertainty, or duplicates another finding's primary ownership.

## 10. Step 6 — Recommendation and package review

Every published recommendation must:

- trace to an approved finding
- remain proportional to the evidence and confidence
- have exactly one primary package
- use only canonical package IDs
- identify prerequisites and dependent packages
- include roadmap phase
- define observable acceptance evidence
- state validation requirements
- record implementation authorization separately

Package-first selling, duplicated implementation ownership, and recommendations created directly from unknown conditions require `HALT`.

## 11. Step 7 — Roadmap review

Verify:

- Phase 1 through Phase 4 sequencing is preserved
- prerequisites and dependency IDs are explicit
- `HALT` conditions block dependent work
- owners and acceptance authority are identified
- completion evidence is observable
- target windows are planning assumptions, not guarantees
- Phase 4 AI work does not bypass workflow, data, privacy, review, escalation, logging, and QA gates

Priority alone cannot justify resequencing.

## 12. Step 8 — DecisionLedger review

Confirm every material decision has a resolvable DecisionLedger record covering:

- score and publication state
- finding approval, suppression, or supersession
- recommendation and package routing
- roadmap phase and dependencies
- accepted limitations or exceptions
- reviewer outcome
- publication approval

Approved records cannot be silently overwritten. Material corrections require superseding records.

## 13. Step 9 — Executive language review

Approved language includes:

- `verified across the reviewed scope`
- `supported by the available evidence`
- `not visible on tested public surfaces`
- `partially confirmed`
- `requires internal validation`
- `the evidence supports a provisional interpretation`

Remove or rewrite:

- unsupported lead-loss, revenue, conversion, ranking, savings, ROI, or market-share claims
- competitor-performance conclusions based on appearance alone
- definitive internal-failure language from public absence
- timeline certainty where access, dependencies, or capacity remain unverified
- statements implying publication approval authorizes implementation

## 14. Step 10 — Version and distribution review

Every release must identify:

```yaml
report_id: OI-REPORT-YYYY-NNN
report_version: ""
assessment_date: YYYY-MM-DD
publication_date: YYYY-MM-DD
publication_state: official|provisional|range_only|blocked|internal_only
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
reviewed_by: ""
supersedes_report_id: null
ledger_ref: OI-DL-YYYY-NNN
```

Confirm prior released versions are retained and distribution matches the approved publication state.

## 15. Publication-state decision

| State | Minimum operational decision |
|---|---|
| `official` | Required scope complete, coverage at least 80%, material confidence adequate, no unresolved blocker, independent review passed, reviewer state `ALLOW` |
| `provisional` | Usable assessment with bounded and prominently disclosed limitations; reviewer state `ALLOW` or documented `REVIEW` |
| `range_only` | Material unknowns prevent a defensible single score; publish ranges and validation priorities only |
| `blocked` | Authorization, evidence integrity, control, traceability, or material conflict prevents defensible release |
| `internal_only` | Work remains incomplete, unapproved, or restricted to internal review |

Coverage threshold alone does not authorize `official` publication.

## 16. Review outcomes

### ALLOW

Use only when all blocking checks pass and warnings are resolved or accepted with rationale.

### REVIEW

Use when no blocking error exists but a bounded limitation, sample issue, recency concern, or reviewer judgment must be documented before release.

### HALT

Use when any of the following exists:

- missing material evidence
- unreproducible score
- unknown scored as zero
- unsupported confidence
- duplicate weighted or package ownership
- finding without complete traceability
- invalid package or roadmap routing
- unsupported executive claim
- missing publication or ledger control
- publication approval treated as implementation authorization

## 17. Quality-review record

```yaml
qc_id: OI-QC-YYYY-NNN
report_id: OI-REPORT-YYYY-NNN|null
report_version: ""
intended_publication_state: ""
final_publication_state: ""
evidence_snapshot_date: YYYY-MM-DD
scope_check_passed: false
evidence_check_passed: false
recalculation_passed: false
confidence_check_passed: false
unknown_check_passed: false
finding_check_passed: false
routing_check_passed: false
roadmap_check_passed: false
ledger_check_passed: false
language_review_passed: false
version_check_passed: false
blocking_errors: []
warnings: []
accepted_exceptions: []
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
reviewed_at: YYYY-MM-DD
publication_authorized: false
implementation_authorized: false
ledger_ref: OI-DL-YYYY-NNN
```

`publication_authorized` and `implementation_authorized` default to `false` and require separate governed decisions.

## 18. Corrective-action loop

When review returns `REVIEW` or `HALT`:

1. assign each issue an owner
2. identify affected evidence, score, finding, recommendation, package, roadmap, report, and ledger records
3. correct the earliest failed control in the chain
4. supersede affected records when material
5. rerun all downstream checks
6. record final disposition in the DecisionLedger

Do not patch only the client-facing wording when the underlying evidence or calculation is defective.

## 19. Release checklist

A deliverable may advance to the separate publication decision only when:

- [ ] scope and applicability are accurate
- [ ] evidence is admissible, attributable, current enough, and traceable
- [ ] scores, weights, coverage, and rounding reproduce
- [ ] confidence and unknown states are correct
- [ ] findings are supported, bounded, and uniquely owned
- [ ] recommendations use one primary package and valid dependencies
- [ ] roadmap sequencing and acceptance evidence are valid
- [ ] DecisionLedger records are complete
- [ ] executive language is evidence-bounded
- [ ] version, supersession, and distribution fields are complete
- [ ] quality-review outcome is recorded
- [ ] publication and implementation authorization remain separate

## 20. Outputs

This playbook produces:

- completed quality-review record
- blocking-error register
- warning and accepted-exception register
- corrective-action list
- final review state
- recommended publication state
- DecisionLedger event
- release-ready or halted artifact set

## 21. Cross references

- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/quality-control-standard.md`
- `standards/publication-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/evidence-register.md`
- `templates/finding-register.md`
- `templates/recommendation-register.md`
- `templates/executive-report.md`
- `templates/roadmap.md`
- `templates/proposal.md`

## 22. v1.0 connection

This playbook makes client-release quality control repeatable, auditable, and executable. It reduces evaluator drift, prevents unsupported publication, preserves DecisionLedger traceability, and establishes the final operational gate required before Operator Intelligence deliverables can be used in a commercial engagement.