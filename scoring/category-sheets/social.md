# Social Presence Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `social`  
Default Operator Score weight: 5%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for the observable quality, consistency, usefulness, and operating discipline of public social profiles and content.

It measures:

- branded profile completeness
- consistency of public business information
- recency and continuity of activity
- use of real project or service evidence
- buyer education
- proof and trust content
- clarity of social calls to action
- connection between social content and relevant website paths
- public response behavior
- alignment between content and service seasonality

It does not independently score:

- website structure or page design
- Google Business Profile operations
- review volume, velocity, or reputation performance
- technical SEO implementation
- lead-capture mechanics after a visitor leaves the social platform
- internal CRM, follow-up, or publishing automation
- revenue, lead volume, reach, engagement, or attribution without verified source data

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix:

```text
OI-SOC-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-SOC-001` | Facebook page exists, is identifiable, and uses current branding | Public Facebook page | Equal |
| `OI-SOC-002` | Social profiles use consistent business information | Profile names, phone, links, location or service area | Equal |
| `OI-SOC-003` | Recent activity demonstrates that profiles are maintained | Post dates and activity history | Equal |
| `OI-SOC-004` | Posts show real work, service delivery, or operational evidence | Project and process posts | Equal |
| `OI-SOC-005` | Content educates buyers and answers material questions | Educational post sample | Equal |
| `OI-SOC-006` | Content includes attributable proof and trust signals | Testimonials, crew, project, review, or process posts | Equal |
| `OI-SOC-007` | Profile buttons and posts provide clear next actions | Profile CTA and post CTA sample | Equal |
| `OI-SOC-008` | Social content connects buyers to relevant website content | Post links and destination pages | Equal |
| `OI-SOC-009` | Public comments and inquiries receive professional responses | Public reply sample and approved response records | Equal |
| `OI-SOC-010` | Content reflects relevant service seasonality and demand windows | Post history and campaign calendar | Equal |

Each criterion has one weighted owner: `social`.

This sheet must not create `OI-FIND-SOC-*` identifiers until a governed Social finding library is approved.

## 3. Required evidence surfaces

### Primary evidence

- all active public social profiles identified by the business
- Facebook page, when Facebook is a commercially relevant channel
- profile name, handle, description, category, phone, website link, location or service-area fields, and primary CTA
- most recent twelve posts per active platform, or all posts from the prior six months when fewer than twelve exist
- post dates and visible gaps in activity
- project, process, team, review, educational, seasonal, and promotional content samples
- outbound links from posts and the destination pages reached
- public comments and business replies on the sampled posts
- visible public response timestamps where available
- approved publishing calendar or campaign record when seasonality is scored above baseline

### Supporting evidence

- native platform exports or analytics
- content calendar
- post approval records
- media library with project attribution
- message-response SOP
- approved response templates
- social lead records
- UTM or campaign naming standards
- client confirmation of channel purpose and ownership

### Evidence that cannot support a point score alone

- follower count
- likes, impressions, reach, or engagement without context and verified source data
- one unusually successful or unsuccessful post
- evaluator preference for a platform or content style
- private messages described but not inspected
- scheduled drafts that were never published
- stock imagery used to imply completed work
- generic third-party social grades
- client statements that a profile is active when current public evidence does not confirm it

## 4. Minimum evaluation scope

A Social category score is admissible only when the evaluator:

1. identifies all active and claimed social profiles
2. reviews every profile used as a current customer-facing channel
3. inspects the most recent twelve posts per active platform, or all posts from the prior six months when fewer exist
4. compares profile business information against the approved source of truth and website
5. classifies sampled posts by real work, education, proof, CTA, website connection, and seasonality
6. opens and validates at least three outbound post links when three exist
7. reviews public business responses on at least ten comment or inquiry threads, or all when fewer exist
8. checks whether activity covers at least one relevant service-demand window when sufficient history exists
9. records platform access, sampling dates, unavailable surfaces, and channel ownership

A single active post, profile screenshot, or narrow platform sample cannot be generalized to the full category.

Private response-time or message-handling claims require system records or approved internal evidence. Public silence may confirm absent public response behavior within the tested sample, but not private-message performance.

## 5. Applicability rules

All `OI-SOC-*` criteria are normally applicable when the business maintains or publicly promotes a social profile.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-SOC-001` when Facebook is intentionally not used and another approved primary social channel fulfills the same business role
- `OI-SOC-008` when the business has no website and the dependency is separately documented
- `OI-SOC-010` when the service has no meaningful seasonal or event-driven demand pattern

The following do not justify `not_applicable`:

- the profile is abandoned
- content was not published
- credentials were unavailable
- the evaluator could not obtain access
- the criterion would reduce the score
- the business considers social unimportant without an approved methodology exception

If the business has no social presence, confirmed absence after required discovery may support score `0` for presence-dependent criteria. Missing access to private records normally produces `unknown` or `blocked`, not score `0`.

## 6. Criterion weighting rule

All applicable Social criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight.

Approved `not_applicable` criteria are removed before internal weights are recalculated.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`.

### Profile presence and consistency — `OI-SOC-001`, `OI-SOC-002`

| Score | Observable condition |
|---:|---|
| 0 | Required profile is absent, impersonated, materially misleading, or uses conflicting business information that creates buyer risk. |
| 25 | A profile exists but branding, description, links, contact details, service area, ownership, or currency is materially incomplete or inconsistent. |
| 50 | Profiles are identifiable and broadly consistent, but one or more important fields, channel controls, or update practices remain incomplete. |
| 75 | Active profiles are current, professionally branded, complete, consistent, and aligned with the approved business-information source of truth. |
| 100 | Profile governance includes accountable ownership, access control, source-of-truth synchronization, review cadence, recovery procedures, and documented change control. |

### Activity and real-work evidence — `OI-SOC-003`, `OI-SOC-004`

| Score | Observable condition |
|---:|---|
| 0 | Profiles are abandoned, deceptive, or contain no credible evidence of current business activity within the required sample. |
| 25 | Activity is sporadic, stale, stock-heavy, mostly promotional, or provides little evidence of real work. |
| 50 | Current activity and some real-work content exist, but cadence, service coverage, attribution, context, or consistency remains incomplete. |
| 75 | Recent content consistently shows authentic projects, service delivery, process, team activity, or completed outcomes across priority services. |
| 100 | Real-work publishing is governed through capture standards, permissions, service mapping, approval, cadence ownership, asset retention, and refresh controls. |

### Education, proof, and buyer action — `OI-SOC-005` through `OI-SOC-008`

| Score | Observable condition |
|---:|---|
| 0 | Content is materially misleading, provides no useful buyer guidance, contains unsupported proof, or gives no viable next action within tested scope. |
| 25 | Some education, proof, CTA, or links exist, but they are generic, inconsistent, unattributable, weakly placed, or disconnected from buyer intent. |
| 50 | Baseline educational and trust content with workable CTAs exists, but topic coverage, proof quality, destination relevance, or measurement readiness remains incomplete. |
| 75 | Content regularly answers buyer questions, uses attributable proof, provides clear next actions, and links to relevant service or inquiry destinations. |
| 100 | Content strategy is governed through approved themes, proof controls, destination standards, campaign tagging, ownership, QA, and decision-oriented review. |

### Response behavior and seasonality — `OI-SOC-009`, `OI-SOC-010`

| Score | Observable condition |
|---:|---|
| 0 | Material public inquiries are ignored, responses are unprofessional, or content materially conflicts with current availability or service timing. |
| 25 | Responses or seasonal activity are inconsistent, delayed, improvised, or unsupported by a repeatable operating practice. |
| 50 | Baseline response and seasonal alignment exist, but ownership, timing standards, escalation, campaign depth, or documentation remains incomplete. |
| 75 | Public responses are timely and professional, and content is intentionally aligned with relevant demand windows and service priorities. |
| 100 | Response and campaign operations are governed through service standards, escalation rules, templates, calendar ownership, outcome review, and controlled improvement. |

Interpolation is not permitted.

## 8. Confidence assignment guidance

| Confidence | Social-specific use |
|---|---|
| High | Direct public profile review, complete post sampling, validated links, attributable media, sufficient comment threads, current records, and approved internal evidence support the selected anchor. |
| Medium | Public evidence is strong, but one internal ownership record, private-response record, campaign record, attribution source, or platform surface remains incomplete. |
| Low | Result relies on narrow post samples, stale captures, client claims, inaccessible comments, unverifiable project media, or inconsistent platform history. |
| Unknown | Evidence is insufficient to select a maturity anchor. |

High confidence that public activity is absent does not establish that private outreach or unpublished content operations do not exist.

Confidence remains separate from maturity score.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- profile ownership cannot be confirmed
- deleted, restricted, or private content prevents representative sampling
- project-media provenance or customer permission cannot be established
- private response behavior is claimed but records are unavailable
- outbound campaign tracking cannot be verified
- seasonal planning is claimed but no calendar or historical record is provided
- platform data is stale or materially inconsistent with current public state

Common `blocked` conditions:

- access, legal, privacy, or consent restrictions prevent minimum inspection
- account disputes or impersonation make ownership unreliable
- platform suspension or outage prevents stable review
- required evidence has been deleted and no authoritative record exists
- material content is under active correction and no stable current state can be assessed

Every material unknown or block must record:

- reason code
- affected criterion
- evidence or test required
- validation owner
- materiality
- next action
- publication effect

Unknown is not score `0`.

## 10. Duplicate-signal boundaries

| Overlap | Primary owner | Social treatment |
|---|---|---|
| Website navigation, layout, and destination-page quality | `website` | Social scores whether relevant links exist and resolve; Website scores destination quality. |
| CTA mechanics, form fields, and inquiry completion | `conversion` | Social scores the clarity and presence of the social next action, not downstream capture performance. |
| GBP posts, profile fields, reviews, and owner responses | `gbp` | Social excludes GBP operations unless methodology explicitly classifies the surface as social evidence without duplicate scoring. |
| Review quality, project proof, credentials, and buyer-risk reduction | `trust` | Social scores how proof is used in social content; Trust scores underlying credibility and buyer-confidence evidence. |
| Search targeting, metadata, schema, and indexation | `seo` | Social may record link support as a dependency but does not score SEO implementation. |
| Lead routing, message automation, reminders, and publishing workflows | `automation` | Social scores observable public execution; Automation scores the internal system producing or handling it. |
| Tracking, attribution, reporting, reach, and conversion measurement | `analytics` | Social records measurement readiness as evidence; Analytics owns instrumentation and reporting performance. |
| Competitor publishing advantage | `competitive` | Social scores the client’s own operating maturity; Competitive scores relative market position. |
| Message differentiation and offer clarity | `messaging_offer` | Social scores execution and consistency on social surfaces, not the underlying message strategy. |

One evidence item may support multiple categories only when each category measures a distinct condition and the DecisionLedger records the boundary.

## 11. Finding and recommendation routing

A Social category score does not automatically create a finding or recommendation.

Because no governed Social finding library currently exists:

- do not create `OI-FIND-SOC-*` identifiers
- route the evidence to an existing governed finding only when that finding’s evidence contract and ownership rules are satisfied
- otherwise record `methodology_gap: social_finding_library_required`
- preserve the observation in the DecisionLedger without promoting it to an unsupported governed finding

Eligible adjacent routing may include:

- profile identity or contact inconsistency to the governed Trust or GBP domain when its contract is satisfied
- weak destination path or CTA dependency to Website or Conversion when its contract is satisfied
- absent tracking or attribution to Analytics when its contract is satisfied
- missing response, publishing, or lead-handling workflow to Automation when its contract is satisfied
- weak differentiation or offer expression to Messaging and Offer when its contract is satisfied

Recommendation routing requires:

1. evidence-backed observation
2. governed finding reference or explicit methodology-gap record
3. business impact stated without unsupported ROI
4. confidence and material unknowns
5. priority rationale
6. implementation dependency
7. package fit assessment
8. roadmap phase
9. DecisionLedger record

Package-first selling is prohibited. A package may be selected only after the evidence, finding eligibility, dependencies, and priority pass review.

## 12. Publication controls

| Publication state | Social-specific treatment |
|---|---|
| `official` | Minimum scope is complete, profile ownership is reliable, at least 80% of applicable criterion weight is scored, no unresolved high-materiality unknown distorts the result, and duplicate checks pass. |
| `provisional` | At least 60% of applicable criterion weight is scored and remaining uncertainty is disclosed with bounds and validation actions. |
| `range_only` | Coverage is below the provisional threshold, profile or response evidence is materially incomplete, or one high-materiality unknown prevents a defensible point score. |
| `blocked` | Ownership, access, consent, platform availability, or evidence integrity prevents minimum evaluation. |

Published output must include:

- observed score or range
- coverage
- confidence index
- sampled platforms and dates
- material unknowns
- publication state
- duplicate-check result
- methodology-gap disclosure when social-specific findings cannot be governed

Do not publish unsupported claims about reach, engagement, leads, revenue, sentiment, response time, or market influence.

## 13. DecisionLedger requirements

Each Social category result must retain:

```yaml
category_key: social
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2-draft"
score_run_id: OI-SCORE-YYYY-NNN
platforms_reviewed: []
sample_period: ""
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
methodology_gaps: []
recommendation_refs: []
package_dependencies: []
roadmap_phase: ""
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Every criterion decision must link evidence, scope, anchor, confidence, applicability state, and evaluator rationale.

## 14. Validation messages

- `CAT-SOC-SCOPE-001` — Required platforms or post sample were not reviewed.
- `CAT-SOC-SCOPE-002` — Public response or outbound-link sample is below minimum scope.
- `CAT-SOC-EVID-001` — Selected anchor is unsupported by direct social evidence.
- `CAT-SOC-EVID-002` — Project, review, or customer proof lacks attribution or permission evidence.
- `CAT-SOC-MAP-001` — Criterion is missing, duplicated, deprecated, or assigned outside `social`.
- `CAT-SOC-DUP-001` — Evidence has been scored again under Website, Conversion, GBP, Trust, Automation, Analytics, Competitive, or Messaging and Offer without distinct logic.
- `CAT-SOC-UNKNOWN-001` — A material unknown lacks owner, action, or publication effect.
- `CAT-SOC-WEIGHT-001` — Applicable criterion weights do not reconcile to 100%.
- `CAT-SOC-GATE-001` — Unsupported reach, engagement, lead, revenue, response-time, or market-performance claim blocks publication.
- `CAT-SOC-GATE-002` — Ungoverned `OI-FIND-SOC-*` identifier was created.
- `CAT-SOC-LEDGER-001` — Required traceability or methodology-gap record is missing.

Blocking messages must identify the failed rule and required correction.

## 15. Worked scoring example

Assume ten applicable criteria with equal 10% internal weight.

| Criterion | State | Anchor | Confidence | Evidence summary |
|---|---|---:|---|---|
| `OI-SOC-001` | scored | 75 | High | Facebook page is current, branded, and identifiable. |
| `OI-SOC-002` | scored | 50 | High | Core fields align, but one profile uses an outdated service-area statement. |
| `OI-SOC-003` | scored | 50 | High | Nine posts in six months with two material inactivity gaps. |
| `OI-SOC-004` | scored | 75 | High | Most sampled posts show attributable local projects and process. |
| `OI-SOC-005` | scored | 25 | Medium | Two educational posts exist, but buyer-question coverage is narrow. |
| `OI-SOC-006` | scored | 50 | Medium | Review and team proof exists, but source attribution is inconsistent. |
| `OI-SOC-007` | scored | 50 | High | Profile CTA works; only half of sampled posts contain a clear next action. |
| `OI-SOC-008` | scored | 25 | High | Links are sparse and mostly route to the homepage rather than relevant service pages. |
| `OI-SOC-009` | unknown | — | Unknown | Public sample is insufficient and private response records were not provided. |
| `OI-SOC-010` | scored | 50 | Medium | Seasonal topics appear, but no approved campaign calendar was provided. |

Observed score over scored criterion weight:

```text
Observed points = 75 + 50 + 50 + 75 + 25 + 50 + 50 + 25 + 50 = 450
Scored criteria = 9
Observed score = 450 ÷ 9 = 50.0
Coverage = 9 ÷ 10 = 90%
```

Bounds preserve the unknown criterion:

```text
Lower bound = (450 + 0) ÷ 10 = 45.0
Upper bound = (450 + 100) ÷ 10 = 55.0
```

Publication decision:

```yaml
observed_score: 50.0
lower_bound: 45.0
upper_bound: 55.0
coverage: 0.90
confidence_index: medium
publication_state: provisional
material_unknowns:
  - criterion_id: OI-SOC-009
    reason: private response records unavailable and public sample insufficient
finding_refs: []
methodology_gaps:
  - social_finding_library_required
ledger_ref: OI-DL-2026-EXAMPLE-SOC
```

The result remains `provisional` because response behavior is materially unknown. No `OI-FIND-SOC-*` identifier is created. Recommendations may route only through an existing governed adjacent finding whose evidence contract is satisfied, or remain a documented methodology gap.

## 16. Completion checklist

- [ ] All ten `OI-SOC-*` criteria are mapped exactly once.
- [ ] Required platforms and post samples are recorded.
- [ ] Profile ownership and business-information consistency are verified.
- [ ] Real-work and proof content is attributable.
- [ ] Outbound links and destination relevance are tested.
- [ ] Public and private response evidence are distinguished.
- [ ] Seasonal relevance is evidence-backed.
- [ ] Unknown, blocked, and not-applicable states are explicit.
- [ ] Confidence remains separate from maturity.
- [ ] Duplicate-signal review passes.
- [ ] No unsupported performance or ROI claims appear.
- [ ] No ungoverned `OI-FIND-SOC-*` identifier is created.
- [ ] Recommendation, package, and roadmap routing are evidence-first.
- [ ] DecisionLedger record is complete.
- [ ] Worked example recalculates correctly.
- [ ] Reviewer approval is recorded before operational use.
