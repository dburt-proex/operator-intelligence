# Conversion Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable conversion findings for Operator Intelligence assessments.

Conversion findings identify where interested buyers may fail to become qualified inquiries because the website, phone path, form path, estimate request flow, or follow-up expectation is unclear, weak, broken, or untracked.

This library converts observable conversion weaknesses into governed findings that can be scored, routed, reported, and implemented without relying on subjective opinion.

## v1.0 connection

Operator Intelligence v1.0 requires findings that are repeatable, evidence-backed, confidence-rated, and directly connected to implementation packages. This file strengthens v1.0 readiness by giving evaluators a controlled conversion finding set that supports:

- scoring consistency
- evidence quality
- recommendation routing
- executive report generation
- implementation package selection
- roadmap sequencing
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Conversion category score is weak, partial, unknown, or inconsistent.
- Buyer action path is unclear on homepage, service pages, contact page, or Google Business Profile-linked landing pages.
- Phone, form, booking, or estimate request flows are difficult to find or complete.
- CTA language does not match buyer intent.
- Inquiry handling, confirmation, or follow-up expectations are not visible.
- CRM capture, lead tracking, or conversion reporting is missing or unverified.

## Outputs and deliverables

A valid use of this file should produce:

- one or more conversion findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- DecisionLedger entry
- report-safe language for client-facing output

## Governance rules

1. Do not create a conversion finding from opinion alone.
2. Do not assume revenue loss without evidence. Use revenue leakage risk language unless validated by analytics, CRM records, or client confirmation.
3. Unknown data must be marked `unknown` or `validation_required`, not scored as failure by default.
4. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
5. Cosmetic preference is not enough to trigger a conversion recommendation.
6. Broken paths, missing action paths, and untracked lead capture outrank design polish.
7. Client-facing language must describe the buyer journey and business impact without blame.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has direct evidence or documented validation gap. | Finding is based only on evaluator preference. | Mark `validation_required` or remove. |
| Buyer Path Gate | Finding affects a buyer's ability to call, submit, book, request, or understand next steps. | Issue is cosmetic and does not affect action. | Do not route as conversion finding. |
| Confidence Gate | Confidence level is assigned using evidence quality. | Certainty is overstated. | Downgrade confidence or request validation. |
| Impact Gate | Business impact is tied to inquiry quality, completion, response speed, trust, or tracking. | Impact is vague. | Rewrite impact. |
| Package Gate | Recommended package is matched to actual weakness. | Package is selected because it is sellable. | Block recommendation. |
| Roadmap Gate | Phase is assigned based on urgency and dependency. | Client cannot see sequence. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct observable evidence confirms the issue, such as screenshots, form test, mobile test, or URL review. |
| Medium | Evidence suggests a pattern, but additional validation would strengthen certainty. |
| Low | Finding depends on client confirmation, analytics, CRM data, or operational context not yet available. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-CONV-001 | Primary CTA is unclear or passive | OI-CONV-001, OI-CONV-002, OI-WEB-005 | Homepage screenshot, service-page screenshot, CTA copy review, mobile review | Interested buyers may not receive a clear next step, reducing inquiry momentum. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-CONV-002 | CTA language does not match buyer intent | OI-CONV-001, OI-CONV-002, OI-MSG related signals | CTA inventory, page intent review, service-page review | Buyers may hesitate when the action does not match the service or urgency they came for. | Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium |
| OI-FIND-CONV-003 | Estimate request path is hard to find | OI-CONV-003, OI-CONV-006, OI-WEB-006 | Homepage review, service-page review, navigation review, mobile test | Qualified buyers may abandon before requesting an estimate. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-CONV-004 | Phone path is visible but not mobile-optimized | OI-CONV-004, OI-CONV-005 | Mobile screenshot, tap-to-call test, header/footer review | Mobile visitors may be less likely to call at the moment of intent. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-CONV-005 | Contact form is generic or low-context | OI-CONV-006, OI-CONV-007, OI-CONV-008 | Form screenshot, field inventory, service-selection review | The business may receive lower-quality inquiries and require more manual clarification. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-CONV-006 | Form creates unnecessary friction | OI-CONV-006, OI-CONV-007 | Form test, mobile form test, field count, error state review | Buyers may abandon before submitting because the request flow feels too difficult or unclear. | Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium to High |
| OI-FIND-CONV-007 | No clear response expectation after inquiry | OI-CONV-008, OI-CONV-009, OI-CONV-010 | Confirmation page screenshot, form submission test, contact page review | Buyers may continue shopping competitors because the follow-up timeline is unclear. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-CONV-008 | Project details are not captured before estimate request | OI-CONV-007, OI-CONV-008, OI-AUTO-001 | Form field inventory, intake process review, client interview | Staff may spend more time qualifying leads, slowing estimate workflow and reducing responsiveness. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Medium |
| OI-FIND-CONV-009 | Inquiry capture is manual or untracked | OI-CONV-010, OI-AUTO-001, OI-AUTO-002, OI-AN-001 | CRM review, spreadsheet review, client interview, form destination validation | Leads may be missed, duplicated, delayed, or handled inconsistently. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Low to Medium unless system access is provided |
| OI-FIND-CONV-010 | Follow-up process is not defined | OI-CONV-009, OI-CONV-010, OI-AUTO-004, OI-AUTO-005 | Client interview, CRM record, email/SMS template review, process review | Interested buyers may not receive timely follow-up after initial contact. | CRM and Follow-Up System | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-CONV-011 | Service pages lack action points at decision moments | OI-CONV-001, OI-CONV-002, OI-SEO-003, OI-WEB-006 | Service-page screenshot, CTA placement review, scroll-depth review if available | High-intent visitors may read service information without being guided toward an estimate request. | Website Conversion Fix Pack | Phase 1 — Quick Wins | High when observable |
| OI-FIND-CONV-012 | Trust proof is missing near conversion areas | OI-CONV-002, OI-TRUST-001, OI-TRUST-003, OI-WEB-006 | CTA area screenshot, review proof review, project proof review | Buyers may lack enough confidence to take action at the point of decision. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-CONV-013 | Conversion tracking is missing or unverified | OI-CONV-010, OI-AN-001, OI-AN-002, OI-AN-004 | Analytics review, tag review, Search Console, form tracking review, CRM source fields | The business may not know which channels or pages generate qualified inquiries. | Operator Dashboard Pack | Phase 3 — Automation and Reporting | Low to Medium unless analytics access is provided |
| OI-FIND-CONV-014 | Multiple action paths compete without hierarchy | OI-CONV-001, OI-WEB-005, OI-MSG related signals | Homepage screenshot, navigation review, CTA inventory | Buyers may be unsure whether to call, book, submit, request, or browse, weakening action clarity. | Website Conversion Fix Pack | Phase 1 — Quick Wins | Medium |
| OI-FIND-CONV-015 | After-hours inquiry path is unclear | OI-CONV-004, OI-CONV-009, OI-AUTO-004 | Contact page review, phone path review, GBP hours review, client interview | Buyers searching outside business hours may not know whether they can request service or expect follow-up. | Website Conversion Fix Pack or CRM and Follow-Up System | Phase 1 if copy-only, Phase 3 if workflow needed | Medium |

## Criteria mapping rules

Use conversion findings as the primary finding type when the weakness affects buyer action, inquiry capture, or follow-up clarity.

Use cross-domain routing when evidence shows dependency on another domain:

| Conversion issue | Cross-domain dependency | Routing rule |
|---|---|---|
| CTA is unclear because page positioning is weak | Messaging | Pair with messaging finding when value proposition is also unclear. |
| Service page lacks CTA and lacks local page structure | SEO | Pair with SEO finding when page architecture also limits local visibility. |
| CTA exists but lacks proof nearby | Trust | Pair with trust finding when proof is the primary hesitation reducer. |
| Form submits but no owner can confirm lead capture | Automation | Pair with automation finding when lead handling is operationally untracked. |
| Website receives leads but source quality is unknown | Analytics | Pair with analytics finding when measurement is missing. |
| GBP drives calls but website path is weak | Google Business Profile | Pair with GBP finding when profile-to-site journey is part of the issue. |

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
| CTA clarity | Screenshot plus CTA copy review. |
| Mobile phone path | Mobile screenshot plus tap-to-call test. |
| Form path | Form screenshot plus form test when safe. |
| Confirmation expectation | Confirmation screenshot or documented absence after test. |
| Lead tracking | CRM record, destination validation, or client interview. |
| Follow-up process | CRM workflow, email/SMS template, SOP, or client interview. |
| Conversion tracking | Analytics/tag review, dashboard review, or marked `validation_required`. |

If the evaluator cannot safely test a form, use screenshot evidence and mark form function as `validation_required`.

## Business impact language

Use report-safe language that frames the issue as buyer journey friction.

| Weak wording | Use instead |
|---|---|
| Your site does not convert. | The buyer journey does not yet provide a strong path from interest to estimate request. |
| Your form is bad. | The inquiry form captures baseline contact information, but it may not collect enough project context to support fast qualification. |
| You are losing leads. | This creates revenue leakage risk because interested buyers may not receive a clear next step or timely follow-up. |
| Nobody knows what to click. | The primary action could be made more visible and specific so buyers understand what to do next. |
| You need automation. | Lead handling appears to rely on manual follow-up, which may reduce consistency as inquiry volume increases. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| CTA, phone, form, or page action issue is visible and fixable without systems work. | Website Conversion Fix Pack | Default Phase 1. |
| Buyer hesitation is caused by weak proof near action areas. | Trust Proof System | Phase 2 unless CTA is also broken. |
| Service-page action weakness is tied to missing service-page architecture. | Local SEO Expansion Pack plus Website Conversion Fix Pack | Sequence CTA fixes first when path is broken. |
| Lead capture exists but no tracking or ownership is confirmed. | CRM and Follow-Up System | Phase 3. Requires client validation. |
| Inquiry sources, form submissions, or calls are not measurable. | Operator Dashboard Pack | Phase 3. Requires analytics or CRM access. |
| Review/testimonial capture is part of conversion trust but not systematized. | Review Generation System | Phase 3 if process is missing. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Buyer cannot easily act, call, submit, or understand next step. |
| Phase 2 — Growth Foundation | Conversion weakness depends on stronger proof, service-page structure, or positioning. |
| Phase 3 — Automation and Reporting | Conversion weakness depends on CRM, follow-up, tracking, dashboards, or internal workflow. |
| Phase 4 — Governed AI Enablement | Only use when AI is being proposed for intake, routing, response drafting, or lead qualification and requires review gates. |

## Report-use rules

A conversion finding can enter a client report only when:

1. The finding is tied to a buyer action path.
2. Evidence is listed or the gap is marked `validation_required`.
3. Confidence is assigned.
4. Impact is stated in business language.
5. Recommended package is justified by the evidence.
6. Roadmap phase is assigned.
7. DecisionLedger entry can be completed.

Do not include low-confidence internal workflow findings in the executive summary unless they affect a visible buyer path or have client confirmation.

## DecisionLedger requirements

Each conversion recommendation must include this ledger record:

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
finding_id: OI-FIND-CONV-007
observation: The form submission path does not state when the buyer should expect a response.
evidence: Contact form test and confirmation screen review.
interpretation: The buyer can submit an inquiry, but the next-step expectation is unclear after submission.
business_impact: This creates revenue leakage risk because interested buyers may continue contacting competitors while waiting.
confidence: High
priority: High
recommended_package: Website Conversion Fix Pack
roadmap_phase: Phase 1 — Quick Wins
owner_validation_needed: No
report_section: Conversion Findings
status: report_ready
```

## Usage instructions

1. Review the conversion score and relevant criteria IDs.
2. Collect evidence before selecting a finding.
3. Match the observed issue to the closest finding ID.
4. Assign confidence based on evidence quality.
5. Route to package and roadmap phase.
6. Write the finding using client-safe language.
7. Add the ledger record.
8. If evidence is missing, mark `validation_required` instead of forcing a recommendation.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Finding affects buyer action or inquiry handling.
- Confidence is not overstated.
- Business impact is clear.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.

