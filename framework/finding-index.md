# Operator Intelligence Finding Index

Version: v0.1 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file is the canonical control layer for resolving findings across the Operator Intelligence methodology.

It does not replace domain finding libraries. It defines how findings are identified, compared, combined, prioritized, routed, recorded, and approved so that the same evidence does not generate duplicate recommendations or contradictory roadmap actions.

## Source libraries

| Domain | Source file | Finding ID prefix | Primary scope |
|---|---|---|---|
| Website | `framework/findings/website-findings.md` | `OI-FIND-WEB-` | Site structure, usability, technical presentation, mobile and page-level weaknesses |
| Conversion | `framework/findings/conversion-findings.md` | `OI-FIND-CONV-` | Calls to action, forms, inquiry paths, friction and conversion readiness |
| Messaging | `framework/findings/messaging-findings.md` | `OI-FIND-MSG-` | Buyer-facing clarity, differentiation, service communication and claim quality |
| SEO | `framework/findings/seo-findings.md` | `OI-FIND-SEO-` | Search visibility, service-location coverage, on-page signals and discoverability |
| Google Business Profile | `framework/findings/gbp-findings.md` | `OI-FIND-GBP-` | Profile completeness, local proof, category fit and profile activity |
| Trust | `framework/findings/trust-findings.md` | `OI-FIND-TRUST-` | Proof, credibility, policies, guarantees, reviews and expectation confidence |
| Competitive | `framework/findings/competitive-findings.md` | `OI-FIND-COMP-` | Relative market gaps supported by observable competitor evidence |
| Offer and sales system | `framework/findings/offer-findings.md` | `OI-FIND-OFFER-` | Entry offer, packaging, qualification, sales process, follow-up and retention |
| Automation | `framework/findings/automation-findings.md` | `OI-FIND-AUTO-` | Workflow ownership, CRM structure, handoffs, triggers and operating consistency |
| Analytics | `framework/findings/analytics-findings.md` | `OI-FIND-AN-` | Measurement, attribution, status visibility, reporting and decision use |
| AI readiness | `framework/findings/ai-readiness-findings.md` | `OI-FIND-AI-` | Governed AI prerequisites, boundaries, review, privacy, auditability and QA |

The finding definition, criteria mapping, evidence requirement, package route, roadmap phase, and default confidence remain authoritative in the source library.

## Canonical finding record

Every reportable finding must resolve to one record with these fields:

| Field | Requirement |
|---|---|
| `finding_id` | Existing ID from a source library |
| `domain` | One primary domain from the registry above |
| `title` | Source-library finding title |
| `observation` | What was directly observed |
| `evidence_refs` | URLs, screenshots, records, interview notes, exports or validation gaps |
| `criteria_refs` | Applicable IDs from `scoring/criteria-library.md` |
| `interpretation` | Evidence-bounded meaning of the observation |
| `business_impact` | Executive-safe risk or opportunity statement |
| `confidence` | `high`, `medium`, `low`, or `unknown` |
| `validation_state` | `verified`, `partial`, `validation_required`, or `not_observed` |
| `priority` | Priority produced by the approved scoring and risk model |
| `primary_package` | Existing implementation package that directly resolves the finding |
| `dependent_packages` | Packages required before or alongside the primary package |
| `roadmap_phase` | Approved implementation phase |
| `dependencies` | Findings, data, approvals or operating prerequisites |
| `decision_state` | `recommend`, `defer`, `validate`, `monitor`, or `block` |
| `ledger_ref` | DecisionLedger record identifier |
| `client_language` | Final report-ready wording |

A finding missing any required field may appear in working notes but cannot enter the final recommendation set.

## Resolution sequence

Resolve findings in this order:

1. Record the observation without interpretation.
2. Attach evidence and identify missing evidence.
3. Match the observation to an existing source-library finding.
4. Assign one primary domain.
5. Add secondary-domain dependencies without creating duplicate findings.
6. Apply confidence and validation state.
7. Determine business impact without unsupported revenue or ROI claims.
8. Route to one primary package and any required dependent packages.
9. Apply roadmap sequencing and prerequisite gates.
10. Write the DecisionLedger record.
11. Produce executive-safe client language.

## Primary-domain rule

Use the domain that owns the root condition, not the surface where it was noticed.

| Observation | Primary domain | Typical dependency |
|---|---|---|
| Buyer cannot find the inquiry action | Conversion | Website or messaging |
| Inquiry action exists but its wording is vague | Messaging | Conversion |
| Service lacks a dedicated search-targeted page | SEO | Website and messaging |
| Service is promoted without validated capacity or scope | Offer | Messaging, SEO or conversion |
| Estimate follow-up depends on memory | Offer | Automation |
| Lead status fields are absent | Automation | Analytics and AI readiness |
| Performance cannot be measured | Analytics | Relevant operating domain |
| AI is proposed for an undefined workflow | AI readiness | Automation or offer prerequisite |
| Competitor appears stronger in one area | Competitive only when comparative evidence changes priority | Underlying operating domain |

## Duplicate-control rules

1. One root condition produces one primary finding.
2. Secondary effects are recorded as dependencies, not cloned findings.
3. Multiple pages showing the same condition are evidence instances under one finding unless page-specific remediation differs materially.
4. A single package may resolve several findings, but each finding retains its own evidence and ledger record.
5. Similar wording does not make two findings duplicates when their root causes, owners, controls or implementation paths differ.
6. Competitive evidence may increase priority but must not duplicate the underlying website, SEO, trust, offer or conversion finding.
7. AI-readiness findings do not replace automation, analytics or process findings that represent missing prerequisites.
8. Unknown data does not create a negative finding unless the relevant library explicitly defines absence of measurement or control as the condition.

## Conflict resolution

When two libraries appear applicable:

1. Prefer the library with the more specific root-condition definition.
2. Prefer the finding with the stronger evidence match.
3. Prefer the finding whose package directly resolves the condition.
4. Record the other domain as a dependency.
5. If neither mapping is defensible, use `validation_required`; do not invent a new finding during assessment delivery.
6. New finding proposals require methodology review and a separate source-library update before use.

## Confidence controls

| Confidence | Minimum basis |
|---|---|
| High | Direct public evidence, verified records, tested workflow, configuration review or repeated confirmed observation |
| Medium | Multiple supporting signals or partial internal evidence with material gaps remaining |
| Low | Limited evidence, owner recollection, inaccessible systems or unverified assumptions |
| Unknown | Evidence is insufficient to support a directional conclusion |

Confidence affects assertion strength, not business importance. A potentially severe condition with low confidence must route to validation, not be presented as fact.

## Decision states

| State | Use when |
|---|---|
| `recommend` | Evidence, confidence, package fit and sequencing gates are sufficient |
| `defer` | Finding is valid but a prerequisite or higher-priority dependency must be completed first |
| `validate` | Material evidence, ownership, capacity, policy or system access is missing |
| `monitor` | Condition is not currently actionable but should be tracked |
| `block` | Recommendation would violate evidence, delivery, privacy, safety, package or roadmap gates |

## Package-routing controls

1. Route to an existing package only.
2. Select the package that resolves the root condition, not the package with the highest commercial value.
3. Separate primary package from prerequisite and dependent packages.
4. Do not route growth packages ahead of offer, capacity, trust, conversion, follow-up or measurement readiness when those gaps would amplify failure.
5. Do not route AI implementation ahead of workflow, data, privacy, review, escalation, logging and QA prerequisites.
6. When no package fits, create a validation or methodology gap record; do not force a package match.

## Roadmap sequencing controls

| Sequence | Default purpose |
|---|---|
| Phase 1 — Quick Wins | Correct clear, high-confidence friction, inconsistency, risk or blocked buyer actions |
| Phase 2 — Growth Foundation | Improve discoverability, service coverage, proof and buyer-facing structure after core readiness |
| Phase 3 — Automation and Reporting | Establish CRM, workflow, handoff, follow-up, data and measurement infrastructure |
| Phase 4 — Governed AI Enablement | Implement bounded AI use cases only after required controls and prerequisites pass |

A source-library phase may be changed only when evidence, dependency, urgency or risk justifies the change and the DecisionLedger records the reason.

## DecisionLedger minimum record

```yaml
ledger_ref: OI-DL-YYYY-NNN
finding_id: OI-FIND-DOMAIN-NNN
observation: ""
evidence_refs: []
criteria_refs: []
confidence: unknown
validation_state: validation_required
business_impact: ""
primary_package: ""
dependent_packages: []
roadmap_phase: ""
decision_state: validate
decision_reason: ""
assumptions: []
unknowns: []
approvals_required: []
```

## Final-report admission gate

A finding may enter the client-facing report only when all statements below are true:

- The finding ID exists in a source library.
- Evidence supports the observation.
- Unknowns and assumptions are explicit.
- Confidence matches evidence quality.
- The root domain is identified.
- Duplicate and dependency checks are complete.
- Business impact uses evidence-safe language.
- Package routing resolves the demonstrated condition.
- Roadmap placement respects prerequisites.
- DecisionLedger traceability exists.
- Client language does not claim unsupported revenue, ROI, rankings, capacity, compliance or certainty.

## Methodology maintenance rule

When a new or changed finding is approved:

1. Update the relevant domain finding library first.
2. Preserve the domain prefix and assign the next available ID.
3. Add criteria, evidence, confidence, impact, package and roadmap mappings.
4. Check for duplicates across all source libraries.
5. Update this registry only when a domain, prefix, resolution rule or canonical field changes.

This file is the framework-level source of truth for finding resolution. Domain libraries remain the source of truth for finding content.