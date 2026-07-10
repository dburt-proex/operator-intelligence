# Operator Intelligence Opportunity Model

Version: v0.4 control-layer refinement  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how Operator Intelligence converts one or more governed findings into a business opportunity that is evidence-bound, outcome-oriented, implementable, measurable, and correctly sequenced.

A finding describes an observed condition. A risk-impact record explains why the condition matters. An opportunity defines the controlled value path that may be created by addressing the condition.

This model prevents reports from becoming disconnected lists of weaknesses, while also preventing speculative upside from being treated as proven value.

## v1.0 connection

Commercial v1.0 requires opportunities that can move cleanly into recommendations, packages, roadmaps, proposals, implementation handoffs, and post-implementation review.

This model strengthens v1.0 readiness by providing:

- a canonical opportunity object
- admission and evidence gates
- outcome and measurement requirements
- effort-adjusted prioritization
- delivery-fit and capacity controls
- qualitative, modeled, and realized value states
- duplicate-opportunity controls
- package and roadmap routing
- DecisionLedger traceability

## Inputs and triggers

Apply this model after:

- findings have been resolved through `framework/finding-index.md`
- one primary impact class has been assigned
- risk exposure has been evaluated through `framework/risk-impact-model.md`
- effort has been estimated through `framework/effort-model.md`
- package eligibility has been checked through `framework/recommendation-index.md`

Reapply it when:

- evidence changes
- effort or scope changes
- a dependency is resolved
- capacity or strategic priorities change
- a baseline becomes available
- implementation results are measured

## Outputs and deliverables

A valid opportunity produces:

- opportunity ID
- source findings
- primary business outcome
- affected buyer or operating journey
- value state
- impact score
- urgency score
- strategic-fit score
- effort inverse
- opportunity priority score
- confidence and validation state
- primary package route
- roadmap phase
- measurement plan
- DecisionLedger record

## Core principles

1. An opportunity must originate from governed findings.
2. Opportunity value is not the same as financial ROI.
3. Evidence quality controls admissibility and confidence; it does not inflate business value.
4. Low evidence plus high potential impact routes to validation, not automatic implementation.
5. Low effort is a convenience advantage, not proof that work should be sold.
6. High impact is not automatically high ROI.
7. Strategic fit requires alignment with current goals, capacity, offer, roadmap phase, and delivery readiness.
8. Multiple findings may support one opportunity when they share one outcome and implementation path.
9. The same modeled benefit must not be counted across several opportunities.
10. Opportunity language must describe potential value without promising results.

## Canonical opportunity object

```yaml
opportunity_id: OI-OPP-YYYY-NNN
source_findings: []
primary_domain: ""
dependent_domains: []
primary_impact_class: ""
secondary_impact_classes: []
business_outcome: ""
affected_journey: ""
value_state: qualitative
impact_score: 1
urgency_score: 1
strategic_fit_score: 1
effort_ref: OI-EFF-YYYY-NNN
effort_level: low
effort_inverse: 5
opportunity_priority_score: 4
opportunity_level: later
confidence: unknown
validation_state: validation_required
primary_package_id: ""
dependent_package_ids: []
roadmap_phase: ""
measurement_plan: []
assumptions: []
unknowns: []
decision_state: validate
ledger_ref: OI-DL-YYYY-NNN
```

## Opportunity categories

| Category | Business value path |
|---|---|
| Visibility | More qualified buyers may discover the business for relevant local intent |
| Buyer clarity | Buyers may understand service, fit, process, location, or next step more quickly |
| Trust | Buyers may receive stronger proof and risk-reduction information |
| Conversion | More interested buyers may complete an inquiry path |
| Lead handling | Fewer inquiries may be missed, delayed, duplicated, or left unowned |
| Follow-up | More open leads and estimates may receive a governed next action |
| Reputation | More completed work may become visible review and testimonial proof |
| Retention | More past customers may receive relevant repeat, maintenance, referral, or reactivation outreach |
| Measurement | Leadership may gain reliable visibility into sources, outcomes, trends, and actions |
| Operational consistency | Repeatable work may become less dependent on memory and informal handoffs |
| Delivery fit | Marketing and sales promises may align more closely with actual capacity and scope |
| AI enablement | AI may support bounded workflows under approved controls and review gates |
| Competitive position | The business may close a material buyer-comparison gap in an underlying domain |

Use one primary category. Secondary categories may be recorded as dependencies or measurement effects.

## Value states

| Value state | Meaning | Report use |
|---|---|---|
| `qualitative` | Evidence supports a business value direction, but no defensible financial model exists | Use impact language only |
| `measurable_operational` | A baseline and operational metric exist, such as response time, follow-up completion, review velocity, or attribution coverage | Use metric target or validation plan |
| `modeled_financial` | Verified or disclosed inputs support an assumption-based financial scenario | Use governed ROI framework and disclaimer |
| `realized` | Post-implementation results have been measured against an approved baseline and window | Report actual observed change with attribution limits |

Do not skip directly from qualitative value to realized value.

## Opportunity admission gates

An opportunity cannot enter the recommendation set until these gates are evaluated.

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Finding Gate | At least one approved source finding exists | Opportunity is based on an idea or sellable service alone | Reject or create validation task |
| Evidence Gate | Source evidence and confidence are recorded | Value claim is opinion-only | Set `validate` |
| Outcome Gate | One specific business outcome is defined | Opportunity says only improve, optimize, or grow | Rewrite outcome |
| Root-Cause Gate | The opportunity addresses the primary condition | Work targets a surface symptom only | Re-route |
| Delivery-Fit Gate | Offer, capacity, service area, process, and policy can support the outcome | Demand may exceed delivery readiness | Defer or block |
| Effort Gate | Effort reference, level, and assumptions exist | Priority uses guessed implementation burden | Complete effort model |
| Package Gate | One eligible primary package is identified | No package resolves the condition | Create methodology or validation gap |
| Measurement Gate | Leading or outcome indicators are defined | Success cannot be reviewed | Add measurement plan |
| Duplicate Gate | Benefit is not already represented by another opportunity | Same value is counted several times | Merge or link |
| Roadmap Gate | Phase and prerequisites are explicit | Opportunity ignores dependencies | Re-sequence |
| Ledger Gate | DecisionLedger traceability exists | Decision cannot be audited | Block admission |

## Scoring model

Opportunity priority uses four dimensions after admission gates pass.

### 1. Impact

Use the impact score from `framework/risk-impact-model.md`.

| Score | Meaning |
|---:|---|
| 1 | Minimal business consequence |
| 2 | Localized or low effect |
| 3 | Material improvement potential |
| 4 | High effect on a key buyer or operating outcome |
| 5 | Severe constraint, blocked path, or major strategic effect |

### 2. Urgency

| Score | Meaning |
|---:|---|
| 1 | No current need; later refinement |
| 2 | Useful but not time-sensitive |
| 3 | Should be addressed in the active roadmap |
| 4 | Repeated or growing constraint requires timely action |
| 5 | Critical path, active exposure, blocked execution, or escalation condition |

Urgency must be supported by evidence, risk, timing, dependency, or active business need. Do not use urgency as sales pressure.

### 3. Strategic fit

| Score | Meaning |
|---:|---|
| 1 | Weak alignment with current goals, capacity, or roadmap |
| 2 | Some relevance but another constraint should lead |
| 3 | Supports an approved goal and current operating direction |
| 4 | Strong alignment with priority services, buyer journey, or readiness phase |
| 5 | Directly enables a critical commercial objective or prerequisite |

### 4. Effort inverse

Use the value from `framework/effort-model.md`.

| Effort level | Effort inverse |
|---|---:|
| Low | 5 |
| Moderate | 4 |
| High | 3 |
| Very High | 2 |
| Program | 1 |

## Opportunity priority formula

```text
Opportunity Priority Score =
Impact
+ Urgency
+ Strategic Fit
+ Effort Inverse
```

Possible range: 4–20.

| Score | Opportunity level | Default treatment |
|---:|---|---|
| 17–20 | Priority | Route into the earliest eligible roadmap phase |
| 13–16 | Strong | Include in the active roadmap when prerequisites pass |
| 9–12 | Supporting | Bundle, sequence, validate, or defer based on dependencies |
| 4–8 | Later | Monitor, exclude, or revisit after higher-value work |

## Evidence and confidence modifier

Evidence and confidence do not add points to the priority score.

They control the decision state:

| Condition | Decision state |
|---|---|
| High or medium confidence with required gates passed | `recommend` |
| Low confidence and material impact | `validate` |
| Unknown evidence | `validate` or `monitor` |
| Valid opportunity with unresolved prerequisite | `defer` |
| Policy, privacy, safety, package, or delivery-fit conflict | `block` |
| Implemented opportunity under measurement | `monitor` |

This prevents a well-documented low-value idea from outranking a material opportunity, while also preventing uncertain claims from entering a proposal as fact.

## Duplicate and aggregation controls

### Multiple findings into one opportunity

Combine findings when they:

- affect the same primary business outcome
- share one root condition or implementation path
- route to one primary package
- can use one measurement plan

Example:

```text
Weak CTA wording
+ buried estimate path
+ unclear form confirmation
→ one conversion opportunity
→ Website Conversion Fix Pack
```

### Keep opportunities separate when they:

- require different owners
- require different packages
- occur in different roadmap phases
- have different acceptance criteria
- create materially different business outcomes

### Benefit overlap rule

Do not add the same lead, revenue, labor, review, or retention benefit to several opportunities.

Assign one primary benefit owner and record secondary contributions as dependencies.

## Opportunity routing patterns

| Pattern | Treatment |
|---|---|
| High impact, low effort, high confidence | Phase 1 when eligible |
| High impact, moderate effort, strong strategic fit | Phase 2 or Phase 3 according to dependency |
| High impact, high effort | Decompose into prerequisites and workstreams |
| High impact, low confidence | Validate before implementation |
| Moderate impact, low effort | Bundle into an active package when scope remains controlled |
| Low impact, high effort | Defer or exclude |
| Growth opportunity with weak capacity or sales readiness | Complete offer, CRM, or measurement prerequisite first |
| AI opportunity without workflow and data readiness | HALT or defer until Phase 3 prerequisites pass |

## Measurement planning

Every opportunity must define at least one indicator.

### Leading indicators

- page or path corrected
- required field or workflow implemented
- tracking coverage established
- response standard adopted
- review request completion
- service-page coverage
- proof asset coverage
- AI review and escalation compliance

### Outcome indicators

- qualified inquiry rate
- lead response time
- follow-up completion
- estimate status visibility
- lost-reason coverage
- review velocity
- attribution completeness
- conversion event volume
- repeat or referral activity
- AI error, escalation, and approval rates

Do not claim causality when several initiatives or external conditions affect the outcome.

## Package routing

Use the canonical package IDs from `framework/recommendation-index.md`.

| Opportunity pattern | Primary package |
|---|---|
| Buyer action and page-path clarity | `OI-PKG-WEB-001` |
| Service and local discoverability | `OI-PKG-SEO-001` |
| Local profile accuracy, proof, and activity | `OI-PKG-GBP-001` |
| Reviews, project proof, credibility, and risk reduction | `OI-PKG-TRUST-001` |
| Lead ownership, stages, handoffs, follow-up, and customer history | `OI-PKG-CRM-001` |
| Review request and testimonial workflow | `OI-PKG-REV-001` |
| Measurement, attribution, reporting, and decision cadence | `OI-PKG-DASH-001` |
| Bounded AI use case with controls | `OI-PKG-AI-001` |

## Roadmap controls

| Phase | Opportunity use |
|---|---|
| Phase 1 — Quick Wins | Correct high-confidence blocked paths, inaccuracies, misleading claims, and narrow friction |
| Phase 2 — Growth Foundation | Improve service coverage, local relevance, proof, buyer support, and profile authority |
| Phase 3 — Automation and Reporting | Establish workflow, CRM, follow-up, data, attribution, and reporting foundations |
| Phase 4 — Governed AI Enablement | Implement bounded AI assistance only after readiness gates pass |

An opportunity may move from its default phase only when evidence, dependencies, risk, readiness, and the DecisionLedger justify the change.

## Client-language standard

Avoid:

- This will generate more revenue.
- This is guaranteed to increase leads.
- Competitors are taking all your business.
- AI will replace the manual process.

Use:

- This creates an opportunity to make the estimate path easier to understand and complete.
- This may improve visibility for verified high-intent local services.
- This can reduce follow-up inconsistency by assigning ownership, timing, and status.
- A bounded AI workflow may assist this task once review, escalation, and data controls pass.

## DecisionLedger requirements

```yaml
opportunity_id: OI-OPP-YYYY-NNN
source_findings: []
primary_impact_class: ""
business_outcome: ""
value_state: qualitative
impact_score: 0
urgency_score: 0
strategic_fit_score: 0
effort_ref: OI-EFF-YYYY-NNN
effort_inverse: 0
opportunity_priority_score: 0
opportunity_level: ""
confidence: unknown
validation_state: validation_required
primary_package_id: ""
dependent_package_ids: []
roadmap_phase: ""
measurement_plan: []
assumptions: []
unknowns: []
decision_state: validate
rationale: ""
```

## Usage instructions

1. Resolve all source findings and dependencies.
2. Select one primary business outcome.
3. Assign value state.
4. Import impact from the risk-impact model.
5. score urgency and strategic fit.
6. Import effort inverse from the effort model.
7. Calculate opportunity priority.
8. Apply evidence and confidence modifier.
9. Check duplicate benefits and package eligibility.
10. Assign roadmap phase and measurement plan.
11. Write the DecisionLedger record.
12. Admit only governed opportunities into recommendations and reports.

## Completion check

Before an opportunity enters a client report, roadmap, or proposal, confirm:

- approved source findings exist
- outcome is specific
- evidence and confidence are explicit
- impact is separated from proof quality
- effort reference exists
- delivery fit and capacity are considered
- benefit is not double counted
- one primary package is eligible
- roadmap dependencies are respected
- measurement plan exists
- language does not promise results
- DecisionLedger traceability exists
