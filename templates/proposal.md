# Governed Implementation Proposal Template

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed commercial v1.0 proposal template

## 1. Purpose

Use this template to convert package-eligible, governed recommendations into bounded commercial scope. A proposal records the offered work and acceptance decision; it does not increase evidence certainty, override a control gate, or authorize implementation by itself.

## 2. Proposal control

| Field | Value |
|---|---|
| Proposal ID | `OI-PROP-YYYY-NNN` |
| Client / assessment ID | |
| Source report ID and version | |
| Proposal version | |
| Supersedes | |
| Methodology version | |
| Evidence snapshot date | |
| Source publication state | `official` / `provisional` / `range_only` / `blocked` |
| QC reference | |
| Prepared by / date | |
| Valid-through condition | |
| DecisionLedger refs | |
| Proposal acceptance | `pending` / `accepted` / `rejected` / `change_requested` |
| Implementation authorized | `false` unless separately granted |
| Authorization reference | |

> A blocked report or unresolved HALT cannot support dependent implementation scope.

## 3. Executive objective

[State the verified condition, bounded implementation objective, and client decision enabled.]

**Client-safe objective statement**

> Based on evidence reviewed as of [snapshot date], this proposal addresses [verified condition] through [eligible package and bounded scope]. Completion will be tested against stated acceptance criteria. Business outcomes require separate measurement.

## 4. Governing assessment basis

| Finding ID | Observation | Evidence refs | Confidence | Recommendation ID | Priority | Gate |
|---|---|---|---|---|---:|---|
| | | | | | | |

### Material unknowns and blockers

| ID | Condition | Effect on scope | Validation required | Owner | Gate |
|---|---|---|---|---|---|
| | | | | | REVIEW / HALT |

Rules:

- Unknown and blocked conditions remain visible.
- Proposal scope cannot rely on suppressed, unsupported, or unpublished findings.
- HALT blocks dependent work until superseded.
- Validation-only items remain Phase 0 and are not sold as implementation packages unless a separately defined validation scope is authorized.

## 5. Package eligibility and route

| Field | Value |
|---|---|
| Package eligibility | `eligible` / `validation_required` / `blocked` / `not_applicable` |
| Primary package | [Canonical package ID and name or None] |
| Routing reference | |
| Root condition | |
| Roadmap phase | 0–5 |
| Prerequisite package refs | |
| Dependent package refs | |
| Reference-only package refs | |
| Routing gate | `ALLOW` / `REVIEW` / `HALT` |

Exactly one primary package is required only for eligible implementation work. Secondary relationships cannot duplicate ownership, scope, or billing.

## 6. Proposed scope of work

| Work item ID | Recommendation ref | Deliverable / action | Included scope | Acceptance criteria | Acceptance evidence | Owner | Gate |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Each item must:

1. trace to a governed recommendation and ledger event
2. remain inside package and proposal boundaries
3. state prerequisites and dependencies
4. define observable acceptance criteria
5. identify completion evidence
6. separate completion from outcome validation

## 7. Excluded, deferred, and blocked scope

| Item | State | Reason | Re-entry condition |
|---|---|---|---|
| | excluded / deferred / blocked / validation_required | | |

Unless expressly included, scope excludes third-party spend, licenses, custom software, brand redesign, professional media production, work outside the primary package, Phase 4 AI implementation before controls pass, and unsupported outcome guarantees.

## 8. Roadmap and sequencing

| Phase | Purpose | Entry gate | Proposed work | Dependencies | Completion gate | Planning window |
|---:|---|---|---|---|---|---|
| 0 | Validation and Access | unresolved evidence/access/authority | validation only | | decision evidence | |
| 1 | Quick Wins | verified bounded correction | | | acceptance evidence | |
| 2 | Growth Foundation | foundation prerequisites pass | | | acceptance evidence | |
| 3 | Automation and Reporting | workflow/data/ownership defined | | | acceptance evidence | |
| 4 | Governed AI Enablement | AI control gates pass | | | acceptance evidence | |
| 5 | Optimization and Renewal | measured implementation/adoption evidence exists | | | renewal/closure decision | |

Priority cannot bypass prerequisites. Planning windows are assumptions unless explicitly contracted.

## 9. Client responsibilities and access gates

| Requirement | Owner | Required by | Verification evidence | Effect if unavailable |
|---|---|---|---|---|
| | | | | delay / REVIEW / HALT / change request |

Client responsibilities may include authorized access, accurate business information, data-use approval, assets, assigned decision owners, timely review, and disclosure of material constraints.

## 10. Commercial terms

| Field | Value |
|---|---|
| Pricing model | fixed / milestone / time-and-materials / retainer |
| Primary package fee | |
| Authorized optional scope | |
| Third-party costs | excluded / listed |
| Payment schedule | |
| Taxes / expenses | |
| Change-control method | written approval + ledger / proposal update |
| Cancellation / pause conditions | |

Pricing reflects proposed scope, not a guarantee of outcomes.

## 11. Change control

A governed change request is required when work alters package, findings relied upon, recommendations, phase, dependencies, authorization, acceptance criteria, timeline assumptions, scope, fees, privacy, data use, or control boundaries.

| Change ID | Requested change | Evidence / control effect | Scope / fee effect | Decision | Ledger ref |
|---|---|---|---|---|---|
| | | | | | |

No material change is effective until approved and recorded.

## 12. Measurement and outcome validation

| Measure ID | Capability / outcome | Baseline state | Method | Review window | Owner | Claim boundary |
|---|---|---|---|---|---|---|
| | | verified / unknown / unavailable | | | | |

Implementation completion proves only that authorized acceptance criteria were met. Realized value requires separate evidence and decision review.

## 13. Acceptance and authorization

### Proposal acceptance

Proposal acceptance confirms agreement with commercial terms and proposed scope. It does not override REVIEW or HALT and does not start work by itself.

| Role | Name | Decision | Date | Reference |
|---|---|---|---|---|
| Client decision owner | | accept / reject / change requested | | |
| Delivery owner | | accept / decline | | |
| Governance reviewer, if required | | ALLOW / REVIEW / HALT | | |

### Separate implementation authorization

Work may begin only when:

- proposal acceptance is recorded
- package and roadmap gates pass
- access, authority, and prerequisites are verified
- no unresolved HALT applies
- authorized scope and exclusions are fixed
- implementation owner accepts responsibility
- `implementation_authorized: true`
- authorization reference resolves

```yaml
implementation_authorized: false
authorization_ref: null
authorized_by: null
authorized_at: null
authorized_scope: []
blocked_scope: []
```

## 14. Pre-release QC checklist

- [ ] Source report, evidence snapshot, publication state, and methodology version resolve.
- [ ] Included findings and recommendations are governed and ledgered.
- [ ] Package eligibility is explicit.
- [ ] Exactly one primary package exists only for eligible work.
- [ ] Phase 0 and phases 1–5 are correctly used.
- [ ] Scope, exclusions, prerequisites, owners, and acceptance evidence are explicit.
- [ ] AI prerequisites pass where applicable.
- [ ] Commercial terms do not imply unsupported ROI or outcome certainty.
- [ ] Proposal acceptance and implementation authorization remain separate.
- [ ] Completion and realized-value evidence remain separate.
- [ ] Any blocking failure routes to HALT.

## 15. Commercial v1.0 connection

This template converts governed assessment decisions into sellable, bounded, auditable work without allowing commercial pressure to override evidence, package eligibility, dependencies, or authorization boundaries.

## 16. References

- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `standards/quality-control-standard.md`
- `standards/decision-ledger-standard.md`
- `templates/executive-report.md`
- `templates/recommendation-register.md`
- `templates/roadmap.md`
- `templates/package-catalog.md`