# Findings Library Manifest

Status: Complete for commercial v1.0 foundation  
Scope: `framework/findings/`  
Canonical control layer: `framework/finding-index.md`

## Purpose

This folder contains the 11 governed domain finding libraries used to convert assessment evidence into traceable, reportable findings.

The files in this folder define reusable finding patterns. They do not independently authorize recommendations, package routing, roadmap placement, or client-facing claims. Those decisions must pass through the canonical controls in `framework/finding-index.md` and the applicable scoring, confidence, risk-impact, recommendation, and DecisionLedger standards.

## Registered libraries

| Domain | File | Registered findings |
|---|---|---:|
| Website | `website-findings.md` | 18 |
| Conversion | `conversion-findings.md` | 15 |
| Messaging | `messaging-findings.md` | 21 |
| SEO | `seo-findings.md` | 18 |
| Google Business Profile | `gbp-findings.md` | 21 |
| Trust | `trust-findings.md` | 18 |
| Competitive | `competitive-findings.md` | 21 |
| Offer and sales system | `offer-findings.md` | 24 |
| Automation | `automation-findings.md` | 17 |
| Analytics | `analytics-findings.md` | 18 |
| AI readiness | `ai-readiness-findings.md` | 26 |
| **Total** | **11 libraries** | **217** |

## Required operating sequence

1. Record the direct observation.
2. Attach evidence references and identify missing evidence.
3. Resolve the observation to one existing finding ID.
4. Assign one primary domain and any dependent domains.
5. Apply confidence and validation state.
6. Map the finding to business impact without unsupported ROI or revenue claims.
7. Apply risk-impact, package-routing, roadmap, and dependency controls.
8. Create or update the DecisionLedger record.
9. Admit the finding to client-facing output only after all gates pass.

## Non-negotiable controls

- Unknown or inaccessible data must not be scored as failure unless the applicable standard explicitly defines the absence of measurement or control as the finding.
- One root condition must not be duplicated across domain libraries.
- Competitive evidence may change priority, but must not duplicate the underlying operating finding.
- AI-readiness findings must not bypass workflow, data, privacy, review, logging, escalation, or QA prerequisites.
- Package routing must resolve the demonstrated condition, not maximize commercial scope.
- Roadmap phases must respect dependencies and implementation readiness.
- Client language must not claim unsupported rankings, compliance, certainty, capacity, revenue, or ROI.
- A finding without evidence, confidence, validation state, impact, routing, roadmap placement, and DecisionLedger traceability is not report-ready.

## Change control

Do not add a new file, finding prefix, or finding ID during assessment delivery.

A proposed finding change requires:

1. documented evidence that the current library cannot represent the condition accurately;
2. duplicate analysis across all 11 libraries;
3. criteria, evidence, confidence, impact, package, and roadmap mappings;
4. approval through the methodology governance process;
5. an update to the relevant domain library first;
6. synchronized updates to `framework/finding-index.md` counts and ranges.

## Folder completion gate

This folder is complete for the commercial v1.0 foundation when:

- all 11 registered libraries exist;
- the aggregate count remains 217 unless an approved methodology change updates it;
- IDs, ranges, and counts reconcile with `framework/finding-index.md`;
- every library preserves evidence gates, confidence handling, unknown-data rules, package routing, roadmap phases, and report-safe language;
- no duplicate or ungoverned finding library exists.

Any failed condition reopens this folder for governed correction before downstream release approval.
