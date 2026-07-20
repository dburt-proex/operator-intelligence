# Governed Implementation Roadmap Template

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed commercial v1.0 working template

## 1. Purpose

Use this template to sequence validation, implementation, optimization, and closure decisions after recommendation and package-routing review.

A roadmap is a governed decision artifact. It is not implementation authorization and does not guarantee dates or outcomes.

## 2. Roadmap metadata

| Field | Value |
|---|---|
| Roadmap ID | `OI-ROAD-YYYY-NNN` |
| Client / assessment | |
| Roadmap version | |
| Supersedes | |
| Methodology version | |
| Prepared date | |
| Evidence snapshot date | |
| Publication state | `internal_only` / `official` / `provisional` / `range_only` / `blocked` |
| QC reference | |
| Roadmap owner | |
| Decision authority | |
| DecisionLedger reference | |
| Implementation authorization | `false` unless separately granted |

## 3. Scope and boundaries

**Primary objective**  
[Evidence-bound operating-state objective.]

**Included scope**

- 

**Excluded scope**

- 

**Material unknowns**

- 

**Blocked conditions**

- 

## 4. Sequencing rules

- Every item traces to evidence, a governed finding, a recommendation or validation requirement, and a DecisionLedger record.
- Package eligibility is explicit before package assignment.
- Exactly one primary package is required only for package-eligible work.
- Phase 0 contains validation/access work and cannot authorize implementation.
- Phases 1–5 follow root condition and dependency state.
- Priority or commercial attractiveness cannot bypass prerequisites.
- Roadmap approval and publication do not authorize implementation.
- Deliverable existence does not prove completion.
- Completion and realized-value validation remain separate.

## 5. Roadmap register

| Item ID | Recommendation / validation ref | Package eligibility | Primary package | Phase | Rank | Status | Review state | Owner | Authority | Dependencies | Acceptance evidence | Implementation authorized | Ledger ref |
|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|
| OI-RM-YYYY-NNN | | | | 0–5 | | | | | | | | false | |

Allowed status values: `proposed`, `validation_required`, `approved`, `blocked`, `authorized`, `in_progress`, `complete`, `monitoring`, `deferred`, `rejected`, `cancelled`.

## 6. Phase 0 — Validation and Access

**Purpose:** Resolve material evidence, access, authority, privacy, scope, eligibility, or control gaps before implementation sequencing.

| Item ID | Condition | Required evidence / decision | Access or authority needed | Owner | Exit condition | State | Ledger ref |
|---|---|---|---|---|---|---|---|
| | | | | | | `validation_required` / `blocked` | |

Rules:

- `primary_package_id` may be null.
- `implementation_authorized` remains false.
- Exit requires a new or superseding recommendation/roadmap decision.

## 7. Phase 1 — Quick Wins

**Purpose:** Correct verified critical friction, accuracy, access, or buyer-path failures with bounded scope.

| Item ID | Action | Root finding | Package | Prerequisites | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 8. Phase 2 — Growth Foundation

**Purpose:** Establish service, proof, local presence, content, offer, and conversion foundations.

| Item ID | Action | Root finding | Package | Dependencies | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 9. Phase 3 — Automation and Reporting

**Purpose:** Standardize workflows, ownership, system-of-record use, follow-up, measurement, and reporting.

| Item ID | Action | Workflow / metric | Package | Control prerequisites | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 10. Phase 4 — Governed AI Enablement

**Purpose:** Introduce bounded AI assistance only after workflow, data, privacy, human review, escalation, logging, QA, and failure controls pass.

| Item ID | Bounded use case | Package | Control refs | Review state | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|---|
| | | | | `ALLOW` / `REVIEW` / `HALT` | | | | |

Any unresolved `HALT` blocks dependent AI implementation.

## 11. Phase 5 — Optimization and Renewal

**Purpose:** Use measured implementation and adoption evidence to govern optimization, maintenance, expansion, renewal, or closure.

| Item ID | Decision | Evidence window | Existing package / renewed scope | Owner | Acceptance or closure criteria | Realized-value evidence | State |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Phase 5 does not create a new default package or imply that outcomes were achieved.

## 12. Start authorization gate

Before any item moves to `in_progress`, verify:

- separate implementation authorization reference resolves
- authorized scope and exclusions are recorded
- owner accepts responsibility
- access and prerequisites pass
- no unresolved `HALT` applies
- rollback, recovery, or escalation requirements are defined where material
- work remains inside the authorized package or validation boundary

## 13. Measurement plan

| Item ID | Measure type | Metric definition | Source | Baseline state | Review window | Owner | Decision triggered | Limitation |
|---|---|---|---|---|---|---|---|---|
| | implementation / adoption / leading indicator / business outcome | | | known / unknown | | | | |

No traffic, ranking, lead, conversion, savings, revenue, market-share, or ROI claim may exceed validated baseline and post-implementation evidence.

## 14. Change control

| Review point | Decision | Evidence reviewed | Version / supersession effect | Owner | Ledger ref |
|---|---|---|---|---|---|
| | advance / hold / validate / halt / complete / monitor / renew / close | | | | |

Material changes require versioning and a superseding DecisionLedger event. Silent resequencing is prohibited.

## 15. Release checklist

- [ ] Source chains resolve.
- [ ] Package eligibility is explicit.
- [ ] Exactly one primary package exists only for eligible work.
- [ ] Phase 0 and phases 1–5 are correctly used.
- [ ] Sequence respects dependencies.
- [ ] Unknowns and blockers remain visible.
- [ ] Owners, authorities, acceptance criteria, and target windows are explicit.
- [ ] Phase 4 controls pass where applicable.
- [ ] Roadmap approval and implementation authorization remain separate.
- [ ] Completion and realized-value evidence remain separate.
- [ ] Client language contains no unsupported outcome or timeline certainty.
- [ ] QC and DecisionLedger references resolve.

## 16. Commercial v1.0 connection

This template turns governed recommendations into a repeatable, client-safe implementation sequence with explicit validation, ownership, authorization, acceptance, monitoring, and closure controls.

## 17. References

- `standards/roadmap-standard.md`
- `standards/package-routing-standard.md`
- `standards/ai-readiness-standard.md`
- `standards/quality-control-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/recommendation-register.md`
- `templates/proposal.md`