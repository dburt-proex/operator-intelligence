# Offer and Sales System Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable offer and sales-system findings for Operator Intelligence assessments.

Offer findings identify where a contractor or local-service business may create buyer confusion, qualification friction, weak follow-up, avoidable sales leakage, or delivery mismatch because its entry offer, service packaging, pricing factors, sales process, estimate follow-up, lost-reason capture, referral path, retention path, or capacity alignment is unclear, inconsistent, unverified, or unsupported.

This library converts observable commercial-system weaknesses into governed findings that can be scored, routed, reported, and implemented without inventing pricing, guarantees, margins, demand, or revenue claims.

## v1.0 connection

Operator Intelligence v1.0 requires an offer and sales-system layer that connects buyer-facing promises to delivery reality, sales process discipline, implementation packages, roadmap sequencing, and DecisionLedger traceability.

This file strengthens v1.0 readiness by supporting:

- entry-offer clarity
- service packaging evaluation
- pricing-factor communication
- sales-process visibility
- estimate follow-up governance
- lost-reason and referral-system diagnosis
- retention and reactivation routing
- capacity and delivery-fit validation
- report-ready commercial recommendations

## Inputs and triggers

Use this finding library when any of the following are present:

- Offer and sales-system score is weak, partial, unknown, or inconsistent.
- Buyers cannot tell whether the next step is an estimate, inspection, consultation, service call, or booking.
- High-value services are not packaged or positioned clearly.
- Pricing factors are hidden, vague, misleading, or unsupported.
- The sales process is undocumented or differs between staff.
- Open estimates are not followed up consistently.
- Lost reasons are not captured or reviewed.
- Referral requests depend on memory.
- Past customers are not segmented for maintenance, seasonal, repeat, or reactivation outreach.
- Marketing emphasis does not match capacity, service area, margin, scheduling reality, or delivery capability.

## Outputs and deliverables

A valid use of this file should produce:

- one or more offer or sales-system findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- cross-domain dependencies
- validation requirements
- DecisionLedger entry
- executive-safe report language

## Governance rules

1. Do not create an offer finding from copy preference alone.
2. Distinguish offer structure from message expression. Route weak wording to `messaging-findings.md` when the commercial structure is otherwise sound.
3. Do not invent prices, discounts, guarantees, financing terms, response commitments, margins, capacity, or service availability.
4. High-value, profitable, or strategic service claims require client confirmation, financial records, capacity evidence, or a documented business priority.
5. Do not recommend broader demand generation before offer scope, qualification, follow-up, and delivery readiness are sufficient.
6. Manual sales processes are not automatically weak if they are documented, consistently executed, auditable, and commercially effective.
7. Unknown pricing, margin, close-rate, loss-reason, capacity, or retention data must be marked `unknown` or `validation_required`.
8. Referral and review requests must be separated. A review request is reputation activity; a referral request is new-demand activity.
9. Follow-up recommendations must define owner, timing, status, stop condition, escalation, and recordkeeping.
10. Recommendations must route to an existing implementation package that resolves the observed weakness. Do not create a generic sales package in this file.
11. A recommendation is valid only when observation, evidence, interpretation, business impact, confidence, priority, package, roadmap phase, and ledger record are present.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has website copy, CTA review, proposal, estimate workflow, CRM record, sales notes, client interview, analytics, or documented validation gap. | Finding relies on assumption or generic sales advice. | Mark `validation_required` or remove. |
| Offer Definition Gate | Entry action, buyer outcome, scope, qualification, and next step are defined. | “Offer” is only a slogan or vague CTA. | Clarify structure before promotion. |
| Delivery Fit Gate | Promise can be fulfilled with current service scope, capacity, geography, process, and policies. | Marketing promise exceeds operating reality. | Halt or narrow recommendation. |
| Pricing Accuracy Gate | Pricing language reflects verified policy and appropriate qualification. | Recommendation invents pricing or implies certainty where variables exist. | Block publication. |
| Qualification Gate | Intake captures enough information to route the buyer appropriately. | Offer invites demand the business cannot classify or serve. | Add qualification dependency. |
| Sales Process Gate | Ownership, stages, timing, handoffs, and outcomes are defined. | Follow-up depends on memory or undocumented behavior. | Route to CRM and Follow-Up System. |
| Capacity Gate | Priority-service emphasis is supported by capacity and strategic evidence. | Demand is directed toward constrained or non-priority work. | Request owner validation. |
| Measurement Gate | Outcome tracking exists or limitation is stated. | Recommendation claims effectiveness without measurement. | Route to Operator Dashboard Pack or lower confidence. |
| Confidence Gate | Confidence reflects public and internal evidence quality. | Internal commercial assumptions are presented as fact. | Downgrade confidence. |
| Package Gate | Existing package resolves the demonstrated weakness. | Package is selected because it is sellable. | Re-route or block. |
| Roadmap Gate | Phase reflects dependency, urgency, and readiness. | Promotion precedes offer or process readiness. | Re-sequence. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct buyer-facing evidence, documented process, CRM records, proposals, or verified workflows confirm the condition. |
| Medium | Public evidence and client interviews support the pattern, but pricing, margin, capacity, or outcome data remains incomplete. |
| Low | Finding depends on owner recollection, undocumented sales behavior, unavailable financials, unclear capacity, or unverified strategic priorities. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-OFFER-001 | Primary entry offer is unclear | OI-OFFER-001, OI-MSG-005 | Homepage, CTA inventory, service pages, contact page | Buyers may not know whether to request an estimate, inspection, consultation, service call, or booking. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-OFFER-002 | Entry offer varies across channels | OI-OFFER-001, OI-MSG related signals | Website, GBP, social profiles, sales materials, phone script | Buyers may receive inconsistent expectations about the next step. | Website Conversion Fix Pack plus Google Business Authority Pack when GBP is affected | Phase 1 — Quick Wins | High when observable |
| OI-FIND-OFFER-003 | Entry offer does not define buyer outcome or next step | OI-OFFER-001, OI-MSG-005, OI-CONV-002 | CTA copy, form confirmation, process copy | Inquiry may feel vague because the buyer cannot see what they receive after acting. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-OFFER-004 | Offer qualification requirements are unclear | OI-OFFER-001, OI-CONV-004, OI-CONV-009 | Intake form, phone script, service rules, client interview | The business may receive lower-context inquiries or spend time on projects outside its fit. | CRM and Follow-Up System plus Website Conversion Fix Pack | Phase 1 for intake, Phase 3 for workflow | Medium |
| OI-FIND-OFFER-005 | High-value services are not packaged clearly | OI-OFFER-002, OI-MSG-010, OI-SEO-002 | Service pages, proposals, client-confirmed priorities, financial or capacity evidence | Strategic services may receive weak buyer attention and inconsistent sales presentation. | Local SEO Expansion Pack plus Website Conversion Fix Pack | Phase 2 — Growth Foundation | Low to Medium until priority is validated |
| OI-FIND-OFFER-006 | Service packages do not define scope or exclusions | OI-OFFER-002, OI-MSG-004 | Service pages, proposals, estimate templates, client interview | Buyers and staff may form inconsistent expectations about what is included. | Website Conversion Fix Pack plus CRM and Follow-Up System when internal workflow is affected | Phase 2 — Growth Foundation | Medium |
| OI-FIND-OFFER-007 | Offer emphasis conflicts with capacity or delivery readiness | OI-OFFER-002, OI-MSG-010 | Capacity review, scheduling data, service mix, owner interview | Marketing may increase demand for work the business cannot fulfill consistently. | Validation task before Local SEO Expansion Pack or Website Conversion Fix Pack | Phase 1 — Quick Wins for correction | Low until validated |
| OI-FIND-OFFER-008 | Pricing factors are not explained where appropriate | OI-OFFER-003, OI-MSG-007 | Service pages, FAQs, estimate policy, client interview | Buyers may delay inquiry because they cannot understand what influences price. | Local SEO Expansion Pack or Website Conversion Fix Pack based on placement | Phase 2 — Growth Foundation | Medium |
| OI-FIND-OFFER-009 | Pricing language creates unsupported certainty | OI-OFFER-003, OI-MSG-009 | Pricing copy, proposal terms, pricing policy | Buyers may receive expectations that cannot be supported across project conditions. | Website Conversion Fix Pack; block publication until validated | Phase 1 — Quick Wins | High when observable |
| OI-FIND-OFFER-010 | Pricing or guarantee terms differ across channels | OI-OFFER-003, OI-TRUST-007 | Website, proposals, GBP, ads, sales scripts | Inconsistent commercial terms may create trust and delivery risk. | Trust Proof System plus Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium to High |
| OI-FIND-OFFER-011 | Sales process is not documented | OI-OFFER-004, OI-AUTO-012 | SOPs, client interview, workflow review | Inquiry handling may vary by person, creating inconsistent buyer experiences and follow-up. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-OFFER-012 | Buyer-facing sales process is unclear | OI-OFFER-004, OI-MSG-006, OI-TRUST-008 | Process section, contact page, form confirmation | Buyers may hesitate because they do not understand the path from inquiry to booked work. | Trust Proof System plus Website Conversion Fix Pack | Phase 1 or Phase 2 based on severity | High when observable |
| OI-FIND-OFFER-013 | Sales stages or handoffs are inconsistent | OI-OFFER-004, OI-AUTO-004, OI-AUTO-005, OI-AUTO-012 | CRM stages, handoff notes, owner interview | Leads and estimates may be delayed, duplicated, or left without clear ownership. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-OFFER-014 | Estimate follow-up depends on memory | OI-OFFER-005, OI-AUTO-006 | CRM tasks, templates, open-estimate review, client interview | Open estimates may not receive consistent follow-up or closure. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-OFFER-015 | Estimate follow-up has no timing or stop rules | OI-OFFER-005, OI-AUTO-006, OI-AUTO-013 | Follow-up sequence, templates, SOP | Follow-up may be inconsistent, excessive, or prematurely abandoned. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-OFFER-016 | Estimate status is not tracked | OI-OFFER-005, OI-AUTO-005, OI-AUTO-007 | CRM, spreadsheet, estimate log | The business may not know which estimates are new, sent, stale, won, or lost. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | High when records are reviewed |
| OI-FIND-OFFER-017 | Lost reasons are not captured | OI-OFFER-006, OI-AUTO-007, OI-AN-006 | CRM fields, lost-estimate review, client interview | The business cannot reliably distinguish pricing, timing, fit, competition, financing, or follow-up issues. | CRM and Follow-Up System plus Operator Dashboard Pack | Phase 3 — Automation and Reporting | High when observable |
| OI-FIND-OFFER-018 | Lost reasons are captured but not reviewed | OI-OFFER-006, OI-AN-009, OI-AN-010 | Dashboard, meeting notes, action log | Sales data may exist without changing offer, qualification, pricing communication, or follow-up decisions. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | High when observable |
| OI-FIND-OFFER-019 | Referral requests are informal or absent | OI-OFFER-007 | Referral script, email/SMS template, completion workflow, client interview | Satisfied customers may not receive a clear and timely invitation to refer similar buyers. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-OFFER-020 | Referral process is not separated from review generation | OI-OFFER-007, OI-AUTO-008 | Review workflow, referral workflow, templates | The business may request reputation proof without creating a distinct path for introductions. | CRM and Follow-Up System plus Review Generation System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-OFFER-021 | Retention or reactivation path is absent | OI-OFFER-008, OI-AUTO-010, OI-AUTO-011 | CRM records, customer list, campaigns, service history | Past customers may not receive relevant maintenance, seasonal, repeat-service, or reactivation outreach. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-OFFER-022 | Reactivation outreach is not segmented by service history or fit | OI-OFFER-008, OI-AUTO-010 | Customer records, service history, campaign rules | Generic outreach may be less relevant and harder to govern. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-OFFER-023 | Offer performance cannot be measured | OI-OFFER-001 through OI-OFFER-008, OI-AN related signals | CRM, analytics, source data, estimates, outcomes | Offer changes cannot be validated against inquiry quality, estimate outcomes, retention, or referral activity. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low until data is available |
| OI-FIND-OFFER-024 | Marketing demand is expanded before sales-system readiness | OI-OFFER-004, OI-OFFER-005, OI-AUTO related signals | Lead flow, response process, follow-up, capacity, owner interview | Additional demand may amplify response delays, qualification gaps, or follow-up inconsistency. | CRM and Follow-Up System before growth packages | Phase 3 prerequisite before Phase 2 expansion | Medium |

## Criteria mapping rules

Use offer findings when the weakness is commercial structure, buyer entry, scope, qualification, sales motion, follow-up, referral, retention, or delivery fit.

| Observed issue | Primary domain | Routing rule |
|---|---|---|
| Offer is structurally sound but poorly worded | Messaging | Use messaging finding and record offer dependency only if needed. |
| Buyer cannot find or act on the offer | Conversion or website | Pair with Website Conversion Fix Pack. |
| High-value service lacks a dedicated page | SEO | Pair with Local SEO Expansion Pack after priority validation. |
| Process or guarantee lacks proof | Trust | Pair with Trust Proof System. |
| Follow-up, stages, handoffs, or customer history are inconsistent | Automation | Route to CRM and Follow-Up System. |
| Offer outcomes cannot be observed | Analytics | Route to Operator Dashboard Pack. |
| Competitor offer appears stronger | Competitive | Use competitive evidence to adjust priority, not to copy the competitor. |

## Evidence requirements

Acceptable evidence includes:

- website and CTA screenshots
- service-page and proposal copy
- estimate templates
- pricing policy
- form and phone-intake review
- CRM or lead tracker
- status and task records
- lost-reason fields
- customer service history
- referral and reactivation templates
- analytics and outcome reports
- client interview
- competitor comparison

Minimum evidence:

| Finding group | Minimum evidence |
|---|---|
| Entry offer | CTA inventory plus landing/contact-page review. |
| Service packaging | Service page or proposal plus owner-validated priority. |
| Pricing factors | Published pricing language plus client-confirmed policy. |
| Sales process | Workflow record, SOP, CRM stages, or client interview. |
| Follow-up | Open-estimate review plus tasks, templates, or owner confirmation. |
| Lost reasons | CRM/report field review. |
| Referral or retention | Workflow, template, CRM history, or marked `validation_required`. |
| Capacity alignment | Owner confirmation plus scheduling, service mix, or capacity evidence when available. |

## Business impact language

| Weak wording | Use instead |
|---|---|
| Your offer is bad. | The buyer-facing entry offer does not yet make the next step and expected outcome sufficiently clear. |
| You are losing sales. | Inconsistent follow-up creates sales leakage risk because open estimates may not receive a governed next action. |
| Your pricing is confusing. | Pricing factors and qualification requirements could be clarified so buyers form more accurate expectations. |
| You need packages. | High-priority services may benefit from clearer scope, fit, and buyer-facing positioning once operational priority is validated. |
| You ignore old customers. | The current system does not yet create a consistent path for relevant repeat, seasonal, maintenance, or reactivation outreach. |

## Recommended package routing

| Condition | Recommended package | Default phase |
|---|---|---|
| Entry offer, CTA, or next step is unclear | Website Conversion Fix Pack | Phase 1 |
| Priority-service packaging or page support is weak | Local SEO Expansion Pack plus Website Conversion Fix Pack | Phase 2 |
| Guarantee, process, or risk reduction lacks proof | Trust Proof System | Phase 2 |
| Sales stages, follow-up, referrals, retention, or reactivation are inconsistent | CRM and Follow-Up System | Phase 3 |
| Lost reasons or offer outcomes are not visible | Operator Dashboard Pack | Phase 3 |
| Demand growth would exceed process readiness | CRM and Follow-Up System before acquisition expansion | Phase 3 prerequisite |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Entry offer, CTA, pricing language, or inconsistent promise creates immediate buyer confusion or risk. |
| Phase 2 — Growth Foundation | Service packaging, priority-page support, differentiation, and proof alignment require foundational work. |
| Phase 3 — Automation and Reporting | Sales stages, follow-up, lost reasons, referrals, retention, reactivation, and measurement require systems. |
| Phase 4 — Governed AI Enablement | AI is proposed for intake, qualification, follow-up drafting, proposal support, or sales assistance after process and review controls exist. |

## Report-use rules

An offer finding can enter a client report only when:

1. The commercial weakness is distinct from writing preference.
2. Evidence is listed or the gap is marked `validation_required`.
3. Pricing, priority, capacity, and performance assumptions are qualified.
4. Confidence is assigned.
5. Business impact is stated without unsupported revenue claims.
6. Package and roadmap phase are justified.
7. DecisionLedger entry is complete.

## DecisionLedger requirements

Each offer recommendation must include:

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
commercial_assumptions:
owner_validation_needed:
capacity_dependency:
measurement_dependency:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-OFFER-014
observation: Open estimates are tracked informally, and no documented follow-up timing or owner rule was provided.
evidence: Client interview and estimate workflow review.
interpretation: Estimate follow-up depends on individual memory rather than a governed sales stage and task sequence.
business_impact: This creates sales leakage risk because open estimates may not receive a consistent next action or closure status.
confidence: Medium
priority: High
recommended_package: CRM and Follow-Up System
roadmap_phase: Phase 3 — Automation and Reporting
commercial_assumptions: No close-rate or revenue impact assumed.
owner_validation_needed: Yes
capacity_dependency: No
measurement_dependency: Estimate status and outcome tracking.
report_section: Offer and Sales System Findings
status: validation_required
```

## Usage instructions

1. Review offer and sales-system criteria.
2. Separate message-expression problems from offer-structure problems.
3. Validate entry action, scope, pricing policy, process, follow-up, referral, retention, and capacity.
4. Capture internal evidence where required.
5. Assign confidence and validation requirements.
6. Route to the existing package that resolves the primary weakness.
7. Sequence prerequisites before demand expansion.
8. Complete the DecisionLedger record.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Offer structure is the primary issue.
- Pricing and capacity assumptions are controlled.
- Business impact avoids unsupported revenue claims.
- Package routing is justified.
- Roadmap sequencing protects delivery readiness.
- Ledger record is complete.
