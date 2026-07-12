# Recommendation Register

Version: v0.1 commercial foundation  
Stage alignment: `templates/`  
Status: Governed working template

## Purpose

Use this register to convert approved findings into controlled, client-safe recommendations that remain traceable through package routing, roadmap sequencing, implementation authorization, acceptance evidence, and DecisionLedger review.

A recommendation may enter a report, roadmap, proposal, or implementation handoff only when its source chain is complete and its scope does not exceed the supporting evidence.

## Register controls

| Field | Value |
|---|---|
| Assessment ID |  |
| Client |  |
| Report version |  |
| Publication state | `internal_only` / `provisional` / `range_only` / `official` / `blocked` |
| Register owner |  |
| Reviewer |  |
| DecisionLedger register ref |  |
| Last reviewed |  |

## Controlled values

**Recommendation class**  
`implementation` · `validation` · `monitoring` · `defer` · `halt`

**Confidence**  
`high` · `medium` · `low` · `unknown`

**Priority**  
`critical` · `high` · `medium` · `low`

**Status**  
`proposed` · `accepted` · `deferred` · `blocked` · `in_progress` · `complete` · `rejected` · `superseded`

**Review state**  
`ALLOW` · `REVIEW` · `HALT`

## Recommendation register

| Recommendation ID | Class | Source finding refs | Evidence refs | Root condition | Confidence | Material unknowns | Risk / impact basis | Priority | Primary package | Dependencies / prerequisites | Roadmap phase | Owner | Acceptance evidence | Status | Review state | DecisionLedger ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OI-REC-YYYY-NNN |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Recommendation record

### 1. Identity and source chain

```yaml
recommendation_id: OI-REC-YYYY-NNN
recommendation_class: implementation|validation|monitoring|defer|halt
status: proposed|accepted|deferred|blocked|in_progress|complete|rejected|superseded
finding_refs: []
evidence_refs: []
criterion_refs: []
ledger_refs: []
```

### 2. Decision basis

**Observed condition**  
State only what the evidence supports.

**Root condition**  
Identify the condition the recommendation directly resolves.

**Interpretation**  
Separate analysis from observed fact.

**Confidence:** `high` / `medium` / `low` / `unknown`

**Confidence basis**  
Document the weakest material evidence dependency.

**Material unknowns**

- 

**Contradictory or limiting evidence**

- 

### 3. Risk, impact, and priority

**Risk level:**  
**Impact class:**  
**Priority:** `critical` / `high` / `medium` / `low`

**Supported operational effect**  
Describe the expected operating-state improvement without asserting unverified financial, traffic, ranking, conversion, lead-volume, market-share, or ROI outcomes.

**Priority rationale**  
Priority does not override prerequisites, blocked conditions, or roadmap order.

### 4. Recommended action

**Recommendation statement**  
Use bounded, implementation-specific language.

**Included scope**

- 

**Excluded scope**

- 

**Validation-first action, when required**

- Missing evidence:
- Minimum validation action:
- Validation owner:
- Decision enabled by validation:

Unknown confidence cannot authorize implementation.

### 5. Package routing

```yaml
primary_package_id: ""
primary_package_name: ""
prerequisite_package_ids: []
dependent_package_ids: []
reference_only_package_ids: []
routing_reason: ""
```

Rules:

- Assign exactly one primary package.
- Route by the verified root condition, not commercial preference.
- Do not duplicate ownership or deliverables across packages.
- When no canonical package fits, record a methodology or validation gap rather than inventing a package.

### 6. Roadmap placement

**Roadmap phase:** `Phase 1` / `Phase 2` / `Phase 3` / `Phase 4`

**Prerequisites**

- 

**Dependencies**

- 

**Blocked conditions**

- 

**Implementation owner:**  
**Decision authority:**

Phase 4 work requires workflow, data, privacy, human-review, escalation, logging, and QA gates to pass before implementation.

### 7. Acceptance and measurement

**Acceptance criteria**

1. 
2. 

**Required acceptance evidence**

- 

**Measurement plan**

| Metric | Definition | Source system | Baseline status | Review window | Owner | Limitation | Decision triggered |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Implementation completion and outcome validation are separate decisions. Deliverable existence alone does not prove completion.

### 8. Authorization and review

```yaml
publication_state: internal_only|provisional|range_only|official|blocked
implementation_authorization: not_requested|pending|approved|denied|withdrawn
review_state: ALLOW|REVIEW|HALT
review_reason: ""
reviewed_by: ""
reviewed_at: ""
approved_by: ""
approved_at: ""
```

Publication approval does not authorize implementation.

### 9. Change control

| Change date | Prior record or version | Material change | Reason | Evidence or finding effect | Package or phase effect | DecisionLedger ref | Reviewer |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Approved recommendations are not silently overwritten. Material changes require a superseding record or updated DecisionLedger event.

## Release validation

Before a recommendation advances, confirm:

- [ ] Source findings are approved and resolvable.
- [ ] Evidence references are valid and current enough for the decision.
- [ ] Observed fact, interpretation, unknowns, and recommended action are separated.
- [ ] Confidence does not exceed the weakest material evidence dependency.
- [ ] Unknown confidence routes to validation rather than implementation.
- [ ] Scope is proportional to the verified root condition.
- [ ] Exactly one canonical primary package is assigned.
- [ ] Duplicate package ownership and duplicate deliverables are absent.
- [ ] Prerequisites, dependencies, and blocked conditions are explicit.
- [ ] Roadmap phase respects the canonical sequence.
- [ ] Acceptance criteria are observable and tied to the source finding.
- [ ] Measurement claims remain within verified baselines and source data.
- [ ] Publication approval and implementation authorization are separate.
- [ ] DecisionLedger traceability is complete.
- [ ] Client language avoids unsupported ROI, revenue, ranking, conversion, lead-loss, market-share, competitor-performance, and timeline claims.

Any failed evidence-integrity, package-ownership, prerequisite, authorization, traceability, or unresolved `HALT` check requires `HALT`.

## Canonical references

Use this template with:

- `templates/finding-register.md`
- `templates/evidence-register.md`
- `templates/decision-ledger.md`
- `templates/roadmap.md`
- `standards/recommendation-standard.md`
- `standards/package-routing-standard.md`
- `standards/roadmap-standard.md`
- `standards/publication-standard.md`
- `framework/recommendation-index.md`
- `scoring/recommendation-map.md`
