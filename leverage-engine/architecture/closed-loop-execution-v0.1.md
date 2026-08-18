# Closed-Loop Execution Contract v0.1

**Status:** Phase 1 implementation
**Parent:** Leverage Engine / Graph Engineering OS
**Decision owner:** Drew Burt
**Tracking:** #40

## Decision

Extend the existing Leverage Engine flow with a machine-readable execution receipt between an approved directive and the human-reviewed outcome record.

Graph Engineering OS is the operator-facing graph/control surface. Leverage Engine remains the prioritization and directive spine. Downstream agents/tools execute only within explicit authorization. The execution receipt records what actually happened so later runs can reuse evidence instead of re-deriving experience from chat history.

## Objective

Close the smallest useful compounding loop:

```text
repository state + evidence + prior outcomes
            ↓
      leverage selection
            ↓
       bounded directive
            ↓
      operator approval
            ↓
    downstream execution
            ↓
     validation evidence
            ↓
     execution receipt
            ↓
       outcome review
            ↓
 reusable learning + next improvement
            ↓
 future repository state / opportunity graph
```

The loop is successful only when a later run can consume a retained learning or failure record from an earlier execution.

## Why an execution receipt is required

The existing `outcome.schema.json` correctly separates completion evidence from realized value, but it intentionally does not describe the mechanics of execution. Compounding requires retaining operational experience that would otherwise be lost:

- context and evidence consumed;
- agent, model, and tool selection;
- ordered actions;
- files, systems, records, or artifacts changed;
- validation performed;
- operator interventions and review events;
- failures and friction;
- reusable learnings;
- residual risk;
- next-improvement proposal.

The execution receipt is not a replacement for the outcome record. It is evidence used by the outcome evaluator and future Leverage Engine runs.

## Record ownership

| Record | Owner | Purpose |
|---|---|---|
| Repository state | Leverage Engine | Current canonical implementation snapshot |
| Opportunity | Leverage Engine | Candidate leverage move |
| Directive | Leverage Engine | Bounded proposed work contract |
| Approval / decision | Operator + DecisionLedger | Authority to proceed |
| Execution receipt | Downstream executor, retained by shared ledger/evidence store | What actually happened |
| Outcome | Human-reviewed Leverage Engine record | Realized value and future priority effect |
| Learning / next improvement | Derived from receipt + outcome | Reusable experience for subsequent runs |

## Authority boundary

This Phase 1 contract does **not** grant autonomous repository-write authority to Leverage Engine.

- Leverage Engine may inspect, rank, draft, and record.
- Repository mutation remains a downstream execution capability.
- The operator owns approval and any authority expansion.
- Any change to policies, prompts, permissions, scoring weights, or authority requires a separate reviewed directive.
- HALT may never be recorded as completed execution.

The operator explicitly authorized the repository changes used to implement this Phase 1 contract. That authorization does not generalize to future autonomous mutations.

## Execution receipt state

`leverage-engine/schemas/execution-receipt.schema.json` defines the machine-readable record.

Required invariants:

1. Every receipt links to one directive and one project.
2. Every receipt identifies the executor, model, tools, context, evidence, and decision references used.
3. Actions are ordered.
4. Validation is mandatory for every receipt.
5. `completed` requires at least one completion-evidence reference and at least one passing validation record.
6. `HALT` cannot coexist with `completed`.
7. Failures, friction, reusable learnings, residual risks, and operator interventions are explicit arrays; absence is represented by an empty array rather than omission.
8. A next-improvement proposal must carry supporting evidence and state whether it requires review.

## First vertical slice

The first live workload is repository engineering because it is frequent, measurable, reversible through version control, and produces strong completion evidence.

### Input

A bounded directive such as:

> Inspect one approved repository, select one evidence-backed improvement, implement it on an isolated branch, validate the change, record the execution receipt, and propose the next improvement without silently expanding scope.

### Preconditions

- repository exists in an approved registry or is explicitly operator-authorized;
- baseline commit is captured;
- directive has an owner and completion contract;
- branch/worktree isolation is available;
- no secrets or unsupported external actions are required.

### Sequence

1. Capture repository baseline and relevant context.
2. Resolve directive scope and exclusions.
3. Record context/evidence/decision references.
4. Select executor/model/tools within the approved boundary.
5. Execute ordered changes on an isolated branch.
6. Run available validation.
7. Record actual changes and validation evidence.
8. Compare completion claim against evidence.
9. Emit execution receipt.
10. Human/outcome evaluator determines realized value separately.
11. Extract reusable learning and one next-improvement proposal.
12. Feed that learning back into the opportunity graph/repository-state analysis for a later run.

## Failure handling

| Failure | Required behavior |
|---|---|
| Missing authority | REVIEW or HALT; do not execute |
| Stale repository baseline | REVIEW before mutation |
| Validation failure | Receipt may be `partial` or `failed`; never false `completed` |
| Tool/agent failure | Record failure and friction; preserve partial evidence |
| Scope expansion discovered | Stop at boundary and propose a new directive |
| Evidence contradiction | REVIEW; preserve both evidence references |
| HALT gate | No completion claim; record reason and residual work |

## Compounding test

Run N creates one or more `reusable_learnings` and an optional `next_improvement`.

Run N+1 must explicitly reference at least one prior execution receipt, learning, outcome, or resulting repository-state change in its context/evidence set when that prior record is relevant.

A system that merely stores receipts but does not consume them on later runs is **not** considered compounding.

## Phase 1 acceptance criteria

1. The execution-receipt schema is valid JSON Schema Draft 2020-12 syntax.
2. A completed valid fixture contains completion evidence and at least one passing validation record.
3. A completed invalid fixture without completion evidence is rejected by the zero-dependency contract validator.
4. The first receipt can point to a real repository baseline/change reference.
5. A next-improvement proposal is evidence-backed and does not self-authorize execution.
6. Existing Leverage Engine authority boundaries remain unchanged.

## Explicitly not in scope

- Graph Engineering OS UI redesign;
- autonomous self-modifying policy or prompts;
- multi-tenant/customer architecture;
- billing, SSO, or enterprise administration;
- broad connector framework;
- autonomous publishing, spending, messaging, or external-impact actions;
- claims that stored receipts alone constitute learning.

## Next gate

After Phase 1 fixtures and validator pass, run the contract against one actual repository-engineering execution. The second live run must demonstrate reuse of information retained by the first before expanding the loop to other work types.
