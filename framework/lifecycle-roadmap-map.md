# Operator Intelligence Lifecycle-Roadmap Map

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file maps the Operator Intelligence engagement lifecycle to evidence states, decision states, implementation packages, roadmap phases, approvals, acceptance criteria, and post-implementation review.

It prevents assessments from becoming disconnected sequences in which scoring, reporting, proposals, and implementation use different states or sequencing rules.

## v1.0 connection

Commercial v1.0 requires one governed engagement path from qualification through monitoring and renewal.

This map strengthens v1.0 readiness by providing:

- one lifecycle state model
- entry and exit criteria for every engagement stage
- explicit handoffs between evidence, scoring, findings, recommendations, proposals, and delivery
- roadmap phase eligibility rules
- approval and escalation points
- completion and rollback states
- post-implementation measurement and learning
- DecisionLedger traceability

## Source alignment

This map coordinates:

- `framework/assessment-lifecycle.md`
- `framework/finding-index.md`
- `framework/risk-impact-model.md`
- `framework/effort-model.md`
- `framework/opportunity-model.md`
- `framework/recommendation-index.md`
- `framework/roi-framework.md`
- `templates/decision-ledger.md`
- `templates/roadmap.md`
- `templates/executive-report.md`
- `templates/proposal.md`

Domain libraries remain authoritative for finding content. Package scope remains authoritative in the recommendation index.

## Core lifecycle principle

No stage advances because a document exists.

A stage advances only when its required evidence, decisions, owners, approvals, and outputs satisfy the exit gate.

## Canonical lifecycle states

| State ID | State | Primary purpose | Required exit evidence |
|---|---|---|---|
| `OI-LC-01` | Qualification | Confirm fit, authority, need, and implementation willingness | Fit decision, known exclusions, access risks, commercial next step |
| `OI-LC-02` | Intake | Capture business context and internal constraints | Complete intake or explicit unknowns and validation plan |
| `OI-LC-03` | Surface Mapping | Inventory buyer-facing and operating surfaces | Surface inventory with access and evidence status |
| `OI-LC-04` | Evidence Collection | Gather sufficient proof for scoring and findings | Evidence log, source refs, coverage gaps, confidence limits |
| `OI-LC-05` | Scoring | Convert evidence into criterion and category scores | Score objects, unknown handling, confidence, normalization record |
| `OI-LC-06` | Finding Resolution | Convert observations into governed findings | Finding IDs, root domains, dependencies, validation states |
| `OI-LC-07` | Risk and Opportunity Synthesis | Interpret business significance and potential value | Risk-impact records, opportunities, effort, eligibility states |
| `OI-LC-08` | Recommendation Routing | Select controlled implementation paths | Recommendation objects, packages, prerequisites, blocked conditions |
| `OI-LC-09` | Report and Roadmap Build | Produce client-ready conclusions and sequencing | Report draft, roadmap, acceptance and measurement plan |
| `OI-LC-10` | Delivery and Decision | Present findings and secure explicit client decisions | Accepted, rejected, deferred, or validation decisions |
| `OI-LC-11` | Proposal and Onboarding | Convert accepted recommendations into governed scope | Signed scope, owners, access, schedule, approvals, change rules |
| `OI-LC-12` | Implementation | Deliver approved package work | Acceptance evidence, issue log, approvals, completion state |
| `OI-LC-13` | Monitoring and Realized Value | Measure adoption, outcomes, risk reduction, and value | Baseline comparison, QA review, realized-value record |
| `OI-LC-14` | Renewal or Closure | Decide next cycle, maintenance, expansion, or closure | Closeout, next roadmap, ownership transfer, archived ledger |

## Lifecycle status vocabulary

| Status | Meaning |
|---|---|
| `not_started` | No governed work has begun |
| `in_progress` | Required work is active |
| `validation_required` | Material evidence or authority is missing |
| `review_required` | Human decision or approval is required |
| `blocked` | A gate prevents advancement |
| `approved` | Required authority accepted the stage output |
| `complete` | Exit criteria and evidence are satisfied |
| `deferred` | Valid work is intentionally postponed |
| `cancelled` | Work will not proceed |
| `monitoring` | Implementation is complete and outcomes are under review |
| `closed` | Engagement or workstream is formally concluded |

## Stage map

### OI-LC-01 — Qualification

Required inputs:

- industry and location
- service-area business model
- visible business presence
- stated concern or growth objective
- decision-maker participation
- willingness and capacity to implement
- budget or commercial-fit signal
- known access constraints

Gate decisions:

- `qualify`
- `qualify_with_conditions`
- `defer`
- `decline`

Do not advance when:

- the requested work is outside the product scope
- the business cannot identify any valid service or offer
- implementation capacity is absent and no readiness work is accepted
- required authority is unavailable
- the client requests unsupported guarantees or manipulative practices

Exit outputs:

- qualification record
- exclusions and conditions
- preliminary access list
- intake authorization

### OI-LC-02 — Intake

Required outputs:

- business identity and contact data
- service area
- core and priority services
- offer and sales-process context
- lead sources and systems
- known competitors
- growth objectives
- capacity and delivery constraints
- CRM, analytics, GBP, and tool access status
- known financial inputs, clearly sourced
- unknowns and validation owners

Exit gate:

Intake may pass with unknowns only when each material unknown has a validation state, owner, and next action.

### OI-LC-03 — Surface Mapping

Required surfaces include, when relevant:

- website and landing pages
- Google Business Profile
- review platforms
- social profiles
- directories
- ads
- forms, phone, chat, booking, and email paths
- CRM and lead tracker
- estimate and proposal workflow
- analytics and Search Console
- automation tools
- AI tools and knowledge sources

Exit outputs:

- canonical surface inventory
- URLs or system identifiers
- owner and access status
- in-scope and excluded surfaces
- evidence-collection plan

### OI-LC-04 — Evidence Collection

Required controls:

- evidence type
- source
- observation date
- evaluator
- related criterion or domain
- access or test limitations
- evidence quality
- client confirmation where required

Exit gate:

A domain may be scored only when evidence meets its threshold or is explicitly routed to unknown handling.

### OI-LC-05 — Scoring

Required outputs:

- criterion scores
- criterion confidence
- category scores
- category coverage
- unknown-data treatment
- normalized weights or score range
- Operator Score
- score assumptions and exclusions

Blocked when:

- unknown data is silently scored as failure
- weights do not reconcile
- confidence is missing
- the same signal is counted twice
- category boundaries are unclear

### OI-LC-06 — Finding Resolution

Required outputs:

- canonical finding ID
- root domain
- observation
- evidence refs
- criteria refs
- interpretation
- impact language
- confidence
- validation state
- dependencies
- DecisionLedger reference

Use `framework/finding-index.md` for duplicate and conflict resolution.

### OI-LC-07 — Risk and Opportunity Synthesis

Required outputs:

- primary impact class
- impact, likelihood, and reach
- risk exposure
- response type
- opportunity state
- effort record
- strategic fit
- capacity and readiness checks
- qualitative or financial value eligibility

Blocked when:

- urgency is exaggerated
- evidence strength is treated as severity
- opportunity value is invented
- effort ignores governance or client dependencies
- capacity is not considered

### OI-LC-08 — Recommendation Routing

Required outputs:

- recommendation ID
- primary package ID
- dependent package IDs
- prerequisites
- included and excluded scope
- roadmap phase
- acceptance criteria
- measurement plan
- implementation owner
- status and rationale

Decision states:

- `recommend`
- `defer`
- `validate`
- `monitor`
- `block`

### OI-LC-09 — Report and Roadmap Build

Report admission requirements:

- all client-facing findings passed report gates
- score limitations are visible
- top strengths and constraints are evidence-backed
- recommendations map to governed packages
- roadmap respects dependencies and capacity
- investment and value language follows ROI controls
- next action is explicit

Roadmap initiatives must use the canonical roadmap object defined below.

### OI-LC-10 — Delivery and Decision

Each recommendation receives one client decision:

- `accepted`
- `accepted_with_conditions`
- `deferred`
- `rejected`
- `validation_required`
- `no_decision`

Delivery must record:

- decision-maker
- date
- questions and objections
- changed assumptions
- approved priorities
- rejected or deferred work
- next action and owner

No silence may be recorded as acceptance.

### OI-LC-11 — Proposal and Onboarding

Required before implementation:

- approved recommendation and package
- complete scope
- exclusions
- acceptance criteria
- client and implementation owners
- required access
- data and content responsibilities
- approval workflow
- change-control rule
- schedule state
- commercial authorization
- privacy, legal, security, or AI approvals when applicable

### OI-LC-12 — Implementation

Implementation states:

- `ready`
- `in_progress`
- `review`
- `blocked`
- `accepted`
- `rework_required`
- `rolled_back`
- `complete`

Required controls:

- issue and decision log
- version or change record
- testing evidence
- client approvals
- acceptance evidence
- unresolved limitations
- rollback or recovery plan where material

### OI-LC-13 — Monitoring and Realized Value

Required outputs:

- adoption status
- operational metrics
- QA results
- risk reduction
- baseline comparison
- attribution state
- modeled-versus-realized value review
- corrective actions
- maintenance owner

Do not report realized ROI when the ROI framework gates do not pass.

### OI-LC-14 — Renewal or Closure

Closure requirements:

- completed and incomplete scope
- accepted deliverables
- unresolved risks and ownership
- maintenance requirements
- access transfer or removal
- final measurement state
- archived DecisionLedger
- next-quarter or renewal recommendation

## Canonical roadmap object

```yaml
roadmap_item_id: OI-RM-YYYY-NNN
source_findings: []
opportunity_id: OI-OPP-YYYY-NNN
recommendation_ref: OI-REC-YYYY-NNN
primary_package_id: OI-PKG-XXX-001
title: ""
objective: ""
roadmap_phase: phase_1
lifecycle_entry_state: OI-LC-08
status: proposed
decision_state: recommend
priority: high
risk_level: high
effort_ref: OI-EFF-YYYY-NNN
prerequisites: []
dependencies: []
blocked_by: []
implementation_owner: ""
client_owner: ""
required_inputs: []
access_requirements: []
acceptance_criteria: []
measurement_plan: []
approvals_required: []
target_window: ""
completion_evidence: []
ledger_ref: OI-DL-YYYY-NNN
```

## Roadmap phases

| Phase | Purpose | Typical package eligibility | Exit condition |
|---|---|---|---|
| Phase 1 — Quick Wins | Correct blocked actions, factual inconsistency, high-confidence friction, and urgent control gaps | Website Conversion Fix Pack and narrow corrective work | Buyer path or control is tested and accepted |
| Phase 2 — Growth Foundation | Build discoverability, proof, service coverage, local relevance, and buyer support | Local SEO, GBP, Trust, and coordinated website work | Foundation assets exist, align, and are measurable |
| Phase 3 — Automation and Reporting | Establish CRM, lead ownership, stages, follow-up, data, attribution, dashboards, and review systems | CRM, Review Generation, Operator Dashboard | Workflow and reporting acceptance criteria pass |
| Phase 4 — Governed AI Enablement | Add bounded AI assistance after workflow, data, knowledge, privacy, review, escalation, logging, and QA gates pass | Governed AI Intake Assistant | Pilot or implementation passes control and QA review |
| Phase 5 — Optimization and Renewal | Improve validated systems using measured evidence | Existing packages or approved new scope | Next-cycle roadmap is approved or engagement is closed |

Phase 5 is an engagement-management phase, not a new implementation package.

## Phase eligibility rules

1. Phase reflects dependency order, not marketing category.
2. A later-phase item may begin early only when all prerequisites pass and the DecisionLedger records the reason.
3. A Phase 1 fix does not automatically outrank a severe Phase 3 control gap.
4. Growth expansion must not precede offer, capacity, lead-handling, or measurement readiness when expansion would amplify failure.
5. AI work cannot precede required workflow, data, privacy, review, escalation, logging, and QA controls.
6. Unknown effort or access may require validation before assignment to a delivery window.
7. Roadmap phase is not a guarantee of calendar completion.

## Roadmap admission gate

A roadmap item is admissible only when:

- its source finding exists
- evidence and confidence are explicit
- root domain and dependencies are resolved
- risk and opportunity records exist
- package eligibility passes
- effort is evaluated
- owner is named
- prerequisites and blockers are visible
- acceptance criteria are testable
- measurement is defined
- client approval state is known
- DecisionLedger traceability exists

## Change-control rules

A roadmap item must be re-evaluated when:

- scope changes
- a dependency fails
- access is unavailable
- capacity changes
- new evidence changes confidence or priority
- package eligibility changes
- legal, privacy, safety, policy, or AI risk emerges
- client priorities change
- cost or effort changes materially

Changes require:

- prior and new state
- reason
- impact on phase, scope, effort, value, and acceptance
- approval owner
- DecisionLedger update

## Completion rules

A roadmap item is complete only when:

- required deliverables exist
- acceptance criteria pass
- completion evidence is attached
- unresolved limitations are disclosed
- ownership is transferred
- monitoring or maintenance is assigned
- DecisionLedger and status are updated

Publication, configuration, or handoff alone is not proof of successful completion.

## Usage instructions

1. Open the assessment lifecycle and identify the current state.
2. Confirm the prior stage exit gate passed.
3. Produce the required state outputs.
4. Apply governance gates and decision states.
5. Build roadmap items only after recommendation routing.
6. Record owners, prerequisites, acceptance, and measurement.
7. Update the DecisionLedger at every material decision.
8. Reapply the map when evidence, scope, priority, or risk changes.
9. Close each workstream with acceptance and monitoring evidence.

## Completion check

Before an engagement or workstream advances, confirm:

- current lifecycle state is explicit
- required inputs are available or governed as unknown
- exit evidence is complete
- decision authority is recorded
- blocked conditions are resolved or disclosed
- roadmap phase and package are eligible
- acceptance and measurement are defined
- DecisionLedger is current
