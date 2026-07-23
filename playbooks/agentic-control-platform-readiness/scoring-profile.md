# Agentic Control Platform Readiness Scoring Profile

Version: 0.1.0
Status: Proposed deterministic profile
Decision unit: One bounded organization, business unit, or platform scope

## 1. Scoring principles

- Score observed readiness, not aspiration or vendor capability.
- Unknown is never zero.
- Evidence coverage and confidence remain separate from readiness.
- Exactly seven canonical domains are weighted.
- A high aggregate score cannot override a critical gate.
- Publication and implementation authorization are separate decisions.

## 2. Domain weights

| Domain | Weight |
|---|---:|
| `AIGR-D1` — Purpose and ownership | 10 |
| `AIGR-D2` — Data and system access | 15 |
| `AIGR-D3` — Tool and action authority | 15 |
| `AIGR-D4` — Workflow approvals and human intervention | 15 |
| `AIGR-D5` — Evaluation and failure testing | 15 |
| `AIGR-D6` — Logging, evidence, and auditability | 15 |
| `AIGR-D7` — Deployment, monitoring, rollback, and incident response | 15 |
| **Total** | **100** |

## 3. Criterion anchors

| Score | Anchor | Required evidence treatment |
|---:|---|---|
| 0 | Admissible operating evidence shows the required control is absent or ineffective | `VERIFIED_GAP` |
| 25 | Control is informal, narrow, manual without reliable governance, or materially inconsistent | `PARTIAL_CONTROL` |
| 50 | Control is defined and partly operating, but material scope, enforcement, ownership, or evidence limits remain | `PARTIAL_CONTROL` |
| 75 | Control is defined, owned, operating, and evidenced for most applicable scope with bounded limitations | `CONTROLLED` or bounded `PARTIAL_CONTROL` |
| 100 | Control is defined, owned, enforced, monitored, tested, and independently reconstructable for the reviewed scope | `CONTROLLED` |

`UNKNOWN`, `blocked`, and `NOT_APPLICABLE` are states, not numeric anchors.

## 4. Calculations

For each domain:

```text
domain_score =
  sum(known_criterion_score × criterion_weight)
  / sum(known_criterion_weight)
```

Overall observed readiness:

```text
readiness_score =
  sum(domain_score × active_domain_weight)
  / sum(active_domain_weight)
```

Evidence coverage:

```text
coverage =
  sum(known_criterion_weight × domain_weight)
  / sum(applicable_criterion_weight × domain_weight)
```

Confidence is assigned from evidence quality, scope, recency, integrity, corroboration, and contradiction. It never modifies the score.

## 5. Publication rules

| State | Conditions |
|---|---|
| `official` | Coverage at least 80%; all seven domains have known evidence; no unresolved material contradiction; independent review complete |
| `provisional` | Coverage 60–79.99%, or a bounded material limitation remains |
| `range_only` | Coverage below 60% but sufficient evidence supports an honest bounded range |
| `blocked` | Authority, safety, integrity, scope, traceability, or critical evidence prevents defensible publication |
| `internal_only` | QC or decision review is incomplete |

## 6. Decision routing

### `READY` / `ALLOW`

All conditions must pass:

- readiness score at least 75;
- evidence coverage at least 80%;
- all seven domains contain known evidence;
- confidence is high or medium with no material unresolved contradiction;
- no `HALT`;
- no verified critical gap;
- change-time and runtime controls are separately evidenced;
- every accepted limitation has a named owner and decision authority;
- independent review and DecisionLedger record are complete.

### `CONDITIONAL` / `REVIEW`

Apply when no `HALT` exists and one or more conditions apply:

- readiness score is 50–74.99;
- evidence coverage is 60–79.99%;
- confidence is low or a material bounded limitation exists;
- a critical control is partial but safely remediable before implementation;
- ownership, integration, evidence, or dependency work is incomplete;
- change-time or runtime evidence is incomplete.

### `NOT_READY` / `HALT`

Apply when admissible evidence verifies a critical condition such as:

- unbounded consequential action authority;
- absent accountable decision owner;
- inability to enforce least privilege for material access;
- no required human decision boundary for a high-impact action;
- no defensible evaluation or release gate for material behavior;
- material actions cannot be reconstructed;
- no containment, rollback, or incident route for critical operations.

### `BLOCKED` / `HALT`

Apply when the evaluator cannot reach a defensible result because authority, safe access, evidence integrity, scope, traceability, or handling controls fail.

## 7. Priority

Use four explicit inputs, each 1–5:

```text
priority_score =
  ((criticality + platform_decision_effect + evidence_strength + dependency_leverage) / 20) × 100
```

| Input | Meaning |
|---|---|
| Criticality | Consequence of leaving the condition unresolved |
| Platform decision effect | Degree to which it blocks or changes procurement, implementation, pilot, or expansion |
| Evidence strength | Strength of the admitted finding evidence, not confidence |
| Dependency leverage | Number and importance of downstream controls unlocked |

Confidence remains a gate. Priority cannot turn low-confidence evidence into implementation authority.

## 8. Scoring record

```yaml
assessment_id: ""
profile_version: "0.1.0"
evidence_snapshot_date: YYYY-MM-DD
domain_results:
  - domain_id: AIGR-D1
    score: null
    applicable_weight: 10
    known_weight: 0
    coverage: 0
    confidence: unknown
    finding_refs: []
    evidence_refs: []
readiness_score: null
evidence_coverage: 0
confidence: unknown
publication_state: internal_only
decision: BLOCKED
control_gate: HALT
decision_reasons: []
independent_reviewer: ""
ledger_refs: []
implementation_authorized: false
```
