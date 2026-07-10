# Operator Intelligence ROI Framework

Version: v0.4 control-layer refinement  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file defines how Operator Intelligence evaluates and communicates potential financial and operational value without presenting assumptions, correlations, or modeled scenarios as guaranteed return.

The ROI framework begins only after findings, risk, opportunity, recommendation, effort, package scope, and measurement conditions are understood.

## v1.0 connection

Commercial v1.0 requires proposals and reports that explain why implementation matters while protecting the client and consultant from unsupported financial claims.

This framework strengthens v1.0 readiness by providing:

- value-state classification
- ROI eligibility gates
- baseline and measurement-window requirements
- benefit and cost definitions
- capacity and attribution controls
- scenario and confidence rules
- package-level measurement guidance
- realized-value review
- DecisionLedger traceability

## Core rule

Never present modeled revenue, savings, ROI, payback, lead growth, conversion improvement, or labor reduction as guaranteed performance.

Use language such as:

- modeled scenario
- assumption-based estimate
- directional opportunity
- potential operational value
- observed post-implementation change
- client-provided input

Avoid language such as:

- guaranteed return
- will generate
- proven revenue increase
- exact financial impact
- guaranteed lead increase
- pays for itself

unless a separate verified analysis directly supports the statement and its limitations are disclosed.

## Inputs and triggers

Use this framework only after:

- governed findings exist
- an opportunity has passed admission gates
- one primary package has been selected
- effort and scope are defined
- a measurement plan exists
- financial or operational inputs are available or explicitly unknown

Reapply it when:

- verified baseline data becomes available
- implementation scope or cost changes
- capacity changes
- the measurement window closes
- actual results are reconciled
- attribution limits change

## Outputs and deliverables

A valid ROI evaluation produces:

- value state
- benefit category
- cost category
- baseline period
- measurement window
- source and confidence for each input
- assumptions and unknowns
- scenario model when eligible
- attribution limits
- capacity constraints
- modeled or realized value statement
- DecisionLedger record

## Value states

| Value state | Definition | Allowed report treatment |
|---|---|---|
| `qualitative` | Evidence supports a likely business effect, but financial modeling inputs are insufficient | Describe business impact and measurement plan only |
| `operational_baseline` | A verified non-financial baseline exists | Model or target operational change without converting it to money |
| `modeled_financial` | Required financial inputs are available and assumptions are disclosed | Present conservative scenarios with confidence labels |
| `measured_financial` | Post-implementation financial data is available for the approved window | Report observed change with attribution limits |
| `validated_roi` | Benefits, costs, baseline, window, and attribution have been reconciled sufficiently for ROI calculation | Present ROI and payback with source notes and limitations |

Most early assessments should remain qualitative or operational-baseline unless reliable client data supports more.

## ROI eligibility gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Finding Gate | Modeled value traces to governed findings and opportunity | ROI is attached to a package or sales idea alone | Block model |
| Baseline Gate | Relevant pre-implementation period and metric are defined | No baseline exists | Use qualitative value or create baseline task |
| Input Source Gate | Each input has a named source | Values are invented or copied from generic benchmarks | Mark unknown or exclude |
| Attribution Gate | Relationship between intervention and outcome is plausible and limitations are stated | Model assumes sole causality | Reduce claim or block |
| Cost Gate | Implementation and recurring costs are included | Benefit is shown without investment burden | Block ROI calculation |
| Capacity Gate | Business can fulfill modeled demand or workload | Modeled upside exceeds delivery capacity | Cap or block scenario |
| Window Gate | Measurement period is appropriate for the outcome | Short window is used for long-cycle results | Extend measurement plan |
| Overlap Gate | Benefit is not counted in several packages or models | Same revenue or savings is duplicated | Assign one primary benefit owner |
| Confidence Gate | Input confidence supports the stated precision | Low-confidence inputs produce exact claims | Use range or qualitative value |
| Ledger Gate | Inputs, formulas, assumptions, and limitations are recorded | Model cannot be audited | Block report admission |

## Canonical ROI object

```yaml
roi_ref: OI-ROI-YYYY-NNN
opportunity_id: OI-OPP-YYYY-NNN
recommendation_ref: OI-REC-YYYY-NNN
primary_package_id: OI-PKG-XXX-001
value_state: qualitative
benefit_categories: []
cost_categories: []
baseline_period: ""
measurement_window: ""
input_sources: []
assumptions: []
unknowns: []
capacity_constraints: []
attribution_limits: []
scenario_set: []
total_investment: null
modeled_gross_benefit: null
modeled_net_benefit: null
modeled_roi_percent: null
modeled_payback_months: null
realized_gross_benefit: null
realized_net_benefit: null
realized_roi_percent: null
confidence: unknown
status: qualitative_only
ledger_ref: OI-DL-YYYY-NNN
```

## Benefit categories

### Revenue-related benefits

Use only when inputs and attribution are sufficient.

- additional qualified inquiries
- improved inquiry completion
- recovered open estimates
- improved close rate
- higher-value service mix
- repeat service
- referral activity
- reduced cancellation or leakage

### Operational benefits

These may be measured without converting them to financial value.

- reduced response time
- improved follow-up completion
- lower manual re-entry
- fewer missed inquiries
- improved status visibility
- reduced reporting time
- improved review-request completion
- faster controlled content or communication drafting
- reduced error or exception frequency

### Risk-reduction benefits

Do not assign arbitrary dollar values.

- reduced privacy exposure
- reduced unsupported commitment risk
- reduced misleading claim risk
- stronger auditability
- clearer escalation
- improved data quality
- reduced dependency on owner memory

## Cost categories

| Cost category | Examples |
|---|---|
| Implementation | Consulting, development, configuration, copy, migration, setup |
| Software | CRM, analytics, call tracking, automation, AI, review, hosting, licenses |
| Client labor | Data preparation, approvals, training, content, testing, process documentation |
| Migration and cleanup | Data mapping, deduplication, import, reconciliation, rollback preparation |
| Training and adoption | Staff training, SOP updates, support, change management |
| Governance and QA | Policy, review, logging, sampling, audit, privacy, escalation, maintenance |
| Ongoing operation | Monthly tools, reporting, content, monitoring, optimization, administration |
| Opportunity cost | Disruption or capacity allocated away from other approved work, when material and defensible |

Do not omit client labor or recurring cost merely to make ROI appear stronger.

## Input source hierarchy

Use sources in this order when available:

1. Verified CRM, accounting, analytics, call-tracking, review, or operational records
2. Reconciled exports or reports
3. Documented client estimates with named owner and date
4. Directional assumptions approved for scenario planning
5. Unknown

Generic industry benchmarks may provide context but cannot replace client data in a client-specific ROI claim.

## Core financial formulas

### Baseline revenue represented by leads

```text
Modeled Revenue from Leads =
Lead Volume × Close Rate × Average Collected Job Value
```

Use collected or realized job value when available, not proposal value alone.

### Incremental gross benefit

```text
Modeled Incremental Gross Benefit =
Incremental Qualified Opportunities
× Expected Conversion Rate
× Average Collected Job Value
```

### Follow-up recovery

```text
Modeled Recovered Gross Benefit =
Eligible Open Opportunities
× Assumed Recovery Rate
× Average Collected Job Value
```

Recovery rate must be client-derived or clearly labeled as an assumption.

### Labor value

```text
Modeled Labor Value =
Verified Hours Reduced
× Loaded Hourly Cost
```

Hours reduced must be measured or scenario-labeled. Time saved is not automatically realized cash savings unless staffing or capacity use changes.

### Net benefit

```text
Modeled Net Benefit =
Modeled Gross Benefit
− Implementation Cost
− Recurring Cost During Measurement Window
− Included Client Labor Cost
```

### ROI percentage

```text
Modeled ROI % =
Modeled Net Benefit ÷ Total Investment × 100
```

### Payback period

```text
Modeled Payback Months =
Total Investment ÷ Modeled Monthly Net Benefit
```

Do not calculate ROI percentage or payback when net benefit, investment, or measurement period is unknown.

## Scenario governance

| Scenario | Rule |
|---|---|
| Conservative | Uses the lowest defensible improvement assumptions and full known cost burden |
| Base | Uses client-supported operating assumptions with disclosed uncertainty |
| Upside | Uses stronger but still capacity-constrained assumptions; never presented as expected outcome |

Do not use an aggressive scenario merely to increase proposal appeal.

Each scenario must disclose:

- inputs
- sources
- assumptions
- capacity limit
- time window
- costs
- confidence
- attribution limits

## Confidence rules

| Confidence | Use when |
|---|---|
| High | Inputs are verified, reconciled, period-matched, and directly relevant; costs and attribution limits are known |
| Medium | Most inputs are client-derived and plausible, but one or more material assumptions remain |
| Low | Model depends heavily on estimates, incomplete records, uncertain attribution, or unverified capacity |
| Unknown | Financial modeling is not defensible |

Low-confidence models should use broad ranges and must not appear in executive summaries as expected results.

## Baseline requirements

```yaml
metric: ""
definition: ""
source: ""
owner: ""
period_start: ""
period_end: ""
value: null
known_limitations: []
confidence: unknown
```

A baseline must use the same metric definition as the post-implementation measurement.

Do not compare:

- leads to qualified leads
- estimate value to collected revenue
- all calls to tracked marketing calls
- gross revenue to contribution margin
- review count to review velocity
- one seasonal month to a non-seasonal period without qualification

## Measurement-window controls

Measurement windows should reflect:

- buyer and sales-cycle length
- implementation completion date
- seasonality
- lead volume
- service frequency
- reporting reliability
- attribution lag
- adoption period

The framework does not prescribe one universal 30-, 60-, or 90-day financial window.

Use a short operational validation window where appropriate, but do not infer long-cycle financial performance from it.

## Capacity constraints

Before modeling additional demand, confirm:

- service is currently offered
- service area is accurate
- schedule and staffing can absorb work
- sales and follow-up systems can handle additional inquiries
- job economics are acceptable
- delivery quality and policy can be maintained

When capacity is constrained:

- cap modeled opportunity
- model service-mix improvement instead of lead volume
- route to offer, CRM, or operational prerequisites
- avoid promising demand growth

## Attribution controls

Business outcomes may be affected by:

- seasonality
- market demand
- weather
- pricing changes
- sales behavior
- staffing
- reputation changes
- paid media
- search algorithm changes
- competitor activity
- implementation quality
- data quality

| State | Meaning |
|---|---|
| `direct` | Outcome is tightly connected to a controlled operational change, such as reduced response time |
| `contributing` | Package plausibly contributed, but other factors materially affected the result |
| `directional` | Evidence suggests movement but causality cannot be isolated |
| `unresolved` | Attribution is insufficient for a result claim |

## Double-counting controls

One financial benefit may have several contributing packages, but it must have one primary modeled owner.

Example:

```text
SEO expansion
+ conversion improvements
+ CRM follow-up
→ may all contribute to booked work
```

Do not create three separate revenue models and add them together.

Instead:

1. define one end-to-end opportunity model
2. assign a primary modeled owner
3. list contributing packages
4. disclose attribution limits
5. measure leading indicators for each package

## Package value and measurement guidance

| Package | Primary value path | Preferred leading indicators | Financial modeling caution |
|---|---|---|---|
| Website Conversion Fix Pack | Reduce visible inquiry friction | path completion, form success, phone clicks, response expectations | Do not assume every corrected visitor becomes a lead |
| Local SEO Expansion Pack | Improve qualified local discoverability | indexed pages, impressions, qualified queries, service-page entries | Do not convert rankings or traffic directly to revenue without funnel data |
| Google Business Authority Pack | Improve profile relevance, proof, and action readiness | profile completeness, calls, clicks, directions, review activity | GBP actions may have attribution and platform-reporting limits |
| Trust Proof System | Reduce buyer uncertainty | proof coverage, CTA-area proof, testimonial and project assets | Do not model reviews or trust directly as revenue without client evidence |
| CRM and Follow-Up System | Reduce missed, unowned, or stale opportunities | response time, ownership, status coverage, follow-up completion, recovery | Separate process adoption from financial outcome |
| Review Generation System | Systematize ethical review and testimonial growth | request completion, review velocity, response completion, testimonial capture | Do not assign arbitrary revenue value to reviews |
| Operator Dashboard Pack | Improve observability and decision quality | attribution coverage, reconciled metrics, decision cadence, action closure | Decision quality is often operational value before financial value |
| Governed AI Intake Assistant | Assist bounded work under controls | handling time, approval rate, escalation rate, error rate, QA findings | Time saved is not cash savings unless capacity use changes |

## Realized-value review

After implementation:

1. confirm the implementation acceptance criteria passed
2. confirm the measurement window
3. reconcile baseline and post-implementation definitions
4. record adoption and exceptions
5. calculate observed operational change
6. calculate financial change only when eligible
7. document attribution limits
8. compare actual cost to planned investment
9. update opportunity, recommendation, and ledger status
10. record lessons for package and methodology refinement

## Client-facing language

### Qualitative

> This recommendation addresses a measurable conversion constraint, but the current data does not support a defensible revenue projection. The implementation should first establish a baseline and conversion tracking.

### Modeled

> Using client-provided lead volume, close rate, job value, and disclosed assumptions, this scenario illustrates potential upside. It is not a guaranteed outcome.

### Realized

> During the defined measurement period, the tracked metric changed from the approved baseline to the observed result. Several operating and market factors may also have contributed.

## Required disclaimer

> Financial projections in this assessment are scenario models, not guaranteed outcomes. Actual results depend on market demand, implementation quality, response time, pricing, close rate, seasonality, operational capacity, data quality, attribution limits, and client execution.

## DecisionLedger requirements

```yaml
roi_ref: OI-ROI-YYYY-NNN
opportunity_id: OI-OPP-YYYY-NNN
recommendation_ref: OI-REC-YYYY-NNN
primary_package_id: OI-PKG-XXX-001
value_state: qualitative
baseline_refs: []
measurement_window: ""
input_sources: []
benefit_categories: []
cost_categories: []
assumptions: []
unknowns: []
capacity_constraints: []
attribution_state: unresolved
attribution_limits: []
scenario_set: []
total_investment: null
modeled_net_benefit: null
modeled_roi_percent: null
realized_net_benefit: null
realized_roi_percent: null
confidence: unknown
status: qualitative_only
rationale: ""
```

## Usage instructions

1. Confirm finding, opportunity, package, scope, and effort records.
2. Select the current value state.
3. Identify benefit and cost categories.
4. Define baseline and measurement window.
5. Record every input source and confidence level.
6. Check attribution, capacity, cost, overlap, and timing gates.
7. Use qualitative value when financial gates fail.
8. Build conservative scenarios only when eligible.
9. Include assumptions, unknowns, limitations, and disclaimer.
10. Reconcile realized value after the measurement window.
11. Store the full record in the DecisionLedger.

## Completion check

Before ROI language enters a client report or proposal, confirm:

- value state is explicit
- governed findings and opportunity exist
- baseline is defined or absence is disclosed
- input sources are named
- costs include implementation, recurring, client, and governance burden where relevant
- capacity is sufficient or modeled value is capped
- attribution limits are stated
- benefits are not double counted
- scenario precision matches confidence
- modeled value is not presented as guaranteed
- measurement window is appropriate
- DecisionLedger traceability exists
