# Operator Intelligence Template Index

Version: v0.1 commercial v1.0 index  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Canonical template registry

## 1. Purpose

This index defines the canonical templates used to qualify, assess, score, report, propose, authorize, deliver, review, and close an Operator Intelligence engagement.

Use the registered file for each record type. Do not create alternate templates that change controlled fields, package identities, publication states, roadmap phases, authorization boundaries, or DecisionLedger requirements without reopening the template completion gate.

## 2. Canonical registry

| Template | Primary role | Trigger | Governed output |
|---|---|---|---|
| `sales-notes.md` | Opportunity and qualification record | Sales/discovery conversation | Fit gate, commitments, next decision |
| `discovery-form.md` | Pre-intake context collection | Qualified prospect | Reported context and intake handoff |
| `client-intake.md` | Scope, access, evidence, authority, and data control | Assessment initiation | Intake ALLOW/REVIEW/HALT |
| `evidence-register.md` | Evidence source of truth | Evidence collection | Admitted, limited, rejected, blocked, and superseded records |
| `finding-register.md` | Governed finding control | Evidence and scoring review | Validated, blocked, suppressed, published, or closed findings |
| `recommendation-register.md` | Evidence-to-action control | Governed findings | Priority, eligibility, route, phase, and acceptance state |
| `decision-ledger.md` | Immutable material decision record | Any governed state change | Traceable decision event |
| `executive-report.md` | Canonical client decision artifact | Assessment synthesis | Published score, findings, recommendations, roadmap, decision memo |
| `contractor-report.md` | Concise owner/operator report | Executive report release | Practical assessment summary using same governed source objects |
| `roadmap.md` | Sequenced validation and implementation plan | Approved recommendations | Phase 0 and phases 1–5 roadmap items |
| `package-catalog.md` | Canonical package and scope registry | Package-eligible recommendation | Versioned package scope and delivery boundaries |
| `proposal.md` | Commercial implementation offer | Eligible package scope | Bounded commercial scope and acceptance decision |
| `onboarding-checklist.md` | Pre-start implementation control | Accepted proposal | Authority, access, prerequisites, testing, and start gate |
| `delivery-checklist.md` | End-to-end engagement control | Engagement start | Lifecycle completion evidence and closure state |
| `quality-control-checklist.md` | Executable release review | Any releasable artifact | Bounded ALLOW/REVIEW/HALT QC decision |

## 3. Record flow

```text
Sales Notes
→ Discovery Form
→ Client Intake
→ Evidence Register
→ Scoring Objects
→ Finding Register
→ Recommendation Register
→ DecisionLedger
→ Executive / Contractor Report
→ Roadmap
→ Package Catalog Scope
→ Proposal
→ Onboarding Checklist
→ Delivery Checklist
→ Completion / Monitoring / Renewal
```

The quality-control checklist applies before every material release or governed advancement.

## 4. Shared invariants

- Unknown is never zero.
- Confidence is separate from maturity and priority.
- Evidence, interpretation, assumptions, and limitations remain distinct.
- Package eligibility precedes package assignment.
- Exactly one primary package exists only for eligible work.
- Phase 0 is validation; phases 1–5 are governed roadmap states.
- QC, publication, roadmap approval, proposal acceptance, and implementation authorization are separate.
- Completion evidence and realized-value evidence are separate.
- Approved history is superseded, not overwritten.
- Unsupported outcome claims are prohibited.
- Material state changes require DecisionLedger records.

## 5. Template selection rules

1. Use `discovery-form.md` for pre-engagement context; do not treat it as evidence.
2. Use `client-intake.md` to authorize assessment scope and testing boundaries.
3. Use `executive-report.md` as the publication authority and `contractor-report.md` as its bounded companion.
4. Use `package-catalog.md` only after package eligibility is governed.
5. Use `proposal.md` to offer scope; use `onboarding-checklist.md` and a separate authorization event before start.
6. Use `delivery-checklist.md` across the lifecycle and retain completion/closure evidence.
7. Use `quality-control-checklist.md` against exact artifact versions.

## 6. Commercial v1.0 connection

This registry makes the client-delivery system repeatable and prevents uncontrolled alternate forms from weakening the assessment architecture.

## 7. References

- `standards/completion-status.md`
- `scoring/completion-status.md`
- `framework/lifecycle-roadmap-map.md`