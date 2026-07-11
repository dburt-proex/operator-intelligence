# Trust Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `trust`  
Default Operator Score weight: 10%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for visible buyer-confidence signals, proof quality, risk-reduction information, human credibility, and local legitimacy.

It measures:

- website review visibility and specificity
- project and before/after proof
- owner or team visibility
- credential clarity
- warranty or satisfaction-promise clarity
- process transparency
- safety and professionalism signals
- local proof
- contact-detail consistency
- placement of trust signals before key decisions

It does not independently score:

- Google Business Profile review volume, velocity, or response operations
- website navigation, page architecture, or general visual quality
- CTA mechanics or lead capture
- social publishing cadence
- technical local SEO implementation
- analytics instrumentation
- whether internal credentials, insurance, or warranties exist when they cannot be verified

Cross-domain effects must be recorded as dependencies, not duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix:

```text
OI-TRUST-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-TRUST-001` | Reviews are visibly integrated into the website | Homepage, service pages, CTA areas | Equal |
| `OI-TRUST-002` | Review language is specific enough to support buyer decisions | Review sample and source links | Equal |
| `OI-TRUST-003` | Real project photos are visible and attributable | Gallery, service pages, project records | Equal |
| `OI-TRUST-004` | Before/after proof exists where materially relevant | Project proof inventory | Equal |
| `OI-TRUST-005` | Owner or team identity is visible and credible | About page, homepage, approved facts | Equal |
| `OI-TRUST-006` | Relevant credentials are stated accurately | Website, credential records | Equal |
| `OI-TRUST-007` | Warranty, workmanship, or satisfaction commitments are clear and supportable | Service pages, policies, approved terms | Equal |
| `OI-TRUST-008` | The customer process is explained clearly | Process sections, SOP or approved workflow | Equal |
| `OI-TRUST-009` | Safety, cleanup, preparation, or professionalism signals appear where relevant | Service pages, project photos, approved procedures | Equal |
| `OI-TRUST-010` | Local proof is visible and supportable | Project locations, reviews, community evidence | Equal |
| `OI-TRUST-011` | Contact details are complete and consistent across tested surfaces | Header, footer, contact page, profiles | Equal |
| `OI-TRUST-012` | Meaningful trust signals appear before primary buyer decisions | Hero, CTA areas, service-page decision points | Equal |

Each criterion has one weighted owner: `trust`.

## 3. Required evidence surfaces

### Primary evidence

- homepage desktop and mobile captures
- at least two priority service pages, or all when fewer than two exist
- contact and about pages
- all visible review modules and linked review sources
- at least twelve review excerpts, or all when fewer exist
- project gallery and service-specific proof sections
- approved project-photo inventory where attribution is required
- owner or team section and approved identity facts
- visible license, insurance, certification, association, warranty, guarantee, or policy statements
- documented customer process or approved operating workflow
- visible safety, cleanup, preparation, and professionalism claims
- local project, service-area, or community proof
- header, footer, contact page, and major profile contact details
- proof placement near primary CTAs and inquiry paths

### Supporting evidence

- client-provided credential documents
- insurance certificate or license lookup
- warranty or workmanship policy
- project completion records
- review exports
- customer-story approvals
- internal SOPs
- approved business-information source of truth
- competitor trust-proof comparison

### Evidence that cannot support a point score alone

- unsupported claims that the business is trusted, licensed, insured, safe, or guaranteed
- stock photos presented without clear context
- evaluator aesthetic preference
- one testimonial used to infer overall review quality
- client claims that proof exists but is not provided
- badges or logos without verification
- a third-party website grade without underlying observations
- generic competitor impressions without controlled comparison

## 4. Minimum evaluation scope

A Trust category score is admissible only when the evaluator reviews:

1. homepage on desktop and mobile
2. at least two priority service pages, or all when fewer than two exist
3. contact and about pages
4. every visible trust or testimonial module on tested pages
5. at least twelve review excerpts across available sources, or all when fewer exist
6. at least twelve project images, or all when fewer exist
7. before/after evidence for each materially transformation-based priority service, where relevant
8. all visible credential, warranty, guarantee, safety, and process claims
9. contact details across at least four relevant surfaces, including the website and major profiles when available
10. proof placement before or adjacent to at least three primary decision points

Where internal verification is required, the evaluator must request the relevant source record. Public absence may establish that a signal is not visible, but not that the underlying credential, policy, or process does not exist.

Scope exceptions require a documented limitation and may reduce publication to `provisional`, `range_only`, or `blocked`.

## 5. Applicability rules

All `OI-TRUST-*` criteria are normally applicable to contractor and local-service businesses.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples:

- `OI-TRUST-004` when the service produces no meaningful visual transformation or before/after comparison
- `OI-TRUST-006` when no license, certification, insurance disclosure, or association is legally, operationally, or commercially relevant
- `OI-TRUST-007` when no warranty, guarantee, or satisfaction commitment is offered and the absence is explicitly confirmed and approved as structurally appropriate
- `OI-TRUST-009` when safety, cleanup, preparation, or site professionalism is not materially relevant to the service model

The following do not justify `not_applicable`:

- evidence was not provided
- verification access was unavailable
- the business has not created the signal
- the signal would reduce the score
- the evaluator considers the signal optional without methodology support

Confirmed public absence after required inspection may support score `0` for visibility criteria. Unverified internal existence normally produces `unknown` or `blocked`, not score `0`.

## 6. Criterion weighting rule

All applicable Trust criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight.

Approved `not_applicable` criteria are removed before weights are recalculated.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`.

### Reviews and testimonial proof — `OI-TRUST-001`, `OI-TRUST-002`

| Score | Observable condition |
|---:|---|
| 0 | Reviews are absent from tested website surfaces, fabricated, materially misleading, or presented without attributable source where attribution is required. |
| 25 | Reviews exist but are sparse, generic, stale, poorly placed, or disconnected from specific services and buyer questions. |
| 50 | Baseline review proof is visible and credible, but specificity, coverage, placement, or source transparency remains incomplete. |
| 75 | Reviews are specific, attributable, service-relevant, and consistently placed near major decision points. |
| 100 | Review proof is governed through approved sourcing, refresh, placement, accuracy, and usage controls tied to accountable ownership. |

### Project and transformation proof — `OI-TRUST-003`, `OI-TRUST-004`

| Score | Observable condition |
|---:|---|
| 0 | Real project proof is absent, materially misleading, or presented in a way that falsely implies ownership or outcome. |
| 25 | Some project imagery exists, but it is thin, stock-heavy, unattributed, low-context, or not aligned to priority services. |
| 50 | Real work is visible, but service coverage, before/after depth, captions, local context, or maintenance remains incomplete. |
| 75 | Real, relevant project proof consistently supports priority services with useful context and before/after evidence where applicable. |
| 100 | Project proof is governed through capture standards, attribution, approval, service mapping, refresh cadence, and reusable evidence records. |

### Human, credential, and risk-reduction proof — `OI-TRUST-005` through `OI-TRUST-009`

| Score | Observable condition |
|---:|---|
| 0 | Claims are absent where required, materially false, unverifiable after required validation, or create material buyer risk. |
| 25 | Some human, credential, warranty, process, or professionalism signals exist, but major gaps, vague wording, or unsupported claims remain. |
| 50 | Baseline credibility and expectation-setting are present, but verification, scope clarity, placement, consistency, or ownership remains incomplete. |
| 75 | Owner or team identity, relevant credentials, process, risk-reduction terms, and professionalism signals are clear, accurate, and buyer-useful. |
| 100 | These signals are verified, version-controlled, approved, consistently published, and maintained through accountable change and review processes. |

### Local proof, contact consistency, and decision-point placement — `OI-TRUST-010` through `OI-TRUST-012`

| Score | Observable condition |
|---:|---|
| 0 | Local legitimacy or contact details are materially absent, conflicting, misleading, or trust proof appears only after the primary decision point. |
| 25 | Some local and contact proof exists, but inconsistencies, weak context, or late placement create material buyer uncertainty. |
| 50 | Baseline local legitimacy and consistent contact details are present, but coverage or decision-point placement remains incomplete. |
| 75 | Local proof and consistent contact details appear clearly across major surfaces and before key inquiry decisions. |
| 100 | Local and contact proof is governed through a source of truth, routine consistency checks, placement standards, and documented ownership. |

Interpolation is not permitted.

## 8. Confidence assignment guidance

| Confidence | Trust-specific use |
|---|---|
| High | Direct page evidence, attributable reviews, verified project records, approved policies, validated credentials, and complete placement review support the selected anchor across required scope. |
| Medium | Public evidence is strong, but one internal record, verification source, project attribution, or policy detail remains incomplete. |
| Low | Result relies on client claims, narrow samples, stale captures, unverified badges, incomplete project provenance, or partial policy evidence. |
| Unknown | Evidence is insufficient to select a maturity anchor. |

High confidence that a signal is not visible does not establish that the underlying credential, policy, or process does not exist.

Confidence remains separate from maturity score.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- review source or permission cannot be established
- project-image ownership or location cannot be verified
- owner or team facts are unconfirmed
- license, insurance, certification, or association status requires unavailable verification
- warranty, guarantee, or satisfaction terms are claimed but not documented
- internal process or safety practice is unavailable for review
- contact-detail source of truth is not provided

Common `blocked` conditions:

- legal, privacy, or consent restrictions prevent proof inspection
- credential verification cannot be completed because the authoritative source is inaccessible
- disputed ownership prevents reliable use of reviews or project images
- the website or profile surfaces required for minimum scope are unavailable
- material claims are under active correction and no stable current state exists

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

| Overlap | Primary owner | Trust treatment |
|---|---|---|
| GBP review count, velocity, and owner responses | `gbp` | Trust may score website use and service specificity of review proof, not GBP operations. |
| CTA visibility, form design, and inquiry mechanics | `conversion` | Trust scores proof placement near the decision point, not the CTA mechanism. |
| Website structure and general usability | `website` | Trust scores credibility evidence, not navigation or layout quality. |
| Service-page search targeting and structured data | `seo` | Trust may record project proof as a dependency, not score SEO implementation. |
| Social posting cadence and response behavior | `social` | Trust may use social proof as evidence but does not score social operations. |
| Review-request workflow and follow-up automation | `automation` | Trust scores visible proof; automation scores the operating system creating it. |
| Tracking review, proof, or conversion outcomes | `analytics` | Trust scores evidence quality and placement, not instrumentation. |
| Competitor proof advantage | `competitive` | Trust scores the client's condition; competitive scores relative market position. |
| Process explanation in message copy | `messaging_offer` | Trust scores risk reduction and expectation-setting; messaging scores clarity and positioning. |

One evidence item may support multiple criteria only when each criterion measures a distinct condition.

## 11. Finding and recommendation routing

Eligible finding IDs are governed by `framework/findings/trust-findings.md`, including:

- `OI-FIND-TRUST-001` through `OI-FIND-TRUST-018`

A weak score does not automatically create a finding.

Routing requires:

1. evidence-backed observation
2. valid governed finding ID
3. buyer-confidence or risk-reduction impact
4. confidence assignment
5. priority
6. package fit
7. roadmap phase
8. DecisionLedger record

Common package dependencies:

| Condition | Eligible package dependency | Typical phase |
|---|---|---|
| Reviews, project proof, human proof, process, or local legitimacy are weak or poorly placed | Trust Proof System | Phase 2 — Growth Foundation |
| Review generation is inconsistent or manual | Review Generation System | Phase 3 — Automation and Reporting |
| Trust weakness directly affects CTA confidence | Website Conversion Fix Pack plus Trust Proof System | Phase 1 if blocking action, otherwise Phase 2 |
| GBP reputation operations are the primary constraint | Google Business Authority Pack | Phase 2 or 3 based on dependency |
| Service pages lack proof and content depth | Local SEO Expansion Pack plus Trust Proof System | Phase 2 |

Package selection is never automatic. Package-first selling is prohibited.

## 12. Publication controls

Apply the common publication states:

| State | Trust-specific requirement |
|---|---|
| `official` | Minimum scope met; material claims verified; score, confidence, coverage, range, and unknowns published. |
| `provisional` | Point score is supportable, but one material verification or scope limitation remains clearly qualified. |
| `range_only` | Material credential, policy, provenance, or coverage gaps prevent defensible point precision. |
| `blocked` | Required surfaces cannot be inspected, or material claims cannot be safely evaluated. |

Force `range_only` or `blocked` when:

- a high-materiality license, insurance, warranty, or safety claim cannot be verified
- disputed review or project-image provenance affects multiple criteria
- minimum decision-point placement review was not completed
- contact-detail conflicts cannot be resolved
- evidence suggests a materially misleading claim requiring correction

Client-facing language must describe visibility, clarity, evidence, buyer uncertainty, or validation needs without implying dishonesty, poor work, or legal noncompliance unless directly established.

## 13. DecisionLedger requirements

Each Trust category result must retain:

```yaml
category_key: trust
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
material_unknowns: []
proof_source_refs: []
credential_validation_refs: []
duplicate_check_passed: false
finding_refs: []
recommendation_refs: []
package_refs: []
roadmap_phase_refs: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Every routed recommendation must preserve:

```text
Evidence → Interpretation → Buyer impact → Confidence → Priority → Recommendation → Package → Roadmap phase
```

## 14. Validation messages

| Code | Blocking condition | Required correction |
|---|---|---|
| `CAT-TRUST-SCOPE-001` | Minimum website, proof, review, or decision-point scope not met | Complete required review or reduce publication state. |
| `CAT-TRUST-EVID-001` | Selected anchor is unsupported by attributable evidence | Add evidence or select a lower/unknown state. |
| `CAT-TRUST-MAP-001` | Criterion or finding is missing or multiply owned | Correct mapping before publication. |
| `CAT-TRUST-DUP-001` | GBP, conversion, website, SEO, social, automation, analytics, or competitive signal is duplicate-scored | Retain one weighted owner and record dependency. |
| `CAT-TRUST-UNKNOWN-001` | Material credential, policy, provenance, or contact-detail unknown is unresolved | Add validation owner, next action, and publication effect. |
| `CAT-TRUST-WEIGHT-001` | Applicable criterion weights do not reconcile to 100% | Recalculate after approved applicability decisions. |
| `CAT-TRUST-GATE-001` | Materially misleading or unsafe claim prevents publication | Correct or remove claim and revalidate. |
| `CAT-TRUST-LEDGER-001` | Required evidence-to-recommendation trace is incomplete | Complete DecisionLedger record. |

## 15. Worked scoring example

Assume all twelve criteria are applicable.

| Criterion | State | Score | Confidence | Evidence note |
|---|---|---:|---|---|
| OI-TRUST-001 | scored | 50 | High | Reviews visible on homepage but absent near service CTAs |
| OI-TRUST-002 | scored | 75 | High | Attributable, service-specific review sample |
| OI-TRUST-003 | scored | 50 | High | Real project photos exist but coverage is uneven |
| OI-TRUST-004 | scored | 25 | Medium | Limited before/after proof for relevant services |
| OI-TRUST-005 | scored | 75 | High | Owner identity and local story visible |
| OI-TRUST-006 | unknown | — | Unknown | Insurance and credential claims require validation |
| OI-TRUST-007 | scored | 50 | Medium | Workmanship language exists but scope is incomplete |
| OI-TRUST-008 | scored | 75 | High | Clear four-step process across priority pages |
| OI-TRUST-009 | scored | 50 | Medium | Cleanup and preparation discussed; safety evidence partial |
| OI-TRUST-010 | scored | 75 | High | Local projects and review locations visible |
| OI-TRUST-011 | scored | 100 | High | Contact details reconcile across tested surfaces |
| OI-TRUST-012 | scored | 50 | High | Some proof precedes CTAs; major gaps remain |

Equal criterion weight:

```text
1 ÷ 12 = 0.083333
```

Observed score across eleven scored criteria:

```text
(50 + 75 + 50 + 25 + 75 + 50 + 75 + 50 + 75 + 100 + 50) ÷ 11
= 61.36
```

Coverage:

```text
11 ÷ 12 = 91.67%
```

Bounds with one unknown criterion:

```text
Lower bound = (675 + 0) ÷ 12 = 56.25
Upper bound = (675 + 100) ÷ 12 = 64.58
```

Publication outcome:

```yaml
observed_score: 61.36
lower_bound: 56.25
upper_bound: 64.58
coverage: 0.9167
publication_state: provisional
material_unknowns:
  - criterion_id: OI-TRUST-006
    reason: credential and insurance evidence pending validation
finding_refs:
  - OI-FIND-TRUST-002
  - OI-FIND-TRUST-007
  - OI-FIND-TRUST-012
ledger_ref: OI-DL-2026-TRUST-001
```

No finding is created solely because the category score is `61.36`. Each finding requires its own evidence and routing record.

## 16. Completion checklist

- [ ] All twelve `OI-TRUST-*` criteria are mapped exactly once.
- [ ] Minimum evaluation scope is complete or limitations are recorded.
- [ ] Review and project proof is attributable.
- [ ] Credential, warranty, safety, and policy claims are verified or marked unknown.
- [ ] Unknown is not scored as zero.
- [ ] Confidence is separate from maturity.
- [ ] Approved `not_applicable` decisions include rationale and approval.
- [ ] Cross-category duplicate checks pass.
- [ ] Finding IDs come from the governed Trust finding library.
- [ ] Package routing is evidence-first and non-automatic.
- [ ] Roadmap phase is assigned after dependencies are evaluated.
- [ ] Client language is executive-safe.
- [ ] DecisionLedger traceability is complete.
- [ ] Worked example recalculates correctly.
- [ ] Reviewer approves this sheet version before production scoring use.
