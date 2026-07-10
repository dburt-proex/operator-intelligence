# Competitive Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable competitive findings for Operator Intelligence assessments.

Competitive findings identify where a contractor or local-service business may be disadvantaged during buyer comparison because competitors present stronger review proof, service coverage, local search visibility, conversion paths, content, positioning, work proof, or overall buyer confidence.

This library converts observable competitive differences into governed findings that can be scored, routed, reported, and implemented without treating competitor imitation, isolated search results, or evaluator preference as strategy.

## v1.0 connection

Operator Intelligence v1.0 requires a competitive layer that explains relative market position without weakening evidence discipline or recommendation precision.

This file strengthens v1.0 readiness by supporting:

- repeatable competitor selection
- comparable-market evidence controls
- competitive gap classification
- cross-domain recommendation routing
- roadmap prioritization
- executive-safe competitive language
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Competitive category score is weak, partial, unknown, or inconsistent.
- The business cannot identify its primary local competitors by service and geography.
- Competitors have materially stronger review count, recency, rating, or response behavior.
- Competitors provide deeper service-page coverage or stronger local relevance.
- Competitors show stronger project proof, case studies, team proof, or risk-reduction signals.
- Competitor messaging is more specific, differentiated, or proof-backed.
- Competitors appear more consistently for verified target searches.
- Competitors make calling, requesting an estimate, or understanding next steps easier.
- Competitors publish more useful project, educational, social, or GBP content.
- Competitive gaps have been observed but are not translated into a governed roadmap.

## Outputs and deliverables

A valid use of this file should produce:

- defined competitive set
- comparison scope and observation date
- one or more competitive findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- primary affected domain
- recommended implementation package
- roadmap phase
- DecisionLedger entry
- report-safe client language

## Governance rules

1. Do not create a competitive finding until the comparison set, geography, service scope, and observation date are documented.
2. Use named, observable competitors that serve a comparable buyer, service category, and market.
3. Do not treat one personalized, localized, or temporary search result as proof of stable ranking position.
4. Do not claim a competitor has higher revenue, profitability, lead volume, conversion rate, market share, or operating quality without reliable evidence.
5. Distinguish visible market presentation from internal operating performance.
6. Do not recommend copying competitor wording, design, offers, claims, photos, or content.
7. Competitive strength is domain-specific. A competitor may lead in reviews while remaining weaker in conversion, proof, messaging, or service depth.
8. Differences must be material enough to affect buyer comparison, discovery, trust, action, or strategic priority.
9. Unknown or inaccessible competitor conditions must be marked `unknown` or `validation_required`.
10. Route recommendations to the domain package that resolves the gap. Do not create a generic competitive package.
11. Brand-polish findings must be tied to clarity, credibility, proof, hierarchy, consistency, or buyer confidence, not taste alone.
12. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Competitive Set Gate | Competitors are named and comparable by service, geography, and buyer type. | Comparison uses unrelated, national, adjacent, or selectively chosen businesses. | Replace or qualify comparison set. |
| Evidence Gate | Finding has dated screenshots, URL inventory, profile comparison, page review, review comparison, search evidence, or documented validation gap. | Finding relies on memory or general impression. | Mark `validation_required` or remove. |
| Comparability Gate | Compared signals use equivalent pages, profiles, services, locations, and timeframes. | Unequal evidence is treated as direct comparison. | Normalize scope or lower confidence. |
| Attribution Gate | The visible gap is assigned to the primary domain causing it. | Competitive language substitutes for domain diagnosis. | Route to website, SEO, GBP, trust, messaging, conversion, offer, automation, or analytics. |
| Search Evidence Gate | Search term, location context, device/context limits, and observation date are recorded. | A single result is presented as stable market position. | Qualify evidence or require broader validation. |
| Materiality Gate | Difference affects buyer discovery, confidence, action, service fit, or implementation priority. | Difference is cosmetic or trivial. | Exclude from client report. |
| Accuracy Gate | Claims describe only what evidence supports. | Internal performance or financial strength is inferred from public presentation. | Rewrite or block finding. |
| Non-Imitation Gate | Recommendation creates an original, evidence-aligned improvement. | Recommendation copies competitor assets or claims. | Redesign recommendation. |
| Confidence Gate | Confidence reflects source quality, comparability, and recency. | Certainty is overstated. | Downgrade confidence. |
| Package Gate | Existing package resolves the diagnosed gap. | Generic competitive work is recommended without domain action. | Re-route or block recommendation. |
| Roadmap Gate | Phase reflects urgency, dependency, and business readiness. | Competitive gaps become an unsequenced wish list. | Assign phase and dependency. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Dated, direct, like-for-like evidence confirms a material difference across named comparable competitors. |
| Medium | Public evidence supports the pattern, but search variability, market comparability, timing, or internal context remains partly uncertain. |
| Low | Finding depends on a narrow sample, client recollection, incomplete competitor coverage, inaccessible pages, or unverified strategic assumptions. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-COMP-001 | Primary competitive set is undefined or unreliable | OI-COMP-001 | Client input, search evidence, service-area review, competitor URLs | The assessment cannot reliably distinguish market gaps from evaluator assumptions. | Operator Dashboard Pack only if ongoing monitoring is required; otherwise validation task | Phase 1 — Quick Wins | Low until validated |
| OI-FIND-COMP-002 | Competitor selection does not match service, geography, or buyer type | OI-COMP-001 | Comparison matrix, service lists, service areas, target-customer review | Weak comparability can misdirect recommendations and roadmap priority. | Validation task before package routing | Phase 1 — Quick Wins | High when mismatch is observable |
| OI-FIND-COMP-003 | Review count is materially weaker than comparable competitors | OI-COMP-002, OI-GBP-007 | Named competitor review-count screenshots, observation date, service and market match | Buyers may encounter substantially more visible reputation proof from competitors. | Review Generation System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-COMP-004 | Review recency or velocity is weaker than comparable competitors | OI-COMP-002, OI-GBP-008 | Recent-review dates, review sample, competitor comparison | Competitors may appear more active and recently validated by customers. | Review Generation System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-COMP-005 | Competitors use reviews more effectively in buyer-facing pages | OI-COMP-002, OI-TRUST-001, OI-TRUST-012 | Website screenshots, CTA-area comparison, review placement | The business may have valid reviews but provide less proof at decision points. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-COMP-006 | Competitors provide deeper core-service page coverage | OI-COMP-003, OI-SEO-001 | URL inventories, service lists, page comparison | Competitors may match high-intent service searches and buyer questions more directly. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when comparable |
| OI-FIND-COMP-007 | Competitors provide stronger high-value service coverage | OI-COMP-003, OI-SEO-002, OI-MSG-010 | Priority-service validation, URL inventories, page comparison | Strategic services may receive weaker visibility and buyer support than competitor equivalents. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium until priorities are confirmed |
| OI-FIND-COMP-008 | Competitors provide stronger local service-area relevance | OI-COMP-003, OI-SEO-007, OI-MSG-008 | Location-page comparison, local project examples, service-area copy | The business may appear less connected to the communities and conditions it serves. | Local SEO Expansion Pack plus Trust Proof System when proof is central | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-COMP-009 | Competitors show stronger project and work proof | OI-COMP-004, OI-TRUST-003, OI-TRUST-004 | Galleries, before/after assets, project-page comparison | Buyers may have more evidence to evaluate competitor quality, fit, and experience. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-COMP-010 | Competitors provide stronger case studies or customer stories | OI-COMP-004, OI-TRUST-004 | Case-study inventory, service relevance, project-detail comparison | Higher-value or complex services may be easier to trust when competitors explain comparable outcomes in more depth. | Trust Proof System plus Local SEO Expansion Pack when pages are indexable growth assets | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-COMP-011 | Competitor messaging is more specific or differentiated | OI-COMP-005, OI-MSG-002 | Homepage and service-page copy comparison, proof review | The business may appear interchangeable when buyers compare providers. | Trust Proof System plus Website Conversion Fix Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-COMP-012 | Competitor differentiators are better supported by proof | OI-COMP-005, OI-MSG-009, OI-TRUST related signals | Claims inventory, proof comparison, process comparison | Competitor claims may be more credible because buyers can see supporting evidence. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-COMP-013 | Business visibility appears weaker for documented target searches | OI-COMP-006 | Dated search screenshots, terms, location context, Search Console when available, competitor results | The business may have reduced discoverability for verified high-intent local searches. | Local SEO Expansion Pack plus Google Business Authority Pack based on result type | Phase 2 — Growth Foundation | Low to Medium without broader validation |
| OI-FIND-COMP-014 | Competitors have stronger Google Business Profile presentation | OI-COMP-002, OI-COMP-006, OI-GBP related signals | Profile comparison, categories, services, photos, reviews, activity | Buyers may encounter stronger relevance, proof, or profile completeness from competitors. | Google Business Authority Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-COMP-015 | Competitors provide clearer or easier inquiry paths | OI-COMP-007, OI-CONV related signals | CTA, phone, form, booking, mobile-path comparison | Buyers may be able to act with less friction on competitor websites. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-COMP-016 | Competitors set clearer response or next-step expectations | OI-COMP-007, OI-CONV-006, OI-CONV-010 | Form confirmation, contact page, process copy, competitor comparison | Competitors may reduce uncertainty more effectively after buyer action. | Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium to High |
| OI-FIND-COMP-017 | Competitors publish more useful project or buyer-education content | OI-COMP-008, OI-SEO-008, OI-SEO-014 | Content inventory, recency, service relevance, project examples | Competitors may provide stronger discovery, proof, and decision support. | Local SEO Expansion Pack plus Trust Proof System when project proof is central | Phase 2 — Growth Foundation | Medium |
| OI-FIND-COMP-018 | Competitor content cadence is higher but strategic value is unverified | OI-COMP-008 | Dated content inventory, topic relevance, engagement or performance data when available | A visible activity gap exists, but publication volume alone does not justify investment. | Operator Dashboard Pack for validation, then domain package if impact is proven | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-COMP-019 | Competitors present stronger professional consistency | OI-COMP-009, OI-WEB-009, OI-TRUST related signals | Cross-page screenshots, photo quality, hierarchy, business-detail consistency | Buyers may perceive competitors as easier to understand or more credible during comparison. | Website Conversion Fix Pack or Trust Proof System based on primary cause | Phase 2 — Growth Foundation | Medium |
| OI-FIND-COMP-020 | Competitive gaps are documented but not prioritized in the roadmap | OI-COMP-010 | Findings ledger, roadmap, package map, priority scores | The assessment may identify differences without converting them into sequenced action. | Route each gap to its existing implementation package | Phase based on underlying finding | High when observable |
| OI-FIND-COMP-021 | Competitive roadmap priorities are based on imitation rather than business fit | OI-COMP-010 | Roadmap rationale, competitor evidence, client goals, capacity and strategy review | The business may invest in features or channels that do not match its offer, capacity, evidence, or buyer journey. | Re-route through DecisionLedger and relevant domain package | Phase 1 — Quick Wins for correction | Medium to High |

## Criteria mapping rules

Use competitive findings when relative market evidence materially changes confidence, priority, or sequencing.

Do not use competitive findings as a substitute for primary domain findings. Every material competitive gap should identify the domain that owns implementation.

| Competitive gap | Primary domain | Routing rule |
|---|---|---|
| Review count, recency, responses, or profile strength | GBP / Trust / Automation | Route to Google Business Authority Pack, Trust Proof System, or Review Generation System. |
| Missing or weak service pages | SEO / Website | Route to Local SEO Expansion Pack. |
| Weak proof, galleries, case studies, or credibility | Trust | Route to Trust Proof System. |
| Generic positioning or unsupported differentiation | Messaging / Trust | Route to Website Conversion Fix Pack and/or Trust Proof System. |
| Weak local search presence | SEO / GBP / Analytics | Route based on whether evidence shows website, profile, or measurement weakness. |
| Harder phone, form, booking, or estimate path | Conversion / Website | Route to Website Conversion Fix Pack. |
| More content without verified impact | Analytics | Validate before recommending production cadence. |
| Offer or sales-process difference | Offer | Route to `offer-findings.md` when commercial structure is the primary gap. |

## Evidence requirements

Acceptable evidence includes:

- dated search screenshot
- named competitor list
- competitor URL inventory
- page copy comparison
- service-page inventory
- GBP screenshot
- review comparison
- CTA and form test
- mobile test
- project-proof comparison
- content inventory
- client interview
- analytics
- Search Console
- CRM or sales record

Minimum evidence by finding type:

| Finding group | Minimum evidence |
|---|---|
| Competitive set | Named competitors, service match, geography, and observation date. |
| Review position | Review count, rating, recent-review dates, and named comparable profiles. |
| Service coverage | Client and competitor URL inventories matched to equivalent services. |
| Work proof | Comparable gallery, project-page, case-study, or before/after review. |
| Messaging | Equivalent homepage or service-page copy plus visible proof comparison. |
| Search visibility | Search term, date, location context, result type, and limitations. |
| Conversion path | Equivalent phone, CTA, form, booking, and mobile path tests. |
| Content cadence | Dated inventory plus relevance to services, proof, or buyer questions. |
| Professional consistency | Specific hierarchy, photography, proof, or business-detail differences, not a general visual opinion. |

## Business impact language

Use report-safe language that explains relative buyer conditions without declaring unsupported superiority.

| Weak wording | Use instead |
|---|---|
| Competitors are crushing you. | Comparable competitors currently present stronger visible proof in several buyer decision areas. |
| You rank below everyone. | The observed search sample shows stronger competitor visibility for the documented target terms; broader validation would improve certainty. |
| Their website is better. | The competitor site provides a clearer path to services, proof, and inquiry in the areas reviewed. |
| Copy what they are doing. | Use the observed gap to build a distinct, evidence-backed implementation aligned with this business. |
| They get more leads. | Public evidence shows a stronger buyer-facing path, but lead volume is not verified. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Competitors have stronger review systems or review velocity. | Review Generation System | Phase 3 when process and tracking are required. |
| Competitors have stronger GBP completeness, services, proof, or activity. | Google Business Authority Pack | Phase 2. |
| Competitors have stronger service coverage or local relevance. | Local SEO Expansion Pack | Phase 2. |
| Competitors show stronger work proof, case studies, credibility, or risk reduction. | Trust Proof System | Phase 2. |
| Competitors make inquiry or next steps easier. | Website Conversion Fix Pack | Phase 1. |
| Competitive conclusions require measurement validation. | Operator Dashboard Pack | Phase 3. |
| Competitor advantage comes from CRM, follow-up, review workflow, or reactivation. | CRM and Follow-Up System or Review Generation System | Phase 3. |
| Gap concerns offer structure or sales process. | Route through `offer-findings.md` | Do not solve a commercial design problem with copy alone. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Competitor comparison exposes a broken buyer path, missing contact option, misleading claim, invalid comparison set, or immediate correction. |
| Phase 2 — Growth Foundation | Default for service pages, local relevance, GBP, proof, positioning, content depth, and professional consistency. |
| Phase 3 — Automation and Reporting | Use for review systems, CRM follow-up, ongoing competitive monitoring, attribution, or performance validation. |
| Phase 4 — Governed AI Enablement | Only use when AI is proposed for monitoring, summarization, content assistance, or comparison and has approved sources, review gates, logging, and escalation. |

## Report-use rules

A competitive finding can enter a client report only when:

1. Named competitors and comparison scope are documented.
2. Evidence is dated and comparable.
3. The difference is material to buyer discovery, trust, action, or strategic priority.
4. Primary implementation domain is identified.
5. Confidence reflects search variability and public-data limitations.
6. Business impact does not claim unknown internal competitor performance.
7. Package and roadmap phase are assigned.
8. DecisionLedger entry can be completed.

Do not use competitive findings to shame the client, imitate a competitor, or inflate urgency.

## DecisionLedger requirements

Each competitive recommendation must include:

```text
finding_id:
comparison_date:
comparison_scope:
competitors_reviewed:
observation:
evidence:
comparability_notes:
interpretation:
primary_domain:
dependent_domains:
business_impact:
confidence:
priority:
recommended_package:
roadmap_phase:
validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-COMP-006
comparison_date: 2026-07-10
comparison_scope: Residential exterior painting in Rochester, Minnesota
competitors_reviewed:
  - Comparable Competitor A
  - Comparable Competitor B
observation: Both reviewed competitors provide dedicated pages for exterior painting, while the client presents the service only within a general painting page.
evidence: Client and competitor URL inventories and service-page screenshots.
comparability_notes: All businesses serve the same local market and residential buyer category.
interpretation: Competitors provide more direct service relevance for buyers and search systems evaluating exterior painting.
primary_domain: SEO
dependent_domains:
  - Website
  - Messaging
business_impact: High-intent buyers may receive clearer service-specific information from competitors.
confidence: High
priority: High
recommended_package: Local SEO Expansion Pack
roadmap_phase: Phase 2 — Growth Foundation
validation_needed: Confirm exterior painting remains a priority service.
report_section: Competitive Position
status: report_ready
```

## Usage instructions

1. Define the service, geography, buyer type, and comparison date.
2. Select named comparable competitors.
3. Collect equivalent evidence across the same domains.
4. Record limitations, search context, and unavailable data.
5. Identify material gaps rather than total activity volume.
6. Assign the primary domain responsible for implementation.
7. Select the matching existing package and roadmap phase.
8. Assign confidence based on comparability, evidence quality, and recency.
9. Write the finding using executive-safe language.
10. Complete the DecisionLedger record.
11. Mark weak evidence `validation_required` rather than forcing a conclusion.

## Completion check

Before final report use, confirm:

- Competitive set is named and comparable.
- Evidence is dated.
- Search limitations are disclosed.
- No internal competitor performance is inferred.
- Finding is material to the buyer journey or strategic priority.
- Primary domain and dependencies are identified.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.
