# Unknown-Heavy Operator Score Run Example

Version: v0.1 scoring execution example  
Stage alignment: Stage 3 — `scoring/`  
Folder alignment: `scoring/examples/`  
Example key: `OI-EX-SCORE-UNKNOWN-001`  
Status: Synthetic methodology stress test for commercial v1.0 validation

## 1. Purpose

This file demonstrates how Operator Intelligence handles an assessment with substantial missing internal evidence without converting unknowns into failures, overstating confidence, inventing findings, or publishing a falsely precise Operator Score.

The company, evidence, and results are synthetic. They must not be presented as a real client assessment.

## 2. Assessment header

```yaml
assessment_id: OI-ASSESS-EXAMPLE-002
client_name: Cedar Ridge Home Services
client_status: synthetic_example
assessment_type: limited_access_operator_assessment
methodology_version: "0.1"
weight_profile: OI-WEIGHT-DEFAULT-01
profile_version: "0.1"
weights_frozen_before_scoring: true
evaluator: Example Evaluator
reviewer: Example Reviewer
publication_state: range_only
publication_reason: "Material internal evidence gaps create a wide score range and prevent a single defensible Operator Score."
```

## 3. Access and evidence inventory

| Evidence ref | Evidence type | Scope | Access state | Use |
|---|---|---|---|---|
| `OI-EV-UNK-001` | Desktop and mobile captures | Homepage, services, contact, about | Available | Public website criteria |
| `OI-EV-UNK-002` | URL and metadata inventory | Public indexable pages | Available | Website and local SEO criteria |
| `OI-EV-UNK-003` | Visible form review | Fields and confirmation screen | Available | Visible conversion criteria only |
| `OI-EV-UNK-004` | Safe form submission | Notification, routing, acknowledgement | Not authorized | Criteria requiring delivery verification remain unknown or blocked |
| `OI-EV-UNK-005` | Google Business Profile review | Public profile surfaces | Available | GBP criteria |
| `OI-EV-UNK-006` | Review sample | 18 public reviews | Available | GBP and trust evidence under duplicate ownership rules |
| `OI-EV-UNK-007` | Social review | Public Facebook activity | Available | Social criteria |
| `OI-EV-UNK-008` | Competitor comparison | Three named local competitors | Available | Public competitive criteria |
| `OI-EV-UNK-009` | CRM and lead records | Ownership, stages, source, follow-up, outcomes | Not provided | Automation and analytics criteria remain unknown |
| `OI-EV-UNK-010` | Analytics and Search Console | Events, traffic, page performance | Access unavailable | Analytics criteria remain unknown or blocked |
| `OI-EV-UNK-011` | SOP and template review | Handoffs, responses, escalation | Partially provided | Narrow support only |
| `OI-EV-UNK-012` | AI use-case and governance review | Data, prompts, logs, review gates, QA | Not provided | AI-readiness criteria remain unknown |

## 4. Evidence gate result

```yaml
evidence_gate: conditional_pass
public_surfaces_complete: true
internal_surfaces_complete: false
unauthorized_testing: false
material_evidence_conflicts: false
unknowns_material_to_operator_score: true
single_score_publication_allowed: false
range_publication_allowed: true
```

The assessment may report verified public findings and a bounded score range. It may not present a single Operator Score as official.

## 5. Weight profile

The default weight profile is frozen before scoring.

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

## 6. Unknown handling rule

For each category:

```text
Observed Category Score = Known Criterion Point Total ÷ Known Criterion Count
Category Coverage = Known Criterion Count ÷ Applicable Criterion Count
Category Minimum = Known Criterion Point Total ÷ Applicable Criterion Count
Category Maximum = (Known Criterion Point Total + 100 × Unknown Criterion Count) ÷ Applicable Criterion Count
```

Blocked criteria remain inside applicable weight unless formally approved as `not_applicable`.

The minimum and maximum are uncertainty bounds, not predictions. They show how much the result could move while unresolved applicable criteria remain unknown.

## 7. Category score register

| Category | Applicable | Known | Unknown or blocked | Coverage | Observed score | Defensible range | Confidence |
|---|---:|---:|---:|---:|---:|---:|---|
| Website structure and UX | 12 | 10 | 2 | 83.3% | 60.00 | 50.00–66.67 | Medium |
| Messaging and offer clarity | 10 | 7 | 3 | 70.0% | 57.14 | 40.00–70.00 | Medium |
| Conversion infrastructure | 14 | 9 | 5 | 64.3% | 50.00 | 32.14–67.86 | Medium |
| Local SEO | 16 | 8 | 8 | 50.0% | 43.75 | 21.88–71.88 | Low |
| Google Business Profile | 12 | 9 | 3 | 75.0% | 66.67 | 50.00–75.00 | Medium |
| Reputation and trust | 12 | 8 | 4 | 66.7% | 62.50 | 41.67–75.00 | Medium |
| Social presence | 10 | 5 | 5 | 50.0% | 40.00 | 20.00–70.00 | Low |
| Automation maturity | 14 | 6 | 8 | 42.9% | 45.83 | 19.64–76.79 | Low |
| AI readiness | 12 | 4 | 8 | 33.3% | 31.25 | 10.42–77.08 | Low |
| Analytics and reporting | 10 | 3 | 7 | 30.0% | 41.67 | 12.50–82.50 | Low |
| Competitive position | 10 | 4 | 6 | 40.0% | 56.25 | 22.50–82.50 | Low |

## 8. Operator Score treatment

```text
Observed Weighted Indicator = Σ(Observed Category Score × Category Weight)
= 51.74

Weighted Evidence Coverage = Σ(Category Coverage × Category Weight)
= 58.6%

Operator Score Minimum = Σ(Category Minimum × Category Weight)
= 31.50

Operator Score Maximum = Σ(Category Maximum × Category Weight)
= 72.91

Defensible Operator Score Range = 32–73
```

The value `51.74` is an internal observed-data indicator only. It is not published as an official Operator Score because 41.4% of weighted evidence remains unresolved and the bounded range is materially wide.

Client-facing publication:

```yaml
operator_score: null
operator_score_range: [32, 73]
observed_weighted_indicator: 51.74
weighted_evidence_coverage: 58.6
publication_state: range_only
```

## 9. Representative criterion states

```yaml
- criterion_id: OI-CONV-006
  category_key: conversion
  state: scored
  score: 25
  confidence: high
  evidence_refs: [OI-EV-UNK-003]
  observation: "The visible confirmation screen does not state a response window or alternate contact path."
  interpretation: "Buyer expectation-setting is incomplete after submission."

- criterion_id: OI-AUTO-002
  category_key: automation
  state: blocked
  score: null
  confidence: unknown
  evidence_refs: [OI-EV-UNK-004]
  observation: "Internal form notification behavior was not tested because submission authorization was not granted."
  interpretation: "Notification reliability cannot be determined from the visible form alone."
  validation_required: "Authorize a safe submission or provide workflow configuration and destination evidence."

- criterion_id: OI-AUTO-005
  category_key: automation
  state: unknown
  score: null
  confidence: unknown
  evidence_refs: [OI-EV-UNK-009]
  observation: "No CRM or lead-stage records were provided."
  interpretation: "Lead-status maturity cannot be assessed."
  validation_required: "Provide stage definitions and a representative sample of recent lead records."

- criterion_id: OI-AI-004
  category_key: ai_readiness
  state: unknown
  score: null
  confidence: unknown
  evidence_refs: [OI-EV-UNK-012]
  observation: "No use-case-specific human review controls were available for inspection."
  interpretation: "The existence and quality of AI review gates cannot be determined."
  validation_required: "Provide the active use-case inventory and review or escalation rules."
```

## 10. Finding controls

Unknown and blocked criteria do not automatically create negative findings.

A finding is allowed only when the observed condition is directly evidenced and all required governance fields are complete.

| Finding ID | Evidence-backed condition | Confidence | Priority | Package | Phase | Ledger ref |
|---|---|---|---|---|---|---|
| `OI-FIND-CONV-006` | Visible form confirmation lacks response timing and an alternate path | High | High | Website Conversion Fix Pack | Phase 1 | `OI-DL-UNK-001` |
| `OI-FIND-SEO-014` | Public project proof is not structured as indexable case-study content | High | Medium | Local Search Foundation | Phase 2 | `OI-DL-UNK-002` |
| `OI-FIND-GBP-009` | Sampled public reviews do not consistently receive owner responses | High | Medium | Review Generation System | Phase 3 | `OI-DL-UNK-003` |

The following statements are prohibited:

- “Leads are being missed” without routing, inbox, call, CRM, or client evidence.
- “Follow-up is inconsistent” without tasks, records, messages, or interview evidence.
- “Analytics are not installed” when access was unavailable.
- “The business is not AI-ready” when required governance evidence was not provided.
- “Competitors convert better” without controlled conversion evidence.

## 11. Validation request register

| Validation ID | Unknown area | Required evidence | Effect if unresolved |
|---|---|---|---|
| `OI-VAL-UNK-001` | Form delivery and internal notification | Authorized safe test or routing configuration | Automation capture remains blocked |
| `OI-VAL-UNK-002` | Lead ownership and pipeline state | CRM fields and representative records | Automation remains low-confidence |
| `OI-VAL-UNK-003` | Follow-up and estimate outcomes | Tasks, messages, stage history, outcome fields | No follow-up or estimate finding allowed |
| `OI-VAL-UNK-004` | Analytics and source attribution | GA4, Search Console, event and source configuration | Analytics remains unknown |
| `OI-VAL-UNK-005` | Internal handoffs and templates | Approved SOPs and current templates | Handoff and communication criteria remain partial |
| `OI-VAL-UNK-006` | AI governance controls | Use cases, data rules, review gates, logs, escalation, QA | AI implementation routing remains blocked |

## 12. DecisionLedger examples

```yaml
- ledger_ref: OI-DL-UNK-001
  category_key: conversion
  criterion_ids: [OI-CONV-006]
  evidence_refs: [OI-EV-UNK-003]
  observation: "Visible form confirmation does not state response timing or an alternate contact path."
  interpretation: "The submission state leaves next-step expectations incomplete."
  business_impact: "Clear acknowledgement may reduce buyer uncertainty after a high-intent action."
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

- ledger_ref: OI-DL-UNK-004
  category_key: automation
  criterion_ids: [OI-AUTO-002, OI-AUTO-005, OI-AUTO-006, OI-AUTO-007]
  evidence_refs: [OI-EV-UNK-004, OI-EV-UNK-009]
  observation: "Internal notification, pipeline, follow-up, and estimate records were unavailable or not authorized for testing."
  interpretation: "Operational maturity cannot be determined from public evidence."
  business_impact: "No impact claim is authorized until validation evidence is reviewed."
  confidence: unknown
  priority: null
  finding_ids: []
  primary_package: null
  dependent_packages: []
  roadmap_phase: null
  unknowns:
    - notification reliability
    - lead ownership
    - stage maintenance
    - follow-up controls
    - estimate outcomes
  blocked_conditions:
    - safe form test not authorized
    - CRM records not provided
  review_state: REVIEW
  reviewed_by: Example Reviewer
```

## 13. Roadmap treatment

### Allowed work

1. Phase 1 may include the directly evidenced form-confirmation correction.
2. Phase 2 may include directly evidenced public SEO and proof improvements.
3. Phase 3 may include review-response process improvements supported by public evidence and client confirmation.

### Validation before routing

1. Do not route CRM or follow-up implementation from unknown internal workflow evidence.
2. Do not route analytics implementation until access or configuration evidence confirms the actual gap.
3. Do not route governed AI implementation until workflow, data, privacy, review, escalation, logging, and QA prerequisites are evaluated.

## 14. Executive-safe report language

> The available public evidence identifies several visible improvement opportunities, including form expectation-setting, project-content depth, and review-response consistency. Internal lead handling, follow-up, analytics, and AI-governance maturity could not be fully verified during this assessment. The current evidence supports a broad Operator Score range of 32–73 rather than a single official score. Completing the listed validation requests would materially narrow that range and support more precise implementation routing.

## 15. Publication decision

```yaml
publication_state: range_only
single_operator_score: prohibited
verified_findings_publishable: true
unknowns_visible: true
validation_register_required: true
reassessment_required_for_official_score: true
```

An `official` score requires sufficient evidence coverage and resolution of material internal unknowns under the governing scoring and publication rules.

## 16. Validation checklist

- [x] Weight profile totals 100% and was frozen before scoring
- [x] Unknown and blocked criteria remain inside applicable weight
- [x] Unknown values were not converted to zero
- [x] Observed score, evidence coverage, and uncertainty range are separate
- [x] Confidence remains separate from maturity
- [x] No finding was created solely from missing access
- [x] No package was routed solely from an unknown criterion
- [x] Unauthorized testing was not performed
- [x] Duplicate-signal ownership was preserved
- [x] Validation requests identify evidence needed to narrow uncertainty
- [x] DecisionLedger records preserve findings, unknowns, and blocked conditions
- [x] Executive language avoids unsupported lead-loss, revenue, conversion, competitor, and ROI claims

## 17. v1.0 connection

This example proves that Operator Intelligence can remain commercially useful under limited access without manufacturing certainty. It preserves score integrity, makes uncertainty measurable, separates verification work from implementation work, and provides a governed path from `range_only` publication to a defensible official assessment.