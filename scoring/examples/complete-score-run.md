# Complete Operator Score Run Example

Version: v0.1 scoring execution example  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Example key: `OI-EX-SCORE-COMPLETE-001`  
Status: Synthetic methodology example for commercial v1.0 validation

## 1. Purpose

This file demonstrates one complete, internally consistent Operator Intelligence scoring run from evidence registration through category scoring, Operator Score calculation, finding routing, package selection, roadmap sequencing, publication control, and DecisionLedger traceability.

The company, evidence, and results below are synthetic. They must not be presented as a real client assessment.

## 2. Assessment header

```yaml
assessment_id: OI-ASSESS-EXAMPLE-001
client_name: Northline Exterior Services
client_status: synthetic_example
assessment_type: full_operator_assessment
methodology_version: "0.1"
weight_profile: OI-WEIGHT-DEFAULT-01
profile_version: "0.1"
profile_selection_reason: "General local-service contractor with no documented structural reason to use a non-default profile."
weights_frozen_before_scoring: true
evaluator: Example Evaluator
reviewer: Example Reviewer
publication_state: official
```

## 3. Evidence inventory

| Evidence ref | Evidence type | Scope | Freshness | Access state | Notes |
|---|---|---|---|---|---|
| `OI-EV-EX-001` | Desktop and mobile captures | Homepage, services, contact, about | Current-run capture | Available | Captured before interpretation. |
| `OI-EV-EX-002` | URL and metadata inventory | All indexable pages | Current-run crawl | Available | Includes titles, descriptions, H1s, canonicals, sitemap, and robots. |
| `OI-EV-EX-003` | Safe form test | Primary estimate form | Current-run test | Authorized | Submission, internal notification, confirmation, and source field checked. |
| `OI-EV-EX-004` | GBP review | Profile, categories, services, photos, posts, reviews, Q&A | Current-run review | Available | Public evidence only. |
| `OI-EV-EX-005` | Review sample | 24 recent reviews | Current-run sample | Available | Source, date, specificity, and owner response recorded. |
| `OI-EV-EX-006` | Project-proof inventory | 18 website and social images | Current-run sample | Available | Attribution and service relevance checked. |
| `OI-EV-EX-007` | Social review | Facebook and Instagram | Prior 90 days | Available | Cadence, proof, education, CTA, and response behavior sampled. |
| `OI-EV-EX-008` | Competitor comparison | Four named local competitors | Current-run review | Available | Same service area and buyer intent used. |
| `OI-EV-EX-009` | CRM and workflow review | 20 recent leads and estimate stages | Prior 90 days | Authorized | Ownership, stage, source, tasks, outcomes, and lost reasons reviewed. |
| `OI-EV-EX-010` | Analytics review | GA4, Search Console, form events, phone clicks | Prior 90 days | Authorized | Configuration and sampled event evidence reviewed. |
| `OI-EV-EX-011` | SOP and template review | Lead response, handoff, review request, escalation | Current approved versions | Available | Owners and revision state checked. |
| `OI-EV-EX-012` | AI-readiness interview and controls review | Use cases, data rules, review gates, prompts, logs | Current-run review | Authorized | No production customer-facing AI was active. |

### Evidence gate result

```yaml
evidence_gate: pass
required_surfaces_complete: true
unauthorized_testing: false
material_evidence_conflicts: false
stale_evidence_blocking_publication: false
```

## 4. Weight profile

The default profile is selected and frozen before scoring.

| Category key | Weight |
|---|---:|
| `website` | 10% |
| `messaging_offer` | 10% |
| `conversion` | 15% |
| `local_seo` | 15% |
| `gbp` | 10% |
| `trust` | 10% |
| `social` | 5% |
| `automation` | 10% |
| `ai_readiness` | 5% |
| `analytics` | 5% |
| `competitive` | 5% |
| **Total** | **100%** |

## 5. Category score register

Each category score is calculated from its applicable criteria under the governing category sheet. This example has no approved `not_applicable`, unknown, or blocked criteria.

| Category | Applicable criteria | Known criteria | Coverage | Category score | Confidence | Weighted contribution |
|---|---:|---:|---:|---:|---|---:|
| Website structure and UX | 12 | 12 | 100% | 62 | High | 6.20 |
| Messaging and offer clarity | 10 | 10 | 100% | 58 | High | 5.80 |
| Conversion infrastructure | 14 | 14 | 100% | 54 | High | 8.10 |
| Local SEO | 16 | 16 | 100% | 47 | High | 7.05 |
| Google Business Profile | 12 | 12 | 100% | 68 | High | 6.80 |
| Reputation and trust | 12 | 12 | 100% | 64 | High | 6.40 |
| Social presence | 10 | 10 | 100% | 42 | High | 2.10 |
| Automation maturity | 14 | 14 | 100% | 50 | High | 5.00 |
| AI readiness | 12 | 12 | 100% | 38 | Medium | 1.90 |
| Analytics and reporting | 10 | 10 | 100% | 45 | High | 2.25 |
| Competitive position | 10 | 10 | 100% | 55 | High | 2.75 |
| **Total** | **132** | **132** | **100%** |  |  | **54.35** |

## 6. Operator Score calculation

```text
Operator Score = Σ(Category Score × Category Weight)

= (62 × 0.10)
+ (58 × 0.10)
+ (54 × 0.15)
+ (47 × 0.15)
+ (68 × 0.10)
+ (64 × 0.10)
+ (42 × 0.05)
+ (50 × 0.10)
+ (38 × 0.05)
+ (45 × 0.05)
+ (55 × 0.05)

= 54.35
Published Operator Score = 54
Weighted Evidence Coverage = 100%
Operator Score Range = 54–54
```

The displayed score is rounded only after the weighted calculation. The unrounded value remains stored in the score object.

## 7. Representative criterion records

The full score object stores all 132 criterion records. The records below demonstrate the required structure across strong, baseline, and weak conditions.

```yaml
- criterion_id: OI-WEB-005
  category_key: website
  state: scored
  score: 75
  confidence: high
  evidence_refs: [OI-EV-EX-001]
  observation: "Tested mobile layouts remained usable and primary actions were tap-accessible."
  interpretation: "Mobile execution supports the buyer path, with minor spacing and hierarchy improvements remaining."
  duplicate_owner: website

- criterion_id: OI-CONV-006
  category_key: conversion
  state: scored
  score: 25
  confidence: high
  evidence_refs: [OI-EV-EX-003]
  observation: "The form displayed a generic success message without a response window or alternate contact path."
  interpretation: "The submission path works, but buyer expectation-setting is incomplete."
  duplicate_owner: conversion

- criterion_id: OI-SEO-014
  category_key: local_seo
  state: scored
  score: 25
  confidence: high
  evidence_refs: [OI-EV-EX-002, OI-EV-EX-006]
  observation: "Project images exist, but no indexable project or case-study pages document service, location, challenge, and outcome."
  interpretation: "Available proof is not structured to support service discovery or local search depth."
  duplicate_owner: local_seo

- criterion_id: OI-AUTO-005
  category_key: automation
  state: scored
  score: 50
  confidence: high
  evidence_refs: [OI-EV-EX-009]
  observation: "Core lead stages exist, but five of twenty sampled records lacked a current status."
  interpretation: "The pipeline is functional but not consistently maintained."
  duplicate_owner: automation

- criterion_id: OI-AI-004
  category_key: ai_readiness
  state: scored
  score: 25
  confidence: medium
  evidence_refs: [OI-EV-EX-011, OI-EV-EX-012]
  observation: "General approval expectations were described, but no use-case-specific human review matrix was documented."
  interpretation: "AI experimentation should remain internal until review gates are defined by risk and output type."
  duplicate_owner: ai_readiness
```

## 8. Finding register

Only evidence-backed gaps with complete governance fields become findings.

| Finding ID | Observation summary | Confidence | Priority | Primary category | Package | Roadmap phase | Ledger ref |
|---|---|---|---|---|---|---|---|
| `OI-FIND-CONV-006` | Form confirmation does not set a response window or alternate path | High | High | Conversion | Website Conversion Fix Pack | Phase 1 | `OI-DL-EX-001` |
| `OI-FIND-SEO-014` | Real project proof is not published as indexable case-study content | High | High | Local SEO | Local Search Foundation | Phase 2 | `OI-DL-EX-002` |
| `OI-FIND-AUTO-005` | Lead stages exist but are not consistently maintained | High | High | Automation | CRM and Follow-Up System | Phase 3 | `OI-DL-EX-003` |
| `OI-FIND-AN-010` | Reporting records metrics but does not consistently assign decisions, owners, and due dates | High | Medium | Analytics | Operator Dashboard Pack | Phase 3 | `OI-DL-EX-004` |
| `OI-FIND-AI-004` | AI review gates are not defined by use case and risk | Medium | Medium | AI readiness | Governed AI Intake Assistant prerequisite work | Phase 4 | `OI-DL-EX-005` |

## 9. Duplicate-signal control

| Shared evidence condition | Weighted owner | Dependency only |
|---|---|---|
| Weak form confirmation | Conversion | Automation records acknowledgement workflow dependency without adding a second score penalty. |
| Project proof lacks indexable pages | Local SEO | Trust records proof availability but does not rescore the same publishing gap. |
| CRM stages are inconsistently maintained | Automation | Analytics records reporting dependency without duplicating the workflow failure. |
| AI review gates are undefined | AI readiness | Automation records the workflow prerequisite only. |

```yaml
duplicate_signal_check: pass
material_duplicate_penalties: 0
```

## 10. Package and roadmap routing

### Phase 1 — Foundations and critical fixes

1. Replace the generic form-success state with a clear confirmation, response standard, and alternate contact path.
2. Verify the changed confirmation behavior through an authorized safe submission.

### Phase 2 — Visibility, proof, and demand capture

1. Convert approved project records into service-specific, locally relevant case-study pages.
2. Add internal links from relevant service pages and proof sections.
3. Preserve attribution and approved customer information.

### Phase 3 — Automation and reporting

1. Define required lead stages, record owners, update rules, stale-record handling, and estimate outcomes.
2. Add follow-up tasks and exception review.
3. Connect the dashboard to named decisions, owners, due dates, and next-review dates.

### Phase 4 — Governed AI enablement

1. Define one low-risk internal AI use case.
2. Document allowed inputs, approved knowledge, review gate, escalation path, logging, privacy rule, and QA sample.
3. Do not enable autonomous customer-facing output until the use-case control gate passes.

## 11. DecisionLedger examples

```yaml
- ledger_ref: OI-DL-EX-001
  category_key: conversion
  criterion_ids: [OI-CONV-006]
  evidence_refs: [OI-EV-EX-003]
  observation: "Primary estimate form confirms submission but does not state response timing or an alternate contact path."
  interpretation: "The functional submission path leaves buyer expectations incomplete after a high-intent action."
  business_impact: "Clear acknowledgement and next-step language may reduce uncertainty and unnecessary repeat contact."
  confidence: high
  priority: high
  finding_ids: [OI-FIND-CONV-006]
  primary_package: Website Conversion Fix Pack
  dependent_packages: []
  roadmap_phase: Phase 1
  unknowns: []
  blocked_conditions: []
  review_state: ALLOW
  reviewed_by: Example Reviewer

- ledger_ref: OI-DL-EX-005
  category_key: ai_readiness
  criterion_ids: [OI-AI-004]
  evidence_refs: [OI-EV-EX-011, OI-EV-EX-012]
  observation: "No use-case-specific human review matrix is documented."
  interpretation: "Customer-facing AI should not advance until review and escalation controls are defined."
  business_impact: "A documented review gate would reduce the risk of unapproved promises, pricing statements, complaint handling, or exception responses."
  confidence: medium
  priority: medium
  finding_ids: [OI-FIND-AI-004]
  primary_package: Governed AI Intake Assistant prerequisite work
  dependent_packages: [CRM and Follow-Up System]
  roadmap_phase: Phase 4
  unknowns: ["Production performance cannot be evaluated because no production customer-facing AI is active."]
  blocked_conditions: ["Autonomous customer-facing deployment remains blocked pending control design and validation."]
  review_state: REVIEW
  reviewed_by: Example Reviewer
```

## 12. Executive-safe output

### Executive summary

Northline Exterior Services has a functional growth-system baseline, with comparatively stronger Google Business Profile and trust signals. The primary constraints are local-search depth, post-inquiry expectation-setting, pipeline consistency, decision-oriented reporting, and governed AI prerequisites.

The evidence supports prioritizing buyer-facing confirmation fixes first, followed by indexable project proof and tighter lead-stage controls. AI work should remain limited to a controlled, low-risk internal use case until review, escalation, privacy, logging, and QA requirements are documented and tested.

### Prohibited interpretation

Do not state that this score proves:

- a specific amount of lost revenue
- a known number of missed leads
- a guaranteed conversion improvement
- competitor revenue or market share
- AI labor savings
- future package ROI

## 13. Publication determination

```yaml
weight_integrity: pass
category_coverage: 100%
weighted_evidence_coverage: 100%
minimum_scope: pass
confidence_assignment: pass
unknown_handling: pass
duplicate_signal_control: pass
finding_governance: pass
package_routing: pass
roadmap_sequence: pass
decision_ledger_traceability: pass
unauthorized_testing: false
unresolved_boundary: false
publication_state: official
```

This run is eligible for `official` publication because the approved profile is used, active weights total 100%, required evidence scope is complete, all applicable criteria are known, duplicate-signal controls pass, findings are traceable, and no unresolved governance boundary blocks the assessment result.

The `REVIEW` state on the proposed AI implementation does not block publication of the assessment. It controls the implementation decision for that use case.

## 14. Final validation checklist

- [x] One approved weight profile selected before scoring
- [x] Active category weights total 100%
- [x] Weights frozen before evidence interpretation
- [x] All criteria have valid states
- [x] Unknown is not converted to zero
- [x] Confidence is separate from maturity score
- [x] Category scores retain unrounded calculation values
- [x] Operator Score is rounded only for display
- [x] Each weighted signal has one category owner
- [x] Findings contain evidence, interpretation, impact, confidence, and priority
- [x] Recommendations route to approved implementation paths
- [x] Roadmap phases respect prerequisites
- [x] DecisionLedger references are present
- [x] Client language avoids unsupported certainty and financial claims
- [x] Publication state is explicitly determined

## 15. Reuse rule

Use this example to test scoring execution and reviewer consistency. Do not copy its scores, findings, priorities, packages, or conclusions into a real assessment. Real runs must be generated from their own evidence, applicability decisions, approved weight profile, and DecisionLedger records.