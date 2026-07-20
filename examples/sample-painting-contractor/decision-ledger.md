# Northstar Painting Co. — Synthetic DecisionLedger

Version: v1.0 sample ledger  
Stage alignment: Stage 7 — `examples/`  
Status: Synthetic immutable decision history

## 1. Ledger control

```yaml
assessment_id: OI-ASSESS-2026-EX001
engagement_id: OI-ENG-2026-EX001
methodology_version: commercial-v1.0
record_version: "1.0"
ledger_owner: Sample Evaluator
reviewer: Sample QC Reviewer
synthetic_data_only: true
```

## 2. Decision register

| Ledger ID | Type | Subject | Decision | Gate | Status | Upstream refs | Downstream effect |
|---|---|---|---|---|---|---|---|
| `OI-DL-2026-EX001` | approval | Engagement scope | Admit fictional painting assessment for regression use | ALLOW | approved | Engagement brief | Evidence collection allowed |
| `OI-DL-2026-EX002` | evidence | Evidence register | Accept 13 records, limit 4, preserve unknown and blocked states | ALLOW | approved | EX001–EX017 | Scoring permitted with limitations |
| `OI-DL-2026-EX003` | scoring/publication | Score run | Publish provisional indicator 50 with range 34–67, coverage 86.5%, confidence 0.779 | REVIEW | approved | Evidence register, scorecard | Provisional report only |
| `OI-DL-2026-EX004` | finding | Finding set | Approve five findings; suppress unsupported social, lead-loss, competitor, and AI candidates | ALLOW | approved | Evidence + scorecard | Recommendation review permitted |
| `OI-DL-2026-EX005` | finding | CONV-EX001 | Validate estimate-qualification finding | ALLOW | approved | EX003, EX004 | Eligible for recommendation |
| `OI-DL-2026-EX006` | finding | SEO-EX001 | Validate cabinet-service architecture finding | ALLOW | approved | EX005, EX006, EX008 | Eligible for recommendation |
| `OI-DL-2026-EX007` | finding | TRUST-EX001 | Validate project-proof context finding | ALLOW | approved | EX007, EX010 | Eligible for recommendation |
| `OI-DL-2026-EX008` | finding | AUTO-EX001 | Validate workflow inconsistency with Phase 0 limitation | REVIEW | approved | EX011–EX013 | Validation recommendation only |
| `OI-DL-2026-EX009` | finding | ANALYTICS-EX001 | Validate reconciliation finding with Phase 0 limitation | REVIEW | approved | EX012, EX014 | Validation recommendation only |
| `OI-DL-2026-EX010` | recommendation | Recommendation set | Approve five bounded recommendations and canonical priority results | ALLOW | approved | EX005–EX009 | Routing/roadmap permitted |
| `OI-DL-2026-EX011` | package_routing | REC-EX001 | Route to `OI-PKG-WEB-001`, subject to form-owner prerequisite | REVIEW | approved | CONV-EX001 | Phase 1 proposal permitted; start blocked |
| `OI-DL-2026-EX012` | package_routing | REC-EX002 | Route to `OI-PKG-SEO-001` | ALLOW | approved | SEO-EX001 | Phase 2 roadmap item |
| `OI-DL-2026-EX013` | package_routing | REC-EX003 | Route to `OI-PKG-TRUST-001` | ALLOW | approved | TRUST-EX001 | Phase 2 roadmap item |
| `OI-DL-2026-EX014` | recommendation | REC-EX004 | Keep workflow mapping validation-only with no package | ALLOW | approved | AUTO-EX001 | Phase 0 item |
| `OI-DL-2026-EX015` | recommendation | REC-EX005 | Keep measurement definition validation-only with no package | ALLOW | approved | ANALYTICS-EX001 | Phase 0 item |
| `OI-DL-2026-EX016` | halt | AI package candidate | Block `OI-PKG-AI-001`; controls incomplete | HALT | blocked | EX015, EX017 | No AI implementation/proposal |
| `OI-DL-2026-EX017` | roadmap | Roadmap v1.0 | Approve Phase 0, Phase 1, Phase 2, deferred Phase 3/5, and halted AI state | ALLOW | approved | Recommendation map | Report build permitted |
| `OI-DL-2026-EX018` | roadmap | Social condition | Preserve unknown; create no social finding or route | REVIEW | approved | EX016 | Disclosure only |
| `OI-DL-2026-EX019` | approval | Executive report build | Approve source-object assembly for QC | ALLOW | approved | Score/findings/recommendations/roadmap | QC permitted |
| `OI-DL-2026-EX020` | publication | Executive report v1.0 | Authorize provisional synthetic repository publication | ALLOW | approved | QC EX001 | Report publishable with conditions |
| `OI-DL-2026-EX021` | proposal | Proposal v1.0 | Permit bounded proposal example; no price, acceptance, or authorization inferred | REVIEW | approved | REC-EX001, route EX011 | Internal synthetic proposal only |
| `OI-DL-2026-EX022` | quality_control | Example artifact set | QC ALLOW with provisional conditions | ALLOW | approved | All sample artifacts | Folder completion review permitted |
| `OI-DL-2026-EX023` | implementation_authorization | All sample work | Implementation authorization denied/not granted | HALT | blocked | Proposal and roadmap | No work may enter in_progress |
| `OI-DL-2026-EX024` | completion | Sample engagement construction | Example artifact set complete; no client outcome claimed | ALLOW | complete | QC EX001 | Examples folder gate may close |

## 3. Material decision detail

### Score publication — `OI-DL-2026-EX003`

```yaml
decision_type: scoring
subject_id: OI-SCORE-2026-EX001
decision: publish_provisional_indicator
rationale: coverage and confidence support a useful point indicator, but social is unknown and material internal controls use limited samples
confidence: medium
publication_state: provisional
implementation_authorized: false
control_gate: REVIEW
```

### Website package route — `OI-DL-2026-EX011`

```yaml
decision_type: package_routing
subject_id: OI-REC-2026-EX001
package_eligibility: eligible
primary_package_id: OI-PKG-WEB-001
roadmap_phase: 1
blocked_conditions:
  - accountable form owner and routing destination not verified
implementation_authorized: false
control_gate: REVIEW
```

### AI halt — `OI-DL-2026-EX016`

```yaml
decision_type: halt
subject_id: OI-PKG-AI-001
package_eligibility: blocked
primary_package_id: null
roadmap_phase: 0
blocked_conditions:
  - privacy and permitted use
  - retention and deletion
  - human review and escalation
  - audit logging
  - QA and evaluation
  - failure and incident handling
implementation_authorized: false
control_gate: HALT
```

### Implementation authorization — `OI-DL-2026-EX023`

```yaml
decision_type: implementation_authorization
subject_id: OI-ASSESS-2026-EX001
implementation_authorized: false
authorization_ref: null
decision: no_sample_work_authorized
rationale: repository example demonstrates planning and commercial scope only
control_gate: HALT
status: blocked
```

## 4. Traceability chain

```text
Synthetic Evidence EX001–EX017
→ Score Run EX001
→ Findings EX001–EX005
→ Recommendations EX001–EX005
→ Package eligibility/routes
→ Roadmap EX001
→ Executive Report EX001
→ Proposal EX001
→ QC EX001
→ Provisional publication
→ Implementation HALT
```

## 5. Integrity rules

- Records are append-only for the sample version.
- Material corrections create superseding IDs.
- No event represents real external approval, implementation, or outcome.
- Implementation remains unauthorized.

## 6. Commercial v1.0 connection

This ledger proves full decision traceability across uncertainty, score publication, finding suppression, package eligibility, AI halt, proposal control, and completion.