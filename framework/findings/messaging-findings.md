# Messaging Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable messaging findings for Operator Intelligence assessments.

Messaging findings identify where contractor and local-service businesses may weaken buyer understanding, relevance, differentiation, confidence, or action readiness because their copy is vague, generic, unsupported, inconsistent, overly technical, locally detached, or incomplete.

This library converts observable communication weaknesses into governed findings that can be scored, routed, reported, and implemented without confusing copy preference with business evidence.

## v1.0 connection

Operator Intelligence v1.0 requires a messaging layer that connects buyer-facing language to website clarity, conversion, local relevance, trust, service prioritization, offer understanding, and implementation packages.

This file strengthens v1.0 readiness by supporting:

- repeatable message evaluation
- evidence-backed hero and service-page findings
- clear separation between messaging and offer structure
- differentiation and proof alignment
- local relevance diagnosis
- package and roadmap routing
- executive-safe report language
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Messaging category score is weak, partial, unknown, or inconsistent.
- The homepage does not quickly state the service, customer outcome, service area, or next step.
- Differentiators are missing, generic, or unsupported.
- Service copy describes tasks without addressing buyer concerns, fit, process, or outcomes.
- The buyer cannot tell what happens after inquiry or during service delivery.
- Pricing factors, timeline, preparation, cleanup, warranty, availability, or other objections are not addressed where appropriate.
- Local relevance is weak or interchangeable with competitors in other markets.
- High-value or strategically important services are not emphasized.
- Claims such as quality, reliable, affordable, experienced, or professional appear without supporting evidence.
- Messaging differs materially across the homepage, service pages, Google Business Profile, social profiles, or sales materials.

## Outputs and deliverables

A valid use of this file should produce:

- one or more messaging findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- cross-domain dependencies
- validation requirements
- DecisionLedger entry
- report-safe client language

## Governance rules

1. Do not create a messaging finding from writing-style preference alone.
2. Messaging criticism must be tied to buyer understanding, relevance, trust, differentiation, qualification, or action readiness.
3. Do not claim that copy changes will produce traffic, leads, sales, or revenue without validated performance evidence.
4. Unknown audience, service priority, margin, delivery process, or operational differentiator information must be marked `unknown` or `validation_required`.
5. Distinguish message expression from offer structure. Use this library when the business has something valid to communicate but communicates it weakly. Route commercial packaging, scope, pricing model, guarantee economics, or sales-system problems to `offer-findings.md`.
6. Distinguish unsupported claims from verified operational differentiators.
7. Do not invent guarantees, credentials, response standards, years in business, pricing claims, availability, service areas, or proof.
8. High-value service emphasis requires client confirmation, reliable financial data, or a documented strategic priority.
9. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
10. Client-facing language must describe communication gaps without insulting the business, brand, owner, or existing copy.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has page copy, screenshots, CTA inventory, service-page review, GBP copy, competitor comparison, client interview, or documented validation gap. | Finding is based only on evaluator taste. | Mark `validation_required` or remove. |
| Buyer Understanding Gate | Finding affects what the buyer understands about service, outcome, fit, process, proof, locality, or next action. | Issue is stylistic only. | Do not route as messaging finding. |
| Accuracy Gate | Recommended language is supported by real services, processes, proof, credentials, service areas, and policies. | Rewrite would introduce unsupported claims. | Block recommendation. |
| Proof Alignment Gate | Claims are paired with available evidence or clearly qualified. | Vague or unsupported superlatives remain. | Replace with proof, process, or specific language. |
| Offer Boundary Gate | The issue is message expression, or an offer dependency is explicitly recorded. | A commercial structure problem is disguised as a copy problem. | Route to offer finding. |
| Local Relevance Gate | Local language reflects real service areas, projects, conditions, or market context. | Copy inserts unsupported locations or generic keyword lists. | Correct or remove. |
| Priority Service Gate | Service emphasis is supported by strategic, demand, capacity, or financial evidence. | Evaluator assumes which service should lead. | Request owner validation. |
| Confidence Gate | Confidence reflects evidence quality and internal-information limits. | Certainty is overstated. | Downgrade confidence. |
| Package Gate | Package selection resolves the demonstrated communication weakness. | Broad work is recommended without evidence. | Narrow or block recommendation. |
| Roadmap Gate | Phase reflects urgency and dependency. | Sequence is unclear. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct page copy, screenshots, CTA review, service-page review, or verified cross-channel comparison confirms the condition. |
| Medium | Buyer-facing evidence confirms the pattern, but audience, service priority, operational proof, or strategic context remains partly unverified. |
| Low | Finding depends on owner recollection, unavailable sales data, unclear service economics, undocumented processes, or unverified differentiators. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-MSG-001 | Hero message does not state a specific customer outcome | OI-MSG-001, OI-WEB-001 | Homepage hero copy, desktop and mobile screenshots | New visitors may understand that services are offered but not why the business is relevant to their immediate need. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-MSG-002 | Hero does not clearly connect service, location, outcome, and action | OI-MSG-001, OI-MSG-005, OI-MSG-008, OI-CONV-001 | Hero copy, CTA, service-area copy, mobile screenshot | Buyers may need additional effort to determine fit and what to do next. | Website Conversion Fix Pack plus Local SEO Expansion Pack when local relevance is also weak | Phase 1 — Quick Wins | High when observable |
| OI-FIND-MSG-003 | Differentiation is absent or generic | OI-MSG-002, OI-WEB-011 | Homepage, about page, service-page copy, competitor comparison | The business may appear interchangeable when buyers compare several local providers. | Trust Proof System plus Website Conversion Fix Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-MSG-004 | Differentiators are stated but unsupported | OI-MSG-002, OI-MSG-009, OI-TRUST related signals | Claims inventory, proof review, process review, client validation | Buyers may encounter promises that do not yet have visible evidence, reducing credibility. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-MSG-005 | Copy lists tasks without addressing buyer pain points | OI-MSG-003 | Service-page copy, FAQ review, competitor comparison, client interview | Buyers may see what the company does but not how it resolves concerns about risk, timeline, quality, disruption, cleanup, price, or communication. | Local SEO Expansion Pack plus Website Conversion Fix Pack when action clarity is affected | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-MSG-006 | Service descriptions are thin, vague, or interchangeable | OI-MSG-004, OI-WEB-010, OI-SEO-008 | Service-page inventory, page copy, URL review | Buyers may not receive enough detail to evaluate scope, fit, process, proof, or next steps. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-MSG-007 | Service descriptions do not clarify customer fit or project scope | OI-MSG-004, OI-CONV-004, OI-CONV-009 | Service-page copy, intake form, qualification questions, client interview | The business may receive lower-context inquiries or create uncertainty about which projects it accepts. | Local SEO Expansion Pack plus CRM and Follow-Up System when intake is also weak | Phase 2 for copy; Phase 3 for workflow | Medium |
| OI-FIND-MSG-008 | The buyer-facing offer is unclear in the copy | OI-MSG-005, OI-CONV-002 | Homepage, service pages, CTA inventory, contact page | Buyers may not know whether they are requesting an estimate, consultation, inspection, quote, service call, or another next step. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-MSG-009 | Process is not explained | OI-MSG-006, OI-TRUST-008 | Homepage, service pages, FAQ, process section | Buyers may hesitate because they do not understand what happens from first contact through completion. | Trust Proof System plus Website Conversion Fix Pack when inquiry expectations are also unclear | Phase 2, or Phase 1 if blocking inquiry | High when observable |
| OI-FIND-MSG-010 | Response or next-step expectations are unclear | OI-MSG-005, OI-MSG-006, OI-CONV-006, OI-CONV-010 | Contact page, form confirmation, CTA copy, process copy | Interested buyers may continue shopping because timing and follow-up expectations are not stated. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-MSG-011 | Common objections are not addressed | OI-MSG-007, OI-SEO-008 | FAQ, service-page copy, sales notes, client interview | Buyers may delay inquiry when pricing factors, timing, preparation, cleanup, access, warranty, or availability questions remain unanswered. | Local SEO Expansion Pack plus Trust Proof System when risk reduction is central | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-MSG-012 | Pricing language is absent, misleading, or insufficiently qualified | OI-MSG-007, OI-MSG-009 | Pricing copy, estimate language, client-confirmed pricing policy | Buyers may form inaccurate expectations or avoid inquiry because cost factors are not explained appropriately. | Website Conversion Fix Pack or Local SEO Expansion Pack based on placement | Phase 2 — Growth Foundation | Low to Medium until pricing policy is validated |
| OI-FIND-MSG-013 | Message lacks local relevance | OI-MSG-008, OI-SEO-007, OI-TRUST-010 | Homepage, service pages, project examples, service-area copy | The business may appear less connected to the actual communities, property conditions, or buyer context it serves. | Local SEO Expansion Pack plus Trust Proof System when local proof is weak | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-MSG-014 | Local language is generic or unsupported | OI-MSG-008, OI-MSG-009 | Location references, service-area validation, project proof, client interview | Generic city lists may add words without increasing buyer confidence or genuine local relevance. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-MSG-015 | Copy relies on vague claims without evidence | OI-MSG-009, OI-TRUST related signals | Full-site claims inventory, review proof, credential review, project proof | Claims such as quality, reliable, affordable, or professional may not meaningfully differentiate the business. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-MSG-016 | Claims overstate guarantees, availability, performance, or service scope | OI-MSG-009 | Claims inventory, policy review, service list, client validation | Unsupported promises may create expectation, credibility, or delivery risk. | Trust Proof System; block publication until validated | Phase 1 if actively misleading; otherwise Phase 2 | Medium until validated |
| OI-FIND-MSG-017 | High-value or strategic services are not emphasized | OI-MSG-010, OI-WEB-004, OI-SEO-002 | Homepage, navigation, CTA inventory, client-confirmed priorities, financial or capacity data when available | Priority services may receive limited buyer attention and weak support across the site. | Local SEO Expansion Pack plus Website Conversion Fix Pack | Phase 2 — Growth Foundation | Low to Medium until priorities are confirmed |
| OI-FIND-MSG-018 | Service emphasis does not match capacity or operating priorities | OI-MSG-010 | Website emphasis, client interview, service mix, capacity constraints | Marketing may direct attention toward work the business does not currently prioritize or have capacity to fulfill. | Local SEO Expansion Pack after owner validation | Phase 2 — Growth Foundation | Low until validated |
| OI-FIND-MSG-019 | Messaging is inconsistent across pages or channels | OI-MSG-001, OI-MSG-002, OI-MSG-004, OI-MSG-008 | Homepage, service pages, GBP, social profiles, sales materials | Buyers may encounter conflicting descriptions of services, location, value, or next steps. | Website Conversion Fix Pack, Google Business Authority Pack, or Local SEO Expansion Pack based on affected channel | Phase 1 for contact/service conflicts; otherwise Phase 2 | High when observable |
| OI-FIND-MSG-020 | Copy uses internal jargon or technical language without buyer context | OI-MSG-003, OI-MSG-004 | Page copy, glossary review, client interview | Buyers may struggle to understand service relevance, scope, or outcomes. | Website Conversion Fix Pack or Local SEO Expansion Pack | Phase 1 for core-page clarity; otherwise Phase 2 | High when observable |
| OI-FIND-MSG-021 | Message does not distinguish residential, commercial, emergency, seasonal, or specialty fit where relevant | OI-MSG-003, OI-MSG-004, OI-MSG-010 | Service-page copy, navigation, intake form, client-confirmed segments | Buyers may not know whether the business serves their project type, urgency, or customer segment. | Local SEO Expansion Pack plus Website Conversion Fix Pack when action paths differ | Phase 2 — Growth Foundation | Medium to High |

## Criteria mapping rules

Use messaging findings as the primary finding type when the weakness concerns what the business communicates, how clearly it communicates it, or whether claims are supported.

Use cross-domain routing when evidence shows another primary dependency:

| Messaging issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Message is clear but CTA path is weak | Conversion | Route the action problem to conversion findings. |
| Service copy is thin because dedicated pages are missing | SEO or Website | Pair with SEO or website finding based on structural cause. |
| Claims lack reviews, credentials, process, or project proof | Trust | Pair with trust finding when missing evidence is the main constraint. |
| The service, scope, pricing model, guarantee economics, or sales motion is undefined | Offer | Route to offer finding; copy cannot resolve an undefined commercial structure. |
| Service priority is unknown | Offer or Analytics | Mark `validation_required` and use financial, demand, capacity, or owner evidence before reprioritizing. |
| GBP description or services conflict with the site | GBP | Pair with GBP finding for channel correction and ownership. |
| Message performance cannot be evaluated | Analytics | Pair with analytics finding when conversion or engagement measurement is unavailable. |
| Competitors make similar claims with stronger proof | Competitive | Pair with competitive finding when market comparison drives priority. |

## Evidence requirements

Acceptable evidence includes:

- screenshot
- URL inventory
- page copy
- CTA review
- form test
- mobile test
- GBP screenshot
- review comparison
- competitor comparison
- analytics
- Search Console
- CRM record
- client interview
- social review
- sales notes
- proposal or estimate language

Minimum evidence by finding type:

| Finding group | Minimum evidence |
|---|---|
| Hero clarity | Desktop and mobile hero copy or screenshots. |
| Differentiation | Copy inventory plus proof review or competitor comparison. |
| Pain-point alignment | Service-page review plus client or buyer-context evidence when available. |
| Service specificity | Service-page inventory and page copy. |
| Offer wording | Homepage, service-page, CTA, and contact-page review. |
| Process and objections | Process, FAQ, form confirmation, or sales-material review. |
| Local relevance | Local copy plus service-area or project-proof validation. |
| Unsupported claims | Claim inventory plus evidence review. |
| Priority-service emphasis | Client confirmation, financial data, demand data, capacity data, or documented strategic priority. |
| Cross-channel consistency | Comparison across at least two buyer-facing channels. |

If internal service priorities, pricing rules, delivery process, guarantees, or differentiation evidence are unavailable, mark the relevant conclusion `validation_required`.

## Business impact language

Use report-safe language that frames the issue as buyer understanding and decision support.

| Weak wording | Use instead |
|---|---|
| Your copy is bad. | The current copy communicates the service at a baseline level, but it does not yet provide a strong outcome, proof, or next-step message. |
| Your business sounds generic. | The messaging uses claims common across local competitors, which may make the business harder to distinguish during comparison. |
| Nobody understands this. | Some service language relies on internal or technical terminology that may require additional buyer context. |
| Your value proposition is weak. | The site does not yet connect its operational strengths to specific buyer concerns and outcomes. |
| You need better sales copy. | The strongest opportunity is to clarify service fit, process, proof, and next steps at key decision points. |
| This will increase revenue. | Clearer messaging may reduce buyer uncertainty; performance impact should be validated through conversion and lead-quality tracking. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Hero, CTA support, response expectation, or core-page clarity is weak. | Website Conversion Fix Pack | Default Phase 1 for action-critical copy. |
| Service descriptions, local relevance, FAQs, or buyer-intent depth are weak. | Local SEO Expansion Pack | Default Phase 2. |
| Differentiators or claims lack proof. | Trust Proof System | Phase 2. Do not invent evidence. |
| GBP messaging conflicts with the website. | Google Business Authority Pack plus relevant website package | Correct both sources of inconsistency. |
| Intake or qualification wording depends on workflow changes. | CRM and Follow-Up System | Phase 3 after message and process are defined. |
| Performance cannot be validated. | Operator Dashboard Pack or analytics validation | Phase 3 if measurement setup is required. |
| Offer itself is undefined. | Defer package routing until `offer-findings.md` identifies the commercial structure issue. | Messaging rewrite is blocked until the offer is valid enough to communicate. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Message weakness affects immediate understanding, contact, CTA meaning, response expectation, or an actively misleading claim. |
| Phase 2 — Growth Foundation | Default for differentiation, service-page depth, process, objections, local relevance, proof alignment, and priority-service emphasis. |
| Phase 3 — Automation and Reporting | Use when messaging depends on CRM fields, qualification logic, response templates, testing, or measurement systems. |
| Phase 4 — Governed AI Enablement | Only use when AI is proposed for content drafting, personalization, response generation, or content operations and requires approved source material, review gates, escalation, and output logging. |

## Report-use rules

A messaging finding can enter a client report only when:

1. The finding affects buyer understanding, relevance, differentiation, confidence, qualification, or action readiness.
2. Evidence is listed or the gap is marked `validation_required`.
3. Confidence is assigned.
4. Business impact is stated without unsupported performance claims.
5. Claims and proposed language can be supported by real operations or proof.
6. Offer dependencies are identified rather than hidden inside copy recommendations.
7. Recommended package is justified by the evidence.
8. Roadmap phase is assigned.
9. DecisionLedger entry can be completed.

Do not publish rewritten claims, guarantees, pricing statements, response standards, credentials, service areas, or differentiators without client validation when direct evidence is unavailable.

## DecisionLedger requirements

Each messaging recommendation must include this ledger record:

```text
finding_id:
observation:
evidence:
interpretation:
business_impact:
confidence:
priority:
primary_domain:
dependent_domains:
claims_requiring_validation:
offer_dependency:
recommended_package:
roadmap_phase:
owner_validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-MSG-001
observation: The homepage hero describes the company as a provider of professional services but does not state a specific customer outcome, service area, or estimate action.
evidence: Desktop and mobile homepage screenshots and hero copy review.
interpretation: Visitors can identify that the business offers services, but they receive limited guidance about relevance, expected value, or next step.
business_impact: This may reduce clarity at the first decision point and require buyers to search deeper before confirming fit.
confidence: High
priority: High
primary_domain: Messaging
dependent_domains:
  - Website
  - Conversion
claims_requiring_validation: None
offer_dependency: No
recommended_package: Website Conversion Fix Pack
roadmap_phase: Phase 1 — Quick Wins
owner_validation_needed: Yes, final outcome and service-area wording
report_section: Messaging Findings
status: report_ready
```

## Usage instructions

1. Review the messaging score and `OI-MSG-001` through `OI-MSG-010`.
2. Capture homepage, service-page, CTA, FAQ, process, local, and proof language.
3. Separate communication weakness from website structure, conversion path, missing proof, and undefined offer problems.
4. Inventory all claims that require evidence or client validation.
5. Confirm service priorities before recommending hierarchy changes.
6. Select the closest governed finding ID.
7. Assign confidence based on evidence quality.
8. Record cross-domain and offer dependencies.
9. Route to an existing package and roadmap phase.
10. Write the finding using client-safe language.
11. Add the DecisionLedger record.
12. Mark missing internal evidence `validation_required` rather than inventing copy.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Finding affects buyer understanding or decision support.
- Message and offer problems are separated.
- Claims are supportable or marked for validation.
- Service priorities are verified before emphasis changes.
- Confidence is not overstated.
- Business impact is clear.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.
