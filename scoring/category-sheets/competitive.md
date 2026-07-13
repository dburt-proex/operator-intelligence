# Competitive Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `competitive`  
Default Operator Score weight: 5%  
Status: Draft candidate for methodology approval

## 1. Purpose and category boundary

This sheet governs scoring for relative buyer-facing market position across named, comparable competitors.

It measures whether the business has a defensible competitive set and how its visible reviews, service coverage, trust proof, messaging, local discovery, conversion paths, content usefulness, professional consistency, and governed response compare within a defined service and geography.

It does not independently score internal competitor revenue, profitability, lead volume, conversion rate, operating quality, stable rank from one search observation, aesthetic preference, or primary-domain execution already owned by GBP, Trust, SEO, Messaging, Conversion, Website, Offer, Automation, or Analytics.

Competitive evidence may alter relative interpretation, confidence, priority, and sequencing. Implementation remains owned by the primary affected domain.

## 2. Included criterion prefix and inventory

Included prefix: `OI-COMP-*`

| Criterion ID | Observable condition | Minimum evidence | Default weighting |
|---|---|---|---|
| `OI-COMP-001` | Main competitors are identifiable and comparable | Competitor matrix, search evidence, client input | Equal |
| `OI-COMP-002` | Review profile is competitive | Dated review comparison | Equal |
| `OI-COMP-003` | Service-page depth is competitive | URL and service inventory | Equal |
| `OI-COMP-004` | Project and trust proof is competitive | Gallery, testimonial, case-study comparison | Equal |
| `OI-COMP-005` | Messaging is differentiated and proof-supported | Homepage and service-copy comparison | Equal |
| `OI-COMP-006` | Business appears for documented target local searches | Dated search evidence; Search Console when available | Equal |
| `OI-COMP-007` | Conversion paths are competitive | Mobile, CTA, phone, form, and next-step comparison | Equal |
| `OI-COMP-008` | Content activity is strategically competitive | Dated content inventory and usefulness review | Equal |
| `OI-COMP-009` | Professional presentation supports buyer confidence | Cross-surface consistency and clarity comparison | Equal |
| `OI-COMP-010` | Material competitive gaps are converted into governed roadmap actions | Findings, DecisionLedger, package map, roadmap | Equal |

Each criterion has one weighted owner: `competitive`.

## 3. Required evidence surfaces

### Primary evidence

- named competitor matrix with service, geography, buyer type, URL, and observation date
- review count, rating, recency, and visible response comparison
- website and GBP screenshots where relevant
- service-page and URL inventories
- project proof, testimonial, and case-study comparison
- homepage and priority-service messaging comparison
- documented target-search observations with term, location context, device or context limitation, and date
- mobile inquiry-path review
- CTA, phone, form, booking, confirmation, and next-step comparison
- content inventory with topic, service relevance, date, and buyer usefulness
- cross-surface clarity, consistency, proof, and professional presentation review
- roadmap and DecisionLedger evidence for material gaps

### Supporting evidence

Client-defined competitors, Search Console, analytics, review exports, controlled local rank tracking, CRM or sales evidence when authorized, and prior dated comparison records may strengthen confidence.

### Evidence that cannot support a point score alone

Evaluator memory, one undated screenshot, one personalized search result, unsupported market-leadership claims, follower count without relevance analysis, visual preference, competitor software assumptions, and estimated competitor revenue, leads, market share, or conversion rate are insufficient.

## 4. Minimum evaluation scope

A category score is admissible only when the evaluator reviews:

1. at least three named comparable competitors unless a documented market limitation applies
2. review profiles for the business and each competitor
3. homepage and at least two comparable priority-service pages per business, or all when fewer exist
4. visible project, testimonial, and case-study proof
5. at least five documented target local searches across relevant service intent, with limitations recorded
6. the primary mobile conversion path for each compared business
7. at least six months of visible content activity, or all available activity when newer
8. cross-surface professional consistency
9. every material competitive finding proposed for the roadmap
10. package and DecisionLedger routing for reported gaps

Incomplete scope requires `provisional`, `range_only`, or `blocked` publication based on materiality.

## 5. Applicability rules

All `OI-COMP-*` criteria are normally applicable.

Use `not_applicable` only when structural irrelevance is documented and approved. Difficulty collecting evidence, inconsistent search results, weak performance, or potential score reduction do not justify `not_applicable`.

Unresolved comparability normally produces `unknown`, `validation_required`, or `blocked`.

## 6. Criterion weighting rule

All applicable criteria use equal weighting:

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting requires a versioned methodology change under `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only `0`, `25`, `50`, `75`, and `100`. Interpolation is prohibited.

### `OI-COMP-001` — competitive-set reliability

| Score | Observable condition |
|---:|---|
| 0 | No defensible competitive set exists, or the set is materially unrelated or misleading. |
| 25 | Some competitors are named, but service, geography, buyer type, or active-market comparability is inconsistent. |
| 50 | A usable set exists, but validation, coverage, documentation, or refresh cadence is incomplete. |
| 75 | Named competitors are directly comparable, documented, dated, and consistently used. |
| 100 | Selection is governed through repeatable qualification, exclusion, review, refresh, and audit controls. |

### `OI-COMP-002` through `OI-COMP-005` — reviews, service depth, proof, and messaging

| Score | Observable condition |
|---:|---|
| 0 | The business is materially weaker across the tested signal, or evidence is misleading or unusable. |
| 25 | Capability exists, but material gaps remain in strength, depth, recency, relevance, placement, or support. |
| 50 | A functional baseline exists, but comparable providers retain meaningful advantages. |
| 75 | The business is consistently competitive or stronger across the tested signal. |
| 100 | Strength is sustained through governed evidence capture, maintenance, differentiation, validation, and accountable refresh. |

### `OI-COMP-006` and `OI-COMP-007` — local discovery and conversion paths

| Score | Observable condition |
|---:|---|
| 0 | The business is materially absent from validated discovery paths, or its inquiry path is broken or substantially weaker. |
| 25 | Visibility or inquiry access exists inconsistently across terms, devices, pages, or next steps. |
| 50 | A functional baseline exists, but competitors are more consistently discoverable or easier to contact and understand. |
| 75 | The business is consistently visible for validated intent and offers competitive, low-friction inquiry paths. |
| 100 | Discovery and conversion competitiveness are monitored through repeatable testing, measurement, exception handling, and governed improvement. |

### `OI-COMP-008` and `OI-COMP-009` — content usefulness and professional consistency

| Score | Observable condition |
|---:|---|
| 0 | Public activity or presentation is materially absent, misleading, confusing, or damaging to buyer confidence. |
| 25 | Some usefulness or consistency exists, but it is stale, generic, irregular, unclear, or materially weaker. |
| 50 | Baseline usefulness and credibility are present, but relevance, freshness, proof, hierarchy, or consistency is incomplete. |
| 75 | Content and presentation consistently support buyer education, proof, clarity, and confidence at a competitive level. |
| 100 | Content and presentation are governed through standards, ownership, evidence controls, refresh cadence, quality review, and measured learning. |

### `OI-COMP-010` — roadmap conversion

| Score | Observable condition |
|---:|---|
| 0 | Material competitive gaps are ignored, copied blindly, or converted into unsupported actions. |
| 25 | Gaps are listed, but ownership, materiality, routing, sequencing, or evidence is weak. |
| 50 | Major gaps are routed into a usable roadmap, but dependencies, prioritization, confidence, or traceability is incomplete. |
| 75 | Material gaps are evidence-backed, domain-owned, package-routed, sequenced, and traceable. |
| 100 | Roadmap decisions are governed through recurring validation, DecisionLedger review, outcome evidence, and controlled reprioritization. |

## 8. Confidence assignment guidance

| Confidence | Competitive-specific use |
|---|---|
| High | Dated, direct, like-for-like evidence confirms the anchor across named comparable competitors and required scope. |
| Medium | Evidence supports the pattern, but one material limitation remains in timing, search variability, comparability, or coverage. |
| Low | The result depends on narrow samples, client recollection, incomplete coverage, inaccessible surfaces, or unverified assumptions. |
| Unknown | Evidence is insufficient to select an anchor. |

Confidence remains separate from maturity. Strong evidence of a weakness may produce a low score with high confidence.

## 9. Unknown, blocked, and not-applicable treatment

Use `unknown` when evidence is insufficient or comparability cannot be established. Use `blocked` when access, authorization, privacy, technical failure, or unstable evidence prevents defensible evaluation. Use `not_applicable` only under Section 5.

Do not score unknown as zero, infer stable rank from one observation, infer internal performance from public appearance, manipulate the competitor set, or remove unknown and blocked criteria from applicable weight.

Every material unknown must record reason code, requested evidence or test, validation owner, materiality, next action, and publication effect.

## 10. Duplicate-signal boundaries

| Competitive evidence | Primary implementation owner | Competitive treatment |
|---|---|---|
| Review count, recency, response, or GBP strength | GBP / Trust / Automation | Score relative position; route correction to the primary domain. |
| Missing or thin service pages | SEO / Website | Score the relative gap; do not duplicate the primary-domain score. |
| Weak project proof or testimonials | Trust | Record competitive materiality and priority only. |
| Generic or unsupported messaging | Messaging / Trust | Route to messaging and proof systems. |
| Weak local search presence | SEO / GBP / Analytics | Qualify variability and route by evidence source. |
| Harder CTA, phone, form, or booking path | Conversion / Website | Score relative friction and route implementation. |
| Content volume without proven usefulness | Analytics / SEO / Social | Do not award or penalize cadence without strategic relevance. |
| Offer or sales-process difference | Offer | Route only when commercial structure is the primary cause. |

Competitive scoring must not create a second weighted score for the same underlying domain condition.

## 11. Finding and recommendation routing

Weak criteria route only to approved `OI-FIND-COMP-*` records in `framework/findings/competitive-findings.md`. There is no generic competitive implementation package.

A category score does not automatically create a finding or recommendation. A valid recommendation requires observation, evidence, interpretation, bounded business impact, confidence, priority, exactly one primary package, roadmap phase, and DecisionLedger record.

Common routing:

| Competitive gap | Primary package | Typical roadmap phase |
|---|---|---|
| Review profile or request-system gap | Review Generation System, Trust Proof System, or Google Business Authority Pack | Phase 2 or Phase 3 |
| Service-page or local relevance gap | Local SEO Expansion Pack | Phase 2 — Growth Foundation |
| Project proof or case-study gap | Trust Proof System | Phase 2 — Growth Foundation |
| Messaging or inquiry-path gap | Website Conversion Fix Pack or Trust Proof System | Phase 1 or Phase 2 |
| Unverified content-volume gap | Operator Dashboard Pack for validation | Phase 3 — Automation and Reporting |
| Roadmap governance gap | Re-route through DecisionLedger and the existing domain package | Based on underlying finding |

## 12. Publication controls

`official` publication requires minimum scope, coverage at or above 80%, a valid competitive set, dated comparable evidence, no unresolved duplicate-signal failure, no unsupported performance claim, and DecisionLedger references for reported findings.

Use `provisional` when coverage is 60–79.99% or one bounded comparison limitation remains. Use `range_only` when competitor selection, search variability, or missing evidence could materially change interpretation. Use `blocked` when a defensible competitive set or minimum evidence cannot be established.

Search observations are time-bound snapshots and must record query, service intent, location context, device or context, observation date, result type, competitors visible, limitations, and evidence reference.

## 13. DecisionLedger minimum record

```yaml
category_key: competitive
category_sheet_version: "0.2"
criterion_inventory_version: ""
score_run_id: OI-SCORE-YYYY-NNN
competitor_set: []
comparison_scope:
  services: []
  geography: ""
  buyer_type: ""
  observation_date: YYYY-MM-DD
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
evidence_refs: []
observed_score: null
lower_bound: null
upper_bound: null
coverage: null
confidence_index: null
publication_state: range_only
finding_refs: []
recommendation_refs: []
primary_package: null
roadmap_phase: null
material_unknowns: []
duplicate_check_passed: false
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 14. Validation messages

### Blocking errors

- `CAT-COMP-SCOPE-001`: minimum comparison scope is incomplete
- `CAT-COMP-EVID-001`: a scored criterion lacks dated comparable evidence
- `CAT-COMP-MAP-001`: criterion inventory or category mapping is incomplete
- `CAT-COMP-DUP-001`: a primary-domain condition is double counted
- `CAT-COMP-UNKNOWN-001`: a material unknown lacks required validation treatment
- `CAT-COMP-WEIGHT-001`: internal weights do not reconcile
- `CAT-COMP-GATE-001`: competitor selection, unsupported claim, or governance boundary blocks publication
- `CAT-COMP-LEDGER-001`: a material output lacks DecisionLedger traceability

### Warnings

- `CAT-COMP-RECENCY-001`: comparison evidence may be stale
- `CAT-COMP-SAMPLE-001`: comparison sample is narrow
- `CAT-COMP-CONTENT-001`: content volume is being treated as strategic value without evidence
- `CAT-COMP-POLISH-001`: presentation judgment may rely on taste rather than buyer-confidence evidence

## 15. Worked scoring example

Assume ten applicable criteria with equal 10% internal weight.

| Criterion | State | Evidence ref | Score | Confidence | Factor | Lower | Upper |
|---|---|---|---:|---|---:|---:|---:|
| `OI-COMP-001` | scored | `OI-EV-2026-4101` | 75 | High | 1.00 | 75 | 75 |
| `OI-COMP-002` | scored | `OI-EV-2026-4102` | 50 | High | 1.00 | 50 | 50 |
| `OI-COMP-003` | scored | `OI-EV-2026-4103` | 50 | High | 1.00 | 50 | 50 |
| `OI-COMP-004` | scored | `OI-EV-2026-4104` | 25 | Medium | 0.75 | 12.5 | 37.5 |
| `OI-COMP-005` | scored | `OI-EV-2026-4105` | 50 | Medium | 0.75 | 37.5 | 62.5 |
| `OI-COMP-006` | unknown | `OI-EV-2026-4106` | — | Unknown | 0.00 | 0 | 100 |
| `OI-COMP-007` | scored | `OI-EV-2026-4107` | 75 | High | 1.00 | 75 | 75 |
| `OI-COMP-008` | unknown | `OI-EV-2026-4108` | — | Unknown | 0.00 | 0 | 100 |
| `OI-COMP-009` | scored | `OI-EV-2026-4109` | 50 | Medium | 0.75 | 37.5 | 62.5 |
| `OI-COMP-010` | scored | `OI-EV-2026-4110` | 75 | High | 1.00 | 75 | 75 |

Calculations:

```text
Known Criterion Weight = 80%
Applicable Criterion Weight = 100%
Observed Category Score = (75 + 50 + 50 + 25 + 50 + 75 + 50 + 75) ÷ 8 = 56.25
Category Coverage = 80 ÷ 100 = 80%
Category Lower Bound = (75 + 50 + 50 + 12.5 + 37.5 + 0 + 75 + 0 + 37.5 + 75) ÷ 10 = 41.25
Category Upper Bound = (75 + 50 + 50 + 37.5 + 62.5 + 100 + 75 + 100 + 62.5 + 75) ÷ 10 = 68.75
Category Confidence Index = ((1 + 1 + 1 + 0.75 + 0.75 + 1 + 0.75 + 1) ÷ 8) = 0.90625
Display Score = 56
Display Range = 41–69
```

Publication state: `range_only` because the unknown local-search and content-usefulness criteria could materially change the relative interpretation despite 80% coverage.

Routing outcome:

- `OI-COMP-004` supports an approved competitive finding concerning weaker visible project proof.
- Primary implementation owner: Trust.
- Primary package: `OI-PKG-TRUST-001` Trust Proof System.
- Roadmap phase: Phase 2 — Growth Foundation.
- `OI-COMP-006` and `OI-COMP-008` create validation actions only; they do not create recommendations.
- DecisionLedger reference: `OI-DL-2026-410`.

Executive-safe statement:

> The reviewed evidence supports a functional competitive baseline, with a verified weakness in visible project proof. Local-search and content-usefulness comparisons remain unresolved, so the current evidence supports a range rather than a single official category result.

## 16. Completion checklist

- [ ] all ten criteria have valid states and evidence references
- [ ] competitor set is named and comparable
- [ ] observation dates and limitations are recorded
- [ ] minimum scope is complete
- [ ] weights reconcile
- [ ] confidence remains separate from maturity
- [ ] unknown and blocked criteria retain applicable weight
- [ ] bounds, coverage, and confidence index reproduce
- [ ] duplicate ownership checks pass
- [ ] findings use approved `OI-FIND-COMP-*` identifiers
- [ ] each recommendation has exactly one primary package
- [ ] DecisionLedger references exist
- [ ] client language avoids unsupported rank, market-share, revenue, lead, conversion, and ROI claims
- [ ] reviewer approves this sheet version

## 17. Governance and usage

Evaluators must use this sheet with `scoring/calculator-spec.md`, `scoring/unknown-data-handling.md`, `scoring/confidence-adjusted-scoring.md`, `framework/findings/competitive-findings.md`, and the publication and quality-control standards.

Until reviewer approval is recorded, the calculator must use the general rubric and equal weighting while marking this category-sheet guidance as unavailable.

Material changes to category boundaries, criterion ownership, anchors, evidence thresholds, weighting, duplicate rules, or publication controls require a version increment, rationale, regression example, impact review, DecisionLedger entry, and methodology approval.

## 18. v1.0 connection

This sheet makes competitive scoring reproducible and auditable by connecting comparable market evidence to criterion states, uncertainty bounds, confidence, findings, primary-domain implementation routing, roadmap phases, publication controls, and DecisionLedger records required for commercial v1.0.
