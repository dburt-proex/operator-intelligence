# Operator Intelligence Finding Index

Version: v0.2 control-layer foundation  
Stage alignment: Stage 2 — `framework/`  
Folder alignment: `framework/`  
Status: Draft foundation for commercial v1.0

## Purpose

This file is the canonical control layer for resolving findings across the Operator Intelligence methodology.

It does not replace domain finding libraries. It defines how findings are registered, identified, compared, combined, prioritized, routed, recorded, and approved so that the same evidence does not generate duplicate recommendations or contradictory roadmap actions.

## v1.0 connection

Commercial v1.0 requires one governed finding system that can support assessment delivery, scoring, recommendations, reports, proposals, roadmaps, implementation, and quality control.

This index strengthens v1.0 readiness by providing:

- a complete domain-library registry
- stable finding prefixes and ranges
- duplicate and conflict controls
- primary-domain ownership rules
- canonical finding records
- package and risk-impact handoffs
- final-report admission gates
- methodology maintenance rules

## Inputs and triggers

Use this index whenever:

- raw evidence is converted into a finding
- several domain libraries appear applicable
- one root problem creates several visible effects
- findings are prepared for scoring, reporting, recommendation routing, or roadmapping
- a new finding is proposed
- a completed implementation is reviewed against its original finding

## Outputs and deliverables

A valid use of this index produces:

- one governed finding ID
- one primary domain
- explicit dependent domains
- evidence and validation state
- confidence level
- business-impact classification
- risk-impact record
- primary and dependent package routes
- roadmap phase
- DecisionLedger record
- report-safe client language

## Source-library registry

| Domain | Source file | Finding range | Count | Primary scope |
|---|---|---:|---:|---|
| Website | `framework/findings/website-findings.md` | `OI-FIND-WEB-001`–`018` | 18 | Site structure, usability, mobile, navigation, page hierarchy, and buyer support |
| Conversion | `framework/findings/conversion-findings.md` | `OI-FIND-CONV-001`–`015` | 15 | Calls to action, forms, inquiry paths, friction, and conversion readiness |
| Messaging | `framework/findings/messaging-findings.md` | `OI-FIND-MSG-001`–`021` | 21 | Buyer-facing clarity, differentiation, service communication, and claim quality |
| SEO | `framework/findings/seo-findings.md` | `OI-FIND-SEO-001`–`018` | 18 | Search visibility, service-location coverage, on-page signals, and discoverability |
| Google Business Profile | `framework/findings/gbp-findings.md` | `OI-FIND-GBP-001`–`021` | 21 | Profile control, completeness, service alignment, proof, reputation, and activity |
| Trust | `framework/findings/trust-findings.md` | `OI-FIND-TRUST-001`–`018` | 18 | Reviews, work proof, human proof, risk reduction, and local legitimacy |
| Competitive | `framework/findings/competitive-findings.md` | `OI-FIND-COMP-001`–`021` | 21 | Relative market gaps supported by comparable, dated evidence |
| Offer and sales system | `framework/findings/offer-findings.md` | `OI-FIND-OFFER-001`–`024` | 24 | Entry offer, packaging, qualification, pricing factors, sales process, follow-up, referral, and retention |
| Automation | `framework/findings/automation-findings.md` | `OI-FIND-AUTO-001`–`017` | 17 | Workflow ownership, CRM structure, handoffs, triggers, failure controls, and operating consistency |
| Analytics | `framework/findings/analytics-findings.md` | `OI-FIND-AN-001`–`018` | 18 | Measurement, attribution, status visibility, reporting, and decision use |
| AI readiness | `framework/findings/ai-readiness-findings.md` | `OI-FIND-AI-001`–`026` | 26 | Governed AI prerequisites, boundaries, review, privacy, auditability, escalation, and QA |

**Registered finding total:** 217

The finding title, criteria mapping, evidence requirement, business impact, package route, roadmap phase, confidence guidance, and report-use rules remain authoritative in each source library.

## Social-signal governance gap

The criteria library includes social-presence signals, but the approved Stage 1 queue contains 11 finding libraries and does not include a standalone social finding library.

Until methodology review resolves this gap:

1. Social evidence may support website, messaging, trust, GBP, competitive, automation, or analytics findings.
2. Do not invent `OI-FIND-SOC-*` IDs during assessment delivery.
3. Do not score social evidence twice across several findings.
4. Record a methodology gap when a material social condition cannot be represented accurately by an existing library.
5. A future social library requires explicit approval, criteria mapping, package routing, and duplicate analysis.

## Canonical finding record

Every reportable finding must resolve to one record with these fields:

| Field | Requirement |
|---|---|
| `finding_id` | Existing ID from a registered source library |
| `domain` | One primary domain from the registry |
| `dependent_domains` | Secondary domains affected by the same root condition |
| `title` | Source-library finding title |
| `observation` | What was directly observed |
| `evidence_refs` | URLs, screenshots, records, interview notes, exports, tests, or validation gaps |
| `criteria_refs` | Applicable IDs from `scoring/criteria-library.md` |
| `interpretation` | Evidence-bounded meaning of the observation |
| `business_impact` | Executive-safe risk or opportunity statement |
| `confidence` | `high`, `medium`, `low`, or `unknown` |
| `validation_state` | `verified`, `partial`, `validation_required`, or `not_observed` |
| `risk_impact_ref` | Record from `framework/risk-impact-model.md` |
| `priority` | Priority produced by approved scoring and risk controls |
| `primary_package` | Canonical package from `framework/recommendation-index.md` |
| `dependent_packages` | Packages required before or alongside the primary package |
| `roadmap_phase` | Approved implementation phase |
| `dependencies` | Findings, data, approvals, capacity, policies, or operating prerequisites |
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
5. Add dependent domains without creating duplicate findings.
6. Apply confidence and validation state.
7. Determine business impact without unsupported revenue or ROI claims.
8. Apply `framework/risk-impact-model.md`.
9. Route through `framework/recommendation-index.md`.
10. Assign roadmap sequencing and prerequisites.
11. Write the DecisionLedger record.
12. Produce executive-safe client language.

## Primary-domain rule

Use the domain that owns the root condition, not the surface where it was noticed.

| Observation | Primary domain | Typical dependency |
|---|---|---|
| Buyer cannot find the inquiry action | Conversion | Website or messaging |
| Inquiry action exists but its wording is vague | Messaging | Conversion |
| Service lacks a dedicated search-targeted page | SEO | Website and messaging |
| Service is promoted without validated capacity or scope | Offer | Messaging, SEO, or conversion |
| Estimate follow-up depends on memory | Offer | Automation |
| Lead status fields are absent | Automation | Analytics and AI readiness |
| Performance cannot be measured | Analytics | Relevant operating domain |
| AI is proposed for an undefined workflow | AI readiness | Automation or offer prerequisite |
| Competitor appears stronger in one area | Competitive only when comparative evidence changes priority | Underlying operating domain |

## Duplicate-control rules

1. One root condition produces one primary finding.
2. Secondary effects are recorded as dependent domains, not cloned findings.
3. Multiple pages showing the same condition are evidence instances under one finding unless remediation differs materially.
4. A single package may resolve several findings, but each finding retains its own evidence and ledger record.
5. Similar wording does not make two findings duplicates when root causes, owners, controls, or implementation paths differ.
6. Competitive evidence may increase priority but must not duplicate the underlying website, SEO, GBP, trust, offer, or conversion finding.
7. AI-readiness findings do not replace automation, analytics, offer, or process findings that represent missing prerequisites.
8. Unknown data does not create a negative finding unless the relevant library defines absence of measurement or control as the condition.
9. Cross-channel evidence should be grouped when it demonstrates one systemic condition.
10. Risk exposure scores from dependent findings must not be added together to manufacture urgency.

## Conflict resolution

When two libraries appear applicable:

1. Prefer the library with the more specific root-condition definition.
2. Prefer the finding with the stronger evidence match.
3. Prefer the finding whose primary package directly resolves the condition.
4. Record the other domain as dependent.
5. If neither mapping is defensible, use `validation_required`; do not invent a finding during assessment delivery.
6. New finding proposals require methodology review and a source-library update before use.

## Confidence controls

| Confidence | Minimum basis |
|---|---|
| High | Direct public evidence, verified records, tested workflow, configuration review, or repeated confirmed observation |
| Medium | Multiple supporting signals or partial internal evidence with material gaps remaining |
| Low | Limited evidence, owner recollection, inaccessible systems, or unverified assumptions |
| Unknown | Evidence is insufficient to support a directional conclusion |

Confidence affects assertion strength, not business importance. A potentially severe condition with low confidence routes to validation or block, not confident reporting.

## Decision states

| State | Use when |
|---|---|
| `recommend` | Evidence, confidence, package fit, risk treatment, and sequencing gates are sufficient |
| `defer` | Finding is valid but a prerequisite or higher-priority dependency must be completed first |
| `validate` | Material evidence, ownership, capacity, policy, access, or system context is missing |
| `monitor` | Condition is not currently actionable but should be tracked |
| `block` | Recommendation would violate evidence, delivery, privacy, safety, accuracy, package, or roadmap gates |

## Package-routing controls

1. Route only through packages registered in `framework/recommendation-index.md`.
2. Select the package that resolves the root condition, not the package with the highest commercial value.
3. Separate primary package from prerequisite and dependent packages.
4. Do not route growth packages ahead of offer, capacity, trust, conversion, follow-up, or measurement readiness when those gaps would amplify failure.
5. Do not route AI implementation ahead of workflow, data, privacy, review, escalation, logging, and QA prerequisites.
6. When no package fits, create a validation or methodology gap record; do not force a package match.

## Roadmap sequencing controls

| Sequence | Default purpose |
|---|---|
| Phase 1 — Quick Wins | Correct clear, high-confidence friction, inconsistency, accuracy risk, or blocked buyer actions |
| Phase 2 — Growth Foundation | Improve discoverability, service coverage, proof, local relevance, and buyer-facing structure after core readiness |
| Phase 3 — Automation and Reporting | Establish CRM, workflow, handoff, follow-up, review, data, and measurement infrastructure |
| Phase 4 — Governed AI Enablement | Implement bounded AI use cases only after required controls and prerequisites pass |

A source-library phase may change only when evidence, dependency, urgency, or risk justifies the change and the DecisionLedger records the reason.

## DecisionLedger minimum record

```yaml
ledger_ref: OI-DL-YYYY-NNN
finding_id: OI-FIND-DOMAIN-NNN
domain: ""
dependent_domains: []
observation: ""
evidence_refs: []
criteria_refs: []
confidence: unknown
validation_state: validation_required
business_impact: ""
risk_impact_ref: ""
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

A finding may enter the client-facing report only when:

- the finding ID exists in a registered source library
- evidence supports the observation
- unknowns and assumptions are explicit
- confidence matches evidence quality
- the root domain is identified
- duplicate and dependency checks are complete
- business impact uses evidence-safe language
- risk-impact evaluation exists
- package routing resolves the demonstrated condition
- roadmap placement respects prerequisites
- DecisionLedger traceability exists
- client language does not claim unsupported revenue, ROI, rankings, capacity, compliance, or certainty

## Methodology maintenance rule

When a new or changed finding is approved:

1. Update the relevant domain finding library first.
2. Preserve the domain prefix and assign the next available ID.
3. Add criteria, evidence, confidence, impact, package, and roadmap mappings.
4. Check for duplicates across all source libraries.
5. Update the registered count and range in this index.
6. Recheck recommendation and risk-impact coverage.
7. Record the methodology change in the future governance-change process.

## Usage instructions

1. Start with evidence, not a conclusion.
2. Resolve the evidence to one source-library finding.
3. Apply primary-domain and duplicate controls.
4. Complete the canonical finding record.
5. Apply the risk-impact model.
6. Apply the recommendation index.
7. Create the DecisionLedger record.
8. Use the approved record in scoring, reports, proposals, and roadmaps.
9. Reopen the finding when evidence, scope, implementation, or results change.

## Completion check

Before release or client use, confirm:

- all 11 approved libraries remain registered
- ID ranges and counts match source files
- no ungoverned finding prefix is used
- primary and dependent domains are explicit
- duplicates are consolidated
- risk and package handoffs exist
- report admission rules pass
- DecisionLedger traceability is complete

This file is the framework-level source of truth for finding resolution. Domain libraries remain the source of truth for finding content.