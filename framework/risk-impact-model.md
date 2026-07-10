# Operator Intelligence Risk-Impact Model

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how Operator Intelligence evaluates the business significance of governed findings without exaggerating risk, confusing uncertainty with failure, or using urgency to force implementation.

`framework/risk-model.md` remains the taxonomy source for risk categories and response types. This model operationalizes that taxonomy by standardizing impact, likelihood, reach, evidence, confidence, escalation, and roadmap routing across all finding domains.

## v1.0 connection

Commercial v1.0 requires consistent impact and risk interpretation before findings become recommendations, packages, roadmap initiatives, or executive conclusions.

This model strengthens v1.0 readiness by providing:

- one impact scale across all domains
- one risk-exposure calculation
- clear separation between evidence strength and business severity
- explicit handling for low-confidence, high-consequence conditions
- escalation rules for privacy, safety, legal, policy, and binding commitments
- roadmap and recommendation-routing controls
- DecisionLedger fields and auditability

## Inputs and triggers

Apply this model after:

- a finding ID has been resolved
- evidence references have been attached
- the root domain and affected outcomes are known
- confidence and validation state have been assigned

Reapply it when:

- stronger evidence becomes available
- scope or reach changes
- a dependency is resolved
- implementation changes exposure
- a finding is proposed for a report, roadmap, or package

## Outputs and deliverables

A valid evaluation produces:

- impact class
- impact score
- likelihood score
- reach score
- risk-exposure score
- risk level
- evidence strength
- confidence
- uncertainty treatment
- response type
- escalation state
- roadmap implication
- DecisionLedger rationale

## Core principle

Business severity and evidence quality are separate.

A weakly evidenced condition is not automatically low impact. It may instead require validation, monitoring, REVIEW, or HALT treatment.

Likewise, strong evidence does not make a low-impact condition urgent.

## Impact classes

| Impact class | Definition | Common domains |
|---|---|---|
| Visibility | Qualified buyers may not discover the business for relevant local intent | SEO, GBP, competitive |
| Buyer clarity | Buyers may not understand service, fit, location, process, or next step | Website, messaging, offer |
| Trust | Buyers may lack proof or risk-reduction information needed to act confidently | Trust, GBP, website |
| Conversion | Interested buyers may encounter friction or fail to complete an inquiry | Conversion, website, messaging |
| Lead handling | Inquiries may be missed, delayed, duplicated, or left unowned | Automation, offer |
| Follow-up | Open opportunities may not receive a governed next action | Offer, automation |
| Reputation | Review, response, testimonial, or public-proof systems may be weak or unmanaged | GBP, trust, automation |
| Retention | Past customers may not receive appropriate repeat, maintenance, referral, or reactivation outreach | Offer, automation |
| Measurement | Leadership may be unable to observe performance, outcomes, or implementation results | Analytics, automation |
| Delivery fit | Marketing or sales promises may exceed actual scope, capacity, geography, or policy | Offer, messaging |
| Operational consistency | Repeatable work may depend on memory, fragmented tools, or unclear handoffs | Automation, offer |
| AI execution | AI may operate without sufficient workflow, data, review, privacy, boundary, escalation, or audit controls | AI readiness |
| Competitive position | Comparable competitors may present materially stronger discovery, proof, clarity, or action signals | Competitive and dependent domains |

Use one primary impact class and up to two secondary impact classes. The primary class should represent the most direct business consequence.

## Impact score

Impact measures the magnitude of the business consequence if the condition remains unresolved.

| Score | Level | Definition |
|---:|---|---|
| 1 | Minimal | Limited inconvenience or polish issue with little effect on buyer or operating outcomes |
| 2 | Low | Localized weakness with modest effect and no blocked path |
| 3 | Moderate | Material friction, uncertainty, inconsistency, or measurement limitation |
| 4 | High | Significant weakness affecting qualified demand, conversion, trust, follow-up, delivery, or management control |
| 5 | Severe | Condition blocks a critical path or creates serious privacy, safety, legal, policy, financial-commitment, or customer-harm exposure |

## Likelihood score

Likelihood measures how often or how plausibly the impact may occur under current conditions.

| Score | Level | Definition |
|---:|---|---|
| 1 | Rare | Requires an unusual event or edge case |
| 2 | Unlikely | Could occur, but evidence suggests limited frequency |
| 3 | Possible | Plausible in normal operations or buyer journeys |
| 4 | Likely | Repeated evidence or workflow design makes recurrence probable |
| 5 | Persistent | Condition affects most relevant journeys, records, transactions, or executions |

Likelihood must reflect observed operation, test results, record review, or explicit workflow logic. Do not infer frequency from one isolated observation.

## Reach score

Reach describes the scope of the condition and is used as a routing modifier, not as a substitute for impact.

| Score | Reach | Definition |
|---:|---|---|
| 1 | Isolated | One page, record, message, or edge case |
| 2 | Localized | One service, channel, team member, or workflow step |
| 3 | Journey-level | One complete buyer, sales, review, or reporting journey |
| 4 | Multi-channel | Several pages, profiles, teams, sources, or connected workflows |
| 5 | System-wide | The condition affects the operating system, governance layer, or nearly all relevant cases |

High reach may increase roadmap urgency when impact and likelihood are already material.

## Evidence strength

Evidence strength supports confidence and recommendation admissibility. It does not increase the inherent severity of the condition.

| Score | Evidence level | Definition |
|---:|---|---|
| 1 | Speculative | Plausible concern with no sufficient direct evidence |
| 2 | Limited | One weak source, recollection, partial screenshot, or inaccessible condition |
| 3 | Supported | Direct public evidence or multiple consistent signals, with material gaps remaining |
| 4 | Strong | Direct evidence, tested behavior, records, or repeated observations support the finding |
| 5 | Verified | Reconciled records, controlled tests, configuration review, or multiple authoritative sources confirm the condition |

Evidence strength maps to confidence but does not replace the domain confidence standard.

## Confidence mapping

| Confidence | Typical evidence strength | Use |
|---|---:|---|
| High | 4–5 | Direct, reliable evidence supports the stated condition |
| Medium | 3–4 | Pattern is supported, but validation gaps remain |
| Low | 1–2 | Material interpretation depends on limited evidence or owner confirmation |
| Unknown | 1 or unavailable | Evidence is insufficient for a directional conclusion |

A confidence level may be lower than the typical mapping when comparability, recency, access, data completeness, or test coverage is weak.

## Risk-exposure calculation

```text
Risk Exposure = Impact × Likelihood
```

| Exposure score | Risk level |
|---:|---|
| 20–25 | Critical |
| 12–19 | High |
| 6–11 | Medium |
| 1–5 | Low |

Reach, evidence, reversibility, and control state modify the response, not the exposure calculation.

## Why evidence is not in the exposure formula

Evidence answers, “How certain are we that this condition exists?”

Impact and likelihood answer, “How serious is the condition if it exists?”

Combining evidence directly into inherent risk can understate severe but insufficiently investigated conditions. Operator Intelligence therefore keeps exposure and certainty separate.

## Response types

| Response | Use when |
|---|---|
| Fix | High-confidence condition blocks or materially weakens a critical buyer or operating path |
| Reduce | Valid condition should be lowered through sequenced implementation |
| Validate | Potentially material condition lacks sufficient evidence, access, ownership, policy, capacity, or internal data |
| Monitor | Condition is currently low exposure, stable, or not actionable but should be reviewed later |
| Accept | Low exposure is knowingly tolerated and the rationale is recorded |
| Escalate | Condition affects privacy, safety, legal obligations, policy, sensitive data, binding commitments, or material customer harm |
| Block | Proposed recommendation or execution would violate evidence, accuracy, dependency, policy, safety, or governance gates |

## Decision matrix

| Risk level | Confidence | Default decision state | Default response |
|---|---|---|---|
| Critical | High or Medium | `recommend` or `block` | Fix or escalate immediately according to dependency |
| Critical | Low or Unknown | `validate` or `block` | Urgent validation; prevent unsafe execution |
| High | High | `recommend` | Fix or reduce in the earliest justified phase |
| High | Medium | `recommend` or `validate` | Implement bounded correction or validate material unknowns |
| High | Low or Unknown | `validate` | Do not present the condition as confirmed |
| Medium | High or Medium | `recommend`, `defer`, or `monitor` | Sequence by effort, dependency, and strategic fit |
| Medium | Low or Unknown | `validate` or `monitor` | Gather evidence before expanding scope |
| Low | Any | `monitor`, `accept`, or bundle | Do not create artificial urgency |

## Escalation overrides

The following conditions override normal commercial prioritization:

- sensitive-data exposure
- unreviewed AI pricing, guarantees, availability, or binding commitments
- unsafe advice or customer-harm potential
- false or misleading business claims
- inaccurate service-area, category, credential, warranty, or policy information
- review gating, artificial reviews, or deceptive reputation practices
- legal, regulatory, or contractual uncertainty that requires qualified review
- unauthorized system access or excessive permissions

For these conditions:

1. mark the relevant recommendation `blocked` or the execution state `HALT`
2. identify the required validation or qualified owner
3. do not substitute commercial urgency for governance resolution
4. record the escalation in the DecisionLedger

## Reversibility modifier

Reversibility does not change the exposure score, but it changes execution control.

| Reversibility | Definition | Control implication |
|---|---|---|
| Easy | Change can be safely undone with limited external effect | Standard approval may be sufficient |
| Moderate | Reversal requires coordination, content rollback, or data correction | Document owner and rollback path |
| Difficult | Change affects customers, records, public profiles, integrations, or significant scope | Require explicit approval and verification |
| Irreversible | Action creates binding commitments, permanent loss, legal exposure, or unrecoverable disclosure | Escalate, REVIEW, or HALT |

## Priority integration

This model supplies `impact_score`, `risk_level`, and response state to the recommendation process.

Recommendation priority remains governed by the approved priority formula:

```text
Priority Score = Impact + Evidence Strength + Effort Inverse + Strategic Fit
```

Risk controls modify that formula as follows:

1. Critical exposure cannot be downgraded solely because implementation is difficult.
2. Low evidence cannot justify a confident recommendation; route to validation.
3. Escalation overrides can block execution regardless of priority score.
4. High reach may break ties between recommendations with similar scores.
5. Dependencies and phase readiness may defer a high-priority recommendation without reducing its underlying risk.

## Roadmap routing

| Condition | Default routing |
|---|---|
| Broken inquiry, contact, accuracy, or actively misleading buyer path | Phase 1 — Quick Wins |
| Discoverability, proof, service coverage, local relevance, or buyer-structure gap | Phase 2 — Growth Foundation |
| CRM, ownership, handoff, follow-up, review workflow, data, or reporting gap | Phase 3 — Automation and Reporting |
| Bounded AI use case with passed prerequisites | Phase 4 — Governed AI Enablement |
| AI, privacy, policy, access, or binding-commitment control failure | HALT or prerequisite correction before Phase 4 |
| High-impact unknown internal condition | Validation task in earliest relevant phase |

Roadmap phase does not equal risk level. A severe Phase 3 prerequisite may remain high risk even when it cannot be completed as a Phase 1 quick win.

## Cross-domain concentration rule

When several findings share one root cause, do not add their exposure scores together as if they were independent.

Instead:

1. identify the root condition
2. record dependent findings
3. use the highest defensible impact score
4. adjust reach to reflect multi-domain scope
5. route one primary package and its dependencies
6. retain each finding’s evidence and DecisionLedger record

This prevents duplicate findings from inflating urgency.

## Unknown-data handling

Unknown is not automatically negative.

Use these rules:

- unknown performance data produces a measurement or validation condition only when observability itself is required
- inaccessible systems lower confidence unless access absence is the governed finding
- owner recollection may support low-confidence interpretation but not precise performance claims
- potentially severe unknowns route to validation or block, not automatic failure
- missing evidence must be stated in client language

## Canonical risk-impact object

```yaml
risk_impact_id: OI-RI-YYYY-NNN
finding_id: OI-FIND-DOMAIN-NNN
ledger_ref: OI-DL-YYYY-NNN
primary_impact_class: ""
secondary_impact_classes: []
impact_score: 0
likelihood_score: 0
reach_score: 0
risk_exposure: 0
risk_level: ""
evidence_strength: 0
confidence: unknown
validation_state: validation_required
reversibility: ""
response_type: validate
escalation_state: none
decision_state: validate
roadmap_phase: ""
rationale: ""
unknowns: []
assumptions: []
```

## Example

```yaml
risk_impact_id: OI-RI-2026-001
finding_id: OI-FIND-CONV-004
primary_impact_class: Conversion
secondary_impact_classes:
  - Lead handling
impact_score: 4
likelihood_score: 4
reach_score: 3
risk_exposure: 16
risk_level: High
evidence_strength: 5
confidence: high
validation_state: verified
reversibility: easy
response_type: fix
decision_state: recommend
roadmap_phase: Phase 1 — Quick Wins
rationale: Mobile testing confirmed that the phone path is difficult to access across primary buyer pages.
```

## Report-language rules

Use evidence-safe language:

| Avoid | Use instead |
|---|---|
| This is costing you thousands. | This creates revenue leakage risk because interested buyers may not receive a clear path to inquiry. |
| Your business is in danger. | This condition materially weakens a critical buyer or operating path and should be addressed early. |
| The system does not work. | The available evidence shows that the current workflow does not consistently produce the required outcome. |
| AI will make a serious mistake. | The proposed AI use case lacks the review or boundary controls needed for safe execution. |
| Competitors are taking your customers. | Comparable competitors present stronger visible signals during buyer comparison. |

## Governance rules

1. Never inflate severity to create urgency.
2. Never infer likelihood from one isolated observation.
3. Never reduce inherent impact merely because evidence is incomplete.
4. Never present an unknown condition as confirmed failure.
5. Never sum overlapping findings to create artificial exposure.
6. Never let commercial priority override privacy, safety, legal, policy, accuracy, or binding-commitment controls.
7. Every Critical or High risk requires a written rationale.
8. Every escalation, block, acceptance, or phase override requires DecisionLedger traceability.

## Usage instructions

1. Resolve the finding through `framework/finding-index.md`.
2. Select the primary impact class.
3. Assign impact, likelihood, reach, and evidence scores.
4. Calculate risk exposure.
5. Assign confidence and validation state.
6. Apply escalation and reversibility controls.
7. Select response type and decision state.
8. Pass the result to `framework/recommendation-index.md`.
9. Record the rationale in the DecisionLedger.
10. Re-score after validation or implementation changes the evidence or condition.

## Completion check

Before report or roadmap use, confirm:

- impact and likelihood are evidence-bounded
- reach is not used to duplicate severity
- evidence and exposure remain separate
- unknowns are explicit
- escalation overrides were checked
- overlapping findings were consolidated
- response type is justified
- roadmap phase respects dependencies
- DecisionLedger reference exists

This file is the framework-level source of truth for risk-impact evaluation. `framework/risk-model.md` remains the risk taxonomy source, and future scoring specifications should implement this model without changing its governance behavior.