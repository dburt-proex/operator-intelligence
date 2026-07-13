# Social Presence Category Scoring Sheet

Version: v0.2 scoring execution foundation  
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

It does not independently score website structure, GBP operations, review performance, technical SEO, downstream lead capture, internal automation, or business outcomes without verified source data.

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix: `OI-SOC-*`

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
- Facebook page when commercially relevant
- profile identity, description, category, phone, website link, service area, and CTA
- most recent twelve posts per active platform, or all posts from the prior six months when fewer exist
- post dates and visible inactivity gaps
- project, process, team, review, educational, seasonal, and promotional content samples
- outbound links and destination pages
- public comments and business replies
- approved campaign record when seasonality is scored above baseline

### Supporting evidence

- native platform exports or analytics
- content calendar and approval records
- attributed media library
- message-response SOP and templates
- social lead records
- UTM or campaign naming standards
- client confirmation of channel purpose and ownership

### Evidence that cannot support a point score alone

- follower count, likes, reach, impressions, or engagement without verified context
- one unusually successful or unsuccessful post
- private messages not inspected
- unpublished drafts
- stock imagery presented as completed work
- generic third-party social grades
- unsupported client assertions

## 4. Minimum evaluation scope

A Social category score is admissible only when the evaluator:

1. identifies all active and claimed social profiles
2. reviews every current customer-facing social channel
3. inspects the required post sample
4. compares business information against the approved source of truth and website
5. classifies posts by real work, education, proof, CTA, website connection, and seasonality
6. validates at least three outbound links when three exist
7. reviews at least ten public comment or inquiry threads, or all when fewer exist
8. tests at least one relevant service-demand window when sufficient history exists
9. records access, sampling dates, unavailable surfaces, and channel ownership

A narrow platform sample must not be generalized to the full category. Private response-time claims require approved internal records.

## 5. Applicability rules

All `OI-SOC-*` criteria are normally applicable when the business maintains or promotes a social profile.

Use `not_applicable` only when structural irrelevance is documented and approved. Abandonment, missing credentials, unavailable evidence, evaluator difficulty, or expected score impact do not justify `not_applicable`.

Confirmed absence after required discovery may support score `0` for presence-dependent criteria. Missing access to private records normally produces `unknown` or `blocked`, not score `0`.

## 6. Criterion weighting rule

All applicable Social criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight. Approved `not_applicable` criteria are removed before recalculation. Unequal weighting is prohibited without an approved methodology change.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`. Interpolation is prohibited.

### Profile presence and consistency — `OI-SOC-001`, `OI-SOC-002`

| Score | Observable condition |
|---:|---|
| 0 | Required profile is absent, impersonated, materially misleading, or uses conflicting business information that creates buyer risk. |
| 25 | A profile exists but branding, description, links, contact details, service area, ownership, or currency is materially incomplete. |
| 50 | Profiles are identifiable and broadly consistent, but important fields or update practices remain incomplete. |
| 75 | Active profiles are current, professionally branded, complete, and aligned with the approved source of truth. |
| 100 | Profile governance includes accountable ownership, access control, synchronization, review cadence, recovery, and change control. |

### Activity and real-work evidence — `OI-SOC-003`, `OI-SOC-004`

| Score | Observable condition |
|---:|---|
| 0 | Profiles are abandoned, deceptive, or contain no credible current activity within the required sample. |
| 25 | Activity is sporadic, stale, stock-heavy, or provides little evidence of real work. |
| 50 | Current activity and some real-work content exist, but cadence, attribution, context, or consistency remains incomplete. |
| 75 | Recent content consistently shows authentic projects, service delivery, process, team activity, or completed outcomes. |
| 100 | Publishing is governed through capture standards, permissions, service mapping, approval, ownership, retention, and refresh controls. |

### Education, proof, and buyer action — `OI-SOC-005` through `OI-SOC-008`

| Score | Observable condition |
|---:|---|
| 0 | Content is materially misleading, lacks useful buyer guidance, uses unsupported proof, or provides no viable next action. |
| 25 | Some education, proof, CTA, or links exist, but they are generic, inconsistent, unattributable, or disconnected from buyer intent. |
| 50 | Baseline educational and trust content with workable CTAs exists, but coverage, proof quality, or destination relevance remains incomplete. |
| 75 | Content regularly answers buyer questions, uses attributable proof, provides clear next actions, and links to relevant destinations. |
| 100 | Content strategy is governed through approved themes, proof controls, destination standards, campaign tagging, ownership, QA, and review. |

### Response behavior and seasonality — `OI-SOC-009`, `OI-SOC-010`

| Score | Observable condition |
|---:|---|
| 0 | Material public inquiries are ignored, responses are unprofessional, or content conflicts with current availability or service timing. |
| 25 | Responses or seasonal activity are inconsistent, delayed, improvised, or unsupported by repeatable practice. |
| 50 | Baseline response and seasonal alignment exist, but ownership, timing standards, escalation, or documentation remains incomplete. |
| 75 | Public responses are timely and professional, and content aligns with relevant demand windows and service priorities. |
| 100 | Response and campaign operations are governed through service standards, escalation rules, templates, ownership, outcome review, and controlled improvement. |

## 8. Confidence assignment guidance

| Confidence | Social-specific use | Factor |
|---|---|---:|
| High | Direct current evidence, complete sampling, validated links, attributable media, sufficient threads, and reliable records support the anchor. | 1.00 |
| Medium | Public evidence is strong, but one internal ownership, response, campaign, attribution, or platform source remains incomplete. | 0.75 |
| Low | The result relies on narrow samples, stale captures, client claims, inaccessible comments, or inconsistent history. | 0.50 |
| Unknown | Evidence is insufficient to select a maturity anchor. | 0.00 |

Confidence remains separate from maturity. High confidence on a narrow sample does not replace coverage.

## 9. Unknown, blocked, and not-applicable treatment

Common unknowns include unconfirmed ownership, restricted content, uncertain media provenance, unavailable private-response records, unverifiable tracking, absent campaign records, and stale platform data.

Common blocks include legal or consent restrictions, account disputes, platform suspension, deleted authoritative evidence, and unstable current state.

Every material unknown or block must record reason code, criterion, required evidence, validation owner, materiality, next action, and publication effect. Unknown is not score `0`.

## 10. Duplicate-signal boundaries

| Overlap | Primary owner | Social treatment |
|---|---|---|
| Website navigation and destination quality | `website` | Score link presence and resolution only. |
| Form and inquiry completion | `conversion` | Score the social next action, not downstream capture. |
| GBP posts, reviews, and owner responses | `gbp` | Exclude GBP operations from Social scoring. |
| Underlying proof and buyer-risk reduction | `trust` | Score use of proof in social content, not the underlying credential. |
| Search targeting and indexation | `seo` | Record dependency only. |
| Publishing and response workflows | `automation` | Score public execution, not the internal system. |
| Tracking and reporting | `analytics` | Record readiness; Analytics owns instrumentation. |
| Relative market position | `competitive` | Score client maturity only. |
| Message and offer strategy | `messaging_offer` | Score execution and consistency only. |

One evidence item may support multiple categories only when each category measures a distinct condition and the DecisionLedger records the boundary.

## 11. Finding and recommendation routing

A Social score does not automatically create a finding or recommendation.

Because no governed Social finding library currently exists:

- do not create `OI-FIND-SOC-*` identifiers
- route evidence to an existing governed finding only when its evidence contract and ownership rules are satisfied
- otherwise record `methodology_gap: social_finding_library_required`
- preserve the observation in the DecisionLedger without promoting it to an unsupported finding

Recommendation routing requires an evidence-backed observation, governed finding or methodology gap, bounded business impact, confidence, priority rationale, dependency, package-fit assessment, roadmap phase, and DecisionLedger record.

Package-first selling is prohibited.

## 12. Publication controls

| Publication state | Social-specific treatment |
|---|---|
| `official` | Minimum scope is complete, ownership is reliable, coverage is at least 80%, no material unknown distorts the result, and duplicate checks pass. |
| `provisional` | Coverage is at least 60%, remaining uncertainty is bounded and disclosed, and no blocking error exists. |
| `range_only` | Coverage is below 60% or a high-materiality unknown prevents a defensible point score. |
| `blocked` | Ownership, access, consent, platform availability, or evidence integrity prevents minimum evaluation. |

Published output must include observed score or range, coverage, numeric confidence index, sampled platforms and dates, material unknowns, publication state, duplicate-check result, and methodology-gap disclosure.

Unsupported claims about reach, engagement, leads, revenue, sentiment, response time, or market influence are prohibited.

## 13. DecisionLedger requirements

```yaml
category_key: social
category_sheet_version: "0.2"
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
primary_package: null
dependent_packages: []
roadmap_phase: null
implementation_authorized: false
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Every criterion decision must link evidence, scope, anchor, confidence, applicability state, and evaluator rationale.

## 14. Validation messages

- `CAT-SOC-SCOPE-001` — Required platforms or post sample were not reviewed.
- `CAT-SOC-SCOPE-002` — Public-response or outbound-link sample is below minimum scope.
- `CAT-SOC-EVID-001` — Selected anchor is unsupported by direct social evidence.
- `CAT-SOC-EVID-002` — Project, review, or customer proof lacks attribution or permission evidence.
- `CAT-SOC-MAP-001` — Criterion is missing, duplicated, deprecated, or assigned outside `social`.
- `CAT-SOC-DUP-001` — Evidence is duplicated across categories without distinct logic.
- `CAT-SOC-UNKNOWN-001` — A material unknown lacks owner, action, or publication effect.
- `CAT-SOC-WEIGHT-001` — Applicable criterion weights do not reconcile to 100%.
- `CAT-SOC-CONF-001` — Confidence index is missing, nonnumeric, or inconsistent with criterion factors.
- `CAT-SOC-BOUND-001` — Published bounds omit unknown weight or confidence uncertainty.
- `CAT-SOC-GATE-001` — Unsupported performance or outcome claim blocks publication.
- `CAT-SOC-GATE-002` — Ungoverned `OI-FIND-SOC-*` identifier was created.
- `CAT-SOC-LEDGER-001` — Required traceability or methodology-gap record is missing.

## 15. Worked scoring example

The canonical regression fixture is `scoring/examples/social-worked-example.md`.

Assume ten applicable criteria with equal 10% internal weight. Nine criteria are scored and `OI-SOC-009` remains unknown. The scored anchors total `450`, producing an observed score of `50.00` and coverage of `90.00%`.

Confidence factors across scored criteria are six High (`1.00`) and three Medium (`0.75`):

```text
Confidence index = ((6 × 1.00) + (3 × 0.75)) ÷ 9
                 = 8.25 ÷ 9
                 = 0.9167
```

Confidence uncertainty is applied to scored criterion weight before the unknown criterion is bounded:

```text
Scored weighted contribution = 450 ÷ 10 = 45.00
Confidence uncertainty = 1 - 0.9167 = 0.0833
Scored uncertainty width = 45.00 × 0.0833 = 3.75
Unknown criterion width = 10.00
Lower bound = 45.00 - 3.75 + 0.00 = 41.25
Upper bound = 45.00 + 3.75 + 10.00 = 58.75
```

```yaml
observed_score: 50.00
lower_bound: 41.25
upper_bound: 58.75
coverage: 0.90
confidence_index: 0.9167
confidence_band: high
publication_state: provisional
material_unknowns:
  - criterion_id: OI-SOC-009
    reason: public sample is insufficient and private response records were not provided
finding_refs: []
methodology_gaps:
  - social_finding_library_required
recommendation_refs: []
primary_package: null
dependent_packages: []
roadmap_phase: null
implementation_authorized: false
ledger_ref: OI-DL-2026-EXAMPLE-SOC
```

The result remains `provisional` because response behavior is materially unknown. No Social finding or package is created without an approved finding contract.

## 16. Completion checklist

- [ ] All ten `OI-SOC-*` criteria are mapped exactly once.
- [ ] Required platforms and samples are recorded.
- [ ] Ownership and business-information consistency are verified.
- [ ] Real-work and proof content is attributable.
- [ ] Outbound links and destination relevance are tested.
- [ ] Public and private response evidence are distinguished.
- [ ] Unknown, blocked, and not-applicable states are explicit.
- [ ] Confidence remains separate from maturity.
- [ ] Numeric confidence index and confidence-adjusted bounds reproduce exactly.
- [ ] Duplicate-signal review passes.
- [ ] No unsupported performance or ROI claims appear.
- [ ] No ungoverned `OI-FIND-SOC-*` identifier is created.
- [ ] Recommendation, package, roadmap, and authorization states are governed.
- [ ] DecisionLedger record is complete.
- [ ] Reviewer approval is recorded before operational use.
