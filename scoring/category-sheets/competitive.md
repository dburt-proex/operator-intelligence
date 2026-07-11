# Competitive Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `competitive`  
Default Operator Score weight: 5%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for relative buyer-facing market position across named, comparable competitors.

It measures whether the business can identify its true competitive set and whether its visible reviews, service coverage, proof, messaging, local search presence, conversion paths, content usefulness, professional consistency, and roadmap response are competitive within a defined service and geography.

It does not independently score:

- internal competitor revenue, profitability, lead volume, conversion rate, or operating quality
- stable search rank from one temporary or personalized result
- aesthetic preference without buyer-confidence relevance
- raw publishing volume without strategic usefulness
- primary-domain execution already owned by GBP, Trust, SEO, Messaging, Conversion, Website, Offer, Automation, or Analytics

Competitive evidence changes relative interpretation, confidence, priority, and sequencing. Implementation remains owned by the primary affected domain.

## 2. Criterion inventory

Included prefix:

```text
OI-COMP-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-COMP-001` | Main competitors are identifiable and comparable | Competitor matrix, search evidence, client input | Equal |
| `OI-COMP-002` | Review profile is competitive | Dated review comparison | Equal |
| `OI-COMP-003` | Service-page depth is competitive | URL and service inventory | Equal |
| `OI-COMP-004` | Project and trust proof is competitive | Gallery, testimonial, case-study comparison | Equal |
| `OI-COMP-005` | Messaging is differentiated and proof-supported | Homepage and service-copy comparison | Equal |
| `OI-COMP-006` | Business appears for documented target local searches | Dated search evidence, Search Console where available | Equal |
| `OI-COMP-007` | Conversion paths are competitive | Mobile, CTA, phone, form, and next-step comparison | Equal |
| `OI-COMP-008` | Content activity is strategically competitive | Dated content inventory and usefulness review | Equal |
| `OI-COMP-009` | Professional presentation supports buyer confidence | Cross-surface consistency and clarity comparison | Equal |
| `OI-COMP-010` | Material competitive gaps are converted into governed roadmap actions | Findings, DecisionLedger, package map, roadmap | Equal |

Each criterion has one weighted owner: `competitive`.

## 3. Competitive-set standard

A competitor is admissible only when the comparison is materially aligned on:

- primary service category
- service geography
- target buyer type
- commercial intent
- active market presence
- observation timeframe

Minimum comparison set:

```text
3 named comparable competitors
```

Use fewer only when the market genuinely contains fewer comparable providers and the limitation is documented.

Exclude or clearly qualify:

- national directories
- lead aggregators
- franchises outside the service market
- adjacent service businesses
- inactive businesses
- businesses selected only because they strengthen a preferred conclusion

## 4. Required evidence surfaces

### Primary evidence

- named competitor matrix with service, geography, buyer type, URL, and observation date
- review count, rating, recency, and visible response comparison
- website and GBP screenshots where relevant
- service-page and URL inventories
- project proof, before/after, testimonial, and case-study comparison
- homepage and priority-service messaging comparison
- documented target-search observations with term, location context, device/context limitation, and date
- mobile inquiry-path review
- CTA, phone, form, booking, confirmation, and next-step comparison
- content inventory with topic, service relevance, date, and buyer usefulness
- cross-page clarity, consistency, proof, and professional presentation review
- roadmap and DecisionLedger evidence for material gaps

### Supporting evidence

- client-defined competitor list
- Search Console
- analytics
- review exports
- local rank tracking
- competitor content archive
- CRM or sales evidence when directly relevant and authorized
- prior dated comparison records

### Evidence that cannot support a point score alone

- evaluator memory
- one undated screenshot
- one personalized search result
- unsupported claims of market leadership
- social follower count without relevance or quality analysis
- visual preference stated as competitive weakness
- competitor software stack assumptions
- estimated competitor revenue, leads, market share, or conversion rate

## 5. Minimum evaluation scope

A Competitive category score is admissible only when the evaluator reviews:

1. at least three named comparable competitors, unless a documented market limitation applies
2. review profiles for the business and each competitor
3. homepage and at least two comparable priority-service pages per business, or all when fewer exist
4. visible project, testimonial, and case-study proof
5. at least five documented target local searches across relevant service intent, with limitations recorded
6. primary mobile conversion path for each compared business
7. at least six months of visible content activity, or all available activity when newer
8. cross-surface professional consistency
9. every material competitive finding proposed for the roadmap
10. package and DecisionLedger routing for reported gaps

Incomplete scope requires `provisional`, `range_only`, or `blocked` publication based on materiality.

## 6. Applicability rules

All `OI-COMP-*` criteria are normally applicable.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-COMP-006` when no meaningful local search discovery path exists for the business model
- `OI-COMP-008` when ongoing public content is not commercially relevant and the absence is strategically documented

The following do not justify `not_applicable`:

- competitors could not be identified yet
- evidence was difficult to collect
- search results were inconsistent
- the business does not currently compete well
- the criterion would lower the score

Unresolved comparability normally produces `unknown`, `validation_required`, or `blocked`, not `not_applicable`.

## 7. Weighting rule

All applicable Competitive criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 8. Category-specific anchors

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is not permitted.

### Competitive-set reliability — `OI-COMP-001`

| Score | Observable condition |
|---:|---|
| 0 | No defensible competitive set exists, or the comparison set is materially unrelated or misleading. |
| 25 | Some competitors are named, but service, geography, buyer type, or active-market comparability is inconsistent. |
| 50 | A usable comparable set exists, but validation, coverage, documentation, or refresh cadence remains incomplete. |
| 75 | Named competitors are directly comparable, documented, dated, and consistently used across the assessment. |
| 100 | Competitive-set selection is governed through repeatable qualification, exclusion, review, refresh, and audit controls. |

### Reviews, service depth, proof, and messaging — `OI-COMP-002` through `OI-COMP-005`

| Score | Observable condition |
|---:|---|
| 0 | The business is materially weaker across the tested signal, or evidence is misleading, absent, or unusable for buyer comparison. |
| 25 | Some competitive capability exists, but material gaps remain in review strength, service coverage, proof, specificity, or differentiation. |
| 50 | The business has a functional competitive baseline, but competitors retain meaningful advantages in depth, recency, relevance, placement, or support. |
| 75 | The business is consistently competitive or stronger across named comparable providers on the tested signal. |
| 100 | Competitive strength is sustained through governed evidence capture, maintenance, differentiation, validation, and accountable refresh. |

### Local discovery and conversion paths — `OI-COMP-006`, `OI-COMP-007`

| Score | Observable condition |
|---:|---|
| 0 | The business is materially absent from validated discovery paths or its inquiry path is broken or substantially weaker than comparable competitors. |
| 25 | Visibility or inquiry access exists inconsistently, with material gaps across terms, devices, pages, or next-step expectations. |
| 50 | A functional baseline exists, but competitors are more consistently discoverable or easier to contact and understand. |
| 75 | The business is consistently visible for validated target intent and offers competitive, low-friction inquiry paths. |
| 100 | Discovery and conversion competitiveness are monitored through repeatable testing, measurement, exception handling, and governed improvement. |

### Content usefulness and professional consistency — `OI-COMP-008`, `OI-COMP-009`

| Score | Observable condition |
|---:|---|
| 0 | Public activity or presentation is materially absent, misleading, confusing, or damaging to buyer confidence relative to the market. |
| 25 | Some useful content or professional consistency exists, but it is stale, generic, irregular, unclear, or materially weaker than competitors. |
| 50 | Baseline usefulness and credibility are present, but strategic relevance, freshness, proof, hierarchy, or consistency remains incomplete. |
| 75 | Content and presentation consistently support buyer education, proof, clarity, and confidence at a competitive level. |
| 100 | Content and presentation are governed through standards, ownership, evidence controls, refresh cadence, quality review, and measured learning. |

### Roadmap conversion — `OI-COMP-010`

| Score | Observable condition |
|---:|---|
| 0 | Material competitive gaps are ignored, copied blindly, or converted into unsupported actions. |
| 25 | Gaps are listed, but ownership, materiality, package routing, sequencing, or evidence remains weak. |
| 50 | Major gaps are routed into a usable roadmap, but dependencies, prioritization, confidence, or ledger traceability remains incomplete. |
| 75 | Material gaps are evidence-backed, domain-owned, package-routed, sequenced, and traceable. |
| 100 | Competitive roadmap decisions are governed through recurring validation, DecisionLedger review, outcome evidence, and controlled reprioritization. |

## 9. Confidence guidance

| Confidence | Competitive-specific use |
|---|---|
| High | Dated, direct, like-for-like evidence confirms the selected anchor across named comparable competitors and required scope. |
| Medium | Public evidence supports the pattern, but one material limitation remains in timing, search variability, comparability, or coverage. |
| Low | Result depends on narrow samples, client recollection, incomplete competitor coverage, inaccessible surfaces, or unverified strategy assumptions. |
| Unknown | Evidence is insufficient to select an anchor. |

Confidence remains separate from maturity. Strong evidence of a competitive weakness may produce a low score with high confidence.

## 10. Unknown, blocked, and not-applicable treatment

Use `unknown` when evidence is insufficient or comparability cannot be established.

Use `blocked` when access, authorization, privacy, technical failure, or unstable evidence prevents defensible evaluation.

Use `not_applicable` only under Section 6.

Do not:

- score unknown as zero
- infer stable rank from one observation
- infer internal performance from visible presentation
- exclude stronger competitors to improve the score
- include unrelated competitors to worsen the score
- remove unknown or blocked criteria from applicable weight

A material unknown affecting competitor selection or search evidence may force `range_only` or `blocked` publication.

## 11. Duplicate-signal boundaries

| Competitive evidence | Primary implementation owner | Competitive treatment |
|---|---|---|
| Review count, recency, response, or GBP strength | GBP / Trust / Automation | Score relative market position; route correction to primary domain. |
| Missing or thin service pages | SEO / Website | Score the relative gap; do not duplicate the primary domain score. |
| Weak project proof or testimonials | Trust | Record competitive materiality and priority only. |
| Generic or unsupported messaging | Messaging / Trust | Route to messaging and proof systems. |
| Weak local search presence | SEO / GBP / Analytics | Qualify variability and route by evidence source. |
| Harder CTA, phone, form, or booking path | Conversion / Website | Score relative friction and route implementation. |
| Higher competitor content volume without proven usefulness | Analytics / SEO / Social | Do not award or penalize cadence without strategic relevance. |
| Offer or sales-process difference | Offer | Route only when the commercial structure is the primary cause. |

Competitive scoring must not create a second weighted score for the same underlying domain condition.

## 12. Finding and package routing

Weak criteria route only to approved `OI-FIND-COMP-*` records in `framework/findings/competitive-findings.md`.

There is no generic competitive implementation package.

| Competitive gap | Primary package | Typical roadmap phase |
|---|---|---|
| Review profile or request-system gap | Review Generation System, Trust Proof System, or Google Business Authority Pack | Phase 2 or Phase 3 |
| Service-page or local relevance gap | Local SEO Expansion Pack | Phase 2 — Growth Foundation |
| Project proof or case-study gap | Trust Proof System | Phase 2 — Growth Foundation |
| Messaging or decision-point clarity gap | Website Conversion Fix Pack and/or Trust Proof System | Phase 1 or Phase 2 |
| Search visibility gap | Local SEO Expansion Pack or Google Business Authority Pack | Phase 2 — Growth Foundation |
| Inquiry-path gap | Website Conversion Fix Pack | Phase 1 — Quick Wins |
| Unverified content-volume gap | Operator Dashboard Pack for validation | Phase 3 — Automation and Reporting |
| Roadmap governance gap | Re-route through DecisionLedger and existing domain package | Phase based on underlying finding |

A category score does not automatically create a finding or package recommendation.

## 13. Search-evidence control

Every search observation must record:

```yaml
query: ""
service_intent: ""
location_context: ""
device_or_context: ""
observation_date: YYYY-MM-DD
business_visible: true|false|unknown
competitors_visible: []
result_type: organic|map_pack|paid|directory|other
limitations: []
evidence_ref: ""
```

Search observations are snapshots, not permanent ranking claims. Use broader sampling, Search Console, or controlled rank evidence before making strong visibility assertions.

## 14. Publication controls

`official` publication requires:

- minimum scope completed
- category coverage at or above 80%
- valid competitive set
- dated and comparable evidence
- no unresolved duplicate-signal failure
- no unsupported internal-performance claim
- DecisionLedger references for reported findings

Use `provisional` when coverage is 60–79.99% or one material comparison limitation remains.

Use `range_only` when unresolved competitor selection, search variability, or missing evidence could materially change interpretation.

Use `blocked` when a defensible competitive set or minimum evidence cannot be established.

## 15. DecisionLedger minimum record

```yaml
category_key: competitive
criterion_ids: []
competitor_set: []
comparison_scope:
  services: []
  geography: ""
  buyer_type: ""
  observation_date: YYYY-MM-DD
evidence_refs: []
observation: ""
interpretation: ""
primary_domain: ""
business_impact: ""
confidence: high|medium|low|unknown
priority: critical|high|medium|low
finding_ids: []
primary_package: null
dependent_packages: []
roadmap_phase: null
unknowns: []
limitations: []
duplicate_check_passed: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 16. Validation messages

### Blocking errors

- `COMP-SET-001`: competitive set is undefined or not comparable
- `COMP-EVID-001`: scored criterion lacks dated comparable evidence
- `COMP-SCOPE-001`: minimum evaluation scope is incomplete
- `COMP-SEARCH-001`: search claim lacks query, context, date, or limitation record
- `COMP-DUP-001`: primary-domain condition is double counted
- `COMP-CLAIM-001`: unsupported competitor performance claim is present
- `COMP-ROUTE-001`: finding lacks primary-domain package routing
- `COMP-LEDGER-001`: reported finding lacks DecisionLedger traceability

### Warnings

- `COMP-COVER-001`: category coverage is below 80%
- `COMP-TIME-001`: evidence may be stale
- `COMP-SAMPLE-001`: comparison sample is narrow
- `COMP-CONTENT-001`: content volume is being treated as strategic value without evidence
- `COMP-POLISH-001`: presentation finding may rely on taste rather than buyer-confidence evidence

## 17. Worked example

Assume 10 applicable criteria:

- 8 criteria are scored
- scored values total 450
- 2 criteria are `unknown`

```text
Known Criterion Count = 8
Applicable Criterion Count = 10
Observed Category Score = 450 ÷ 8 = 56.25
Category Coverage = 8 ÷ 10 × 100 = 80%
```

The published category score is `56`, with `80%` coverage. Unknown criteria remain visible and retain applicable weight.

Executive-safe statement:

> The business has a functional competitive baseline, but comparable providers currently present stronger evidence in selected buyer-facing areas. Search and content observations are time-bound, and the recommended actions are routed to the primary domains responsible for each verified gap.

## 18. Completion checklist

Before publishing, confirm:

- all 10 criteria have valid states
- competitor set is named and comparable
- observation dates and limitations are recorded
- minimum scope is complete
- search evidence is qualified
- weights reconcile
- confidence is separate from maturity
- unknown and blocked criteria retain applicable weight
- visible presentation is not treated as internal performance
- duplicate ownership checks pass
- findings use approved `OI-FIND-COMP-*` identifiers
- every gap routes to an existing primary-domain package
- roadmap actions are original, evidence-backed, and not competitor imitation
- DecisionLedger references exist
- client language avoids unsupported rank, market-share, revenue, lead, conversion, and ROI claims

## 19. v1.0 connection

This sheet completes the category-level competitive scoring layer by converting relative market evidence into reproducible scores, controlled confidence, primary-domain routing, sequenced roadmap decisions, and auditable executive reporting required for commercial v1.0.