# Assessment Lifecycle

Version: v0.2 governed lifecycle alignment  
Stage alignment: Stage 2 — `framework/`  
Status: Controlled foundation for commercial v1.0

## Purpose

This file defines the mandatory operating sequence for an Operator Intelligence engagement. It is the concise execution contract for assessors, reviewers, report builders, and implementation owners.

The detailed state definitions, required fields, roadmap object, acceptance rules, and rollback controls remain authoritative in `framework/lifecycle-roadmap-map.md`.

## Lifecycle authority

When lifecycle documents appear to conflict, apply this order:

1. `framework/lifecycle-roadmap-map.md` for state definitions, gates, and handoffs
2. this file for the required operating sequence and global invariants
3. domain standards for category-specific evaluation rules
4. templates for record structure and client-facing presentation

No template, playbook, or delivery preference may bypass a lifecycle gate.

## Mandatory engagement sequence

| State | Required outcome | Advancement gate |
|---|---|---|
| `OI-LC-01` Qualification | Fit, exclusions, authority, and commercial next step are recorded | Scope and implementation willingness are credible |
| `OI-LC-02` Intake | Business context, systems, constraints, objectives, and material unknowns are recorded | Each material unknown has a validation state, owner, and next action |
| `OI-LC-03` Surface Mapping | In-scope buyer and operating surfaces are inventoried | Access, exclusions, and collection targets are explicit |
| `OI-LC-04` Evidence Collection | Evidence records support evaluation or controlled unknown handling | Evidence thresholds pass or the criterion is routed to unknown |
| `OI-LC-05` Scoring | Criterion scores, confidence, coverage, normalization, and Operator Score are reproducible | Weights reconcile and unknowns are not treated as failures |
| `OI-LC-06` Finding Resolution | Governed findings connect observations to evidence, impact, confidence, and dependencies | Duplicate, conflict, and report-admission controls pass |
| `OI-LC-07` Risk and Opportunity Synthesis | Business significance, effort, readiness, and value eligibility are evaluated | Severity, confidence, and value remain distinct and supportable |
| `OI-LC-08` Recommendation Routing | Findings are routed to approved actions, packages, prerequisites, and acceptance criteria | Every recommendation has traceable evidence and an implementation path |
| `OI-LC-09` Report and Roadmap Build | Executive conclusions, score limitations, priorities, sequencing, and next actions are assembled | Client-facing claims pass evidence, confidence, and language gates |
| `OI-LC-10` Delivery and Decision | Client decisions, objections, conditions, owners, and next actions are recorded | No silence or ambiguity is treated as approval |
| `OI-LC-11` Proposal and Onboarding | Accepted recommendations become controlled scope, ownership, access, and approvals | Commercial authorization and delivery prerequisites exist |
| `OI-LC-12` Implementation | Approved package work is executed, tested, reviewed, and accepted | Acceptance evidence and unresolved limitations are recorded |
| `OI-LC-13` Monitoring and Realized Value | Adoption, performance, risk reduction, and modeled-versus-realized value are reviewed | Attribution and measurement limits are explicit |
| `OI-LC-14` Renewal or Closure | Ownership, remaining risks, maintenance, access, and next-cycle decisions are resolved | DecisionLedger and closeout records are complete |

## Global invariants

The following rules apply to every state:

- Evidence precedes scoring, findings, recommendations, and client-facing claims.
- Unknown information remains unknown until validated.
- Missing evidence does not automatically become a negative score.
- Confidence reflects evidence strength and does not substitute for severity.
- Category scores remain reproducible from criterion-level records.
- A finding must reference evidence, criteria, impact, confidence, and validation state.
- A recommendation must reference governed findings and an approved implementation package.
- Every recommendation, decision, deferral, rejection, and material change must remain DecisionLedger traceable.
- Roadmap order must respect dependencies, capacity, readiness, and approval requirements.
- Financial or ROI language is prohibited unless the applicable value and attribution gates pass.
- Draft, blocked, superseded, or validation-required findings cannot enter the executive report as confirmed conclusions.
- Implementation cannot begin from an unapproved recommendation or incomplete scope.

## Unknown-data handling

A material unknown must include:

- the missing fact or evidence
- affected criterion, finding, score, or decision
- current validation state
- responsible owner
- next validation action
- decision impact

Unknowns may reduce coverage or confidence. They must not be silently imputed, converted to zero, or removed from the audit trail.

## DecisionLedger checkpoints

A DecisionLedger record is required when:

- a material criterion is scored with limitations
- a finding is admitted, merged, superseded, blocked, or excluded
- a recommendation is routed, deferred, rejected, or conditioned
- a package or roadmap phase is selected
- a client approves, rejects, or changes a proposed action
- implementation scope, acceptance criteria, or ownership changes
- realized-value claims are accepted, limited, or rejected
- an engagement is renewed, transferred, or closed

## Advancement rule

A document being complete does not advance the engagement. Advancement requires the current state's evidence, decisions, owners, approvals, and outputs to satisfy its exit gate.

When a gate fails, use one of the controlled states defined in `framework/lifecycle-roadmap-map.md`, including `validation_required`, `review_required`, `blocked`, `deferred`, or `cancelled`.

## Commercial v1.0 acceptance criteria

This lifecycle is ready for commercial use only when a complete sample engagement demonstrates:

- intake through closure using the canonical state IDs
- evidence-to-score reproducibility
- governed unknown-data treatment
- finding and recommendation traceability
- package and roadmap routing
- executive-safe reporting
- explicit client decisions
- implementation acceptance evidence
- monitoring and closeout records

Until that end-to-end sample passes, this file governs execution but does not by itself establish commercial v1.0 completion.
