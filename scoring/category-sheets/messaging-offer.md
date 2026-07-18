# Messaging and Offer Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `messaging_offer`  
Default Operator Score weight: 10%  
Status: Reconciled commercial v1.0 scoring contract

## 1. Purpose and category boundary

This sheet governs the combined `messaging_offer` category while preserving separate criterion records for messaging and offer conditions.

The category measures whether a buyer can understand:

- what the business does
- who the service is for
- what outcome or problem is addressed
- why the company is meaningfully different
- what the buyer receives
- what action begins the sales process
- how pricing, process, follow-up, referral, and reactivation are explained or operated

Messaging criteria measure how the business expresses its services, value, differentiation, relevance, proof, process, and next step.

Offer criteria measure the commercial structure behind the buyer action, including entry offer, service packaging, pricing-factor explanation, sales-process clarity, estimate follow-up, lost-reason capture, referral, and reactivation.

This category does not independently score:

- website navigation, layout, responsiveness, or technical usability
- CTA placement, form functionality, lead capture, or confirmation behavior
- search optimization or indexability
- proof quality or review strength
- CRM implementation quality beyond offer-system criteria explicitly listed here
- competitive position merely because language resembles competitors

Cross-domain effects must be recorded as dependencies rather than duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefixes:

```text
OI-MSG-*
OI-OFFER-*
```

### Messaging criteria

| Criterion | Observable condition | Primary evidence |
|---|---|---|
| `OI-MSG-001` | Hero states a specific customer outcome | Homepage hero copy |
| `OI-MSG-002` | Copy explains meaningful differentiation | Homepage, about, service pages |
| `OI-MSG-003` | Copy addresses buyer pain points | Service-page copy |
| `OI-MSG-004` | Service descriptions are specific | Service-page inventory |
| `OI-MSG-005` | Buyer-facing offer is clear | Homepage, service pages, CTAs |
| `OI-MSG-006` | Copy explains the process | Homepage and service pages |
| `OI-MSG-007` | Copy reduces material objections | FAQs and service pages |
| `OI-MSG-008` | Message is locally relevant | Local references and project examples |
| `OI-MSG-009` | Copy avoids vague unsupported claims | Full-site copy review |
| `OI-MSG-010` | Confirmed high-value services are emphasized | Homepage, navigation, service priorities |

### Offer criteria

| Criterion | Observable condition | Primary evidence |
|---|---|---|
| `OI-OFFER-001` | Business has a clear entry offer | Homepage, CTAs, sales materials |
| `OI-OFFER-002` | High-value services are packaged clearly | Service pages and proposal language |
| `OI-OFFER-003` | Pricing factors are explained when appropriate | FAQs and service pages |
| `OI-OFFER-004` | Sales process is clear | Website process, interview, SOP |
| `OI-OFFER-005` | Estimate follow-up is consistent | CRM, templates, owner interview |
| `OI-OFFER-006` | Lost reasons are captured | CRM and reporting records |
| `OI-OFFER-007` | Referral system exists | Templates and process records |
| `OI-OFFER-008` | Retention or reactivation path exists | CRM campaigns and customer records |

Each criterion retains its original ID and evidence record. Aggregation into one category must not merge, replace, or duplicate criterion records.

## 3. Required evidence surfaces

Primary public evidence:

- homepage hero and primary offer
- core service pages
- about page
- FAQ content
- contact or estimate page
- visible process sections
- proposal or sales-material language when supplied
- Google Business Profile description when used for consistency validation

Primary internal evidence for offer-system criteria:

- sales-process documentation
- CRM stages and fields
- estimate follow-up records or templates
- lost-reason fields and reports
- referral request process
- reactivation or retention campaigns
- client interview with named process owner

Supporting evidence:

- competitor message comparison
- customer interview notes
- call scripts
- email and SMS templates
- proposal examples
- service-margin or strategic-priority records

Evidence that cannot support a point score alone:

- evaluator writing preference
- an unverified client statement without corroborating records when system behavior is scored
- one isolated phrase taken outside the page or sales context
- assumptions about profitable services without client confirmation or reliable data
- generic industry best practices without observed client evidence

## 4. Minimum evaluation scope

Before an official category score is admissible, evaluate at minimum:

- homepage hero and primary CTA language
- all primary navigation service labels
- at least two core service pages when available
- contact or estimate page
- visible process and FAQ content
- one complete buyer path from landing page to stated next step
- offer-system interview or documentation review for `OI-OFFER-004` through `OI-OFFER-008`
- service-priority confirmation for `OI-MSG-010` and `OI-OFFER-002`

When fewer than two service pages exist, inspect every available service surface and record the scope limitation.

Public evidence may support messaging and public offer-clarity criteria. Internal operational offer criteria remain `unknown` or `blocked` when required records or access are unavailable.

## 5. Applicability rules

All 18 criteria are applicable by default for an operating local-service or contractor business.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples may include:

- no estimate stage exists because the business uses immediate fixed-price transactions
- no repeat or reactivation opportunity exists by the verified nature of the service
- referral activity is prohibited by a documented legal, contractual, or platform restriction

The following are not valid reasons for `not_applicable`:

- the business has not built the process
- records are unavailable
- the owner does not know the answer
- the evaluator cannot access the CRM
- the criterion would lower the score

Absence of a required system is scored only when the absence is directly verified. Otherwise use `unknown` or `blocked`.

## 6. Criterion weighting rule

Use equal weighting across all applicable messaging and offer criteria.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

With all 18 criteria applicable, each criterion carries `5.5556%` of the category.

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before internal weights are recalculated.

Messaging and offer subgroups do not receive separate category weights. Evaluators must not rebalance the category based on observed strengths, evidence availability, or package opportunity.

## 7. Category-specific anchor guidance

### A. Outcome, clarity, and buyer relevance

Applies primarily to `OI-MSG-001`, `OI-MSG-003`, `OI-MSG-004`, `OI-MSG-005`, `OI-MSG-006`, and `OI-OFFER-001`.

| Score | Observable condition |
|---:|---|
| 0 | Tested surfaces do not identify a usable service, buyer outcome, entry action, or next-step process, or contain materially misleading language. |
| 25 | Basic service language exists but is vague, inconsistent, task-only, or insufficient for a buyer to understand fit and next action. |
| 50 | Core service, offer, and next step are understandable, but important outcomes, pain points, process, or expectations remain incomplete. |
| 75 | Major buyer-facing surfaces consistently explain service, outcome, fit, process, and next action in commercially useful language. |
| 100 | Language is consistently specific, validated, differentiated, objection-aware, locally relevant, measured, and integrated across public and sales surfaces. |

### B. Differentiation, proof alignment, and claim quality

Applies primarily to `OI-MSG-002`, `OI-MSG-008`, and `OI-MSG-009`.

| Score | Observable condition |
|---:|---|
| 0 | Claims are materially false, misleading, contradictory, or unsupported after verification. |
| 25 | Differentiation relies mainly on vague claims such as quality, affordable, reliable, or professional without operational proof. |
| 50 | Some real differentiators or local signals appear, but they are incomplete, inconsistently placed, or weakly supported. |
| 75 | Verified differentiators and local relevance are clearly expressed near major decision points and supported by evidence. |
| 100 | Differentiation is verified, distinctive, consistently expressed, linked to buyer priorities, and supported by current proof and operational controls. |

### C. Service priority, packaging, and pricing clarity

Applies primarily to `OI-MSG-010`, `OI-OFFER-002`, and `OI-OFFER-003`.

| Score | Observable condition |
|---:|---|
| 0 | Confirmed strategic services are hidden, materially misrepresented, or packaged in a way that prevents reasonable buyer understanding. |
| 25 | Services are listed but priority, scope, fit, packaging, or pricing factors are materially unclear. |
| 50 | Primary services and basic pricing factors are understandable, but packaging and strategic emphasis remain inconsistent or incomplete. |
| 75 | Confirmed priority services are clearly packaged and emphasized, with appropriate scope and pricing-factor explanations. |
| 100 | Service packaging is validated against strategy and delivery capacity, consistently represented across sales surfaces, measured, and maintained by an owner. |

### D. Sales-process operation

Applies primarily to `OI-OFFER-004` through `OI-OFFER-008`.

| Score | Observable condition |
|---:|---|
| 0 | Direct evidence confirms the process is absent, broken, misleading, or routinely loses required follow-up or customer records. |
| 25 | Activity occurs informally, inconsistently, or without reliable ownership, records, stages, or review. |
| 50 | A functional baseline exists with repeatable steps, but coverage, adoption, reporting, or ownership is incomplete. |
| 75 | The process is documented, consistently used, owned, and supported by reliable records and review. |
| 100 | The process is documented, integrated, measured, governed, routinely improved, and traceable from inquiry through follow-up, outcome, referral, and reactivation. |

Interpolation is prohibited unless an approved future version defines a specific rule.

## 8. Confidence assignment guidance

### High confidence

Use when:

- direct page copy or system records are captured
- required surfaces and records are current
- observed behavior is tested or corroborated
- service priorities and differentiators are verified
- public language and internal process evidence agree

### Medium confidence

Use when:

- direct public evidence is complete but internal corroboration is partial
- records are credible but the sample is limited
- process ownership is confirmed but usage consistency is not fully tested
- competitor or local relevance comparison is current but narrow

### Low confidence

Use when:

- conclusions depend substantially on interviews or screenshots without system access
- service priority, differentiation, or pricing context is only partially verified
- available records are stale, incomplete, or inconsistent
- only a narrow buyer path or service sample was reviewed

### Unknown confidence

Use when evidence is insufficient to assign an anchor.

Confidence must not be multiplied into criterion or category performance. High confidence on public messaging does not increase coverage for uninspected internal offer-system criteria.

## 9. Unknown, blocked, and not-applicable treatment

Common unknown conditions:

- strategic service priorities are not confirmed
- operational differentiators cannot be verified
- pricing policy or pricing factors are unavailable
- CRM stages, follow-up records, or lost reasons are inaccessible
- referral and reactivation activity cannot be validated
- sales-process ownership is unclear

Common blocked conditions:

- access is denied after internal records are required
- contradictory owner and system evidence cannot be resolved
- legal, privacy, or contractual restrictions prevent inspection
- proposed language would require unsupported claims, guarantees, credentials, pricing, availability, or response standards

Each material unknown or block must record:

```yaml
criterion_id: OI-OFFER-005
state: unknown
reason_code: ""
evidence_requested: []
validation_owner: ""
materiality: high
next_action: ""
publication_effect: range_only
```

A high-materiality unknown affecting service priority, entry offer, sales process, estimate follow-up, or pricing representation may force `range_only`, `REVIEW`, or `HALT`.

## 10. Duplicate-signal boundaries

| Overlap | Primary ownership rule | Secondary treatment |
|---|---|---|
| Website | Website owns layout, navigation, hierarchy, and usability; this category owns meaning and offer clarity | Record dependency only |
| Conversion | Conversion owns CTA placement, form function, lead capture, confirmation, and routing; this category owns what the CTA or offer communicates | Record dependency only |
| Trust | Trust owns proof strength and credibility; messaging owns how verified proof and claims are expressed | Do not score the same missing proof twice |
| SEO | SEO owns search intent, metadata, indexability, and keyword targeting; messaging owns buyer-facing clarity | Record cross-domain impact |
| Automation | Automation owns workflow execution; offer owns whether follow-up, referral, or reactivation systems exist and support the sales model | Automation may score implementation maturity only when measuring distinct controls |
| Analytics | Analytics owns instrumentation and reporting quality; offer owns whether lost reasons and process outcomes are captured as a sales-system condition | Avoid duplicate penalties for one missing field |
| Competitive | Competitive owns relative position; messaging owns direct differentiation clarity | Competitor similarity may support evidence, not automatic duplicate scoring |

`OI-MSG-005` and `OI-OFFER-001` are distinct only when:

- `OI-MSG-005` evaluates whether the buyer-facing language clearly explains the offer and action
- `OI-OFFER-001` evaluates whether a valid, defined entry offer exists across public and sales operations

When one observation supports both, record separate interpretations and prohibit duplicate impact inflation.

## 11. Finding and recommendation routing

A category score does not automatically create a finding or recommendation.

Eligible finding domains:

- `OI-FIND-MSG-*` for expression, relevance, specificity, differentiation, objection handling, local messaging, and claim-quality conditions
- `OI-FIND-OFFER-*` for entry offer, packaging, pricing structure, sales process, follow-up, lost reasons, referral, and reactivation conditions

Route to the primary root domain. Record adjacent effects as dependencies.

Potential package dependencies may include:

- `OI-PKG-WEB-001` when message correction requires website implementation
- `OI-PKG-CRM-001` when follow-up, lost reasons, referral, or reactivation require CRM workflow implementation
- `OI-PKG-TRUST-001` when claims require proof-system support
- `OI-PKG-DASH-001` when sales-process measurement requires governed reporting

Package selection requires observation, evidence, interpretation, impact, confidence, priority, package fit, roadmap phase, and DecisionLedger traceability.

Package-first selling is prohibited. Narrow correction must be preferred when it resolves the evidenced condition.

## 12. Publication controls

`official` requires:

- minimum public-surface scope complete
- internal evidence reviewed for applicable offer-system criteria
- service priorities and differentiators verified where scored
- no unresolved unsupported-claim or pricing boundary
- weighted category coverage meeting common publication thresholds
- duplicate-signal check passed
- category confidence index meeting common requirements
- no unresolved high-materiality unknown invalidating the point estimate

Use `provisional` when a qualified point score remains useful but material evidence limitations require explicit disclosure.

Use `range_only` when internal offer-system evidence is materially incomplete or the point estimate would imply false precision.

Use `blocked` when:

- a G4 boundary is unresolved
- unsupported or misleading claims are required to support the proposed score
- criterion mapping or weighting fails
- traceability is missing
- contradictory evidence cannot be resolved

Client-facing reporting must separate:

- communication clarity
- offer-system maturity
- evidence coverage
- material unknowns
- validation requirements

Do not describe the category score as proof of revenue performance, sales effectiveness, market demand, or implementation ROI.

## 13. DecisionLedger requirements

```yaml
category_key: messaging_offer
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2"
score_run_id: OI-SCORE-YYYY-NNN
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
messaging_criterion_refs: []
offer_criterion_refs: []
observed_score: null
lower_bound: null
upper_bound: null
coverage: null
confidence_index: null
publication_state: range_only
material_unknowns: []
unsupported_claim_check_passed: false
service_priority_verified: false
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
roadmap_phase_refs: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 14. Validation messages

### Blocking

- `CAT-MSGO-SCOPE-001`: minimum public messaging scope not completed
- `CAT-MSGO-SCOPE-002`: required internal offer-system review not completed
- `CAT-MSGO-EVID-001`: selected anchor is unsupported by captured evidence
- `CAT-MSGO-MAP-001`: messaging or offer criterion is missing, duplicated, or assigned to the wrong category
- `CAT-MSGO-DUP-001`: one operating condition is materially double-scored across categories
- `CAT-MSGO-WEIGHT-001`: internal applicable weights do not reconcile
- `CAT-MSGO-GATE-001`: unsupported claim, pricing, privacy, legal, or governance boundary blocks scoring or publication
- `CAT-MSGO-LEDGER-001`: required criterion or category traceability is missing

### Review or warning

- `CAT-MSGO-UNKNOWN-001`: strategic service priority is unresolved
- `CAT-MSGO-UNKNOWN-002`: internal sales-process evidence is materially incomplete
- `CAT-MSGO-CLAIM-001`: public claim requires verification before recommendation
- `CAT-MSGO-CONSIST-001`: public messaging and internal offer process conflict
- `CAT-MSGO-COVER-001`: category coverage limits point-score interpretation

## 15. Canonical worked scoring example

The controlled regression fixture is:

```text
scoring/examples/messaging-offer-worked-example.md
```

The fixture evaluates all 18 applicable criteria and produces:

```text
Observed indicator = 51.47
Coverage = 94.44%
Confidence index = 0.8971
Defensible range = 43.75–59.03
Publication state = range_only
Review state = REVIEW
Implementation authorized = false
```

`OI-OFFER-008` remains unknown because retention or reactivation records were not provided. The unresolved applicable weight contributes `0–100` to the category range and cannot be removed or scored as zero. The high confidence index applies only to the 17 scored criteria and does not resolve the material offer-system unknown.

The verified generic-differentiation condition routes through `OI-FIND-MSG-003` to exactly one primary package, `OI-PKG-TRUST-001`, in `Phase 2 — Growth Foundation`. The unresolved reactivation criterion routes to validation and does not independently create a CRM, Automation, Dashboard, or AI package commitment.

Example executive-safe statement:

> The reviewed messaging clearly identifies the core services and free-estimate next step, while estimate follow-up and lost-reason controls are directly supported by records. Differentiation and local relevance remain only partially supported, and reactivation evidence was not provided. The current evidence therefore supports a range of 43.75–59.03 rather than a single official Messaging and Offer Clarity score. Validation and reviewed scope approval are required before implementation is authorized.

## 16. Completion checklist

Before approving this category result, confirm:

- all 18 governed criteria are mapped once
- messaging and offer records remain separate
- minimum public and internal scope is documented
- service priorities are verified before scoring emphasis criteria
- differentiators and claims are verified before high scores or rewrites
- pricing language does not overcommit or invent policy
- equal weighting or approved alternative weighting is recorded
- unknown and blocked criteria remain inside applicable weight
- duplicate-signal boundaries pass
- findings use governed messaging or offer IDs
- package selection is evidence-led
- roadmap phase and prerequisites are recorded
- category score, range, coverage, and confidence recalculate correctly
- material unknowns and publication effects are disclosed
- DecisionLedger traceability is complete
- reviewer approval is recorded
