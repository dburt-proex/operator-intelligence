# Finding-to-Recommendation Review Playbook

## Purpose

Use this playbook to convert an approved finding into a bounded, traceable recommendation without overstating evidence, duplicating ownership, bypassing dependencies, or implying unsupported outcomes.

It operationalizes the finding, recommendation, package-routing, roadmap, quality-control, and DecisionLedger standards. It does not replace those standards or their templates.

## Required inputs

- Approved Finding Register entry
- Supporting and contradictory Evidence IDs
- Applicable criterion and score treatment
- Recommendation Register
- Canonical package registry
- Roadmap Standard
- DecisionLedger
- Current publication state

## Required outputs

- Recommendation decision: `ALLOW`, `REVIEW`, or `HALT`
- Bounded recommendation statement
- One primary package route
- Prerequisites and dependency chain
- Roadmap phase
- Acceptance evidence
- DecisionLedger references for material decisions

## Review sequence

### 1. Confirm finding eligibility

Proceed only when the finding:

- has a stable Finding ID;
- is supported by admissible evidence;
- preserves contradictory evidence and material limitations;
- has an evidence-bounded confidence state;
- treats unknown and blocked conditions as unscored;
- has passed required review or approval gates.

Use `HALT` when the finding is unsupported, materially contradictory, improperly scored, or not authorized for downstream use.

### 2. Define the verified condition

State the condition narrowly enough that another reviewer can identify:

- what is happening;
- where it occurs;
- which evidence proves or limits it;
- which criterion or control is affected;
- what remains unknown.

Do not convert assumptions, public absence, reported claims, or missing access into verified failure language.

### 3. Test recommendation necessity

A recommendation is warranted only when a controlled action can address the verified condition or validate a material unknown.

Reject or revise recommendations that are:

- generic best practice without finding-specific evidence;
- commercially preferred but not evidence-supported;
- duplicative of an existing recommendation;
- broader than the approved scope;
- dependent on an unresolved `HALT` condition.

Unknown or blocked findings route to validation work before implementation work.

### 4. Bound the action

Define:

- action to perform;
- affected system, workflow, or owner;
- included scope;
- excluded scope;
- prerequisites;
- dependencies;
- material risks;
- completion evidence.

Recommendation scope must not exceed the supporting finding, evidence, authorization, or confidence state.

### 5. Assign one primary package

Select the canonical package that owns the root implementation condition.

Rules:

1. assign exactly one primary package;
2. list secondary packages only as prerequisite, dependency, downstream, or reference-only relationships;
3. do not duplicate deliverables or ownership across packages;
4. do not invent a package when an approved package already covers the work;
5. route disputed ownership to `REVIEW` and record the decision when material.

Missing, conflicting, or duplicate primary ownership requires `HALT`.

### 6. Place the recommendation on the roadmap

Assign the earliest phase whose entry gates and dependencies are satisfied.

- Phase 1: foundational controls, access, measurement, ownership, or material risk containment
- Phase 2: defined workflow and operational reliability improvements
- Phase 3: optimization after foundations and workflows are stable
- Phase 4: governed AI enablement after workflow, data, privacy, human-review, escalation, logging, and QA gates pass

Priority, commercial preference, or implementation ease cannot bypass prerequisites.

### 7. Define acceptance evidence

Completion must be demonstrated by observable evidence, such as:

- approved configuration or policy record;
- tested workflow result;
- access or ownership confirmation;
- reproducible measurement output;
- documented control operation;
- reviewer-approved validation artifact.

Deliverable existence alone does not prove completion. Implementation completion does not prove business outcome.

### 8. Control claims and language

Use executive-safe language that distinguishes:

- verified condition;
- interpretation;
- recommended action;
- expected operational purpose;
- unverified outcome.

Do not claim guaranteed ROI, revenue, conversion, ranking, lead recovery, market share, competitor performance, savings, or delivery timelines without separately admissible evidence and approved methodology.

### 9. Record the decision

Create or reference DecisionLedger records for material:

- recommendation approval or rejection;
- scope exception;
- confidence override;
- package route;
- roadmap phase or resequencing;
- dependency waiver;
- `HALT` resolution;
- publication restriction;
- supersession.

Approved recommendations are changed through controlled revision or supersession, never silent replacement.

## Decision gates

### ALLOW

Use when the recommendation is finding-specific, evidence-bounded, uniquely routed, dependency-compliant, measurable, and authorized for its stated downstream use.

### REVIEW

Use when the finding is valid but package ownership, scope, sequencing, acceptance evidence, or a bounded contradiction requires a documented reviewer decision.

### HALT

Use when any of the following exists:

- unsupported or unauthorized finding;
- unknown treated as verified failure;
- recommendation scope exceeds evidence;
- duplicate or missing primary package ownership;
- unresolved dependency or prerequisite;
- Phase 4 work bypassing governance gates;
- unsupported outcome claim;
- missing required DecisionLedger traceability.

## Completion checklist

- [ ] Finding is approved for downstream use
- [ ] Evidence and limitations are resolvable
- [ ] Unknown and blocked conditions remain explicit
- [ ] Recommendation directly addresses the verified condition
- [ ] Scope is bounded and exclusions are stated
- [ ] Exactly one primary package is assigned
- [ ] Dependencies and roadmap phase are valid
- [ ] Acceptance evidence is observable
- [ ] Publication and implementation authorization remain separate
- [ ] Executive language avoids unsupported outcomes
- [ ] Material decisions are traceable in the DecisionLedger

## Cross-references

- `playbooks/evidence-validation-playbook.md`
- `templates/finding-register.md`
- `templates/recommendation-register.md`
- `templates/decision-ledger.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/quality-control-standard.md`
- `standards/decision-ledger-standard.md`
