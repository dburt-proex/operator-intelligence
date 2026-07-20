# Operator Intelligence Finding Register Template

Version: v0.2 template reconciliation  
Stage alignment: Stage 5 — `templates/`  
Folder alignment: `templates/`  
Status: Governed commercial v1.0 finding template

## 1. Purpose

Use this register to control material assessment findings from evidence review through validation, suppression, publication, recommendation development, package eligibility, roadmap placement, and DecisionLedger traceability.

A plausible condition is not automatically a finding. A publishable finding requires admissible evidence, bounded interpretation, supported business impact, confidence, duplicate control, and executive-safe language.

## 2. Register control

```yaml
assessment_id: ""
register_version: ""
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
publication_state: internal_only|official|provisional|range_only|blocked
register_owner: ""
reviewer: ""
qc_ref: null
ledger_ref: OI-DL-YYYY-NNN
```

## 3. Finding states

- `candidate`
- `validation_required`
- `validated`
- `suppressed`
- `blocked`
- `published`
- `closed`
- `superseded`

## 4. Finding record

```yaml
finding_id: OI-FIND-DOMAIN-NNN
finding_version: "1.0"
supersedes: null
title: ""
domain: website|conversion|messaging|offer|seo|gbp|trust|competitive|automation|analytics|ai_readiness
category_key: ""
criterion_refs: []
evidence_refs: []
contradictory_evidence_refs: []
state: candidate|validation_required|validated|suppressed|blocked|published|closed|superseded
observation: ""
interpretation: ""
business_impact: ""
confidence: high|medium|low|unknown
confidence_basis: ""
assumptions: []
limitations: []
unknowns: []
validation_required: []
weighted_owner: ""
reference_only_uses: []
severity: G1|G2|G3|G4
score_effect: ""
report_use: include|internal_only|validation_note|suppress
recommendation_refs: []
package_eligibility: eligible|validation_required|blocked|not_applicable|null
primary_package_id: null
roadmap_phase: 0|1|2|3|4|5|null
review_state: ALLOW|REVIEW|HALT
qc_ref: null
ledger_refs: []
approved_by: null
approved_at: null
```

## 5. Finding statement contract

Use this sequence:

```text
Observation
→ Evidence
→ Interpretation
→ Business impact
→ Confidence and limitations
→ Required decision
```

- **Observation:** what was directly observed or supplied.
- **Evidence:** exact evidence IDs, dates, methods, and scope.
- **Interpretation:** what the evidence supports, not assumed cause.
- **Business impact:** bounded operational, buyer-path, trust, visibility, measurement, or governance relevance.
- **Confidence/limitations:** what is known, unknown, conflicting, or blocked.
- **Required decision:** validate, develop a recommendation, monitor, defer, suppress, close, or halt.

## 6. Evidence and unknown-data rules

- Missing access is unknown or blocked, not negative evidence.
- Public absence does not prove internal absence.
- Class D or inferred evidence normally supports validation, not a negative finding.
- A finding with no resolvable admitted evidence cannot advance beyond candidate/validation required.
- Contradictory evidence remains visible and routes to REVIEW.
- Confidence cannot exceed the evidence chain.
- Unknown conditions do not create package-eligible implementation routes.

## 7. Duplicate ownership

Each material signal has one primary weighted owner. Other findings or categories may reference it only when they represent distinct root conditions or reference-only effects.

Unresolved duplication affecting score, priority, package route, scope, or publication requires HALT.

## 8. Recommendation and package transition

- A validated finding may support one or more distinct recommendations.
- Package eligibility is determined at the recommendation/routing layer.
- Exactly one primary package is required only for package-eligible work.
- Validation and blocked findings normally use Phase 0 and no primary package.
- Priority cannot bypass prerequisites.
- G4 and unresolved HALT conditions block dependent work.
- AI work cannot advance before all readiness gates pass.

## 9. Suppression and closure

A finding may be suppressed or closed only with a ledgered reason:

- duplicate ownership
- immaterial or out of scope
- unsupported by admissible evidence
- superseded by a more precise finding
- verified resolved before publication
- accepted monitoring condition

Suppression cannot conceal a material unknown, contradiction, blocker, or release risk.

## 10. Executive-safe language

Approved patterns:

- “The reviewed evidence shows…”
- “The condition was not visible on the tested public surfaces…”
- “This may constrain…”
- “Internal validation is required before implementation…”

Prohibit blame, universal claims, and unsupported financial or performance certainty.

## 11. Pre-publication validation

- [ ] ID, domain, criteria, and finding-library mapping are valid.
- [ ] Evidence refs are admitted and traceable.
- [ ] Observation and interpretation are separated.
- [ ] Impact is supported and bounded.
- [ ] Confidence, unknowns, limitations, and contradictions are visible.
- [ ] Duplicate ownership is resolved.
- [ ] Score effect is reproducible or explicitly unscored.
- [ ] Package eligibility and phase treatment are valid where referenced.
- [ ] QC and DecisionLedger refs resolve.
- [ ] Publication state permits release.
- [ ] Executive-safe language passes.

Any failed evidence, duplication, unknown-state, traceability, or publication check requires HALT.

## 12. Commercial v1.0 connection

This register makes finding construction repeatable and protects the transition from evidence to recommendation and package routing.

## 13. References

- `framework/finding-index.md`
- `framework/findings/`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/quality-control-standard.md`
- `templates/evidence-register.md`
- `templates/recommendation-register.md`