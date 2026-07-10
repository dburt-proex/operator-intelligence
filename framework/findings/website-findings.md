# Website Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable website findings for Operator Intelligence assessments.

Website findings identify where a contractor or local-service website may weaken buyer understanding, trust, navigation, mobile usability, service discovery, or inquiry readiness because the site structure, hierarchy, content presentation, or action paths are unclear, incomplete, broken, or unverified.

This library converts observable website weaknesses into governed findings that can be scored, routed, reported, and implemented without treating visual preference as business evidence.

## v1.0 connection

Operator Intelligence v1.0 requires a governed website layer that connects visible buyer-journey evidence to scoring, recommendations, implementation packages, and report-ready language.

This file strengthens v1.0 readiness by supporting:

- repeatable website evaluation
- clear separation between website, messaging, SEO, trust, and conversion findings
- mobile and navigation evidence standards
- package and roadmap routing
- executive-safe report language
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Website category score is weak, partial, unknown, or inconsistent.
- A visitor cannot quickly identify the business type, services, service area, or next action.
- Services, contact options, proof, or estimate paths are difficult to find.
- Core or high-value services lack clear page architecture.
- Mobile navigation, tap targets, forms, or layouts are difficult to use.
- Page hierarchy, visual hierarchy, or footer structure creates buyer friction.
- Website content does not support buyer decisions with process, proof, expectations, or objections.
- Broken pages, dead links, outdated information, or inconsistent business details are observed.

## Outputs and deliverables

A valid use of this file should produce:

- one or more website findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- cross-domain dependencies
- DecisionLedger entry
- report-safe client language

## Governance rules

1. Do not create a website finding from visual preference alone.
2. Aesthetic criticism must be tied to clarity, usability, trust, accessibility, or action readiness.
3. Do not classify a messaging, SEO, trust, conversion, or analytics weakness as a website finding when another domain is primary.
4. Unknown functionality must be marked `unknown` or `validation_required`, not assumed broken.
5. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
6. Broken paths, mobile failures, inaccessible contact routes, and unclear service architecture outrank cosmetic refinement.
7. Do not recommend a full redesign when a narrower page, navigation, content, or conversion correction resolves the evidence-backed issue.
8. This library does not create a standalone website redesign package. Route work through existing justified packages.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has screenshots, URL inventory, mobile test, navigation review, page copy, link test, form test, or documented validation gap. | Finding is opinion-only. | Mark `validation_required` or remove. |
| Buyer Journey Gate | Finding affects understanding, discovery, trust, usability, or action. | Issue is cosmetic only. | Do not route as website finding. |
| Domain Boundary Gate | Website structure is the primary weakness, or cross-domain dependencies are explicitly recorded. | Finding duplicates another domain without distinction. | Re-route or link dependent findings. |
| Mobile Gate | Mobile behavior is tested for navigation, readability, tap targets, calls, and forms when applicable. | Desktop evidence is used to infer mobile performance. | Test mobile or mark unknown. |
| Function Gate | Links, menus, forms, and action paths are tested when safe. | Visible presence is assumed functional. | Test or state limitation. |
| Confidence Gate | Confidence reflects evidence quality and test coverage. | Certainty is overstated. | Downgrade confidence. |
| Package Gate | Package selection resolves the observed weakness. | A broad redesign is recommended without necessity. | Narrow or block recommendation. |
| Roadmap Gate | Phase reflects urgency and dependency. | Sequence is unclear. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct screenshots, URL review, mobile testing, navigation testing, link testing, or form testing confirms the condition. |
| Medium | Evidence is visible but some device, browser, workflow, or internal context remains untested. |
| Low | Finding depends on client confirmation, inaccessible functionality, unclear CMS behavior, or incomplete page access. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-WEB-001 | Homepage does not immediately communicate the business type | OI-WEB-001, OI-MSG-001 | Above-fold desktop and mobile screenshots | New visitors may need extra effort to determine whether the business matches their need. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-WEB-002 | Service area is unclear or difficult to verify | OI-WEB-002, OI-MSG-008, OI-SEO-007 | Hero, footer, contact page, service-area copy | Local buyers may not know whether the company serves their location. | Local SEO Expansion Pack plus Website Conversion Fix Pack when action clarity is affected | Phase 1 or Phase 2 | High when observable |
| OI-FIND-WEB-003 | Navigation is not organized around buyer tasks | OI-WEB-003, OI-WEB-008 | Desktop and mobile navigation screenshots, menu test, URL inventory | Buyers may struggle to find services, proof, contact information, or estimate paths. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-004 | Core services are collapsed into an overly broad page | OI-WEB-004, OI-SEO-001 | Service list, URL inventory, navigation review | Buyers may receive insufficient detail, while high-intent service discovery remains weak. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-WEB-005 | High-value services are difficult to discover | OI-WEB-004, OI-MSG-010, OI-SEO-002 | Homepage, navigation, service-page inventory, client-confirmed priority services | Strategic services may receive less visibility and fewer qualified inquiry opportunities. | Local SEO Expansion Pack plus Website Conversion Fix Pack if action paths are weak | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-WEB-006 | Contact or estimate path requires unnecessary navigation | OI-WEB-007, OI-CONV-001, OI-CONV-003 | Navigation test, CTA inventory, page-path review | Interested buyers may abandon before reaching an inquiry option. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-007 | Phone number is difficult to find or use | OI-WEB-006, OI-CONV-007 | Header, footer, contact page, mobile tap-to-call test | High-intent visitors may not be able to call quickly, especially on mobile. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-008 | Mobile navigation is difficult or unreliable | OI-WEB-003, OI-WEB-005 | Mobile menu test, screenshots, device/browser notes | Mobile visitors may be unable to discover services or reach contact paths efficiently. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-009 | Mobile readability or tap targets create friction | OI-WEB-005, OI-WEB-009 | Mobile screenshots, text-size review, tap-target test | Visitors may struggle to scan content or complete intended actions. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-010 | Mobile forms are difficult to complete | OI-WEB-005, OI-CONV-004, OI-CONV-005 | Mobile form test, field review, error-state review | Qualified buyers may abandon the inquiry process before submission. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-011 | Visual hierarchy does not support scanning | OI-WEB-009 | Key-page screenshots, heading review, CTA visibility review | Buyers may miss important services, proof, differentiators, or next steps. | Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium to High |
| OI-FIND-WEB-012 | Service pages do not support buyer decision-making | OI-WEB-010, OI-MSG-003, OI-MSG-006, OI-MSG-007 | Service-page copy, process, FAQ, proof, and CTA review | Buyers may understand the service category but lack enough context to move toward an estimate. | Local SEO Expansion Pack, Trust Proof System, or Website Conversion Fix Pack based on primary gap | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-WEB-013 | Website presentation is generic relative to local competitors | OI-WEB-011, OI-MSG-002, OI-COMP related signals | Homepage comparison, competitor screenshots, copy review | The business may be harder to distinguish when buyers compare several local providers. | Trust Proof System plus Website Conversion Fix Pack when differentiation is absent from decision areas | Phase 2 — Growth Foundation | Medium |
| OI-FIND-WEB-014 | Footer does not support navigation, contact, or credibility | OI-WEB-012 | Footer screenshot, link test, business-detail review | Buyers may lose access to important service, contact, location, or trust information at the end of a page. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-WEB-015 | Trust proof is not integrated into key pages | OI-WEB-010, OI-TRUST-001, OI-TRUST-003 | Homepage, service pages, CTA sections, project proof review | Buyers may not encounter enough evidence to reduce uncertainty during the decision journey. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-WEB-016 | Broken links, dead pages, or incomplete paths are present | OI-WEB-008 | Link test, URL inventory, error screenshots | Broken paths may interrupt service discovery, reduce credibility, or block inquiries. | Website Conversion Fix Pack for buyer-facing paths; Local SEO Expansion Pack for structural URL issues | Phase 1 — Quick Wins | High when tested |
| OI-FIND-WEB-017 | Business information is inconsistent across website sections | OI-WEB-002, OI-WEB-012, OI-SEO-015 | Header, footer, contact page, service-area page, GBP comparison | Inconsistent contact or service-area details may create buyer confusion and local-search risk. | Local SEO Expansion Pack plus Google Business Authority Pack when GBP is involved | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-WEB-018 | Website functionality or ownership is unverified | OI-WEB related signals | CMS access, hosting information, form destination, domain records, client interview | Implementation planning may be unreliable until access, ownership, and system constraints are confirmed. | Validation task before package commitment | Phase 1 validation gate | Low or Unknown |

## Criteria mapping rules

Use website findings as the primary finding type when the main issue is page structure, navigation, hierarchy, usability, mobile behavior, page availability, or functional buyer access.

Use cross-domain routing when another domain explains the primary weakness:

| Website observation | Primary or dependent domain | Routing rule |
|---|---|---|
| Hero exists but message is vague | Messaging | Messaging finding is primary; website finding may document placement. |
| Service pages are absent | SEO | SEO finding is primary; website finding documents architecture impact. |
| CTA exists but is passive or poorly placed | Conversion | Conversion finding is primary. |
| Proof assets are missing or poorly placed | Trust | Trust finding is primary. |
| Forms submit but leads are not tracked | Automation | Automation finding is primary. |
| Website activity cannot be measured | Analytics | Analytics finding is primary. |
| GBP and website details conflict | GBP | Pair website and GBP findings with one shared evidence record. |
| Competitors provide materially stronger buyer paths | Competitive | Pair with competitive finding when comparison determines priority. |

## Evidence requirements

Acceptable evidence includes:

- desktop screenshot
- mobile screenshot
- URL inventory
- navigation test
- page copy review
- CTA review
- form test
- tap-to-call test
- link test
- footer review
- competitor comparison
- GBP screenshot
- analytics or Search Console evidence
- CMS or hosting access
- client interview

Minimum evidence by finding type:

| Finding group | Minimum evidence |
|---|---|
| First impression | Desktop and mobile above-fold screenshots. |
| Navigation | Desktop and mobile menu screenshots plus path test. |
| Service architecture | Service list compared with URL inventory. |
| Contact path | CTA inventory plus path or tap test. |
| Mobile usability | Mobile screenshots plus interaction test. |
| Content support | Service-page review covering process, proof, objections, and action. |
| Broken functionality | Test result plus screenshot or URL. |
| Ownership/access | CMS, hosting, form destination, domain, or client-confirmed access record. |

If a form, call link, CMS, device, or browser cannot be tested safely, mark the relevant condition `validation_required`.

## Business impact language

Use executive-safe language focused on the buyer journey.

| Avoid | Use instead |
|---|---|
| The website is bad. | The website provides baseline information, but the buyer journey does not yet create a strong path from interest to estimate request. |
| The design is outdated. | The current presentation may make key services, proof, and next actions harder to identify quickly. |
| The mobile site is terrible. | The mobile experience contains usability friction that may make service discovery or inquiry completion more difficult. |
| The navigation makes no sense. | The navigation could be reorganized around the primary tasks buyers need to complete. |
| You need a new website. | The evidence supports targeted improvements to structure, mobile usability, service architecture, and action paths before a full rebuild is considered. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Navigation, CTA access, phone visibility, mobile usability, or contact path is weak. | Website Conversion Fix Pack | Default for Phase 1 buyer-path corrections. |
| Core or high-value service architecture is missing. | Local SEO Expansion Pack | Default for service-page structure and discovery. |
| Reviews, project proof, team proof, or risk reduction are absent from key pages. | Trust Proof System | Use when proof is the primary constraint. |
| Website and GBP information or service coverage conflict. | Google Business Authority Pack plus Local SEO Expansion Pack | Coordinate shared business information and service alignment. |
| Forms function but routing, ownership, or follow-up is weak. | CRM and Follow-Up System | Website finding remains dependent. |
| Website outcomes cannot be measured. | Operator Dashboard Pack | Route to Phase 3 measurement work. |
| Access, ownership, hosting, or form destinations are unknown. | Validation task before package commitment | Do not scope a rebuild from unverified constraints. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Broken navigation, unclear first impression, buried contact path, unusable mobile interactions, dead links, or missing phone visibility directly obstruct buyer action. |
| Phase 2 — Growth Foundation | Service architecture, content depth, proof integration, differentiation, local relevance, or structural page improvements are required. |
| Phase 3 — Automation and Reporting | Website forms, attribution, analytics, CRM routing, or reporting must be connected to internal systems. |
| Phase 4 — Governed AI Enablement | Only use when AI is proposed for intake, content assistance, chat, personalization, or site operations and governed review controls are required. |

## Report-use rules

A website finding can enter a client report only when:

1. The observation affects buyer understanding, discovery, trust, usability, or action readiness.
2. Evidence is listed or the gap is marked `validation_required`.
3. The primary domain and any dependent domains are identified.
4. Confidence is assigned.
5. Business impact is stated without unsupported performance claims.
6. Package selection is narrow enough to resolve the evidence-backed issue.
7. Roadmap phase is assigned.
8. DecisionLedger entry can be completed.

Do not recommend a full website rebuild solely because the current design appears dated or generic.

## DecisionLedger requirements

Each website recommendation must include:

```text
finding_id:
observation:
evidence:
primary_domain:
dependent_domains:
interpretation:
business_impact:
confidence:
priority:
recommended_package:
roadmap_phase:
validation_required:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-WEB-003
observation: The mobile menu does not provide a direct path to the service list or estimate page.
evidence: Mobile navigation screenshot and menu interaction test.
primary_domain: Website
 dependent_domains:
  - Conversion
interpretation: Mobile buyers must navigate through multiple pages before reaching core services or an inquiry path.
business_impact: This may increase buyer friction during high-intent mobile visits.
confidence: High
priority: High
recommended_package: Website Conversion Fix Pack
roadmap_phase: Phase 1 — Quick Wins
validation_required: No
report_section: Website and Buyer Journey
status: report_ready
```

## Usage instructions

1. Review the website score and applicable criteria.
2. Capture desktop and mobile evidence from the same key pages.
3. Test navigation, phone links, forms, and contact paths when safe.
4. Compare the service list with the available page architecture.
5. Separate structural website issues from messaging, SEO, trust, conversion, automation, and analytics issues.
6. Select the narrowest matching finding.
7. Assign confidence based on actual test coverage.
8. Route to an existing implementation package and roadmap phase.
9. Complete the DecisionLedger record.
10. Mark inaccessible or untested functionality `validation_required`.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Finding is not aesthetic opinion presented as business fact.
- Primary and dependent domains are clear.
- Mobile evidence is included when applicable.
- Functionality is tested or marked unknown.
- Confidence is not overstated.
- Package selection is justified and narrow.
- Roadmap phase is sequenced.
- Ledger record is complete.
