# Agentic Control Platform Readiness Protocol

Version: 0.1.0
Directive: `LD-2026-07-23-SNOW-001`
Decision owner: Buyer-designated executive or platform authority
Default control gate: `REVIEW`

## 1. Purpose

Answer one bounded question:

> Is the reviewed organization sufficiently inventoried, controlled, evidenced, owned, and operationally prepared to implement or expand an enterprise AI governance and control platform for the stated scope?

Readiness is limited to the recorded decision, estate, evidence snapshot, and review period. It is not certification, regulatory attestation, vendor endorsement, procurement approval, production approval, or proof of control effectiveness outside the reviewed sample.

## 2. Actors and authority

| Actor | Required authority | Allowed action | Prohibited action |
|---|---|---|---|
| Executive sponsor | Owns the decision and scope | Approve scope, accept limitations, make platform decision | Delegate risk acceptance without recorded authority |
| Platform owner | Owns target operating environment | Supply architecture, ownership, lifecycle, integration, and operating evidence | Represent planned controls as operating controls |
| Security / identity owner | Owns access and security decisions | Validate identities, permissions, secrets, monitoring, and response evidence | Disclose restricted evidence outside approved handling |
| AI governance lead | Owns policy and lifecycle governance | Map obligations, decisions, approvals, and inventory requirements | Treat policy existence as enforcement proof |
| Evaluator | Written assessment authority | Review authorized evidence, interview owners, run approved safe tests, record findings | Modify systems, expand scope, select a vendor, certify, or authorize implementation |
| Independent reviewer | Review authority | Challenge evidence, scoring, gates, conflicts, and decision language | Suppress unresolved material limitations |

## 3. Entry criteria

Intake requires:

- named decision and decision date or window;
- bounded agent or AI-asset portfolio;
- named sponsor, platform owner, governance owner, and security/identity owner;
- in-scope environments, workflows, data classes, integrations, and exclusions;
- evidence access and handling authority;
- safe-test authority where demonstrations are requested;
- declared vendor, implementation, or commercial conflicts;
- assessment, methodology, protocol, and DecisionLedger identifiers.

Missing decision authority, unsafe access, unbounded production testing, secret exposure, or absent evidence handling rules route to `HALT`.

## 4. Canonical seven domains

The sprint inherits the exact seven domains from the Agentic AI Governance Readiness Assessment:

| ID | Domain | Platform-readiness decision |
|---|---|---|
| `AIGR-D1` | Agent purpose and ownership | Can the platform bind assets, purposes, versions, and accountable owners to lifecycle decisions? |
| `AIGR-D2` | Data and system access | Can identity, permissions, data classes, sources, retention, and access reviews be represented and enforced? |
| `AIGR-D3` | Tool and action authority | Can allowed actions, prohibited actions, approvals, limits, containment, and least privilege be enforced? |
| `AIGR-D4` | Workflow approvals and human intervention | Are review, exception, override, escalation, and risk-acceptance routes operationally defined? |
| `AIGR-D5` | Evaluation and failure testing | Are evaluation sets, thresholds, regressions, drift signals, defects, and test owners platform-ready? |
| `AIGR-D6` | Logging, evidence, and auditability | Can material activity and decisions be correlated, retained, exported, reconstructed, and reviewed? |
| `AIGR-D7` | Deployment, monitoring, rollback, and incident response | Are release, monitoring, alert, containment, rollback, incident, and learning paths defined and exercised? |

No engagement-specific domain may be added without a recorded methodology decision. Additional considerations must map to one primary domain and may be referenced elsewhere without duplicate weighting.

## 5. Workflow and gates

| Step | Required action | Record changed | Exit gate |
|---|---|---|---|
| 1. Qualify | Confirm buyer, decision, scope, authority, independence, and exclusions | Sprint control record | `ALLOW`, `REVIEW`, or `HALT` |
| 2. Inventory | Register AI assets, owners, workflows, tools, identities, data, environments, and platforms | Estate inventory | `REVIEW` until minimum scope coverage passes |
| 3. Collect | Capture authorized records, exports, configurations, logs, demonstrations, interviews, and safe tests | Evidence register | Admission decision per source |
| 4. Map | Map evidence and controls to one primary domain and an enforcement plane | Control map | Duplicate ownership or unmapped material control requires `REVIEW` |
| 5. Assess | Assign finding state, evidence strength, confidence, severity, owner, and decision effect | Gap register | Material findings require admitted evidence |
| 6. Score | Calculate observed readiness, evidence coverage, and confidence separately | Scoring record | Publication rules in `scoring-profile.md` |
| 7. Prioritize | Sequence validation and remediation by criticality, dependency, effort, and platform decision effect | Roadmap | Owner and acceptance evidence required |
| 8. Demonstrate | Run the authorized DiffWall proof when change-time control evidence is in scope | Demonstration record | Safe, reversible, non-production test only |
| 9. Decide | Issue executive decision and reconcile the machine-readable export | Decision brief and export | Independent review and DecisionLedger event |

## 6. Control and enforcement planes

- `governance`: policy, inventory, ownership, risk, lifecycle, exception, and decision records.
- `change_time`: controls evaluated before code, configuration, model, prompt, policy, or workflow changes are accepted.
- `runtime`: identity, permission, action, monitoring, evaluation, containment, and incident controls applied while systems operate.
- `assurance`: evidence integrity, testing, auditability, review, and realized-control verification.

A governance document is not evidence that a change-time or runtime control operates. Planned configuration is not operating evidence. Each control must declare its plane and evidence state.

## 7. Decision routes

| Decision | Gate | Meaning |
|---|---|---|
| `READY` | `ALLOW` | The reviewed scope meets readiness, coverage, confidence, ownership, and critical-control conditions. Implementation still requires a separate authorization. |
| `CONDITIONAL` | `REVIEW` | Bounded remediation, validation, ownership, evidence, or dependency work is required before the platform decision can advance. |
| `NOT_READY` | `HALT` | A verified critical gap makes the proposed implementation or expansion unsafe or indefensible within scope. |
| `BLOCKED` | `HALT` | Authority, evidence integrity, access, scope, safety, or traceability prevents a defensible readiness decision. |

## 8. Failure and recovery

| Failure | Required response | Recovery evidence |
|---|---|---|
| Missing or conflicting evidence | Preserve `UNKNOWN`; route to `REVIEW` | Superseding evidence decision |
| Unauthorized or unsafe test | Stop the test and isolate affected records | Written authority and revised safe-test plan |
| Sensitive-data exposure | Stop collection, follow incident route, restrict affected evidence | Incident disposition and approved handling |
| Broken traceability | Block publication and export | Reconciled identifiers and independent review |
| Unsupported readiness or certification claim | Withdraw or supersede the artifact | Corrected language and DecisionLedger record |
| Scope expansion | Stop dependent work | Approved versioned scope |

## 9. Completion and handoff

Completion requires the ten package artifacts, reconciled identifiers, independent review, a recorded decision, and an export that validates against `export-schema.json`.

Completion does not prove implementation, adoption, control effectiveness after the snapshot, regulatory compliance, business outcomes, or realized value.
