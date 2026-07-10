# Google Business Profile Findings Library

Version: v0.3 finding library foundation  
Stage alignment: Stage 1 — `framework/findings/`  
Folder alignment: `framework/findings/`  
Status: Draft foundation for v1.0 methodology hardening

## Purpose

This file defines repeatable Google Business Profile findings for Operator Intelligence assessments.

Google Business Profile findings identify where a contractor or local-service business may weaken local discovery, buyer trust, service relevance, or inquiry readiness because its profile is missing, duplicated, incomplete, misaligned, inactive, under-documented, or unverified.

This library converts observable profile weaknesses into governed findings that can be scored, routed, reported, and implemented without treating every incomplete field as equally important.

## v1.0 connection

Operator Intelligence v1.0 requires a governed local-profile layer that connects profile evidence to local visibility, reputation strength, website alignment, inquiry routing, implementation packages, and roadmap sequencing.

This file strengthens v1.0 readiness by supporting:

- repeatable Google Business Profile evaluation
- evidence-backed local visibility findings
- review and photo-strength diagnosis
- service and website alignment checks
- Google Business Authority Pack routing
- Review Generation System routing
- cross-domain recommendation control
- DecisionLedger traceability

## Inputs and triggers

Use this finding library when any of the following are present:

- Google Business Profile category score is weak, partial, unknown, or inconsistent.
- The profile is missing, duplicated, suspended, inaccessible, or difficult to verify.
- Primary or secondary categories do not clearly support the core service mix.
- Services, description, service area, hours, phone number, website link, or booking path are incomplete or inconsistent.
- Photos are sparse, outdated, customer-only, or weak as proof of work.
- Review count, recency, velocity, specificity, or owner responses are weak or unverified.
- Q&A, posts, updates, or profile activity are absent or unmanaged.
- Website pages and profile services do not align.
- Competitors present stronger profile completeness, proof, or reputation signals.

## Outputs and deliverables

A valid use of this file should produce:

- one or more Google Business Profile findings
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

1. Do not infer profile ownership, verification status, suspension state, or administrative access without direct evidence or client confirmation.
2. Do not promise rankings, map visibility, call volume, lead volume, or revenue impact from profile changes.
3. Unknown profile fields or inaccessible administrative settings must be marked `unknown` or `validation_required`.
4. A missing or weak field is only reportable when it affects discoverability, relevance, trust, action readiness, consistency, or governance.
5. Review findings must distinguish count, rating, recency, velocity, specificity, and response behavior as separate conditions.
6. Competitor comparisons must use named profiles and comparable local service markets.
7. Do not recommend artificial review generation, review gating, keyword manipulation, inaccurate categories, false locations, or unsupported service claims.
8. Profile work must remain aligned with actual services, service areas, business identity, hours, and customer experience.
9. A recommendation is valid only when observation, evidence, interpretation, impact, confidence, priority, package, and roadmap phase are present.

## Governance gates

| Gate | Pass requirement | Fail condition | Action |
|---|---|---|---|
| Evidence Gate | Finding has profile screenshots, public profile review, administrative evidence, competitor comparison, website comparison, client interview, or documented validation gap. | Finding is based on assumption or memory. | Mark `validation_required` or remove. |
| Profile Control Gate | Ownership, verification, duplicate, suspension, and access conditions are directly validated when relevant. | Public visibility is treated as proof of administrative control. | Request client validation. |
| Accuracy Gate | Business name, phone, hours, service area, categories, services, and links reflect the real business. | Recommendation introduces inaccurate or unsupported information. | Block recommendation. |
| Policy Safety Gate | Recommendation avoids review gating, fake reviews, false locations, category abuse, and misleading claims. | Implementation depends on manipulation. | Halt recommendation. |
| Service Alignment Gate | Categories and services align with actual offerings and website coverage. | Profile claims cannot be supported elsewhere. | Correct scope before expansion. |
| Reputation Gate | Review count, recency, velocity, quality, and responses are evaluated separately. | One review metric is used to represent total reputation strength. | Split the finding. |
| Inquiry Path Gate | Phone, website, booking, messaging, or direction paths are tested when applicable. | Visible links are assumed functional. | Test or mark unknown. |
| Confidence Gate | Confidence reflects evidence quality and access limitations. | Certainty is overstated. | Downgrade confidence. |
| Package Gate | Package selection resolves the demonstrated weakness. | Broad work is recommended without evidence. | Narrow or block recommendation. |
| Roadmap Gate | Phase reflects urgency, dependency, and internal readiness. | Sequence is unclear. | Assign phase before report use. |
| Ledger Gate | Finding can be traced through DecisionLedger fields. | Recommendation cannot be audited. | Block from final report. |

## Confidence standard

| Confidence | Use when |
|---|---|
| High | Direct profile screenshots, public profile review, tested links, administrative access, or documented competitor comparison confirms the condition. |
| Medium | Public evidence confirms much of the condition, but ownership, workflow, or internal context remains unverified. |
| Low | Finding depends on client recollection, inaccessible settings, unavailable review history, or incomplete competitor context. |
| Unknown | Evidence is insufficient. Unknown is not automatically negative. |

## Core findings table

| Finding ID | Finding | Criteria mapping | Required evidence | Business impact | Recommended package | Roadmap phase | Default confidence |
|---|---|---|---|---|---|---|---|
| OI-FIND-GBP-001 | Profile is missing, duplicated, suspended, or difficult to verify | OI-GBP-001 | Search screenshot, profile URLs, duplicate comparison, client access confirmation | Local buyers may encounter no profile, conflicting profiles, or an unreliable discovery path. | Google Business Authority Pack | Phase 1 if access or duplication blocks visibility; otherwise Phase 2 | Medium until control is verified |
| OI-FIND-GBP-002 | Profile ownership or administrative access is unverified | OI-GBP-001 | Client interview, administrative screenshot, ownership confirmation | The business may be unable to maintain accurate information, respond to issues, or implement improvements reliably. | Google Business Authority Pack | Phase 1 — Quick Wins | Low to Medium |
| OI-FIND-GBP-003 | Primary category does not clearly match the core service | OI-GBP-002 | Category screenshot, service list, website comparison | The profile may communicate weaker relevance for the business's primary service category. | Google Business Authority Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-004 | Secondary categories do not support the verified service mix | OI-GBP-003 | Category review, service inventory, website comparison | Relevant services may not be represented as clearly as the actual business scope allows. | Google Business Authority Pack | Phase 2 — Growth Foundation | Medium to High |
| OI-FIND-GBP-005 | Service listings are incomplete, vague, or outdated | OI-GBP-004 | Services screenshot, website service inventory, client-confirmed service list | Buyers may not see the full or current service offering when evaluating the profile. | Google Business Authority Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-006 | Business description is generic, outdated, or unsupported | OI-GBP-005 | Description screenshot, website copy, service-area review | The profile may provide limited clarity about services, local relevance, and customer value. | Google Business Authority Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-007 | Phone number, website link, hours, or service area is incomplete or inconsistent | OI-GBP-001, OI-GBP-012, OI-TRUST-011 | Profile screenshot, website comparison, call/link test, hours review | Buyers may encounter confusion or fail to reach the business through the intended path. | Google Business Authority Pack plus Website Conversion Fix Pack when website paths are affected | Phase 1 — Quick Wins | High when tested |
| OI-FIND-GBP-008 | Website link routes to a weak or mismatched destination | OI-GBP-012, OI-CONV related signals | Link test, destination-page review, service comparison | High-intent profile visitors may arrive on a page that does not match the service or provide a clear next step. | Website Conversion Fix Pack plus Google Business Authority Pack | Phase 1 — Quick Wins | High when tested |
| OI-FIND-GBP-009 | Profile services and website service pages are misaligned | OI-GBP-004, OI-GBP-012, OI-SEO related signals | Profile service list, URL inventory, website service review | Buyers and search systems may receive inconsistent signals about what the business offers. | Google Business Authority Pack plus Local SEO Expansion Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-010 | Photo library is sparse, outdated, or weak as proof of work | OI-GBP-006, OI-TRUST-003, OI-TRUST-004 | Photo-tab screenshots, upload dates, project-proof comparison | Buyers may have limited visual evidence of recent work, team presence, equipment, or completed outcomes. | Google Business Authority Pack plus Trust Proof System | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-011 | Owner-uploaded photos do not provide enough controlled proof | OI-GBP-006 | Photo-source review, project-photo inventory, client interview | The business may depend on customer-submitted images that do not consistently represent current work or positioning. | Google Business Authority Pack plus Trust Proof System | Phase 2 — Growth Foundation | Medium |
| OI-FIND-GBP-012 | Review count is weak relative to comparable local competitors | OI-GBP-007, OI-TRUST-001 | Named competitor comparison, review-count screenshots, market/service match | The profile may present less visible reputation proof during local buyer comparison. | Review Generation System | Phase 3 — Automation and Reporting | Medium to High |
| OI-FIND-GBP-013 | Review recency or velocity is weak or inconsistent | OI-GBP-008, OI-TRUST-001 | Review dates, recent-review sample, competitor comparison | Buyers may see limited evidence of current customer activity. | Review Generation System | Phase 3 — Automation and Reporting | High when review history is visible |
| OI-FIND-GBP-014 | Reviews lack service-specific or decision-useful detail | OI-GBP-007, OI-GBP-008, OI-TRUST-002 | Review sample, service references, competitor review comparison | Review proof may be positive but less useful for buyers evaluating a specific service, process, or outcome. | Review Generation System plus Trust Proof System | Phase 3 for process; Phase 2 for proof placement | Medium |
| OI-FIND-GBP-015 | Owner responses are absent, generic, or inconsistent | OI-GBP-009 | Review-response screenshots, response-rate review, competitor comparison | The profile may underuse a visible opportunity to demonstrate responsiveness and professionalism. | Google Business Authority Pack or Review Generation System | Phase 2 if manual correction; Phase 3 if workflow needed | High when observable |
| OI-FIND-GBP-016 | Negative or sensitive reviews lack a controlled response process | OI-GBP-009, OI-AUTO related signals | Review examples, client interview, response workflow, escalation rules | Reputation handling may depend on inconsistent judgment without clear escalation or approval. | Review Generation System | Phase 3 — Automation and Reporting | Low to Medium unless workflow is documented |
| OI-FIND-GBP-017 | Q&A is unmanaged or does not address common buyer questions | OI-GBP-010 | Q&A screenshot, unanswered questions, FAQ comparison | Buyers may encounter unanswered questions or miss useful service and expectation information. | Google Business Authority Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-018 | Posts or updates are inactive, inconsistent, or disconnected from business priorities | OI-GBP-011 | Post history, dates, content review, seasonal/service priorities | The profile may provide limited evidence of current activity, recent work, or timely service relevance. | Google Business Authority Pack | Phase 2 — Growth Foundation | High when observable |
| OI-FIND-GBP-019 | Booking, appointment, messaging, or inquiry path is missing or unverified where relevant | OI-GBP-001, OI-CONV related signals | Profile action review, link test, phone test, client workflow confirmation | Buyers may lack a reliable profile-level path to request service or understand the next step. | Google Business Authority Pack plus Website Conversion Fix Pack or CRM and Follow-Up System based on workflow | Phase 1 for broken path; Phase 3 for workflow | Medium to High |
| OI-FIND-GBP-020 | Profile activity lacks an accountable owner or maintenance cadence | OI-GBP-006, OI-GBP-009, OI-GBP-010, OI-GBP-011 | Client interview, task ownership, content/review workflow, update history | Profile accuracy, proof, responses, and activity may degrade because maintenance depends on informal memory. | Google Business Authority Pack or Review Generation System | Phase 3 — Automation and Reporting | Low to Medium |
| OI-FIND-GBP-021 | Comparable competitors present stronger profile completeness or proof | OI-GBP-002 through OI-GBP-012, OI-COMP related signals | Named competitor comparison across categories, services, photos, reviews, Q&A, and posts | Buyers may encounter clearer relevance, stronger proof, or more active profiles when comparing local providers. | Google Business Authority Pack plus the package tied to the specific gap | Phase 2 — Growth Foundation | Medium to High |

## Criteria mapping rules

Use Google Business Profile findings as the primary finding type when the weakness exists primarily inside the profile or its maintenance workflow.

Use cross-domain routing when evidence shows a dependency:

| GBP issue | Cross-domain dependency | Routing rule |
|---|---|---|
| Profile link leads to a weak page | Conversion or Website | Pair with website or conversion finding when the landing experience is the main action barrier. |
| Profile services lack matching pages | SEO | Pair with SEO finding when website service architecture is incomplete. |
| Review proof is weak or poorly used | Trust | Pair with trust finding when buyer confidence is the main weakness. |
| Review requests or responses are inconsistent | Automation | Pair with automation finding when no repeatable workflow exists. |
| Review growth or profile leads are unmeasured | Analytics | Pair with analytics finding when reporting is absent. |
| Description or service copy is vague | Messaging | Pair with messaging finding when offer clarity is the primary weakness. |
| Competitors have stronger profiles | Competitive | Pair with competitive finding only when named comparison materially affects priority. |

## Evidence requirements

Acceptable evidence includes:

- Google search screenshot
- profile screenshot
- GBP administrative screenshot
- category review
- service-list comparison
- website link test
- phone or booking-path test
- service-area and hours review
- photo-tab review
- review-count and review-date comparison
- owner-response review
- Q&A review
- post/update history
- competitor comparison
- website URL inventory
- client interview
- CRM or call-tracking evidence

Minimum evidence by finding group:

| Finding group | Minimum evidence |
|---|---|
| Existence, duplication, or suspension | Search screenshot and profile URLs; administrative confirmation when available. |
| Ownership or access | Administrative screenshot or client confirmation. |
| Categories and services | Profile screenshots plus verified service list. |
| Contact, hours, service area, and links | Profile screenshot plus website or action-path test. |
| Photos | Photo-tab review including recency and source where visible. |
| Review strength | Review count, rating, dates, sample language, and named competitor context when comparative. |
| Review responses | Response screenshots and observable response consistency. |
| Q&A and posts | Public section review and activity dates. |
| Website alignment | Profile service list plus website URL/service inventory. |
| Maintenance workflow | Client interview, task ownership, templates, or process record. |

If administrative access, ownership, suspension status, source attribution, or internal workflow cannot be verified, mark the condition `validation_required`.

## Business impact language

Use report-safe language that frames the issue as local discovery, relevance, trust, or action readiness.

| Weak wording | Use instead |
|---|---|
| Your Google profile is bad. | The profile provides a baseline local presence, but several fields and proof signals could better support buyer discovery and confidence. |
| You are not ranking because of this. | The profile may not communicate the strongest available service and local relevance signals. |
| Your reviews are weak. | Review proof appears less current, specific, or competitive than the visible local comparison set. |
| You need to post constantly. | A defined update cadence could help keep project proof, seasonal relevance, and profile activity current. |
| Add every category possible. | Categories should be limited to accurate options that reflect verified services. |
| You are losing calls. | The current profile-to-inquiry path creates contact friction risk because the action route is incomplete, inconsistent, or unverified. |

## Recommended package routing

| Condition | Recommended package | Notes |
|---|---|---|
| Profile access, categories, services, description, photos, Q&A, posts, or core information need correction. | Google Business Authority Pack | Default Phase 2, with Phase 1 for blocked access or broken buyer paths. |
| Review count, recency, velocity, or request consistency is weak. | Review Generation System | Phase 3 when a repeatable process is needed. |
| Reviews or photos exist but are not used as website proof. | Trust Proof System | Pair with GBP work when profile proof is stronger than website proof. |
| Website service pages do not align with profile services. | Local SEO Expansion Pack plus Google Business Authority Pack | Phase 2. |
| Profile traffic reaches a weak or broken destination. | Website Conversion Fix Pack plus Google Business Authority Pack | Phase 1 when inquiry access is affected. |
| Profile inquiry handling is untracked or lacks ownership. | CRM and Follow-Up System | Phase 3. |
| Profile calls, clicks, reviews, or actions are not measured. | Operator Dashboard Pack | Phase 3. |

## Roadmap phase rules

| Phase | Use when |
|---|---|
| Phase 1 — Quick Wins | Profile access, duplication, incorrect contact details, broken links, wrong hours, or action-path failures create immediate buyer friction. |
| Phase 2 — Growth Foundation | Default for categories, services, description, photos, Q&A, posts, website alignment, and competitor-position corrections. |
| Phase 3 — Automation and Reporting | Use for review generation, response workflows, profile maintenance ownership, lead routing, and measurement. |
| Phase 4 — Governed AI Enablement | Only use when AI assists review responses, Q&A drafts, post drafts, or profile maintenance with human approval, source controls, escalation, and logging. |

## Report-use rules

A Google Business Profile finding can enter a client report only when:

1. The finding is tied to discovery, relevance, trust, consistency, action readiness, or profile governance.
2. Evidence is listed or the gap is marked `validation_required`.
3. Confidence is assigned.
4. Business impact avoids unsupported ranking, lead, or revenue claims.
5. Competitor comparisons identify comparable named profiles when used.
6. Recommended package is justified by the evidence.
7. Roadmap phase is assigned.
8. DecisionLedger entry can be completed.

Do not report ownership, suspension, administrative access, call performance, or lead impact as confirmed unless direct evidence exists.

## DecisionLedger requirements

Each Google Business Profile recommendation must include:

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
primary_domain:
dependent_domains:
validation_required:
policy_or_accuracy_risk:
owner_validation_needed:
report_section:
status:
```

## Example ledger record

```text
finding_id: OI-FIND-GBP-009
observation: The profile lists several services that do not have corresponding website service pages, while two website services are absent from the profile.
evidence: GBP service-list screenshot and website URL inventory.
interpretation: The profile and website do not present a consistent service architecture.
business_impact: Buyers and search systems may receive inconsistent information about the company's service coverage.
confidence: High
priority: High
recommended_package: Google Business Authority Pack plus Local SEO Expansion Pack
roadmap_phase: Phase 2 — Growth Foundation
primary_domain: Google Business Profile
dependent_domains: Local SEO, Website
validation_required: Confirm final service priorities with owner
policy_or_accuracy_risk: Services must reflect actual offerings
owner_validation_needed: Yes
report_section: Google Business Profile Findings
status: report_ready_after_validation
```

## Usage instructions

1. Search for and document all visible business profiles before scoring.
2. Confirm profile identity, duplication risk, and ownership status when evidence is available.
3. Capture categories, services, description, contact details, hours, service area, links, photos, reviews, Q&A, and posts.
4. Compare profile services against the website service inventory.
5. Review reputation dimensions separately: count, rating, recency, velocity, specificity, and responses.
6. Compare only against relevant named local competitors.
7. Test inquiry paths when safe.
8. Assign confidence based on public evidence and administrative access.
9. Route to package and roadmap phase.
10. Record dependencies and validation needs in the DecisionLedger.

## Completion check

Before final report use, confirm:

- Profile identity and evidence are documented.
- Ownership or access assumptions are disclosed.
- Categories and services reflect real offerings.
- Contact details and action paths are verified or marked unknown.
- Review dimensions are evaluated separately.
- Competitor comparisons are relevant and named.
- No manipulative or inaccurate tactic is recommended.
- Confidence is not overstated.
- Package selection is justified.
- Roadmap phase is sequenced.
- Ledger record is complete.
