# Operator Intelligence Framework

## Purpose

This folder contains the governed assessment models that convert validated evidence into reproducible findings, scores, decisions, recommendations, roadmap sequencing, and executive-safe deliverables.

This manifest defines document authority and execution order. It does not replace the detailed controls in the referenced files.

## Canonical execution order

1. Apply `assessment-lifecycle.md` to determine the active lifecycle state and required advancement gate.
2. Apply `governance-gate-index.md` before admitting evidence, scores, findings, recommendations, reports, proposals, or implementation work.
3. Resolve canonical findings through `finding-index.md` and the approved libraries in `findings/`.
4. Evaluate business consequence through `risk-impact-model.md` and `opportunity-model.md` without converting unknowns into negative evidence.
5. Evaluate delivery burden and dependencies through `effort-model.md`.
6. Route governed recommendations through `recommendation-index.md` and the package-routing standard.
7. Map approved work to lifecycle and roadmap phases through `lifecycle-roadmap-map.md`.
8. Use `roi-framework.md` only when baseline, source, confidence, cost, attribution, capacity, and measurement controls permit modeled or measured value language.
9. Preserve every material decision in the DecisionLedger before client publication or implementation authorization.

## Authority map

| Decision area | Primary authority | Required downstream alignment |
|---|---|---|
| Lifecycle state and advancement | `assessment-lifecycle.md` | Gates, roadmap, report status, DecisionLedger |
| Admission, escalation, and control outcomes | `governance-gate-index.md` | All framework, scoring, standards, templates, and delivery artifacts |
| Canonical finding identity and ownership | `finding-index.md` and `findings/` | Scoring, synthesis, recommendations, reports |
| Risk and impact interpretation | `risk-impact-model.md` | Priority, executive language, roadmap |
| Opportunity eligibility | `opportunity-model.md` | Recommendation and package routing |
| Effort and dependency state | `effort-model.md` | Priority, package scope, roadmap phase |
| Recommendation identity and routing | `recommendation-index.md` | Package, proposal, roadmap, implementation |
| Lifecycle-to-roadmap mapping | `lifecycle-roadmap-map.md` | Sequencing, dependencies, client delivery |
| Value and ROI language | `roi-framework.md` | Reports, proposals, measurement plans |

## Non-negotiable invariants

- Evidence precedes interpretation.
- Interpretation precedes scoring and findings.
- Findings precede recommendations.
- Recommendations precede package and roadmap assignment.
- Unknown remains unknown and is disclosed through coverage and confidence controls.
- Confidence reflects evidence quality; it does not repair missing evidence.
- One root condition has one primary finding owner.
- One recommendation has one primary package owner.
- A downstream pass cannot override an upstream review or halt state.
- No client-facing claim may exceed the strength of its evidence.
- No modeled value may be presented as guaranteed ROI.
- Every material recommendation must remain traceable through the DecisionLedger.

## Conflict resolution

When framework files appear to conflict:

1. Preserve evidence, privacy, legal, safety, authorization, and unknown-data controls.
2. Apply the governance gate with the highest severity.
3. Defer advancement rather than infer missing evidence or authority.
4. Record the conflict, affected records, interim state, owner, and restart condition in the DecisionLedger.
5. Update the primary authority file before changing dependent artifacts.

No evaluator may resolve a framework conflict by silently changing weights, confidence, finding ownership, package routing, roadmap phase, or client language.

## Framework completion gate

The framework folder is ready to hand off to scoring only when:

- lifecycle states and advancement gates reconcile;
- canonical finding ownership is defined;
- unknown and confidence handling are explicit;
- risk, opportunity, and effort states are reproducible;
- recommendation and package routing remain traceable;
- roadmap sequencing preserves prerequisites;
- ROI language is evidence-safe;
- DecisionLedger requirements are enforceable; and
- no duplicate framework file claims authority over the same decision.

Until every condition passes, the framework remains under review and downstream artifacts must not treat it as commercially approved.