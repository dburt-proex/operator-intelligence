# Governed Implementation Roadmap Template

Use this template only after recommendations have passed evidence, confidence, package-routing, and publication review. Target windows are planning fields, not guarantees.

## 1. Roadmap metadata

| Field | Value |
|---|---|
| Client | [Client name] |
| Assessment ID | [Assessment ID] |
| Roadmap version | [v0.1] |
| Prepared date | [YYYY-MM-DD] |
| Publication state | [official / provisional / range_only / blocked / internal_only] |
| Implementation authorization | [not_requested / pending / approved / limited / denied] |
| DecisionLedger record | [Ledger reference] |
| Roadmap owner | [Named owner] |
| Decision authority | [Named authority] |

## 2. Scope and operating boundaries

**Primary objective**  
[Evidence-bound objective]

**Included scope**

- [Approved package or workstream]

**Excluded scope**

- [Explicit exclusion]

**Material unknowns**

- [Unknown condition, missing evidence, and validation action]

**Blocked conditions**

- [Access, authority, privacy, safety, policy, data, technical, or control blocker]

## 3. Sequencing rules

- Every roadmap item must trace to evidence, a governed finding, an approved recommendation, one primary package, and a DecisionLedger record.
- Unknown or low-confidence conditions normally enter as `validation_required`, not implementation work.
- Higher phases cannot bypass unresolved lower-phase dependencies.
- Priority or commercial attractiveness alone cannot determine sequence.
- Implementation approval is separate from report publication approval.
- Deliverable existence alone does not prove completion.
- Business outcome validation remains separate from implementation completion.

## 4. Roadmap register

| Item ID | Recommendation | Primary package | Phase | Rank | Status | Review state | Owner | Target window | Dependencies | Acceptance evidence | Ledger ref |
|---|---|---|---:|---:|---|---|---|---|---|---|---|
| OI-RM-[YYYY]-[NNN] | [Recommendation ID] | [Package ID] | [1–4] | [1] | [proposed / validation_required / approved / blocked / in_progress / complete / deferred / rejected] | [ALLOW / REVIEW / HALT] | [Owner] | [Planning window] | [IDs] | [Evidence required] | [Ledger ID] |

## 5. Phase 1 — Quick Wins

**Purpose:** Correct verified critical friction, accuracy, access, or buyer-path failures with bounded scope.

**Entry gate**

- verified condition and current evidence
- bounded implementation scope
- owner, authority, and access confirmed
- no unresolved material dependency
- observable acceptance criteria

| Item ID | Action | Root condition | Prerequisites | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|
| [ID] | [Action] | [Finding ID] | [Prerequisites] | [Owner] | [Observable pass condition] | [Evidence ref] | [State] |

## 6. Phase 2 — Growth Foundation

**Purpose:** Establish service, proof, local presence, content, and conversion foundations required for durable growth work.

**Entry gate**

- service, location, and offer claims are supportable
- required content, access, and ownership are available
- dependent Phase 1 conditions are resolved
- scope does not exceed verified capacity or package boundaries

| Item ID | Action | Root condition | Prerequisites | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|
| [ID] | [Action] | [Finding ID] | [Prerequisites] | [Owner] | [Observable pass condition] | [Evidence ref] | [State] |

## 7. Phase 3 — Automation and Reporting

**Purpose:** Standardize workflows, ownership, system-of-record use, follow-up, measurement, and reporting.

**Entry gate**

- workflow stages, triggers, exceptions, and handoffs are documented
- owners and system of record are defined
- metric definitions and decision use are named
- access and implementation authority are confirmed
- unresolved `HALT` conditions are absent

| Item ID | Action | Workflow or metric | Prerequisites | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|
| [ID] | [Action] | [Workflow or metric] | [Prerequisites] | [Owner] | [Observable pass condition] | [Evidence ref] | [State] |

## 8. Phase 4 — Governed AI Enablement

**Purpose:** Introduce bounded AI assistance only after workflow, data, privacy, review, escalation, logging, and QA controls pass.

**Mandatory entry gate**

- bounded use case
- documented workflow and structured inputs
- approved knowledge sources
- privacy and permission controls
- allowed and blocked topics
- human review and escalation rules
- audit logging
- QA owner and cadence
- explicit `ALLOW`, `REVIEW`, or `HALT` decision

Any unresolved `HALT` blocks dependent AI implementation.

| Item ID | AI use case | Control prerequisites | Review state | Owner | Acceptance criteria | Completion evidence | State |
|---|---|---|---|---|---|---|---|
| [ID] | [Bounded use case] | [Control refs] | [ALLOW / REVIEW / HALT] | [Owner] | [Observable pass condition] | [Evidence ref] | [State] |

## 9. Validation and blocked-work register

| Item ID | Missing evidence or blocker | Why it matters | Minimum validation action | Owner | Effect on sequence | Review state |
|---|---|---|---|---|---|---|
| [ID] | [Condition] | [Decision relevance] | [Validation step] | [Owner] | [Blocked/deferred dependency] | [REVIEW/HALT] |

## 10. Measurement plan

| Item ID | Measure type | Metric definition | Source | Baseline state | Review window | Owner | Decision triggered | Limitation |
|---|---|---|---|---|---|---|---|---|
| [ID] | [implementation / adoption / leading indicator / business outcome] | [Definition] | [Source] | [Known / unknown] | [Window] | [Owner] | [Decision] | [Limitation] |

Do not promise or infer traffic, rankings, leads, close rate, savings, revenue, market share, or ROI without validated baseline and post-implementation evidence.

## 11. Review and change control

| Review point | Required decision | Evidence reviewed | Owner | Ledger record |
|---|---|---|---|---|
| [Gate or date] | [Advance / hold / validate / halt / complete] | [Evidence refs] | [Owner] | [Ledger ID] |

Reopen roadmap review when evidence, confidence, package route, scope, dependencies, phase, ownership, authority, acceptance criteria, or measurement plans materially change. Silent resequencing is prohibited.

## 12. Release checklist

- [ ] Every item has a complete evidence-to-ledger source chain.
- [ ] Exactly one primary package is assigned per recommendation.
- [ ] Phase and sequence respect prerequisites and dependencies.
- [ ] Unknowns and blocked conditions remain visible.
- [ ] Ownership, authority, access, and target windows are explicit.
- [ ] Entry and acceptance criteria are observable.
- [ ] Phase 4 controls are complete where applicable.
- [ ] Implementation completion and outcome validation are separated.
- [ ] Client language contains no unsupported outcome or timeline certainty.
- [ ] Material decisions and changes are recorded in the DecisionLedger.

## 13. Executive-safe summary

> This roadmap sequences approved work according to verified conditions, prerequisites, capacity, and governance gates. Target windows are planning assumptions rather than guarantees. Items with missing evidence, blocked access, or unresolved controls remain in validation, deferred, or halted states until the required decision evidence is available.