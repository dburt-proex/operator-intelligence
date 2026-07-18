# Local SEO Category Scoring Sheet

Version: v0.2 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `seo`  
Default Operator Score weight: 15%  
Status: Reconciled commercial v1.0 scoring contract

## 1. Purpose and category boundary

This sheet governs scoring for local SEO readiness and discoverability.

The category measures whether the website and supporting local search signals create clear, indexable, service-specific, locally relevant paths for high-intent buyers.

It includes:

- service-page coverage
- high-value service coverage
- title tags and meta descriptions
- H1 alignment
- internal linking
- local service-area content
- buyer-intent content depth
- image alt context
- URL clarity
- indexability
- XML sitemap status
- service-led content strategy
- project or case-study content
- citation consistency
- applicable structured data

It does not independently score:

- website usability or navigation quality
- message strength or offer clarity
- CTA effectiveness or inquiry capture
- Google Business Profile completeness
- review quality or trust depth
- analytics instrumentation or reporting quality
- competitor performance beyond evidence needed to interpret search pressure

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix:

```text
OI-SEO-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-SEO-001` | Core services have dedicated pages | Service list, URL inventory, sitemap | Equal |
| `OI-SEO-002` | High-value services have dedicated pages | Priority service list versus URL inventory | Equal |
| `OI-SEO-003` | Title tags include service and location where appropriate | Title-tag inventory or crawl | Equal |
| `OI-SEO-004` | Meta descriptions are unique, specific, and action-oriented | Meta-description inventory or crawl | Equal |
| `OI-SEO-005` | H1 headings clearly match page intent | H1 inventory and page review | Equal |
| `OI-SEO-006` | Internal links support discovery of priority pages | Link crawl and manual page review | Equal |
| `OI-SEO-007` | Website contains accurate service-area content | Homepage, footer, service-area and location pages | Equal |
| `OI-SEO-008` | Service pages answer common buyer questions | Service-page and FAQ review | Equal |
| `OI-SEO-009` | Important images use descriptive alt text | Image and alt-attribute review | Equal |
| `OI-SEO-010` | URLs are clean and descriptive | URL inventory | Equal |
| `OI-SEO-011` | Important pages are technically indexable | Robots, canonical, noindex, response and search checks | Equal |
| `OI-SEO-012` | XML sitemap exists and reflects current indexable pages | Sitemap file and CMS settings | Equal |
| `OI-SEO-013` | Content targets service and buyer intent | Content inventory and topic-to-service mapping | Equal |
| `OI-SEO-014` | Project or case-study content is indexable and descriptive | Project pages, gallery, blog or case-study review | Equal |
| `OI-SEO-015` | Local citations use consistent business information | Citation audit and approved business record | Equal |
| `OI-SEO-016` | Relevant structured-data opportunities are addressed | Rendered source, validator output or schema inventory | Equal |

Each criterion has one weighted owner: `seo`.

## 3. Required evidence surfaces

### Primary evidence

- approved service inventory
- priority or high-value service list when available
- complete public URL inventory or crawl
- XML sitemap
- homepage and all core service pages
- title, meta-description and H1 inventory
- internal-link review for priority service pages
- service-area and location content
- indexability checks for sampled priority pages
- project, gallery or case-study inventory
- citation sample against approved business information
- structured-data inspection on representative page types

### Supporting evidence

- Google Search Console coverage and performance exports
- CMS page and indexing settings
- robots.txt and canonical configuration
- rank-tracking or SERP evidence with date and location
- competitor service-page comparison
- content briefs and keyword-to-page maps
- schema validator output
- client-approved name, address, phone and website record

### Evidence that cannot support a point score alone

- keyword-volume estimates without page evidence
- a single search result observed without location, date and query controls
- client claims that pages rank without current source evidence
- tool-generated SEO grades without underlying observations
- sitemap presence without page-level indexability checks
- schema markup present in source but invalid or irrelevant
- one page used to infer site-wide metadata, linking or content quality

## 4. Minimum evaluation scope

An SEO category score is admissible only when the evaluator reviews, where present:

1. all core and priority services against the public URL inventory
2. homepage
3. at least three core service pages, or all when fewer than three exist
4. all high-value service pages identified by the client, or a documented access limitation
5. title, meta description, H1 and URL structure for the sampled pages
6. internal links into and out of each sampled priority page
7. service-area content and at least one location page when location pages exist
8. robots.txt, XML sitemap and page-level indexability for sampled priority pages
9. at least five representative images across priority pages
10. project or case-study content where the business has completed-work assets
11. at least five material citation sources, or all identified sources when fewer than five exist
12. structured data on homepage and representative service, FAQ, breadcrumb and review-bearing pages where present

A narrow page sample cannot be generalized to the full category unless the evidence establishes a site-wide configuration.

Scope exceptions require a documented limitation and may reduce publication to `provisional`, `range_only`, or `blocked`.

## 5. Applicability rules

All `OI-SEO-*` criteria are normally applicable to a local-service business using a public website to support discovery.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-SEO-014` when the business has no completed-work model and project content would misrepresent the service
- `OI-SEO-015` when the business operates without public local identity or citations by approved design
- `OI-SEO-016` when no relevant structured-data type applies to the reviewed page type

The following do not justify `not_applicable`:

- Search Console was not provided
- the site could not be crawled by the evaluator's preferred tool
- citation access was incomplete
- project assets were not supplied
- schema was difficult to inspect
- the criterion would lower the score

Confirmed public absence after required inspection may support score `0`. Missing internal access normally produces `unknown` or `blocked`.

## 6. Criterion weighting rule

All applicable SEO criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight.

Approved `not_applicable` criteria are removed before weights are recalculated.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`.

### Service and local page coverage — `OI-SEO-001`, `OI-SEO-002`, `OI-SEO-007`

| Score | Observable condition |
|---:|---|
| 0 | Core or priority services have no discoverable page coverage, or local claims are materially false or misleading. |
| 25 | Some services or locations appear, but major gaps, thin consolidation, or inconsistent local relevance remain. |
| 50 | Core services have baseline coverage, but high-value services, service areas, or page depth are incomplete. |
| 75 | Core and priority services have clear dedicated pages with accurate local relevance across the assessed market. |
| 100 | Coverage is complete, intentionally mapped, monitored, governed and maintained against service and market changes. |

### Metadata, headings and URLs — `OI-SEO-003`, `OI-SEO-004`, `OI-SEO-005`, `OI-SEO-010`

| Score | Observable condition |
|---:|---|
| 0 | Priority pages are missing, duplicated, misleading or technically unusable in one or more core elements. |
| 25 | Elements exist but are generic, duplicated, inconsistent, poorly structured or weakly aligned to page intent. |
| 50 | Most sampled pages have functional baseline elements with material consistency or intent-alignment gaps. |
| 75 | Sampled priority pages consistently use unique, descriptive and intent-aligned titles, descriptions, H1s and URLs. |
| 100 | Elements are complete, governed, tested, monitored and maintained through a controlled page-publication process. |

### Internal discovery and buyer-intent content — `OI-SEO-006`, `OI-SEO-008`, `OI-SEO-013`, `OI-SEO-014`

| Score | Observable condition |
|---:|---|
| 0 | Priority pages are orphaned, content is misleading, or published material fails to support the represented service. |
| 25 | Links and content exist but are thin, generic, disconnected from buyer questions, or focused on low-intent topics. |
| 50 | A functional baseline supports discovery and service understanding, but material topic, proof or linking gaps remain. |
| 75 | Priority pages are well connected and answer service-specific questions using relevant process, project and decision content. |
| 100 | Content and linking are mapped to buyer journeys, measured, governed, refreshed and connected to service priorities. |

### Image context and structured data — `OI-SEO-009`, `OI-SEO-016`

| Score | Observable condition |
|---:|---|
| 0 | Important image context is absent or misleading, or structured data materially misrepresents the business. |
| 25 | Some descriptive attributes or markup exist but are sparse, generic, invalid or inconsistently applied. |
| 50 | Representative pages use a functional baseline with material coverage or validation gaps. |
| 75 | Relevant images are described and applicable structured data is valid and consistently implemented. |
| 100 | Coverage is validated, governed, maintained and included in publication quality control. |

### Indexability and sitemap controls — `OI-SEO-011`, `OI-SEO-012`

| Score | Observable condition |
|---:|---|
| 0 | Important pages are confirmed blocked, noindexed, canonicalized incorrectly, broken or absent from required discovery paths. |
| 25 | Indexing controls exist but contain material errors, stale sitemap entries, conflicts or unreliable coverage. |
| 50 | Priority pages are generally indexable and a sitemap exists, but validation or maintenance gaps remain. |
| 75 | Priority pages pass indexability checks and the sitemap accurately reflects intended indexable content. |
| 100 | Indexability is monitored, exceptions are governed, sitemap integrity is maintained and issues have accountable owners. |

### Citation consistency — `OI-SEO-015`

| Score | Observable condition |
|---:|---|
| 0 | Material public sources use conflicting identity data that is confirmed against the approved business record. |
| 25 | Multiple material inconsistencies, duplicates or stale records are present. |
| 50 | Major sources are mostly consistent, but some material cleanup or ownership gaps remain. |
| 75 | Material citation sources consistently use approved business identity information. |
| 100 | Citation identity is governed, monitored, corrected through an owned process and reconciled after business changes. |

Interpolation is not permitted.

## 8. Confidence assignment guidance

| Confidence | SEO-specific use |
|---|---|
| High | Direct page, crawl, metadata, indexability, sitemap, citation and structured-data evidence supports the selected anchor across required scope. |
| Medium | Public evidence is strong, but one representative page group, internal configuration, citation subset or search-performance source remains incomplete. |
| Low | The result relies on narrow sampling, stale exports, uncontrolled search observations, client claims or incomplete technical checks. |
| Unknown | Evidence is insufficient to select a maturity anchor. |

Search Console absence does not automatically reduce maturity, but it may limit confidence in index status or performance conclusions.

High confidence on one page type does not establish full-category coverage.

Confidence remains separate from maturity score.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- approved service or priority-service inventory is unavailable
- Search Console is unavailable where index status cannot be otherwise validated
- citation records cannot be reconciled to an approved business identity record
- CMS-generated canonicals, sitemap rules or noindex settings cannot be inspected
- structured data cannot be validated on rendered production pages
- project-content applicability is unresolved

Common `blocked` conditions:

- authentication or permissions prevent required inspection
- robots or security controls prevent any reliable public or authorized crawl
- production and staging versions conflict materially
- third-party citation tools or records are unavailable and no substitute sample is possible
- legal, privacy or platform restrictions prevent authorized evidence collection

Every material unknown or block must record:

- reason code
- affected criterion
- evidence or test required
- validation owner
- materiality
- next action
- publication effect

Unknown is not score `0`.

Confirmed public absence may support score `0` only after the required search or test is completed.

## 10. Duplicate-signal boundaries

| Overlap | SEO owns | Adjacent category owns |
|---|---|---|
| Website | Search-oriented page coverage, URLs and internal discovery support | General navigation, usability, hierarchy and buyer-path accessibility |
| Messaging and offer | Search-intent alignment and discoverable service-topic coverage | Positioning, differentiation, offer clarity and objection handling |
| Conversion | Discoverability of high-intent entry pages | CTA strength, form capture, confirmation and inquiry-path effectiveness |
| GBP | Website-side local relevance and profile-to-page alignment dependency | Profile existence, categories, services, photos, posts, Q&A and profile operations |
| Trust | Search visibility of project or authority content as a page asset | Validity, recency, credibility and depth of proof |
| Analytics | Technical discoverability and indexability state | Search reporting, instrumentation, interpretation and decision use |
| Competitive | Search architecture on the assessed business website | Comparative market position and competitor evidence model |

One page may support several criteria only when each criterion measures a distinct condition.

Duplicate scoring is prohibited when service coverage, message quality, conversion quality, trust quality or analytics availability are treated as the same signal.

## 11. Finding and recommendation routing

A weak SEO score does not automatically create a finding or package recommendation.

Eligible primary finding domain:

```text
OI-FIND-SEO-*
```

Common governed routing:

| Evidence-backed condition | Primary route | Common package dependency |
|---|---|---|
| Core or high-value service pages are missing | `OI-FIND-SEO-001` or `OI-FIND-SEO-002` | Local SEO Expansion Pack |
| Local targeting is broad or inconsistent | `OI-FIND-SEO-003` or `OI-FIND-SEO-004` | Local SEO Expansion Pack |
| Titles, headings, URLs or metadata are weak | `OI-FIND-SEO-005`, `006`, `007` or `018` | Local SEO Expansion Pack |
| Internal links do not support priority pages | `OI-FIND-SEO-008` | Local SEO Expansion Pack |
| Buyer-intent content or FAQs are thin | `OI-FIND-SEO-009`, `010` or `012` | Local SEO Expansion Pack |
| Local project proof is missing | `OI-FIND-SEO-011` with Trust dependency | Trust Proof System plus Local SEO Expansion Pack |
| Technical basics are not validated or fail | `OI-FIND-SEO-013` | Local SEO Expansion Pack; analytics validation when measurement is required |
| Competitors have stronger service coverage | `OI-FIND-SEO-014` with Competitive dependency | Local SEO Expansion Pack |
| Citation or authority signals are weak | `OI-FIND-SEO-015` | Google Business Authority Pack or Trust Proof System |
| GBP and website service coverage do not align | `OI-FIND-SEO-016` with GBP dependency | Google Business Authority Pack plus Local SEO Expansion Pack |
| Seasonal or urgent demand lacks page coverage | `OI-FIND-SEO-017` | Local SEO Expansion Pack |

Routing requires observation, evidence, interpretation, business impact, confidence, priority, package fit, roadmap phase and DecisionLedger traceability.

Package-first selling is prohibited.

Ranking, traffic, lead-volume and revenue promises are prohibited unless validated data supports the statement.

## 12. Publication controls

Use the common publication states:

| State | SEO-specific minimum treatment |
|---|---|
| `official` | Required scope is met; score, confidence, coverage, range and material unknowns are published. |
| `provisional` | A qualified point score is supportable, but one material page group, citation subset or internal control remains unresolved. |
| `range_only` | Missing scope or material technical uncertainty prevents responsible point precision. |
| `blocked` | Required inspection cannot be performed or traceability is incomplete. |

Additional controls:

- `OI-SEO-011` cannot receive a positive point score from sitemap presence alone.
- citation conclusions require comparison against an approved business identity record.
- ranking or traffic conclusions require dated, attributable evidence.
- invalid or misleading schema triggers `REVIEW` and may trigger `HALT` if client-facing claims are materially affected.
- a high-materiality unknown affecting core service indexability may force `range_only` even when overall numeric coverage exceeds the normal threshold.

## 13. DecisionLedger requirements

Each SEO category result must retain:

```yaml
category_key: seo
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2"
score_run_id: OI-SCORE-YYYY-NNN
applicable_criteria: []
scored_criteria: []
unknown_criteria: []
blocked_criteria: []
not_applicable_criteria: []
observed_score: null
lower_bound: null
upper_bound: null
coverage: null
confidence_index: null
publication_state: range_only
service_inventory_ref: ""
url_inventory_ref: ""
indexability_evidence_refs: []
citation_evidence_refs: []
material_unknowns: []
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
roadmap_phase_refs: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Each routed finding must preserve:

```text
Evidence → Observation → Interpretation → Business impact → Confidence → Priority → Package fit → Roadmap phase → Action
```

## 14. Validation messages

| Code | Blocking condition | Required correction |
|---|---|---|
| `CAT-SEO-SCOPE-001` | Required service, page or technical scope is incomplete | Complete the missing review or downgrade publication state |
| `CAT-SEO-EVID-001` | Selected anchor is unsupported by direct evidence | Add evidence or revise the anchor |
| `CAT-SEO-MAP-001` | An `OI-SEO-*` criterion is missing, duplicated or owned elsewhere | Repair criterion inventory mapping |
| `CAT-SEO-DUP-001` | SEO condition is also scored as website, messaging, conversion, trust, GBP, analytics or competitive performance | Assign one primary owner and record dependencies |
| `CAT-SEO-UNKNOWN-001` | A material service, indexability, citation or schema unknown is unresolved | Record validation owner, next action and publication effect |
| `CAT-SEO-WEIGHT-001` | Applicable criterion weights do not reconcile to 100% | Recalculate after approved applicability decisions |
| `CAT-SEO-GATE-001` | Ranking, traffic, lead or revenue claim lacks validated evidence | Remove or qualify the claim before publication |
| `CAT-SEO-LEDGER-001` | Evidence, finding or recommendation traceability is incomplete | Complete the DecisionLedger record |

## 15. Canonical worked scoring example

The controlled regression fixture is:

```text
scoring/examples/seo-worked-example.md
```

The fixture evaluates all 16 applicable criteria and produces:

```text
Observed provisional score = 53.33
Coverage = 93.75%
Confidence index = 0.9167
Defensible range = 46.09–60.16
Publication state = provisional
Review state = REVIEW
Implementation authorized = false
```

`OI-SEO-015` remains unknown because the five-source citation sample cannot be reconciled without an approved business identity record. The unresolved applicable weight contributes `0–100` to the category range and cannot be removed or scored as zero. Because the unknown is confined to a material citation subset rather than core indexability, the governed output is a qualified provisional score with a disclosed range.

The verified priority-service architecture condition routes through `OI-FIND-SEO-002` to exactly one primary package, `OI-PKG-SEO-001`, in `Phase 2 — Growth Foundation`. Citation remediation remains validation-only and does not independently create a GBP, Trust, Dashboard, or additional SEO package commitment.

Example executive-safe statement:

> The reviewed site provides a functional local-search baseline, including dedicated core-service pages, clean URLs, indexable priority pages, and a sitemap aligned to the public inventory. One confirmed priority service remains consolidated inside a broad page, while metadata, internal linking, image context, project-page depth, and structured-data coverage remain uneven. Citation consistency could not be validated without an approved business identity record. The current evidence supports a provisional Local SEO score of 53.33 with a defensible range of 46.09–60.16. Validation and reviewed scope approval are required before official publication or implementation.

## 16. Completion checklist

- [ ] All 16 `OI-SEO-*` criteria are mapped exactly once.
- [ ] Service and priority-service inventories are documented.
- [ ] Required page, metadata, internal-link and technical scope is complete.
- [ ] Applicability decisions include approved rationale.
- [ ] Applicable criterion weights reconcile to 100%.
- [ ] Selected anchors are supported by observable evidence.
- [ ] Confidence is assigned independently from maturity.
- [ ] Unknown and blocked conditions use governed reason codes.
- [ ] Duplicate-signal boundaries pass review.
- [ ] Findings use governed `OI-FIND-SEO-*` IDs.
- [ ] Package routing follows evidence and business impact.
- [ ] Roadmap phase is assigned before report publication.
- [ ] Ranking, traffic, lead and revenue claims pass evidence gates.
- [ ] DecisionLedger traceability is complete.
- [ ] Worked example recalculates correctly.
- [ ] Reviewer approves category-sheet version.
