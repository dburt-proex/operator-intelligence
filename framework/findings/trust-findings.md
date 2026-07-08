# Trust Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable trust findings for Operator Intelligence assessments.

Trust findings identify where contractor and local-service businesses may fail to reduce buyer uncertainty because review proof, work proof, human proof, risk-reduction information, or local legitimacy signals are weak, missing, delayed, inconsistent, or unverified.

This library converts observable trust weaknesses into governed findings that can be scored, routed, reported, and implemented without using blame-based or vague reputation advice.

## v1.0 connection

Operator Intelligence v1.0 requires trust findings that connect buyer confidence, visible proof, local credibility, and risk reduction to specific implementation paths.

This file strengthens v1.0 readiness by giving evaluators a controlled trust finding set that supports:

- consistent trust evaluation
- proof inventory discipline
- review and project-proof diagnosis
- Trust Proof System routing
- Review Generation System routing
- executive-safe report language
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Trust category score is weak, partial, unknown, or inconsistent.
- Reviews exist but are not visible near decision points.
- Review quality, recency, service specificity, or owner response pattern is weak or unverified.
- Project photos, before/after examples, case studies, or job-site proof are missing or thin.
- Owner, team, or local identity is not visible.
- License, insurance, warranty, safety, process, or expectation-setting details are unclear.
- Local legitimacy is weak, such as limited local project examples, service-area proof, or community signals.
- Competitors show stronger review, proof, or credibility signals.

## Outputs and deliverables

A valid use of this file should produce:

- one or more trust findings
- evidence record for each finding
- confidence level for each finding
- business impact statement
- recommended implementation package
- roadmap phase
- DecisionLedger entry
- report-safe language for client-facing output

## Governance rules

1. Do not create a trust finding from taste, aesthetics, or personal preference alone.
2. Do not imply dishonesty, low quality, or poor work without direct evidence.
3. Use buyer confidence, risk reduction, and proof visibility language instead of blame.
4. Unknown reputation, licensing, warranty, or insurance data must be marked `unknown` or `validation_required`.
5. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.
6. Trust findings must distinguish between proof that exists but is underused and proof that is missing or unverified.
7. Review proof, work proof, and risk reduction near conversion areas outrank general brand polish.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has screenshot, page review, review comparison, GBP screenshot, project-proof inventory, competitor comparison, client interview, or documented validation gap. | Finding is based only on evaluator preference. | Mark `validation_required` or remove. |
| Buyer Confidence Gate | Finding affects buyer uncertainty, credibility, perceived risk, or willingness to request an estimate. | Issue is cosmetic only. | Do not route as trust finding. |
| Proof Location Gate | Finding evaluates where proof appears in the buyer journey. | Proof is counted without placement context. | Review placement near CTA and service pages. |
| Confidence Gate | Confidence level is assigned using evidence quality. | Certainty is overstated. | Downgrade confidence or request validation. |
| Impact Gate | Business impact is tied to hesitation, trust, risk, local credibility, or conversion confidence. | Impact is vague. | Rewrite impact. |
| Package Gate | Recommended package is matched to actual weakness. | Package is selected because it is sellable. | Block recommendation. |
| Roadmap Gate | Phase is assigned based on dependency and implementation sequence. | Client cannot see sequence. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct observable evidence confirms the issue, such as screenshots, review inventory, GBP review check, project gallery review, service-page proof review, or competitor comparison. |
| Medium | Evidence suggests a pattern, but additional validation would strengthen certainty. |
| Low | Finding depends on client confirmation, internal customer records, licensing/insurance documents, warranty policy, or unavailable operational context. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-TRUST-001 | Reviews exist but are not integrated into the website | OI-TRUST-001, OI-TRUST-002, OI-CONV related signals | Website screenshot, review inventory, GBP screenshot | Buyers may not see third-party proof at the moment they are deciding whether to inquire. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-TRUST-002 | Review highlights are missing near primary CTA areas | OI-TRUST-001, OI-TRUST-003, OI-CONV-002 | CTA area screenshot, homepage review, service-page review | The site may not provide enough confidence near action points to reduce hesitation. | Trust Proof System plus Website Conversion Fix Pack if CTA is weak | Phase 1 if CTA-adjacent, otherwise Phase 2 | High when observable |
| OI-FIND-TRUST-003 | Review recency or velocity is weak or unverified | OI-TRUST-001, OI-TRUST-002, OI-GBP related signals | GBP screenshot, review date review, competitor comparison | Buyers may perceive weaker current market activity if recent customer feedback is limited. | Review Generation System | Phase 3 — Automation and Reporting | Medium unless review data is complete |
| OI-FIND-TRUST-004 | Reviews lack service-specific detail | OI-TRUST-002, OI-SEO related signals | Review sample review, GBP screenshot, service review comparison | Reviews may provide general reputation proof but not enough confidence for specific service decisions. | Review Generation System plus Trust Proof System | Phase 3 for system, Phase 2 for placement | Medium |
| OI-FIND-TRUST-005 | Owner responses to reviews are missing or inconsistent | OI-TRUST-001, OI-GBP related signals | GBP screenshot, review response review, competitor comparison | The business may miss a visible opportunity to show responsiveness and professionalism. | Google Business Authority Pack or Review Generation System | Phase 2 or Phase 3 based on process need | Medium to High |
| OI-FIND-TRUST-006 | Project gallery is missing or thin | OI-TRUST-003, OI-TRUST-004, OI-WEB related signals | Gallery review, service-page screenshot, project photo inventory | Buyers may not see enough work proof to evaluate quality, fit, or project similarity. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-TRUST-007 | Before-and-after proof is missing where relevant | OI-TRUST-003, OI-TRUST-004 | Project proof inventory, service-page review, competitor comparison | The site may underuse one of the strongest proof types for visual or transformation-based services. | Trust Proof System | Phase 2 — Growth Foundation | High when relevant and observable |
| OI-FIND-TRUST-008 | Service pages lack project proof | OI-TRUST-003, OI-TRUST-004, OI-SEO related signals | Service-page review, project proof placement review | High-intent service pages may not provide enough evidence to support buyer confidence. | Trust Proof System plus Local SEO Expansion Pack if page depth is weak | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-TRUST-009 | Case studies or customer stories are missing for high-value services | OI-TRUST-004, OI-MSG related signals | Service mix review, project proof review, competitor comparison | High-value services may lack the deeper proof needed for larger or more complex purchase decisions. | Trust Proof System | Phase 2 — Growth Foundation | Medium |
| OI-FIND-TRUST-010 | Owner or team identity is not visible | OI-TRUST-005, OI-WEB related signals | About page review, homepage review, team/owner section review | Buyers may have less human confidence in who will perform or manage the work. | Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-TRUST-011 | Local story or community legitimacy is weak | OI-TRUST-005, OI-TRUST-012, OI-SEO related signals | About page review, local proof review, service-area review | The business may not fully communicate local credibility or market familiarity. | Trust Proof System plus Local SEO Expansion Pack if local relevance is also weak | Phase 2 — Growth Foundation | Medium |
| OI-FIND-TRUST-012 | License, insurance, or credential details are unclear | OI-TRUST-006, OI-TRUST-007 | Website review, credential review, client interview if not public | Buyers may not receive enough risk-reduction information before requesting an estimate. | Trust Proof System | Phase 2 — Growth Foundation | Low to Medium unless publicly visible |
| OI-FIND-TRUST-013 | Warranty or guarantee language is missing or unclear | OI-TRUST-006, OI-TRUST-007 | Service-page review, FAQ review, client interview | Buyers may have unanswered risk questions about what happens after the project is complete. | Trust Proof System | Phase 2 — Growth Foundation | Low to Medium unless publicly visible |
| OI-FIND-TRUST-014 | Process expectations are unclear | OI-TRUST-006, OI-TRUST-008, OI-CONV related signals | Process section review, estimate workflow review, FAQ review | Buyers may hesitate because they do not understand what happens from inquiry to completion. | Trust Proof System plus Website Conversion Fix Pack if next step is weak | Phase 2, or Phase 1 if blocking inquiry | Medium to High |
| OI-FIND-TRUST-015 | Safety or job-site professionalism signals are missing where relevant | OI-TRUST-007, OI-TRUST-008 | Service-page review, project photos, client interview, credential review | For higher-risk services, buyers may not see enough evidence that the work is handled professionally and safely. | Trust Proof System | Phase 2 — Growth Foundation | Low to Medium |
| OI-FIND-TRUST-016 | Local project examples are missing | OI-TRUST-012, OI-SEO related signals | Project proof review, service-area review, competitor comparison | Buyers may not see enough evidence that the business has completed similar work in the local market. | Trust Proof System plus Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-TRUST-017 | Competitors show stronger visible trust proof | OI-TRUST-001, OI-TRUST-003, OI-COMP related signals | Competitor comparison, review comparison, project proof comparison | The business may face competitive pressure because buyers can see stronger proof elsewhere. | Trust Proof System | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-TRUST-018 | Trust signals appear too late in the buyer journey | OI-TRUST-001, OI-TRUST-003, OI-CONV related signals | Homepage review, scroll review, CTA placement review, service-page review | Buyers may make an early judgment before encountering meaningful proof. | Trust Proof System plus Website Conversion Fix Pack if CTA areas are affected | Phase 1 if CTA-adjacent, otherwise Phase 2 | High when observable |

## Criteria mapping rules

Use trust findings as the primary finding type when the weakness affects buyer confidence, credibility, proof visibility, risk reduction, or local legitimacy.

Use cross-domain routing when evidence shows dependency on another domain:

| Trust issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Proof is missing near CTA areas | Conversion | Pair with conversion finding when lack of proof may reduce action confidence. |
| Project proof is missing from service pages | SEO | Pair with SEO finding when proof also affects local relevance and content depth. |
| Review system is inconsistent | Automation | Pair with automation finding when review requests are not systematized. |
| GBP reviews are weak or underused | Google Business Profile | Pair with GBP finding when profile reputation is central. |
| Trust proof exists but message is unclear | Messaging | Pair with messaging finding when proof does not support positioning. |
| Competitors show stronger visible proof | Competitive | Pair with competitive finding when competitor comparison drives priority. |
| Review/reporting data is unavailable | Analytics | Pair with analytics finding when reputation or conversion effects cannot be measured. |

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
| Review proof | GBP screenshot, website review placement, or review comparison. |
| Work proof | Project gallery review, service-page screenshot, or project proof inventory. |
| Human proof | About page review, owner/team section screenshot, or client interview. |
| Risk reduction | License/insurance/warranty/process review or marked `validation_required`. |
| Local legitimacy | Service-area review, local project proof, community proof, or competitor comparison. |
| Competitor pressure | Named competitor comparison with specific proof differences. |
| Review process | Review request workflow, CRM record, template, or client interview. |

If licensing, insurance, warranty, safety, or internal review process evidence is unavailable, mark the finding `validation_required` and avoid implying failure.

## Business impact language

Use report-safe language that frames the issue as buyer confidence and risk reduction.

| Weak wording | Use instead |
|---|---|
| You do not look trustworthy. | The business has an opportunity to make trust signals more visible during the buyer journey. |
| Your reviews are bad. | Review proof may not yet communicate enough recency, specificity, or responsiveness to reduce buyer uncertainty. |
| Your gallery is weak. | The site could show more project proof so buyers can evaluate quality, fit, and similar work. |
| Nobody knows who you are. | Owner or team visibility could be improved to create more human confidence before inquiry. |
| You need guarantees. | Risk-reduction details such as process, warranty, insurance, or expectations could be clarified where appropriate. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Reviews, project proof, human proof, process, or local legitimacy are weak or poorly placed. | Trust Proof System | Default Phase 2. |
| Review generation is weak, inconsistent, or not systematized. | Review Generation System | Phase 3 when workflow/process is needed. |
| GBP reputation is incomplete, underused, or weaker than competitors. | Google Business Authority Pack | Pair with review system when process is missing. |
| Trust weakness appears near CTA or estimate request path. | Website Conversion Fix Pack plus Trust Proof System | Phase 1 if blocking action; otherwise Phase 2. |
| Service pages lack proof and content depth. | Local SEO Expansion Pack plus Trust Proof System | Phase 2. |
| Trust performance cannot be measured. | Operator Dashboard Pack or analytics validation | Phase 3 if reporting setup is required. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Trust proof is missing near primary CTA, estimate request, contact path, or high-intent service page action point. |
| Phase 2 — Growth Foundation | Default for proof library, review placement, project gallery, human proof, process, local legitimacy, and risk-reduction copy. |
| Phase 3 — Automation and Reporting | Use when review generation, testimonial capture, proof collection, or reputation tracking needs a system. |
| Phase 4 — Governed AI Enablement | Only use when AI is proposed for review response drafting, testimonial processing, project-story generation, or proof library automation and requires review gates. |

## Report-use rules

A trust finding can enter a client report only when:

1. The finding is tied to buyer confidence, credibility, proof visibility, local legitimacy, or risk reduction.
2. Evidence is listed or the gap is marked `validation_required`.
3. Confidence is assigned.
4. Impact is stated in business language.
5. Recommended package is justified by the evidence.
6. Roadmap phase is assigned.
7. DecisionLedger entry can be completed.

Do not include claims about work quality, honesty, safety, licensing, insurance, or warranty unless verified by direct evidence or client confirmation.

## DecisionLedger requirements

Each trust recommendation must include this ledger record:

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
finding_id: OI-FIND-TRUST-006
observation: The website includes limited visible project proof and does not present a structured gallery of completed work.
evidence: Website gallery review and service-page screenshot review.
interpretation: Buyers can understand the services offered, but they have limited visual proof to evaluate quality, fit, or similar project experience.
business_impact: This may increase buyer hesitation before requesting an estimate, especially for visual or higher-value services.
confidence: High
priority: High
recommended_package: Trust Proof System
roadmap_phase: Phase 2 — Growth Foundation
owner_validation_needed: No
report_section: Trust Findings
status: report_ready
```

## Usage instructions

1. Review the trust score and relevant criteria IDs.
2. Inventory review proof, project proof, human proof, risk-reduction proof, and local legitimacy proof.
3. Check proof placement near CTAs, service pages, and estimate request paths.
4. Compare review and project proof against local competitors when evidence is available.
5. Assign confidence based on evidence quality.
6. Route to package and roadmap phase.
7. Write the finding using client-safe language.
8. Add the ledger record.
9. If evidence is missing, mark `validation_required` instead of forcing a recommendation.

## Completion check

Before final report use, confirm:

- Finding is evidence-backed.
- Finding affects buyer confidence, credibility, risk reduction, or local legitimacy.
- Confidence is not overstated.
- Business impact is clear.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.
