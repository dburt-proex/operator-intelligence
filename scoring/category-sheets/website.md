# Website Structure and UX Category Scoring Sheet

Version: v0.1 scoring execution foundation  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/category-sheets/`  
Category key: `website`  
Default Operator Score weight: 10%  
Status: Draft foundation for commercial v1.0

## 1. Purpose and category boundary

This sheet governs scoring for website structure and user experience.

The category measures whether the website gives buyers a usable, accessible, and logically organized path to understand the business, discover services, navigate key pages, and reach contact options.

It includes:

- page and navigation structure
- service-page organization
- mobile usability
- phone and contact-path accessibility
- page hierarchy
- visual scanning support
- footer utility
- functional links and buyer paths

It does not independently score:

- message strength or offer quality
- CTA persuasiveness or lead-capture workflow
- search visibility or technical SEO
- trust-asset quality
- follow-up automation
- analytics instrumentation
- competitive performance

Cross-domain effects must be recorded as dependencies rather than duplicate scores.

## 2. Included criterion prefixes and criterion inventory

Included prefix:

```text
OI-WEB-*
```

| Criterion ID | Observable condition | Primary evidence | Default weighting |
|---|---|---|---|
| `OI-WEB-001` | Homepage communicates the business type immediately | Desktop and mobile above-fold screenshots | Equal |
| `OI-WEB-002` | Homepage communicates the service area | Hero, footer, contact page, service-area copy | Equal |
| `OI-WEB-003` | Navigation is simple and buyer-oriented | Desktop and mobile menu tests | Equal |
| `OI-WEB-004` | Services are organized into clear pages | URL inventory, menu, service-page inventory | Equal |
| `OI-WEB-005` | Website works cleanly on mobile | Mobile screenshots and interaction tests | Equal |
| `OI-WEB-006` | Phone number is visible and usable | Header, footer, contact page, tap-to-call test | Equal |
| `OI-WEB-007` | Contact or estimate page is easy to reach | Navigation and path testing | Equal |
| `OI-WEB-008` | Website has a logical page hierarchy | Sitemap, URL inventory, internal links | Equal |
| `OI-WEB-009` | Visual hierarchy supports scanning | Key-page screenshots and heading review | Equal |
| `OI-WEB-010` | Page content supports buyer decision-making | Homepage and service-page review | Equal |
| `OI-WEB-011` | Website avoids template-generic presentation | Homepage and relevant competitor comparison | Equal |
| `OI-WEB-012` | Footer supports trust and navigation | Footer screenshot and link test | Equal |

Each criterion has one weighted owner: `website`.

## 3. Required evidence surfaces

### Primary evidence

- homepage desktop screenshot
- homepage mobile screenshot
- desktop navigation test
- mobile navigation test
- URL and page inventory
- core service-page review
- contact or estimate path test
- phone-link test
- footer review
- broken-link or dead-path observations

### Supporting evidence

- sitemap
- CMS page inventory
- browser or device notes
- competitor screenshots
- client-confirmed service priorities
- hosting, CMS, or domain-access records

### Evidence that cannot support a point score alone

- evaluator preference
- visual-design opinion without buyer-impact evidence
- client claim without observable support
- one desktop screenshot used to infer mobile behavior
- visible form or link without a safe function test
- automated audit result without manual verification of the affected buyer path

## 4. Minimum evaluation scope

A website category score is admissible only when the evaluator reviews, where present:

1. homepage on desktop and mobile
2. desktop and mobile navigation
3. contact or estimate page
4. at least two core service pages, or all core service pages when fewer than two exist
5. footer
6. phone and primary contact paths
7. service-page and URL inventory
8. at least one complete path from homepage to inquiry option

A single-page review cannot be generalized to the entire category.

Minimum scope exceptions require a documented limitation and may reduce publication to `provisional` or `range_only`.

## 5. Applicability rules

All `OI-WEB-*` criteria are normally applicable when the business has a public website.

Use `not_applicable` only when structural irrelevance is documented and approved. Examples may include:

- no phone channel exists by approved operating design for `OI-WEB-006`
- the approved assessment scope excludes competitor comparison for `OI-WEB-011`

The following do not justify `not_applicable`:

- the page could not be found
- access was unavailable
- mobile testing was not completed
- functionality was difficult to test
- the criterion would reduce the score

If no website exists, confirmed absence may support score `0` for relevant public-site criteria. Internal ownership, hosting, and system details remain `unknown` unless verified.

## 6. Criterion weighting rule

All applicable website criteria use equal weighting.

```text
Criterion Weight = 1 ÷ Applicable Criterion Count
```

Unknown and blocked criteria remain inside applicable weight.

Approved `not_applicable` criteria are removed before weights are recalculated.

Unequal weighting is prohibited until a versioned methodology change satisfies `scoring/weight-rules.md`.

## 7. Category-specific anchor guidance

Use only the approved anchors: `0`, `25`, `50`, `75`, `100`.

### Business and service-area clarity — `OI-WEB-001`, `OI-WEB-002`

| Score | Observable condition |
|---:|---|
| 0 | Business type or service area is absent, materially misleading, or cannot be determined within the tested surfaces. |
| 25 | Information exists but is vague, buried, inconsistent, or missing on a primary surface. |
| 50 | Business type and service area are understandable after normal review, but immediate clarity or consistency is limited. |
| 75 | Both are clear on major buyer-entry surfaces and remain consistent across key pages. |
| 100 | Clarity is immediate, consistent, locally specific, tested across devices, and governed through documented content ownership. |

### Navigation and page architecture — `OI-WEB-003`, `OI-WEB-004`, `OI-WEB-008`

| Score | Observable condition |
|---:|---|
| 0 | Key pages are inaccessible, broken, materially misleading, or absent within the tested scope. |
| 25 | Navigation or service architecture exists but important pages are buried, collapsed, inconsistent, or difficult to discover. |
| 50 | Core pages can be reached and hierarchy is functional, but important services or buyer tasks require unnecessary effort. |
| 75 | Navigation and page architecture consistently support major buyer tasks across desktop and mobile. |
| 100 | Architecture is complete, scalable, tested, consistently maintained, and aligned to documented service priorities and buyer paths. |

### Mobile usability — `OI-WEB-005`

| Score | Observable condition |
|---:|---|
| 0 | Mobile layout or interaction failures block navigation, reading, calling, or inquiry access. |
| 25 | The site loads but contains material readability, menu, tap-target, layout, or form friction. |
| 50 | Core tasks are possible, with recurring but non-blocking mobile usability issues. |
| 75 | Key pages and actions work cleanly across the tested mobile scope. |
| 100 | Mobile behavior is consistently usable, tested across representative devices or browsers, monitored, and owned through a maintenance process. |

### Contact accessibility — `OI-WEB-006`, `OI-WEB-007`

| Score | Observable condition |
|---:|---|
| 0 | Phone or contact paths are absent, broken, misleading, or inaccessible within tested buyer journeys. |
| 25 | A contact route exists but is buried, difficult to use, inconsistent, or requires avoidable steps. |
| 50 | Buyers can reach a valid contact path with normal effort, but placement or device usability is inconsistent. |
| 75 | Contact and phone paths are prominent, functional, and consistent across key pages and devices. |
| 100 | Contact access is consistently tested, accessible, monitored, and governed with documented ownership and fallback paths. |

### Scanning and buyer support — `OI-WEB-009`, `OI-WEB-010`

| Score | Observable condition |
|---:|---|
| 0 | Page structure actively prevents comprehension or materially omits information required to understand the buyer path. |
| 25 | Dense, unclear, or incomplete page structure makes key services, proof, process, or next steps difficult to identify. |
| 50 | Pages provide a functional baseline but contain material gaps in hierarchy, process, proof placement, objections, or expectations. |
| 75 | Key pages consistently support scanning and buyer decision-making with clear structure and relevant support content. |
| 100 | Decision-support structure is complete, tested, measured, consistently maintained, and integrated across primary buyer journeys. |

### Differentiation and footer utility — `OI-WEB-011`, `OI-WEB-012`

| Score | Observable condition |
|---:|---|
| 0 | Presentation is materially misleading, footer paths are broken, or key business details are absent across tested surfaces. |
| 25 | Presentation is highly generic or the footer omits important navigation, contact, service-area, or credibility information. |
| 50 | The site and footer are functional but provide limited differentiation or incomplete end-of-page support. |
| 75 | Presentation is recognizably specific to the business and the footer reliably supports navigation and contact. |
| 100 | Differentiation is evidence-backed and consistently integrated, while footer content is complete, governed, tested, and maintained. |

Interpolation is not permitted.

## 8. Confidence assignment guidance

| Confidence | Website-specific use |
|---|---|
| High | Direct screenshots and completed desktop, mobile, navigation, link, phone, or contact-path tests confirm the condition across required scope. |
| Medium | Visible evidence is strong, but one representative device, browser, page group, competitor comparison, or functional path remains incomplete. |
| Low | The assessment depends on inaccessible pages, client statements, uncertain CMS behavior, incomplete tests, or narrow sampling. |
| Unknown | Evidence is insufficient to select a maturity anchor. |

High confidence on one page does not replace category coverage.

Confidence must remain separate from the maturity score.

## 9. Unknown, blocked, and not-applicable treatment

Common `unknown` conditions:

- mobile behavior not tested
- contact destination cannot be verified
- service-page inventory is incomplete
- business-priority services are not confirmed
- competitor evidence required by `OI-WEB-011` is unavailable
- CMS or ownership information is unavailable

Common `blocked` conditions:

- site access is denied or technically unavailable
- safe form, link, or phone testing cannot proceed
- malware, privacy, credential, or client-harm risk prevents testing
- conflicting versions of the website prevent reliable evaluation

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

| Overlap | Website owns | Adjacent category owns |
|---|---|---|
| Messaging and offer | Placement, structure, and accessibility of content | Strength, specificity, differentiation, and offer quality |
| Conversion | Ability to reach a contact or estimate path | CTA effectiveness, form design, confirmation, routing, and capture quality |
| SEO | Page and navigation architecture | Search intent, indexability, metadata, local relevance, and organic visibility |
| Trust | Location and accessibility of proof | Quality, completeness, and credibility of proof assets |
| Automation | Public path to a form or contact route | Lead handling, assignment, acknowledgement, and follow-up |
| Analytics | Presence of usable buyer paths | Instrumentation, attribution, reporting, and decision use |
| Competitive | Site-specific structure and usability | Relative market position and benchmark interpretation |

Duplicate scoring is prohibited when two criteria measure the same condition without distinct logic.

## 11. Finding and recommendation routing

A weak website score does not automatically create a finding or package recommendation.

Eligible primary finding domain:

```text
OI-FIND-WEB-*
```

Common governed routing:

| Evidence-backed condition | Primary route | Common package dependency |
|---|---|---|
| Navigation, mobile usability, phone visibility, or contact access is weak | Website finding | `OI-PKG-WEB-001` Website Conversion Fix Pack |
| Core service-page architecture is absent | SEO finding primary; website dependency | `OI-PKG-SEO-001` Local SEO Expansion Pack |
| Proof is unavailable or poorly integrated | Trust finding primary | `OI-PKG-TRUST-001` Trust Proof System |
| Form exists but lead handling is weak | Automation or conversion finding primary | `OI-PKG-CRM-001` CRM and Follow-Up System |
| Outcomes cannot be measured | Analytics finding primary | `OI-PKG-DASH-001` Operator Dashboard Pack |
| Website ownership or functionality is unverified | Validation record | No package commitment until validation passes |

Recommendation routing requires observation, evidence, interpretation, impact, confidence, priority, package fit, roadmap phase, and DecisionLedger traceability.

Do not recommend a full redesign when a narrower correction resolves the evidence-backed condition.

## 12. Publication controls

Website category results use the shared publication states:

- `official`
- `provisional`
- `range_only`
- `blocked`

Additional website controls:

- no `official` score without desktop and mobile evaluation
- no `official` score without navigation and contact-path testing
- no score for untested functionality represented as confirmed failure
- a blocked primary buyer path requires `REVIEW` and may require `HALT`
- unresolved high-materiality website unknowns may force `range_only`
- duplicate-domain mapping failures block publication

Client reporting must include coverage, confidence, score range, and material limitations.

## 13. DecisionLedger requirements

```yaml
category_key: website
category_sheet_version: "0.1"
criterion_inventory_version: "criteria-library-v0.2"
score_run_id: OI-SCORE-YYYY-NNN
required_scope_completed: false
desktop_tested: false
mobile_tested: false
navigation_tested: false
contact_path_tested: false
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
roadmap_phases: []
reviewed_by: ""
approved_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

## 14. Validation messages

### Blocking

- `CAT-WEB-SCOPE-001`: minimum page and device scope is not complete
- `CAT-WEB-EVID-001`: selected anchor is not supported by website evidence
- `CAT-WEB-MAP-001`: website criterion is missing, duplicated, or assigned to another weighted owner
- `CAT-WEB-DUP-001`: website condition is duplicated in an adjacent category
- `CAT-WEB-WEIGHT-001`: applicable criterion weights do not total 100%
- `CAT-WEB-GATE-001`: access, safety, privacy, or buyer-path failure blocks scoring or publication
- `CAT-WEB-LEDGER-001`: required evidence or scoring trace is missing

### Warnings

- `CAT-WEB-UNKNOWN-001`: unresolved material website unknown affects score reliability
- `CAT-WEB-MOBILE-001`: mobile scope is incomplete
- `CAT-WEB-FUNCTION-001`: visible functionality was not tested
- `CAT-WEB-COMP-001`: differentiation criterion lacks sufficient comparison evidence

## 15. Worked scoring example

Assume all 12 criteria are applicable and equally weighted.

| Criterion | State | Score | Confidence |
|---|---|---:|---|
| OI-WEB-001 | scored | 75 | High |
| OI-WEB-002 | scored | 50 | High |
| OI-WEB-003 | scored | 50 | High |
| OI-WEB-004 | scored | 25 | High |
| OI-WEB-005 | scored | 50 | Medium |
| OI-WEB-006 | scored | 75 | High |
| OI-WEB-007 | scored | 50 | High |
| OI-WEB-008 | scored | 50 | Medium |
| OI-WEB-009 | scored | 50 | Medium |
| OI-WEB-010 | scored | 25 | Medium |
| OI-WEB-011 | unknown | — | Unknown |
| OI-WEB-012 | scored | 50 | High |

With equal criterion weight:

```text
Applicable Criterion Weight = 12
Known Scored Weight = 11
Category Coverage = 11 ÷ 12 = 91.67%
Observed Category Score = 550 ÷ 11 = 50.00
```

Confidence factors:

```text
High = 1.00
Medium = 0.75
Unknown = 0.00
```

Known-evidence confidence index:

```text
(7 × 1.00 + 4 × 0.75) ÷ 11 = 0.9091
```

The unknown criterion retains a 0–100 uncertainty range. Using the approved criterion bounds for known evidence produces a category range that must be calculated and stored by the calculator from unrounded criterion inputs.

Result:

```yaml
observed_score: 50.0000
coverage: 0.9167
confidence_index: 0.9091
publication_state: provisional
material_unknowns:
  - criterion_id: OI-WEB-011
    reason: competitor comparison not completed
finding_routing:
  - OI-FIND-WEB-004
  - OI-FIND-WEB-012
package_candidates:
  - OI-PKG-SEO-001
  - OI-PKG-WEB-001
ledger_ref: OI-DL-2026-001
```

The category remains provisional because differentiation evidence is incomplete and multiple material structural weaknesses require reviewed finding routing. Package candidates are not automatically approved.

## 16. Completion checklist

Before approving a website category result, confirm:

- all 12 criteria are resolved to an approved state
- desktop and mobile scope is complete or limitations are recorded
- navigation and contact paths were tested safely
- core service pages and URL inventory were reviewed
- visible functionality was not assumed operational
- score anchors match observable evidence
- confidence matches directness and scope
- unknown and blocked items retain applicable weight
- website and adjacent-domain conditions are not double counted
- findings use governed IDs
- package routing is evidence-led
- roadmap phase and dependencies are recorded
- DecisionLedger fields are complete
- publication state matches coverage, confidence, and material unknowns
- client language avoids unsupported redesign, revenue, or outcome claims
