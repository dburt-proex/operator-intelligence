# 5W-config

## Purpose

5W-config is the canonical pre-execution configuration primitive for turning a vague objective into an implementation-ready operating contract.

It is intentionally lightweight. The kernel form detects whether a material task is sufficiently defined; the skill form performs the deeper configuration pass only when complexity, consequence, ambiguity, or reuse justify it.

## Canonical fields

- **WHO** — actor, operator, owner, affected users/systems, and decision authority.
- **WHAT** — exact capability, object, decision, or outcome being defined.
- **WHEN** — trigger, cadence, activation condition, deadline, stop condition, and restart condition when relevant.
- **WHERE** — execution layer, repository, runtime, interface, data boundary, and source of truth.
- **WHY** — objective, expected value, problem being solved, and risk of not acting.
- **HOW** — implementation method, tools, controls, sequence, verification, and escalation path.
- **SUCCESS** — measurable definition of done / acceptance criteria.
- **CONSTRAINTS** — hard boundaries: governance, safety, authority, scope, time, cost, compatibility, and quality limits.

## Kernel gate

Use the minimal gate before non-trivial implementation, automation, agent design, kernel changes, workflow creation, or consequential system changes.

A task is **CONFIGURED** when the available context is sufficient to determine WHO, WHAT, WHEN, WHERE, WHY, HOW, SUCCESS, and CONSTRAINTS without inventing material facts.

A task is **REVIEW** when a missing field could materially change architecture, authority, data handling, cost, safety, or definition of done.

A task is **ALLOW** when the missing detail is non-material and can be resolved safely during execution.

Do not turn 5W-config into mandatory questioning. Reuse already-known context. Ask only when a genuinely material field cannot be resolved from evidence or bounded assumptions.

## Skill mode

Run the full 5W-config skill when one or more conditions apply:

1. The task spans multiple systems, repositories, agents, tools, or teams.
2. The work is reusable or intended to become a standard, skill, kernel, automation, or product capability.
3. The build has meaningful cost, migration, persistence, security, governance, or quality consequences.
4. The objective is vague enough that multiple reasonable implementations would produce materially different outcomes.
5. Rework risk is high.

### Procedure

1. Populate the eight canonical fields using verified context first.
2. Separate facts from assumptions; label material assumptions.
3. Resolve authority and source-of-truth conflicts before implementation.
4. Define SUCCESS before selecting the implementation sequence.
5. Define CONSTRAINTS before optimization so speed cannot silently trade away quality or governance.
6. Run dependency / critical-path optimization when the task is a build or multi-step implementation.
7. Execute against the resulting configuration.
8. Verify the result against SUCCESS and record material deviations.

## Output contract

```text
5W-CONFIG

WHO:
WHAT:
WHEN:
WHERE:
WHY:
HOW:
SUCCESS:
CONSTRAINTS:

STATE: ALLOW | REVIEW | HALT
MATERIAL ASSUMPTIONS:
NEXT ACTION:
```

## Invariants

- Operator authority is never superseded by this primitive.
- Existing verified context must be reused; do not force the operator to repeat known information.
- Unknown material facts remain unknown until resolved.
- Speed optimization follows, and never overrides, SUCCESS and CONSTRAINTS.
- A configuration is not complete merely because every field contains text; each material field must be decision-useful.
- 5W-config defines the problem and operating contract; specialized skills perform the work.

## Relationship to other primitives

```text
Objective
   ↓
5W-config kernel gate
   ↓
5W-config skill (only when warranted)
   ↓
Critical-path / build optimization
   ↓
Specialized skill / agent / workflow
   ↓
Governance + execution
   ↓
Verification against SUCCESS
```

## Recommended use

Use 5W-config broadly for major builds, agents, automations, kernels, workflows, product features, architectural decisions, and high-value operating procedures. Skip the full pass for trivial, reversible, well-specified tasks where it would create more process than signal.
