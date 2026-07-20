# Publication Quality Review Playbook

Version: v1.0 commercial operating playbook  
Stage alignment: Stage 6 — `playbooks/`  
Folder alignment: `playbooks/`  
Status: Governed pre-publication review workflow

## 1. Purpose

Use this playbook before releasing an assessment, score, finding/recommendation set, roadmap, report, proposal, package scope, or completion record.

It executes the quality-control and publication standards. QC ALLOW permits a separate publication decision only and never authorizes implementation.

## 2. Inputs

- fixed artifact ID/version and audience
- approved scope and exclusions
- evidence register and snapshot
- score run/category outputs where applicable
- finding and recommendation registers
- package/roadmap records
- DecisionLedger events
- completed quality-control checklist

## 3. Review sequence

```text
Scope and version
→ Evidence
→ Scoring and unknowns
→ Findings
→ Recommendations and package eligibility
→ Roadmap and authorization
→ DecisionLedger
→ Executive language
→ Distribution
→ QC decision
→ Separate publication decision
```

Correct the earliest failed control and rerun downstream checks.

## 4. Scope and version review

Verify included/excluded systems, channels, categories, locations, date ranges, applicability, access limits, artifact version, methodology version, evidence snapshot, and supersession state.

HALT when the represented scope or version cannot be supported.

## 5. Evidence review

Verify material claims against admitted evidence, including identity, provenance, recency, relevance, scope, integrity, authorization, contradictions, limitations, and duplicate ownership.

Reported/inferred evidence may not be upgraded through wording.

## 6. Scoring review

Independently reproduce applicable weight, known weight, category scores/bounds, evidence coverage, confidence index, Operator Score/range, validation messages, rounding, and publication gates.

Unknown and blocked remain inside applicable coverage and are never zero. Confidence never changes maturity.

## 7. Finding review

Every published finding must have governed ID, observation, evidence, interpretation, impact, confidence, limitations/unknowns, ownership, report-use state, QC ref, and DecisionLedger ref.

## 8. Recommendation and package review

Verify:

- finding/evidence traceability
- canonical priority inputs and reproducible score
- confidence separation
- proportional scope
- package eligibility
- exactly one primary package only when eligible
- dependencies/exclusions
- acceptance evidence
- Phase 0 or phases 1–5
- authorization state remains separate

Package-first selling or routing an unknown condition directly into implementation requires HALT.

## 9. Roadmap and authorization review

- Phase 0 is validation only.
- Phase order and dependencies are preserved.
- Owners, authority, start gates, and completion evidence are explicit.
- Phase 4 controls pass.
- Roadmap approval, proposal acceptance, and publication do not authorize implementation.
- Completion evidence and realized-value evidence remain separate.

## 10. DecisionLedger review

Confirm material evidence, scoring, finding, priority, eligibility, routing, phase, QC, publication, authorization, completion, monitoring, and supersession decisions resolve.

## 11. Executive language review

Approved language is bounded to reviewed scope. Remove unsupported lead, revenue, conversion, ranking, savings, ROI, market-share, competitor-performance, causation, and timeline certainty.

Public absence cannot become internal-failure language.

## 12. Distribution review

```yaml
artifact_id: ""
artifact_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
intended_audience: []
publication_state: official|provisional|range_only|blocked|internal_only
supersedes: null
retention_location: ""
distribution_owner: ""
qc_ref: OI-QC-YYYY-NNN
publication_ledger_ref: null
```

Prior released versions remain retained.

## 13. Publication states

| State | Use |
|---|---|
| `official` | All official gates, including required coverage/confidence and independent review, pass |
| `provisional` | Usable bounded output with prominent limitations |
| `range_only` | Material uncertainty prevents a defensible point score |
| `blocked` | Evidence, authority, traceability, control, or conflict prevents release |
| `internal_only` | Incomplete, unapproved, or restricted work |

Coverage alone does not authorize publication.

## 14. QC and publication decisions

```yaml
qc_state: ALLOW|REVIEW|HALT
qc_ref: OI-QC-YYYY-NNN
publication_decision: pending|approved|declined|blocked
publication_state: official|provisional|range_only|blocked|internal_only
publication_authority: ""
publication_ledger_ref: null
implementation_authorized: false
```

## 15. Corrective-action loop

For REVIEW/HALT:

1. assign owner and validation code
2. identify affected source objects
3. correct earliest failed control
4. supersede material records
5. rerun all affected checks
6. issue new QC/publication decisions

Do not repair wording while leaving defective evidence or calculation unchanged.

## 16. Release checklist

- [ ] Scope, version, method, snapshot, and audience are fixed.
- [ ] Evidence is admissible and traceable.
- [ ] Scores/coverage/bounds reproduce.
- [ ] Unknown and confidence handling pass.
- [ ] Findings are governed and uniquely owned.
- [ ] Priority and package eligibility pass.
- [ ] Phase and authorization controls pass.
- [ ] Ledger, language, supersession, and distribution pass.
- [ ] QC and publication are separately decided.
- [ ] Implementation authorization remains false unless separately granted.

## 17. Commercial v1.0 connection

This playbook creates a repeatable client-release gate and protects commercial reports from unsupported certainty and authority drift.

## 18. References

- `standards/quality-control-standard.md`
- `standards/publication-standard.md`
- `templates/quality-control-checklist.md`
- `templates/executive-report.md`