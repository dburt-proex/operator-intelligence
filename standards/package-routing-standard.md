# Package Routing Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard governs how approved findings and recommendations are routed into the canonical Operator Intelligence package catalog.

It defines package ownership, dependency handling, validation-first routing, roadmap alignment, scope boundaries, completion evidence, and DecisionLedger traceability.

This standard does not create new packages, redefine finding severity, alter Operator Scores, or authorize implementation.

## 2. Governing principle

Package routing must follow the verified root condition, not sales preference, category proximity, or deliverable convenience.

Every routed recommendation must answer:

1. Which verified condition requires work?
2. Which package directly resolves that condition?
3. Which packages are prerequisites or dependencies only?
4. Which roadmap phase admits the work?
5. What evidence proves completion?
6. What remains unknown or blocked?
7. Where is the routing decision recorded?

## 3. Required routing chain

A client-facing route is admissible only when this trace exists:

```text
Evidence Record
  → Governed Finding
  → Recommendation Object
  → Primary Package
  → Dependencies and Prerequisites
  → Roadmap Phase
  → Acceptance Evidence
  → DecisionLedger Record
```

A missing link blocks implementation routing.

## 4. Canonical source of truth

All package identifiers, package names, supported outcomes, exclusions, and commercial boundaries must resolve to the canonical package registry in:

```text
framework/recommendation-index.md
```

Do not:

- invent package names during assessment delivery
- rename a package inside a report
- route work to an unregistered package
- expand package scope through narrative implication
- treat a category label as a package identifier

When no package fits, create a methodology or validation gap record. Do not improvise a client-facing package.

## 5. One-primary-package rule

Each recommendation must have exactly one primary package.

The primary package is the package that directly resolves the recommendation's root condition.

Additional packages may be recorded only as:

- `prerequisite`
- `dependency`
- `downstream`
- `reference_only`

A secondary package may not duplicate ownership of the same finding or deliverable.

## 6. Minimum routing object

```yaml
routing_id: OI-ROUTE-YYYY-NNN
recommendation_id: ""
finding_refs: []
evidence_refs: []
primary_package_id: ""
primary_package_name: ""
routing_reason: ""
secondary_routes:
  - package_id: ""
    relationship: prerequisite|dependency|downstream|reference_only
    reason: ""
roadmap_phase: ""
prerequisites: []
dependency_ids: []
unknowns: []
blocked_conditions: []
included_scope: []
excluded_scope: []
acceptance_criteria: []
acceptance_evidence_refs: []
confidence: high|medium|low|unknown
review_state: ALLOW|REVIEW|HALT
approval_state: proposed|approved|deferred|blocked|rejected|complete
ledger_refs: []
```

Required fields may not be replaced by narrative implication.

## 7. Routing admission rules

A recommendation may route to an implementation package only when:

- the source finding is governed and traceable
- evidence is admissible and current enough for the decision
- confidence is assigned separately from maturity
- the root condition is explicit
- one canonical primary package directly fits the root condition
- scope is proportional to verified need
- prerequisites and dependencies are explicit
- roadmap phase rules are satisfied
- unknowns and blocked conditions are visible
- acceptance criteria are observable
- DecisionLedger references exist
- language is executive-safe

Failure of any material gate routes the recommendation to `REVIEW`, `HALT`, validation, or deferment.

## 8. Primary ownership test

Assign primary ownership using this sequence:

1. Identify the verified root condition.
2. Remove adjacent symptoms and downstream effects.
3. Compare the root condition against canonical package outcomes.
4. Select the smallest package that fully owns the corrective work.
5. Record other necessary packages as prerequisites or dependencies.
6. Confirm the route does not duplicate another recommendation.
7. Record the reasoning in the DecisionLedger.

Do not select a package because it:

- has higher commercial value
- contains familiar deliverables
- appears adjacent to the scoring category
- was discussed previously with the client
- can absorb unrelated work

## 9. Cross-category findings

A finding may involve several scoring categories but still has one primary package.

Route according to the root condition, not the number of categories affected.

Example:

```text
Finding: inquiries are submitted but ownership and follow-up state are not recorded.
Primary package: workflow or operating-system package that establishes intake ownership.
Dependency: analytics package for later stage and outcome reporting.
Not allowed: assigning both packages as co-primary.
```

Category references remain useful for evidence and score traceability but do not determine package ownership.

## 10. Unknown and blocked handling

Unknown is not negative evidence and does not justify implementation routing.

When a material condition is unknown:

- record the missing evidence
- route to a bounded validation action
- define the minimum evidence needed
- preserve applicable scoring weight
- prohibit package expansion based on assumption

Use `blocked` when access, authorization, privacy, safety, legal, policy, technical control, or client constraints prevent validation or implementation.

A blocked route must state:

- blocking condition
- affected package and dependency
- owner or decision authority
- unblock requirement
- next review point

## 11. Roadmap phase controls

Default sequence:

```text
Phase 1 — Quick Wins
Phase 2 — Growth Foundation
Phase 3 — Automation and Reporting
Phase 4 — Governed AI Enablement
```

Routing rules:

1. Visible critical failures and foundational accuracy work precede expansion.
2. Offer, proof, service, and conversion foundations precede scaled acquisition work.
3. Undefined workflows must be documented before automation.
4. Metric definitions and source systems must exist before reporting implementation.
5. Workflow, data, privacy, review, escalation, logging, and QA controls must pass before Phase 4 AI work.
6. An unresolved `HALT` blocks all dependent routes.
7. Phase assignment may not be accelerated solely by priority score or client preference.

## 12. Scope controls

Included scope must contain only the work needed to resolve the source recommendation.

Excluded scope must name adjacent work that is unsupported, deferred, unauthorized, or assigned elsewhere.

Prohibited routing patterns include:

- one broken form routed to a full-site rebuild
- one missing report routed to a broad data-platform project
- inconsistent follow-up routed directly to automation before workflow definition
- weak proof routed to unrestricted content production
- general AI interest routed to customer-facing AI deployment
- one finding duplicated across several packages to increase scope

## 13. Package completion

Package completion requires acceptance evidence tied to the source finding.

Valid completion evidence may include:

- tested operating state
- reconciled source records
- approved workflow and ownership map
- published and verified client-facing asset
- passed QA record
- signed acceptance record
- controlled AI test results with review and logging evidence

Deliverable existence alone does not prove completion.

Implementation completion must remain separate from business-outcome validation.

## 14. DecisionLedger requirements

Every routing decision must record:

```yaml
ledger_event: package_route_created|package_route_changed|package_route_blocked|package_route_completed
routing_id: ""
recommendation_id: ""
finding_refs: []
evidence_refs: []
primary_package_id: ""
secondary_routes: []
roadmap_phase: ""
routing_reason: ""
confidence: ""
unknowns: []
blocked_conditions: []
review_state: ""
approval_state: ""
decision_owner: ""
decision_date: ""
change_reason: ""
previous_route_ref: ""
```

Material route changes require a new ledger event. Do not overwrite prior reasoning.

## 15. Executive-safe language

Client-facing package language must distinguish:

- verified condition
- recommended corrective scope
- dependencies
- unknowns
- implementation status
- outcome measurement status

Do not claim or imply guaranteed traffic, rankings, lead volume, close rate, savings, revenue, market share, or ROI without validated baseline and post-implementation evidence.

Use language such as:

- "This package addresses the verified intake ownership gap."
- "Analytics work is a downstream dependency, not part of the primary corrective scope."
- "Implementation is deferred until access and workflow validation are complete."
- "Completion confirms the operating control was implemented; business impact requires separate measurement."

## 16. Validation codes

| Code | Meaning |
|---|---|
| `PKG-ROUTE-001` | No valid canonical primary package is assigned. |
| `PKG-OWNER-001` | More than one package is marked primary. |
| `PKG-SCOPE-001` | Routed scope exceeds the verified root condition. |
| `PKG-PHASE-001` | Roadmap phase bypasses a required prerequisite. |
| `PKG-UNKNOWN-001` | Unknown evidence was treated as implementation evidence. |
| `PKG-TRACE-001` | Required evidence, finding, recommendation, or ledger trace is missing. |
| `PKG-DUP-001` | The same finding or deliverable is owned by multiple packages. |
| `PKG-COMPLETE-001` | Completion lacks acceptance evidence. |

## 17. Blocking errors

The route must be blocked when:

- no canonical package fits
- multiple primary packages are assigned
- the root condition is unsupported
- material evidence is unknown or inadmissible
- a required prerequisite is unresolved
- a `HALT` condition applies
- implementation exceeds authorized scope
- acceptance criteria are not observable
- DecisionLedger traceability is absent
- client language contains unsupported outcome claims

## 18. Warnings

Governance review is required when:

- confidence is low
- evidence is conflicting or stale
- the route depends on client-reported conditions only
- package scope approaches a commercial boundary
- ownership overlaps another active recommendation
- phase sequencing is being changed
- completion evidence is indirect

Warnings do not automatically block routing, but they must remain visible and resolved or accepted by an authorized reviewer.

## 19. Worked routing example

```yaml
routing_id: OI-ROUTE-2026-001
recommendation_id: OI-REC-2026-014
finding_refs: [OI-FND-2026-022]
evidence_refs: [OI-EV-2026-118, OI-EV-2026-119]
primary_package_id: OI-PKG-WORKFLOW
primary_package_name: Workflow Foundation
routing_reason: "The verified root condition is unassigned inquiry ownership and undefined follow-up state."
secondary_routes:
  - package_id: OI-PKG-ANALYTICS
    relationship: downstream
    reason: "Stage and outcome reporting depends on the workflow state model."
roadmap_phase: "Phase 3 — Automation and Reporting"
prerequisites:
  - approved intake stages
  - named ownership rules
unknowns: []
blocked_conditions: []
included_scope:
  - inquiry ownership model
  - stage definitions
  - escalation rules
excluded_scope:
  - dashboard implementation
  - AI-assisted response generation
acceptance_criteria:
  - "Every test inquiry enters the approved system of record with owner and stage."
confidence: high
review_state: ALLOW
approval_state: approved
```

## 20. Governance checklist

Before approving a package route, confirm:

- [ ] Source evidence and finding are traceable.
- [ ] Root condition is explicit.
- [ ] Exactly one canonical primary package is assigned.
- [ ] Secondary packages have defined relationships.
- [ ] Scope is proportional and non-duplicative.
- [ ] Unknowns and blocked conditions are visible.
- [ ] Roadmap prerequisites are satisfied.
- [ ] Acceptance criteria are observable.
- [ ] Unsupported outcome claims are absent.
- [ ] DecisionLedger record is complete.

## 21. Cross references

- `framework/recommendation-index.md`
- `framework/findings/`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/recommendation-standard.md`
- `standards/roadmap-standard.md`
- `scoring/category-sheets/`
