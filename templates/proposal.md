# Governed Implementation Proposal Template

## 1. Proposal control

| Field | Value |
|---|---|
| Client | [Client name] |
| Proposal ID | [PROP-YYYY-NNN] |
| Assessment/report version | [Version] |
| Publication state | [official / provisional / range_only] |
| Weighted evidence coverage | [Percent] |
| Prepared by | Drew D. Burt |
| Prepared date | [YYYY-MM-DD] |
| Valid through | [YYYY-MM-DD or stated review condition] |
| DecisionLedger references | [Ledger IDs] |
| Implementation authorization | [not_requested / pending / approved / denied / halted] |

> This proposal converts approved assessment recommendations into bounded implementation work. It does not increase the certainty of the underlying evidence, authorize work by itself, or guarantee business outcomes.

## 2. Executive objective

[State the verified operating condition, the approved implementation objective, and the decision this proposal enables. Use evidence-supported language only.]

### Client-safe objective statement

> Based on the assessment evidence available as of [snapshot date], this proposal addresses [verified condition] through [primary package]. The work is designed to establish [observable capability or control]. Outcome performance will require separate measurement after implementation.

## 3. Governing assessment basis

| Finding ID | Verified condition | Confidence | Evidence IDs | Recommendation ID | Gate |
|---|---|---:|---|---|---|
| [F-###] | [Condition] | [high / medium / low / unknown] | [E-###] | [R-###] | [ALLOW / REVIEW / HALT] |

### Material unknowns and blockers

| ID | Condition | Effect on scope | Required validation | Owner | Gate |
|---|---|---|---|---|---|
| [U-###] | [Unknown or blocked condition] | [Effect] | [Validation action] | [Owner] | [REVIEW / HALT] |

Rules:

- Unknown and blocked conditions remain visible and are not converted into failures.
- `HALT` conditions block dependent work until a superseding DecisionLedger record resolves them.
- Proposal scope may not rely on unpublished, suppressed, or unsupported findings.

## 4. Selected package and routing

| Field | Value |
|---|---|
| Primary package | [Registered package name] |
| Package routing reason | [Verified root condition and routing rationale] |
| Secondary references | [Reference-only packages, if applicable] |
| Roadmap phase | [Phase 1 / Phase 2 / Phase 3 / Phase 4] |
| Dependency IDs | [Recommendation, package, or roadmap IDs] |
| Package approval state | [pending / approved / denied / halted] |

Every recommendation included below must have exactly one primary package. Secondary references cannot duplicate ownership or billing.

## 5. Authorized scope of work

| Work item ID | Recommendation ID | Deliverable or action | Acceptance criterion | Acceptance evidence | Owner | Gate |
|---|---|---|---|---|---|---|
| [WI-###] | [R-###] | [Bounded work] | [Observable pass condition] | [Artifact, test, log, approval, or record] | [Owner] | [ALLOW / REVIEW / HALT] |

### Scope requirements

Each work item must:

1. Trace to an approved recommendation and DecisionLedger record.
2. Remain within the selected primary package.
3. State prerequisites and dependencies.
4. Define observable acceptance criteria.
5. Identify acceptance evidence.
6. Separate implementation completion from outcome validation.

## 6. Excluded and deferred scope

| Item | Status | Reason | Re-entry condition |
|---|---|---|---|
| [Item] | [excluded / deferred / blocked] | [Reason] | [Evidence, approval, prerequisite, or future phase] |

Unless explicitly included and authorized, the proposal excludes:

- work outside the registered primary package;
- unsupported package expansion;
- paid media spend, third-party licenses, and vendor fees;
- professional media production or brand redesign;
- custom software beyond stated scope;
- Phase 4 AI implementation before required workflow, data, privacy, review, escalation, logging, and QA controls exist;
- outcome guarantees, unsupported ROI, revenue, conversion, ranking, lead-loss, market-share, or competitor-performance claims.

## 7. Roadmap and sequencing

| Phase | Entry gate | Authorized work | Dependencies | Completion gate | Planning window |
|---|---|---|---|---|---|
| Phase 1 — Validate and stabilize | [Gate] | [Work] | [Dependencies] | [Evidence required] | [Assumption, not guarantee] |
| Phase 2 — Standardize and control | [Gate] | [Work] | [Dependencies] | [Evidence required] | [Assumption, not guarantee] |
| Phase 3 — Integrate and automate | [Gate] | [Work] | [Dependencies] | [Evidence required] | [Assumption, not guarantee] |
| Phase 4 — Governed AI enablement | [Gate] | [Work] | [Dependencies] | [Evidence required] | [Assumption, not guarantee] |

Rules:

- Priority cannot bypass prerequisites.
- Dates and windows are planning assumptions unless explicitly contracted as fixed obligations.
- Material resequencing requires review and a new or superseding DecisionLedger record.

## 8. Client responsibilities and access gates

| Requirement | Owner | Required by | Verification evidence | Effect if unavailable |
|---|---|---|---|---|
| [Account access, approval, data, asset, SME input] | [Client/operator] | [Milestone] | [Evidence] | [Delay / REVIEW / HALT / scope change] |

Client responsibilities may include:

- providing authorized access to required systems and records;
- confirming data ownership, privacy, retention, and permitted use;
- supplying accurate business information and approved assets;
- assigning decision owners and reviewers;
- reviewing deliverables within the agreed governance window;
- disclosing material constraints that affect evidence, implementation, or acceptance.

Missing access remains an unknown or blocker. It is not treated as proof that a capability does not exist.

## 9. Commercial terms

| Field | Value |
|---|---|
| Pricing model | [fixed / milestone / time-and-materials / retainer] |
| Primary package fee | [$ amount] |
| Approved optional work | [$ amount or none] |
| Third-party costs | [Excluded or listed] |
| Payment schedule | [Terms] |
| Change-control method | [Written approval and ledger update] |

Pricing reflects the authorized implementation scope, not a guarantee of financial or operational outcomes.

### Change control

A change request is required when work would alter:

- the primary package;
- findings or recommendations relied upon;
- roadmap phase or dependencies;
- implementation authorization;
- acceptance criteria;
- material timeline assumptions;
- commercial scope or fees.

No material change is effective until approved and recorded.

## 10. Measurement and outcome validation

| Measure ID | Capability or outcome | Baseline status | Collection method | Review point | Claim boundary |
|---|---|---|---|---|---|
| [M-###] | [Measure] | [verified / unknown / unavailable] | [Method] | [Date or milestone] | [What may and may not be concluded] |

Implementation completion confirms only that agreed acceptance criteria were met. Business, customer, financial, ranking, conversion, or reliability outcomes require separate baseline, observation period, and validation evidence.

## 11. Acceptance and authorization

### Proposal acceptance

Proposal acceptance confirms agreement with the commercial and implementation scope. It does not override a `REVIEW` or `HALT` gate.

| Role | Name | Decision | Date | Reference |
|---|---|---|---|---|
| Client decision owner | [Name] | [approve / reject / request change] | [YYYY-MM-DD] | [Record] |
| Delivery owner | [Name] | [accept / decline] | [YYYY-MM-DD] | [Record] |
| Governance reviewer, if required | [Name] | [approve / reject / halt] | [YYYY-MM-DD] | [Ledger ID] |

### Authorization boundary

Work may begin only when:

- the proposal is accepted;
- the relevant package and roadmap gates are approved;
- required access and prerequisites are verified;
- no unresolved `HALT` applies;
- the implementation authorization state is `approved`.

## 12. Pre-release quality-control checklist

- [ ] Assessment/report version and publication state are identified.
- [ ] Evidence coverage, confidence, unknowns, and blockers are disclosed.
- [ ] Every included finding is evidence-backed and ledger-traceable.
- [ ] Every recommendation has exactly one primary package.
- [ ] Scope is proportional to the verified condition.
- [ ] Roadmap phases and dependencies follow the canonical sequence.
- [ ] Phase 4 AI prerequisites are satisfied or explicitly blocked.
- [ ] Acceptance criteria and evidence are observable.
- [ ] Implementation completion is separated from outcome validation.
- [ ] Commercial terms do not imply unsupported ROI or outcome certainty.
- [ ] Publication approval is not presented as implementation authorization.
- [ ] Material changes require approval and DecisionLedger traceability.
- [ ] Executive language is accurate, bounded, and client-safe.
- [ ] Any failed blocking check results in `HALT`.
