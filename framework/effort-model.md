# Operator Intelligence Effort Model

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how Operator Intelligence estimates implementation effort without confusing technical complexity, client readiness, calendar duration, package price, or business value.

The effort model converts a governed recommendation into a scoped implementation burden that can be compared, sequenced, proposed, assigned, and reviewed consistently.

## v1.0 connection

Commercial v1.0 requires recommendations that are not only evidence-backed, but also realistic to implement.

This model strengthens v1.0 readiness by providing:

- one effort scale across all implementation packages
- separation between implementation burden and calendar duration
- explicit client-input and access dependencies
- effort-inverse values for prioritization
- change, migration, testing, and governance burden controls
- package-scoping inputs for proposals and roadmaps
- DecisionLedger traceability

## Inputs and triggers

Apply this model after:

- a finding has passed the finding index
- risk and impact have been evaluated
- a primary package route has been identified
- prerequisites and dependent packages are known
- the intended implementation outcome is defined

Reapply it when:

- scope changes
- access becomes available or is removed
- client responsibilities change
- a dependency is resolved
- a package is split or combined
- testing or governance requirements increase

## Outputs and deliverables

A valid effort evaluation produces:

- raw effort score
- effort level
- effort inverse
- delivery shape
- estimated implementation owners
- client inputs
- access requirements
- dependencies
- migration needs
- testing and acceptance burden
- governance burden
- duration state
- confidence level
- DecisionLedger rationale

## Core principles

1. Effort is not business value.
2. Effort is not package price.
3. Effort is not calendar duration.
4. High effort does not make an initiative low priority when risk, impact, or strategic need is material.
5. Low effort does not make an initiative worthwhile when evidence or impact is weak.
6. Unknown access, data, scope, ownership, or approval conditions must reduce effort confidence.
7. Client delay must not be represented as consultant implementation effort.
8. Reusable templates may reduce delivery effort but do not eliminate client-specific validation.
9. Governance, testing, migration, and adoption work are implementation effort, not optional overhead.
10. Effort estimates must describe assumptions and exclusions.

## Canonical effort object

```yaml
effort_ref: OI-EFF-YYYY-NNN
recommendation_ref: OI-REC-YYYY-NNN
primary_package_id: OI-PKG-XXX-001
scope_summary: ""
complexity_score: 1
change_reach_score: 1
dependency_score: 1
data_migration_score: 1
validation_score: 1
governance_score: 1
raw_effort_score: 6
effort_level: low
effort_inverse: 5
delivery_shape: focused_change
implementation_owners: []
client_inputs: []
access_requirements: []
dependencies: []
assumptions: []
exclusions: []
duration_state: estimate_pending
confidence: unknown
ledger_ref: OI-DL-YYYY-NNN
```

## Effort dimensions

Score each dimension from 1 to 5.

### 1. Implementation complexity

| Score | Definition |
|---:|---|
| 1 | Direct configuration, copy, field, page, or rule change using known systems |
| 2 | Several coordinated changes inside one established system |
| 3 | Multi-step implementation requiring design, configuration, or integration work |
| 4 | Cross-system implementation with material architecture, migration, or workflow design |
| 5 | Program-level change with substantial custom logic, operating redesign, or controlled rollout |

### 2. Change reach

| Score | Definition |
|---:|---|
| 1 | One page, field, template, message, or configuration |
| 2 | One service, channel, profile, or workflow step |
| 3 | One complete buyer, sales, review, or reporting journey |
| 4 | Several channels, teams, systems, or connected journeys |
| 5 | Business-wide operating or governance change |

### 3. Dependency load

| Score | Definition |
|---:|---|
| 1 | No material prerequisite beyond normal approval |
| 2 | One known dependency with clear owner and path |
| 3 | Several coordinated dependencies or one uncertain prerequisite |
| 4 | Multiple external, client, vendor, data, or package dependencies |
| 5 | Delivery cannot be scoped reliably until major prerequisites are resolved |

### 4. Data and migration burden

| Score | Definition |
|---:|---|
| 1 | No migration or only a small verified input set |
| 2 | Light cleanup, structured import, or content transfer |
| 3 | Moderate data cleanup, mapping, deduplication, or source reconciliation |
| 4 | Large or inconsistent data set, multi-source migration, or material history requirements |
| 5 | Sensitive, high-volume, poorly structured, or high-risk migration with rollback needs |

### 5. Validation and acceptance burden

| Score | Definition |
|---:|---|
| 1 | Simple visual or functional confirmation |
| 2 | Standard checklist across a small number of cases |
| 3 | Multi-device, multi-path, workflow, data, or stakeholder acceptance testing |
| 4 | Repeated test cases, exception handling, reconciliation, or performance verification |
| 5 | Controlled pilot, staged rollout, audit evidence, rollback, or formal acceptance process |

### 6. Governance burden

| Score | Definition |
|---:|---|
| 1 | Normal approval and change record |
| 2 | Named owner, access control, and routine documentation |
| 3 | Policy, escalation, audit, privacy, quality, or change-control requirements |
| 4 | Sensitive customer actions, permissions, cross-role approvals, or recurring QA |
| 5 | Safety, legal, privacy, financial commitment, AI execution, or irreversible-action controls |

## Raw effort calculation

```text
Raw Effort Score =
Complexity
+ Change Reach
+ Dependency Load
+ Data and Migration Burden
+ Validation and Acceptance Burden
+ Governance Burden
```

Possible range: 6–30.

| Raw score | Effort level | Meaning |
|---:|---|---|
| 6–10 | Low | Focused change with limited coordination and straightforward acceptance |
| 11–16 | Moderate | Defined project requiring several coordinated implementation steps |
| 17–22 | High | Cross-domain or cross-system initiative with material dependencies and testing |
| 23–26 | Very High | Large implementation requiring staged delivery, migration, or substantial governance |
| 27–30 | Program | Business-wide or high-control transformation that should be split into governed workstreams |

## Effort inverse

Opportunity and recommendation priority use effort inverse, where easier work receives a higher convenience value.

| Effort level | Effort inverse |
|---|---:|
| Low | 5 |
| Moderate | 4 |
| High | 3 |
| Very High | 2 |
| Program | 1 |

Effort inverse is a prioritization input only. It must never override severe risk, blocked buyer paths, legal or privacy escalation, or prerequisite sequencing.

## Delivery shapes

| Delivery shape | Use when |
|---|---|
| `focused_change` | One narrow page, configuration, template, field, or control can resolve the issue |
| `package_project` | One canonical implementation package can resolve the primary condition |
| `multi_package_initiative` | Several packages must coordinate around one outcome |
| `prerequisite_build` | Readiness work must occur before the primary recommendation is eligible |
| `controlled_pilot` | Limited implementation is required to validate behavior before expansion |
| `program_workstream` | Scope must be divided into phases, owners, gates, and acceptance reviews |

## Duration controls

Do not convert effort directly into dates.

Calendar duration depends on:

- access availability
- client response time
- content and data readiness
- external vendors
- approval cadence
- implementation capacity
- testing windows
- seasonality or operating constraints
- dependency completion

Use one duration state:

| State | Meaning |
|---|---|
| `estimate_ready` | Scope, dependencies, access, owner, and acceptance criteria are sufficient for scheduling |
| `estimate_pending` | Material planning inputs are missing |
| `blocked` | A prerequisite, access, policy, or control condition prevents scheduling |
| `pilot_only` | Only a bounded validation period can be scheduled |

## Client-dependency controls

List client responsibilities separately from implementation effort.

Common client inputs include:

- service and priority validation
- access credentials
- analytics, CRM, or financial records
- pricing and policy confirmation
- credentials, guarantees, and warranty scope
- photos, reviews, project history, and proof assets
- approval of copy, workflows, fields, and rules
- staff availability for testing and training

A recommendation with unresolved client dependencies cannot receive high effort confidence.

## Package baseline guidance

These are starting shapes, not fixed estimates.

| Package | Typical delivery shape | Common effort drivers |
|---|---|---|
| Website Conversion Fix Pack | Focused change or package project | page count, mobile behavior, form logic, approval speed |
| Local SEO Expansion Pack | Package project | service count, location scope, content readiness, technical access |
| Google Business Authority Pack | Focused change or package project | profile access, duplicate issues, proof assets, review workflow |
| Trust Proof System | Package project | proof inventory, photography, policy validation, placement scope |
| CRM and Follow-Up System | Multi-package initiative | process definition, migration, fields, integrations, adoption |
| Review Generation System | Package project | completion trigger, CRM access, templates, tracking, escalation |
| Operator Dashboard Pack | Multi-package initiative | analytics access, definitions, attribution, reconciliation, cadence |
| Governed AI Intake Assistant | Controlled pilot or program workstream | workflow readiness, data, knowledge, review, privacy, logging, QA |

## Effort confidence

| Confidence | Use when |
|---|---|
| High | Scope, systems, access, dependencies, owners, data, and acceptance criteria are verified |
| Medium | Core scope is known, but one or more implementation conditions remain partially unverified |
| Low | Estimate depends on assumptions, inaccessible systems, unknown data, unclear ownership, or incomplete requirements |
| Unknown | No defensible implementation estimate can be made |

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Scope Gate | Included outcome, assets, systems, and exclusions are defined | Effort is estimated from a package name alone | Clarify scope |
| Dependency Gate | Prerequisites and external dependencies are listed | Hidden dependencies may change delivery materially | Lower confidence or block scheduling |
| Access Gate | Required systems and permission levels are known | Access is assumed | Mark `estimate_pending` |
| Client Input Gate | Required client records, approvals, and content are listed | Delivery depends on undocumented client work | Add dependency record |
| Migration Gate | Data source, quality, volume, and rollback need are known | Migration burden is ignored | Re-score effort |
| Validation Gate | Test and acceptance method is defined | Completion is subjective | Add acceptance criteria |
| Governance Gate | Privacy, policy, escalation, audit, and approval controls are included | Control work is excluded from effort | Re-score or block |
| Duration Gate | Dates are based on readiness and capacity, not effort score alone | Raw effort is presented as a schedule | Remove date claim |
| Ledger Gate | Effort rationale is recorded | Estimate cannot be audited | Block proposal admission |

## Priority use

Effort participates in prioritization only after evidence, impact, risk, and eligibility gates pass.

Use:

```text
Effort Inverse = convenience input
```

Do not use:

```text
Low effort = automatic recommendation
High effort = automatic deferral
```

A high-impact, high-effort initiative may remain a top roadmap priority but should be decomposed into prerequisites, phases, and acceptance gates.

## DecisionLedger requirements

```yaml
effort_ref: OI-EFF-YYYY-NNN
recommendation_ref: OI-REC-YYYY-NNN
raw_effort_score: 0
effort_level: unknown
effort_inverse: 0
delivery_shape: ""
implementation_owners: []
client_inputs: []
access_requirements: []
dependencies: []
assumptions: []
exclusions: []
acceptance_requirements: []
duration_state: estimate_pending
confidence: unknown
rationale: ""
```

## Usage instructions

1. Confirm the governed recommendation and primary package.
2. Define the implementation outcome and exclusions.
3. Score all six effort dimensions.
4. Calculate raw effort and effort level.
5. Assign effort inverse.
6. Identify delivery shape.
7. Separate client inputs from implementation work.
8. Document access, migration, testing, and governance conditions.
9. Assign duration state and confidence.
10. Record the effort object in the DecisionLedger.

## Completion check

Before an effort estimate enters a roadmap or proposal, confirm:

- scope is explicit
- package eligibility has passed
- prerequisites are visible
- client inputs are separated
- access is known or marked pending
- migration is included where relevant
- acceptance criteria are defined
- governance work is included
- duration is not inferred from score alone
- confidence and assumptions are disclosed
- DecisionLedger traceability exists
