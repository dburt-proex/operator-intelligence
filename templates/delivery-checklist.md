# Operator Intelligence Delivery Checklist

Version: v0.1 commercial v1.0 checklist  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed engagement-delivery template

## 1. Purpose

Use this checklist to control an Operator Intelligence engagement from accepted intake through assessment delivery, client decision, authorized implementation handoff, completion, monitoring, and closure.

## 2. Engagement control

```yaml
engagement_id: OI-ENG-YYYY-NNN
assessment_id: ""
client: ""
engagement_owner: ""
decision_authority: ""
methodology_version: ""
current_lifecycle_state: OI-LC-01|OI-LC-02|OI-LC-03|OI-LC-04|OI-LC-05|OI-LC-06|OI-LC-07|OI-LC-08|OI-LC-09|OI-LC-10|OI-LC-11|OI-LC-12|OI-LC-13|OI-LC-14
review_state: ALLOW|REVIEW|HALT
ledger_ref: OI-DL-YYYY-NNN
```

## 3. Qualification and intake

- [ ] Client and intended use are qualified.
- [ ] Scope, locations, systems, channels, date range, and exclusions are defined.
- [ ] Decision questions and authority are identified.
- [ ] Access and testing permissions are explicit.
- [ ] Data handling, retention, confidentiality, and deletion rules are recorded.
- [ ] Material unknowns and blockers are visible.
- [ ] Intake gate is ledgered as ALLOW, REVIEW, or HALT.

Completion evidence: approved intake, scope record, access register, ledger event.

## 4. Surface mapping and evidence collection

- [ ] Applicable public and internal surfaces are inventoried.
- [ ] Evidence IDs, source data, date, scope, owner, and integrity refs are assigned.
- [ ] Safe tests are authorized and documented.
- [ ] Client statements are marked reported until corroborated.
- [ ] Contradictions, gaps, and access blocks are retained.
- [ ] Evidence snapshot is frozen before scoring.

Completion evidence: surface inventory, evidence register, validation log.

## 5. Scoring and finding resolution

- [ ] Criteria and category applicability are approved.
- [ ] Scoring calculations and coverage reproduce.
- [ ] Unknown, blocked, and not-applicable states are correct.
- [ ] Confidence and bounds are derived separately from maturity.
- [ ] Candidate findings map to governed libraries.
- [ ] Duplicate ownership is resolved.
- [ ] Findings are validated, suppressed, blocked, or closed with ledger refs.

Completion evidence: score run, category objects, finding register, ledger events.

## 6. Synthesis and recommendation routing

- [ ] Risk, impact, opportunity, effort, and priority inputs use canonical authorities.
- [ ] Recommendations are proportional and evidence-bound.
- [ ] Package eligibility is explicit.
- [ ] Primary package is assigned only when eligible.
- [ ] Phase 0 and phases 1–5 are valid.
- [ ] Dependencies, owners, acceptance criteria, and exclusions are recorded.
- [ ] Unsupported ROI and outcome claims are absent.

Completion evidence: recommendation register, routing objects, roadmap draft.

## 7. Report, roadmap, and proposal release

- [ ] Executive and contractor report outputs use the approved publication state.
- [ ] Score display includes coverage, confidence/bounds, and limitations.
- [ ] QC checklist is complete.
- [ ] QC state and publication approval are separately ledgered.
- [ ] Roadmap includes validation, implementation, monitoring, and closure states.
- [ ] Proposal scope matches eligible package scope.
- [ ] Proposal acceptance does not imply implementation authorization.

Completion evidence: released report, QC record, roadmap, proposal, publication ledger.

## 8. Client delivery and decision

- [ ] Client received the correct artifact versions.
- [ ] Findings, limitations, unknowns, and publication state were explained.
- [ ] Decision requested is explicit.
- [ ] Client decisions, deferrals, rejections, and questions are recorded.
- [ ] No verbal or written statement exceeded the evidence.
- [ ] Next gate, owner, and due condition are recorded.

Completion evidence: delivery notes, decision memo, client acknowledgement, ledger event.

## 9. Onboarding and implementation handoff

- [ ] Accepted proposal and authorized package scope resolve.
- [ ] Separate implementation authorization is recorded.
- [ ] Owner, access, prerequisites, dependencies, and exclusions pass.
- [ ] Work plan, acceptance tests, rollback, escalation, and communication cadence are defined.
- [ ] AI controls pass before Phase 4 work.
- [ ] No unresolved HALT applies.

Completion evidence: onboarding checklist, authorization record, implementation plan.

## 10. Completion and monitoring

- [ ] Acceptance criteria are tested against authorized scope.
- [ ] Completion evidence is retained.
- [ ] Defects, exceptions, and residual risks are recorded.
- [ ] Client acceptance or rejection is recorded.
- [ ] Realized-value measurement uses a separate baseline and review window.
- [ ] Phase 5 optimization, renewal, maintenance, or closure decision is ledgered.

Completion evidence: completion record, acceptance evidence, monitoring record, renewal/closure decision.

## 11. Delivery issue register

| Issue ID | Lifecycle state | Condition | Severity | Owner | Gate | Corrective action | Resolution evidence |
|---|---|---|---|---|---|---|---|
| | | | G1–G4 | | ALLOW / REVIEW / HALT | | |

## 12. Final engagement state

```yaml
final_state: complete|monitoring|renewed|closed|cancelled|halted
open_unknowns: []
open_risks: []
completion_evidence_refs: []
realized_value_evidence_refs: []
client_decision_ref: null
closure_ledger_ref: OI-DL-YYYY-NNN
```

## 13. Commercial v1.0 connection

This checklist makes the paid-audit and implementation lifecycle repeatable, auditable, and resistant to scope drift.

## 14. References

- `framework/assessment-lifecycle.md`
- `framework/lifecycle-roadmap-map.md`
- `standards/quality-control-standard.md`
- `templates/client-intake.md`
- `templates/onboarding-checklist.md`