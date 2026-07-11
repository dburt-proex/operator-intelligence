# Google Business Profile Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `gbp`  
Default Operator Score weight: 10%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for Google Business Profile completeness, operational quality, buyer usefulness, and alignment with the business's actual services and website.

It measures:

- profile existence and findability
- primary and secondary category fit
- service-list completeness
- business-description specificity
- photo recency and usefulness
- review-volume competitiveness
- review velocity
- owner-response consistency
- Q&A management
- post or update activity
- alignment between GBP services and website service coverage

It does not independently score:

- website usability or page architecture
- website-side local SEO implementation
- review quality across all channels
- lead follow-up after a GBP inquiry
- analytics instrumentation or attribution
- social-platform activity outside GBP

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix:

```text
OI-GBP-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-GBP-001` | Profile exists, is findable, and is not materially duplicated | Branded and category search results, profile URL | Equal |
| `OI-GBP-002` | Primary category accurately reflects the core service | Profile category evidence, approved service inventory | Equal |
| `OI-GBP-003` | Secondary categories accurately support offered services | Category inventory, approved service inventory | Equal |
| `OI-GBP-004` | Major services are listed completely and accurately | GBP services, approved service inventory | Equal |
| `OI-GBP-005` | Business description is specific, current, and non-misleading | GBP description, approved business facts | Equal |
| `OI-GBP-006` | Photos are recent, relevant, and useful to buyers | Photo tab, upload dates, image sample | Equal |
| `OI-GBP-007` | Review count is competitive within a controlled local peer set | Review count and defined competitor sample | Equal |
| `OI-GBP-008` | Recent review activity demonstrates ongoing collection | Review dates across defined lookback period | Equal |
| `OI-GBP-009` | Owner responses are consistent and professional | Review-response sample | Equal |
| `OI-GBP-010` | Q&A is monitored and materially useful | Q&A section and response ownership evidence | Equal |
| `OI-GBP-011` | Posts or updates are used with reasonable recency | GBP update history | Equal |
| `OI-GBP-012` | GBP services align with corresponding website service coverage | GBP-to-website service map | Equal |

Each criterion has one weighted owner: `gbp`.

## 3. Required evidence surfaces

### Primary evidence

- live GBP profile URL
- branded desktop and mobile search results
- primary and secondary category evidence
- complete GBP service inventory
- current business description
- photo inventory with dates where visible
- all review counts and review dates required by the sample
- owner-response sample
- Q&A section
- posts or updates history
- approved service inventory
- website service-page inventory for alignment review
- defined local competitor sample for `OI-GBP-007`

### Supporting evidence

- authorized GBP manager screenshots
- platform exports
- business-information source of truth
- review-request process documentation
- photo-upload calendar
- ownership or verification records
- change log for categories, services, hours, and description

### Evidence that cannot support a point score alone

- client claims that the profile is optimized
- a third-party GBP grade without underlying observations
- one screenshot used to infer all profile fields
- competitor review counts without a documented comparison method
- current total review count without review-date analysis
- posting plans without published updates
- website service pages without the live GBP service inventory

## 4. Minimum evaluation scope

A GBP category score is admissible only when the evaluator reviews, where present:

1. branded search and at least one relevant category-plus-location search
2. the live profile and any visible duplicate profiles
3. primary and all visible secondary categories
4. all listed GBP services against the approved service inventory
5. the full business description
6. at least twelve recent profile photos, or all when fewer than twelve exist
7. current review count and rating
8. review dates covering at least the most recent twelve reviews or six months, whichever yields more evidence
9. owner responses for at least the most recent twelve reviews, or all when fewer than twelve exist
10. all visible Q&A items
11. at least six months of posts or updates, or the full available history when shorter
12. all major GBP services against corresponding website service pages
13. at least three directly comparable local competitors for review-count context, unless fewer credible peers exist

A single search observation cannot establish complete findability or duplicate status.

Scope exceptions require a documented limitation and may reduce publication to `provisional`, `range_only`, or `blocked`.

## 5. Applicability rules

All `OI-GBP-*` criteria are normally applicable when the business uses or should reasonably use a Google Business Profile for local discovery.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- no lawful or platform-compliant GBP can exist for the operating model
- `OI-GBP-010` when the Q&A feature is unavailable on the reviewed profile and this is platform-confirmed
- `OI-GBP-011` when posts are unavailable for the profile type and this is platform-confirmed

The following do not justify `not_applicable`:

- login access was not provided
- profile ownership is disputed
- competitor research was incomplete
- posting has not occurred
- review history is sparse
- the criterion would reduce the score

Confirmed public absence after required inspection may support score `0`. Missing authorized access normally produces `unknown` or `blocked` where public evidence is insufficient.

## 6. Criterion weighting rule

All applicable GBP criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight.

Approved `not_applicable` criteria are removed before weights are recalculated.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`.

### Profile existence, categories, and services — `OI-GBP-001` through `OI-GBP-004`

| Score | Observable condition |
|---:|---|
| 0 | Profile is absent, materially duplicated, misleading, unclaimed where ownership is required, or categories and services materially misrepresent the business. |
| 25 | Profile exists, but category selection or service coverage contains major gaps, conflicts, or stale information. |
| 50 | Profile is functional and generally accurate, but category precision, service completeness, or duplicate control remains materially incomplete. |
| 75 | Profile is clearly findable, categories are accurate, and major services are complete and consistent with the approved service inventory. |
| 100 | Profile ownership, duplicate control, categories, and services are accurate, governed, monitored, and maintained through an accountable change process. |

### Description and visual proof — `OI-GBP-005`, `OI-GBP-006`

| Score | Observable condition |
|---:|---|
| 0 | Description or imagery is absent, materially false, prohibited, or misleading. |
| 25 | Description and photos exist but are generic, stale, sparse, low-value, or inconsistent with current operations. |
| 50 | Baseline profile content is accurate and usable, but recency, specificity, coverage, or maintenance gaps remain. |
| 75 | Description is specific and current; photos regularly show real services, team, projects, equipment, or location-relevant proof. |
| 100 | Content is governed by an owned refresh cadence, quality standard, approval process, and documented source controls. |

### Review strength and response operations — `OI-GBP-007` through `OI-GBP-009`

| Score | Observable condition |
|---:|---|
| 0 | Review evidence is absent where expected, manipulated, materially misleading, or owner responses create material reputational harm. |
| 25 | Review count materially trails comparable peers, recent activity is weak, or responses are rare, generic, or inconsistent. |
| 50 | Review presence is functional, but competitive depth, velocity, response consistency, or ownership remains incomplete. |
| 75 | Review count is credible in the defined peer set, recent reviews are recurring, and owner responses are timely and specific. |
| 100 | Review generation and response are governed, measured, monitored, and tied to accountable post-service workflows without unsupported performance claims. |

For `OI-GBP-007`, competitive scoring requires a documented peer set based on comparable service, geography, and market visibility. Raw count alone is insufficient.

### Q&A and update activity — `OI-GBP-010`, `OI-GBP-011`

| Score | Observable condition |
|---:|---|
| 0 | Material questions are unanswered or inaccurate, or updates contain false, prohibited, or harmful claims. |
| 25 | Q&A and updates are absent, stale, inconsistent, or unmanaged despite clear buyer need. |
| 50 | Some useful activity exists, but cadence, ownership, completeness, or monitoring is inconsistent. |
| 75 | Material questions are addressed accurately and updates remain reasonably current and relevant. |
| 100 | Q&A and updates are governed through an owned monitoring, approval, refresh, and escalation process. |

### GBP-to-website alignment — `OI-GBP-012`

| Score | Observable condition |
|---:|---|
| 0 | GBP and website materially conflict on core services or direct buyers toward unavailable services. |
| 25 | Multiple major services are unmatched, outdated, or inconsistently named across GBP and website. |
| 50 | Core alignment exists, but material service, terminology, or landing-page gaps remain. |
| 75 | Major GBP services accurately align to corresponding website coverage and current business priorities. |
| 100 | Alignment is governed, monitored, versioned, and reviewed whenever services or profile content change. |

Interpolation is not permitted.

## 8. Confidence assignment guidance

| Confidence | GBP-specific use |
|---|---|
| High | Direct live-profile evidence, authorized screenshots where needed, controlled review sampling, approved service records, and documented competitor comparison support the selected anchor across required scope. |
| Medium | Public evidence is strong, but one internal ownership record, historical field state, competitor subset, or workflow record remains incomplete. |
| Low | Result relies on narrow screenshots, stale captures, client claims, incomplete peer comparison, or limited review history. |
| Unknown | Evidence is insufficient to select a maturity anchor. |

High confidence on public profile completeness does not establish high confidence in ownership, monitoring, or workflow governance.

Confidence remains separate from maturity score.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- authorized profile ownership or verification status cannot be established
- approved service inventory is unavailable
- category history or hidden secondary categories cannot be verified
- photo recency cannot be established from public evidence
- review-request workflow is claimed but not evidenced
- competitor comparability is unresolved
- Q&A or post history is only partially visible

Common `blocked` conditions:

- profile access restrictions prevent required inspection and public evidence is insufficient
- an ownership dispute prevents reliable validation
- platform suspension or merge activity prevents stable evaluation
- legal or privacy restrictions prevent authorized evidence capture
- duplicate profiles cannot be reliably resolved during the score run

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

| Overlap | GBP owns | Adjacent category owns |
|---|---|---|
| Website | Profile fields and buyer-facing GBP content | Website usability, navigation, structure, and page quality |
| SEO | GBP categories, services, description, media, reviews, Q&A, and updates | Website-side indexability, metadata, citations, local pages, and schema |
| Trust | GBP review volume, velocity, and owner-response operations | Cross-channel proof quality, credibility depth, credentials, warranties, and onsite trust placement |
| Conversion | Profile completeness and buyer-facing profile paths | Inquiry capture, form quality, confirmations, routing, and follow-up |
| Analytics | Observable GBP operating state | Instrumentation, attribution, reporting, trend interpretation, and decision use |
| Social | GBP updates only | Non-GBP social channels, content systems, and social engagement |

One evidence item may support multiple categories only when each category measures a distinct condition.

Duplicate scoring is prohibited.

## 11. Finding and recommendation routing

Eligible finding domain:

```text
OI-FIND-GBP-*
```

Use governed findings from `framework/findings/gbp-findings.md`.

A weak criterion does not automatically create a finding or recommendation. Routing requires:

1. evidence-backed observation
2. governed finding ID
3. stated business impact without unsupported lead or revenue claims
4. confidence assignment
5. priority assignment
6. recommendation fit
7. package fit
8. roadmap phase
9. DecisionLedger record

Common recommendation dependencies may include:

- profile ownership and duplicate cleanup
- category and service correction
- description rewrite
- photo capture and upload process
- review-request workflow
- owner-response operating standard
- Q&A monitoring
- post or update cadence
- GBP-to-website service alignment

Package-first selling is prohibited.

## 12. Publication controls

Apply the common publication states:

| State | GBP-specific requirement |
|---|---|
| `official` | Required scope is met; profile identity, service inventory, review sample, competitor context, and material unknowns are resolved or explicitly disclosed. |
| `provisional` | Point score is supportable, but one material ownership, historical, competitor, or workflow evidence gap remains. |
| `range_only` | Evidence supports directional maturity only; material criteria remain unknown or blocked. |
| `blocked` | Profile identity, duplicate status, or access conflict prevents a defensible category result. |

Publication must include score, confidence, evidence coverage, score range, material unknowns, and any competitor-sample limitations.

A high-materiality duplicate, suspension, ownership, or misrepresentation issue may force `REVIEW` or `HALT`.

## 13. DecisionLedger requirements

Each GBP result must retain:

```yaml
category_key: gbp
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2"
score_run_id: OI-SCORE-YYYY-NNN
profile_url: ""
profile_identity_status: verified|provisional|disputed|unknown
competitor_sample_ref: ""
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
material_unknowns: []
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
package_refs: []
roadmap_phase_refs: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Each recommendation record must trace:

```text
Evidence
→ Interpretation
→ Business impact
→ Confidence
→ Priority
→ Recommendation
→ Package
→ Roadmap phase
```

## 14. Validation messages

| Code | Blocking condition | Required correction |
|---|---|---|
| `CAT-GBP-SCOPE-001` | Minimum profile review scope not met | Complete the missing profile, review, Q&A, post, website-alignment, or competitor checks |
| `CAT-GBP-EVID-001` | Selected anchor exceeds observable evidence | Add direct evidence or lower the anchor |
| `CAT-GBP-MAP-001` | `OI-GBP-*` criterion is missing, duplicated, or mapped elsewhere | Reconcile criterion ownership and inventory |
| `CAT-GBP-DUP-001` | Same condition is scored in GBP and an adjacent category | Retain one primary owner and record the secondary effect as a dependency |
| `CAT-GBP-UNKNOWN-001` | Material unknown lacks owner or next action | Complete the unknown-data record |
| `CAT-GBP-WEIGHT-001` | Applicable criterion weights do not reconcile to 100% | Recalculate after approved applicability decisions |
| `CAT-GBP-GATE-001` | Ownership, duplication, suspension, or misrepresentation issue blocks publication | Resolve or escalate through the governance gate |
| `CAT-GBP-LEDGER-001` | Required traceability is missing | Complete the DecisionLedger record before publication |

## 15. Worked scoring example

Assume twelve criteria are applicable and equally weighted.

| Criterion | State | Score | Confidence |
|---|---|---:|---|
| `OI-GBP-001` | Scored | 75 | High |
| `OI-GBP-002` | Scored | 75 | High |
| `OI-GBP-003` | Scored | 50 | Medium |
| `OI-GBP-004` | Scored | 50 | High |
| `OI-GBP-005` | Scored | 50 | High |
| `OI-GBP-006` | Scored | 25 | Medium |
| `OI-GBP-007` | Unknown | — | Unknown |
| `OI-GBP-008` | Scored | 50 | High |
| `OI-GBP-009` | Scored | 75 | High |
| `OI-GBP-010` | Scored | 25 | Medium |
| `OI-GBP-011` | Scored | 25 | High |
| `OI-GBP-012` | Scored | 50 | High |

Observed score across eleven scored criteria:

```text
(75 + 75 + 50 + 50 + 50 + 25 + 50 + 75 + 25 + 25 + 50) ÷ 11 = 50.0
```

Coverage:

```text
11 ÷ 12 = 91.7%
```

Bounds with one unknown criterion:

```text
Lower bound = (550 + 0) ÷ 12 = 45.8
Upper bound = (550 + 100) ÷ 12 = 54.2
```

Publication state:

```text
provisional
```

Reason: numeric coverage is high, but `OI-GBP-007` remains unknown because no governed local peer set was established. The evaluator may publish `50.0`, range `45.8–54.2`, with the competitor-sample limitation disclosed.

Finding routing may proceed only for directly evidenced criteria. No finding may claim the review count is uncompetitive until `OI-GBP-007` is validated.

DecisionLedger reference:

```text
OI-DL-2026-GBP-001
```

## 16. Completion checklist

- [ ] All twelve `OI-GBP-*` criteria are mapped once
- [ ] Profile identity and duplicate status are verified
- [ ] Minimum evaluation scope is met
- [ ] Anchors are supported by direct evidence
- [ ] Competitor sample is governed before `OI-GBP-007` is scored
- [ ] Confidence is assigned separately from maturity
- [ ] Unknown and blocked criteria include reason, owner, and next action
- [ ] Duplicate-signal review passes
- [ ] Finding IDs exist in the governed GBP findings library
- [ ] Recommendation, package, and roadmap routing is evidence-led
- [ ] Publication state matches coverage and materiality
- [ ] Worked example recalculates correctly
- [ ] DecisionLedger record is complete
- [ ] Reviewer approves the sheet version
