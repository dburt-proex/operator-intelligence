# SEO Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable local SEO findings for Operator Intelligence assessments.

SEO findings identify where contractor and local-service businesses may be harder to discover for high-intent local searches because service coverage, local relevance, page structure, content depth, technical basics, or authority signals are weak, missing, inconsistent, or unverified.

This library converts observable local search weaknesses into governed findings that can be scored, routed, reported, and implemented without relying on generic SEO advice.

## v1.0 connection

Operator Intelligence v1.0 requires local search findings that are specific enough to support repeatable assessment, clear enough for executive reports, and grounded enough to justify implementation packages.

This file strengthens v1.0 readiness by giving evaluators a controlled SEO finding set that supports:

- service-page architecture decisions
- local visibility diagnosis
- competitor comparison
- evidence-backed SEO recommendations
- Local SEO Expansion Pack routing
- roadmap sequencing
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- SEO category score is weak, partial, unknown, or inconsistent.
- Core services do not have dedicated pages.
- High-value services are buried on broad pages.
- Local targeting is vague, inconsistent, or missing.
- Page titles, headings, URLs, or internal links are generic.
- Buyer questions, process details, pricing factors, FAQs, or project proof are thin or absent.
- Competitors have stronger service-page coverage or local proof.
- Indexability, mobile usability, sitemap, SSL, or broken-page status is unverified.

## Outputs and deliverables

A valid use of this file should produce:

- one or more SEO findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- DecisionLedger entry
- report-safe language for client-facing output

## Governance rules

1. Do not create an SEO finding from keyword preference alone.
2. Do not promise rankings, traffic, lead volume, or revenue impact without validated data.
3. Use visibility risk, discoverability risk, and competitive disadvantage language unless Search Console, analytics, ranking, or CRM evidence supports stronger claims.
4. Unknown data must be marked `unknown` or `validation_required`, not scored as failure by default.
5. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
6. Service-page and local-intent gaps outrank blog/content suggestions for contractor and local-service businesses.
7. Client-facing language must explain discoverability and buyer intent without blame.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has URL, screenshot, page inventory, competitor comparison, Search Console, analytics, or documented validation gap. | Finding is based only on evaluator opinion. | Mark `validation_required` or remove. |
| Search Intent Gate | Finding connects to a service, location, buyer question, or discovery path. | Finding is abstract SEO theory. | Do not route as SEO finding. |
| Local Relevance Gate | Local market, service area, or nearby community relevance is evaluated when applicable. | Local context is ignored. | Add local relevance review. |
| Confidence Gate | Confidence level is assigned using evidence quality. | Certainty is overstated. | Downgrade confidence or request validation. |
| Impact Gate | Business impact is tied to discoverability, qualified traffic, competitor pressure, or buyer education. | Impact is vague. | Rewrite impact. |
| Package Gate | Recommended package is matched to actual weakness. | Package is selected because it is sellable. | Block recommendation. |
| Roadmap Gate | Phase is assigned based on dependency and implementation sequence. | Client cannot see sequence. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct observable evidence confirms the issue, such as URL inventory, page review, metadata review, crawl evidence, screenshots, or competitor comparison. |
| Medium | Evidence suggests a pattern, but additional validation would strengthen certainty. |
| Low | Finding depends on Search Console, analytics, ranking tools, CRM attribution, or client confirmation not yet available. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-SEO-001 | Core service pages are missing | OI-SEO-001, OI-SEO-002, OI-WEB related signals | URL inventory, navigation review, sitemap review, service list comparison | High-intent buyers may not find a dedicated page matching the service they searched for. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-SEO-002 | High-value services are buried on broad pages | OI-SEO-001, OI-SEO-002, OI-MSG related signals | Service-page review, page copy review, competitor comparison | Priority services may receive weaker visibility and weaker buyer relevance than dedicated service pages would provide. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-SEO-003 | Local targeting is broad or inconsistent | OI-SEO-003, OI-SEO-004, OI-GBP related signals | Page copy review, location references, service-area review, GBP comparison | The site may not strongly reinforce relevance for the actual markets the business serves. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-SEO-004 | Nearby communities are not represented where justified | OI-SEO-003, OI-SEO-004 | Service-area review, customer geography if available, competitor comparison | Search visibility may be limited in valuable nearby markets. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-005 | Page titles are generic or duplicated | OI-SEO-005, OI-SEO-006 | Metadata review, screenshot or crawl export, page inventory | Search engines and buyers may receive weaker service and location signals. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when reviewed |
| OI-FIND-SEO-006 | H1/H2 structure does not reinforce service intent | OI-SEO-005, OI-SEO-006 | Page structure review, screenshot, HTML/crawl review when available | Pages may communicate less clearly what service and location the page is meant to rank for. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-SEO-007 | URL structure is unclear or not service-specific | OI-SEO-005, OI-SEO-006 | URL inventory, service-page review | Weak URL structure may reduce page clarity for users, evaluators, and search engines. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-008 | Internal linking does not support priority services | OI-SEO-007, OI-WEB related signals | Navigation review, internal link review, service-page review | Priority service pages may receive weaker discovery support across the site. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-009 | Content depth is thin for buyer-intent pages | OI-SEO-008, OI-SEO-009, OI-MSG related signals | Page copy review, competitor comparison, buyer-question review | Buyers may not receive enough context to understand fit, process, pricing factors, or next steps. | Local SEO Expansion Pack plus Website Conversion Fix Pack if CTA is weak | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-SEO-010 | Buyer questions and FAQs are missing | OI-SEO-008, OI-SEO-009 | Page review, FAQ inventory, competitor comparison, client interview | The site may miss opportunities to answer high-intent search questions and reduce buyer hesitation. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-SEO-011 | Local project proof is missing from service pages | OI-SEO-004, OI-SEO-009, OI-TRUST related signals | Project gallery review, service-page proof review, local testimonial review | Pages may not provide enough local proof to support both search relevance and buyer trust. | Trust Proof System plus Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-SEO-012 | Blog/content exists but does not target buyer-intent terms | OI-SEO-008, OI-SEO-009 | Content inventory, blog review, keyword-to-page review | Content may consume effort without supporting high-intent service discovery. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-013 | Technical SEO basics are unverified | OI-SEO-010, OI-SEO-011, OI-SEO-012 | Indexability check, sitemap review, SSL check, mobile test, broken-page review | Visibility may be constrained by technical issues, but the level of risk requires validation. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Low to Medium unless tested |
| OI-FIND-SEO-014 | Competitors have stronger service-page coverage | OI-SEO-001, OI-SEO-002, OI-COMP related signals | Competitor comparison, service-page inventory, SERP review if available | The business may face competitive pressure because competing sites better match high-intent service searches. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-SEO-015 | Authority signals are weak or not visible | OI-SEO-013, OI-TRUST related signals | Review comparison, citation audit, backlink/association review, local proof review | Buyers and search engines may see fewer trust and authority indicators than competitors provide. | Google Business Authority Pack or Trust Proof System | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-016 | GBP-to-website alignment is weak | OI-SEO-003, OI-GBP related signals | GBP screenshot, service list review, website service-page comparison | Profile visitors may not find aligned service pages that reinforce the service they selected or searched for. | Google Business Authority Pack plus Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-SEO-017 | Seasonal or urgent-service demand is not addressed | OI-SEO-001, OI-SEO-002, OI-SEO-008 | Service inventory, seasonal service review, client interview, competitor comparison | The business may miss high-intent demand during seasonal or urgent service windows. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | Medium |
| OI-FIND-SEO-018 | Metadata does not support service and location relevance | OI-SEO-005, OI-SEO-006 | Title tag review, meta description review, page inventory | Search snippets may communicate weaker relevance than the underlying service offering deserves. | Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when reviewed |

## Criteria mapping rules

Use SEO findings as the primary finding type when the weakness affects discoverability, search relevance, page architecture, local intent coverage, or competitive search position.

Use cross-domain routing when evidence shows dependency on another domain:

| SEO issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Service page exists but CTA is weak | Conversion | Pair with conversion finding when the page receives or could receive high-intent traffic but does not guide action. |
| Service page exists but message is vague | Messaging | Pair with messaging finding when the offer, audience, service fit, or value proposition is unclear. |
| Local proof is missing from service pages | Trust | Pair with trust finding when proof is the main weakness. |
| GBP service list does not match website pages | Google Business Profile | Pair with GBP finding when profile-to-website alignment is weak. |
| Search visibility is unknown due to missing data | Analytics | Pair with analytics finding when Search Console or reporting is missing. |
| Competitors have broader service architecture | Competitive | Pair with competitive finding when competitor comparison is central to priority. |

## Evidence requirements

Acceptable evidence includes:

- screenshot
- URL inventory
- page copy review
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
- citation audit

Minimum evidence by finding type:

| Finding group | Minimum evidence |
|---|---|
| Service-page gaps | URL inventory plus service list comparison. |
| Local relevance | Page copy review plus service-area review. |
| Metadata and headings | Title/H1/H2 review or crawl export. |
| Content depth | Page copy review plus buyer-question review. |
| Technical basics | Indexability, sitemap, SSL, mobile, or broken-page validation. |
| Competitor pressure | Competitor comparison with named competitors or documented SERP review. |
| GBP alignment | GBP screenshot plus website service-page comparison. |
| Authority signals | Review comparison, citation audit, association review, or local proof review. |

If Search Console, analytics, ranking data, or CRM attribution is missing, mark performance conclusions as `validation_required`.

## Business impact language

Use report-safe language that frames the issue as discoverability and buyer-intent alignment.

| Weak wording | Use instead |
|---|---|
| Your SEO is bad. | The site has limited service-page coverage, which may reduce visibility for high-intent local searches. |
| You do not rank. | Current evidence suggests the site may not be strongly aligned to the service and location searches buyers use. |
| Your pages are thin. | The service pages provide baseline information, but they do not yet answer enough buyer questions to fully support search relevance and decision confidence. |
| Your competitors are beating you. | Competitors appear to provide stronger service-specific coverage, which may create local search pressure. |
| You need blogs. | The stronger first move is to improve high-intent service and location coverage before expanding lower-intent content. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Service pages are missing, thin, or overly broad. | Local SEO Expansion Pack | Default Phase 2. |
| Local relevance is weak or inconsistent. | Local SEO Expansion Pack | Include service-area and local proof improvements. |
| GBP service alignment is weak. | Google Business Authority Pack plus Local SEO Expansion Pack | Coordinate GBP services with website pages. |
| Proof weakness limits local relevance and buyer trust. | Trust Proof System plus Local SEO Expansion Pack | Use when project proof and reviews are missing from service pages. |
| Service page has traffic potential but weak CTA. | Website Conversion Fix Pack plus Local SEO Expansion Pack | Fix conversion path before scaling traffic. |
| Search performance cannot be validated. | Operator Dashboard Pack or analytics validation | Phase 3 if measurement setup is required. |
| Competitor service coverage is stronger. | Local SEO Expansion Pack | Prioritize high-value services first. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Only use when an SEO issue is tightly coupled to a broken conversion path, such as missing CTA on an existing high-intent page. |
| Phase 2 — Growth Foundation | Default for service-page architecture, local relevance, metadata, content depth, internal links, GBP alignment, and competitor search pressure. |
| Phase 3 — Automation and Reporting | Use when Search Console, analytics, source tracking, or CRM attribution must be installed before stronger conclusions can be made. |
| Phase 4 — Governed AI Enablement | Only use when AI is proposed for content production, SEO monitoring, page generation, or review response and requires review gates. |

## Report-use rules

An SEO finding can enter a client report only when:

1. The finding is tied to local buyer discoverability or search-intent alignment.
2. Evidence is listed or the gap is marked `validation_required`.
3. Confidence is assigned.
4. Impact is stated in business language.
5. Recommended package is justified by the evidence.
6. Roadmap phase is assigned.
7. DecisionLedger entry can be completed.

Do not include ranking, traffic, or revenue claims unless supported by Search Console, analytics, rank tracking, CRM attribution, or client-provided records.

## DecisionLedger requirements

Each SEO recommendation must include this ledger record:

```text
finding_id:
observation:
evidence:
interpretation:
business_impact:
confidence:
priority:
recommended_package:
roadmap_phase:
owner_validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-SEO-001
observation: The site lists multiple services on one broad services page, but dedicated pages for high-value services are not present.
evidence: URL inventory, navigation review, and service list comparison.
interpretation: The current structure provides general information, but it does not create strong dedicated relevance for each priority service.
business_impact: The business may be less discoverable for high-intent local searches tied to specific services.
confidence: High
priority: High
recommended_package: Local SEO Expansion Pack
roadmap_phase: Phase 2 — Growth Foundation
owner_validation_needed: No
report_section: Local SEO Findings
status: report_ready
```

## Usage instructions

1. Review the SEO score and relevant criteria IDs.
2. Build a URL inventory before selecting a finding.
3. Compare services offered against pages available.
4. Check local relevance, metadata, headings, internal links, content depth, and proof.
5. Compare against key local competitors when competitor evidence is available.
6. Assign confidence based on evidence quality.
7. Route to package and roadmap phase.
8. Write the finding using client-safe language.
9. Add the ledger record.
10. If evidence is missing, mark `validation_required` instead of forcing a recommendation.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Finding affects local discoverability, search relevance, or competitor pressure.
- Confidence is not overstated.
- Business impact is clear.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.
