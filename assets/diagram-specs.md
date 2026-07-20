# Operator Intelligence Diagram Specifications

Version: v1.0 commercial asset specification  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Canonical diagram registry

## 1. Purpose

Define the diagrams required to explain Operator Intelligence architecture, buyer journey, evidence-to-decision flow, package routing, governance gates, and implementation lifecycle.

Every diagram must have a textual equivalent and resolvable source references.

## 2. Diagram registry

### `OI-DIAG-001` — Assessment Decision Engine

```text
Evidence
→ Criteria
→ Category Scores
→ Operator Score
→ Findings
→ Risk / Opportunity
→ Recommendations
→ Package Eligibility and Routing
→ Roadmap
→ Report / Proposal
→ Authorization
→ Completion / Monitoring
→ DecisionLedger
```

Controls shown:

- evidence admission
- unknown/blocked branch
- publication gate
- Phase 0 validation
- implementation authorization
- QC and supersession

### `OI-DIAG-002` — ALLOW / REVIEW / HALT Control Flow

```text
Proposed state change
→ Evidence + Authority + Scope + Dependencies
→ ALLOW / REVIEW / HALT
→ Next separate governed decision
```

Show that ALLOW is bounded and does not imply downstream authorization.

### `OI-DIAG-003` — Buyer Journey and Operating Handoff

```text
Discover
→ Evaluate service/location/trust
→ Call or submit
→ Confirmation
→ Ownership
→ Qualification
→ Estimate
→ Follow-up
→ Job outcome
→ Review / measurement
```

Map public and internal evidence separately. Do not imply every business uses the same stages.

### `OI-DIAG-004` — Recommendation Routing

```text
Finding
→ Priority inputs
→ Confidence gate
→ Recommendation class
→ Package eligibility
  ├─ eligible → one primary package → phase
  ├─ validation_required → Phase 0 / no package
  ├─ blocked → HALT / no package
  └─ not_applicable → monitoring/defer/closure
```

### `OI-DIAG-005` — Commercial Delivery Lifecycle

Use OI-LC-01 through OI-LC-14. Show QC, publication, proposal, onboarding, authorization, implementation, monitoring, renewal, and closure as distinct states.

### `OI-DIAG-006` — Operator Score Publication States

Show official, provisional, range-only, blocked, and internal-only as separate branches with required fields.

## 3. Node contract

Every governed node may include:

```yaml
node_id: ""
object_type: evidence|criterion|score|finding|recommendation|package|roadmap|report|decision|authorization|completion
object_ref: ""
state: ""
owner: ""
confidence: null
review_state: null
ledger_ref: null
```

## 4. Connector contract

Allowed connector labels:

- supports
- contradicts
- scores
- produces
- validates
- routes
- depends on
- blocks
- supersedes
- authorizes
- completes
- monitors

Avoid unlabeled arrows where the relationship could be ambiguous.

## 5. Visual rules

- Evidence and facts use neutral structures.
- Interpretation and decisions use distinct shapes.
- REVIEW and HALT branches remain visible.
- Unknown is shown as a state, not an empty gap.
- Package nodes appear only after eligibility.
- Authorization nodes are separate from report/proposal nodes.
- Completion and outcome nodes are separate.
- Use consistent left-to-right or top-to-bottom flow.
- Large diagrams include a legend and version.

## 6. Textual-equivalent requirement

Every diagram ships with:

- title and purpose
- ordered node list
- relationship list
- decision/gate descriptions
- source files
- limitations
- version and owner

## 7. Governance validation

HALT diagram release when:

- an arrow implies unsupported causation
- a package appears before eligibility
- publication appears to authorize implementation
- Phase 0 appears as implementation
- unknown/blocked branches are omitted
- AI appears autonomous or outside human/control boundaries
- a score state omits uncertainty/publication treatment

## 8. Commercial v1.0 connection

This registry provides the minimum architecture and delivery diagrams required to explain, sell, train, and audit the system without simplifying away governance.

## 9. References

- `framework/lifecycle-roadmap-map.md`
- `framework/recommendation-index.md`
- `standards/governance-gate-index.md`
- `assets/design-system.md`