# Package Routing Standard

Version: v0.2 standards reconciliation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Reconciled commercial v1.0 control standard; pending folder approval

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

A missing link blocks package eligibility or routes the item to validation. A package route by itself never authorizes implementation.

## 4. Canonical source of truth

Package identifiers, names, default phases, triggers, outcomes, exclusions, and commercial boundaries resolve first to framework/recommendation-index.md.

scoring/recommendation-map.md supplies criteria-to-package trigger context and baseline deliverables only when it does not conflict with the framework registry. framework/lifecycle-roadmap-map.md governs canonical roadmap phases. This standard governs routing behavior and authorization separation.

| Package ID | Canonical package | Default phase |
|---|---|---|
| OI-PKG-WEB-001 | Website Conversion Fix Pack | Phase 1 — Quick Wins |
| OI-PKG-SEO-001 | Local SEO Expansion Pack | Phase 2 — Growth Foundation |
| OI-PKG-GBP-001 | Google Business Authority Pack | Phase 2 — Growth Foundation |
| OI-PKG-TRUST-001 | Trust Proof System | Phase 2 — Growth Foundation |
| OI-PKG-CRM-001 | CRM and Follow-Up System | Phase 3 — Automation and Reporting |
| OI-PKG-REV-001 | Review Generation System | Phase 3 — Automation and Reporting |
| OI-PKG-DASH-001 | Operator Dashboard Pack | Phase 3 — Automation and Reporting |
| OI-PKG-AI-001 | Governed AI Intake Assistant | Phase 4 — Governed AI Enablement |

Reports, proposals, roadmaps, fixtures, and ledgers must use the package ID and canonical name together.

Do not:

- invent package names during assessment delivery
- use unversioned aliases as canonical IDs
- rename a package inside a report
- route work to an unregistered package
- expand package scope through narrative implication
- treat a category label as a package identifier

When no package fits, create a methodology or validation gap record. Do not improvise a client-facing package.

## 5. Package eligibility and one-primary-package rule

Each package-eligible implementation or deferred recommendation must have exactly one primary package.

The primary package is the registered package that directly resolves the verified root condition. Additional packages may be recorded only as prerequisite, dependency, downstream, or reference_only.

Validation, monitoring, halt, and blocked recommendations may have no primary package while eligibility is unresolved. Their route state must remain validation_required, blocked, or not_routed, with the next gate recorded.

A secondary package may not duplicate ownership of the same finding or deliverable.

## 6. Minimum routing object

~~~yaml
routing_id: OI-ROUTE-YYYY-NNN
routing_version: ""
supersedes: null
recommendation_id: OI-REC-YYYY-NNN
recommendation_class: implementation|validation|monitoring|defer|halt
finding_refs: []
evidence_refs: []
package_registry_version: ""
package_eligibility: eligible|validation_required|blocked|not_applicable
route_state: routed|validation_required|deferred|blocked|not_routed|complete
primary_package_id: null
primary_package_name: null
routing_reason: ""
secondary_routes:
  - package_id: ""
    relationship: prerequisite|dependency|downstream|reference_only
    reason: ""
roadmap_phase: "Phase 0|Phase 1|Phase 2|Phase 3|Phase 4|Phase 5"
prerequisites: []
dependency_ids: []
unknowns: []
blocked_conditions: []
included_scope: []
excluded_scope: []
acceptance_criteria: []
acceptance_evidence_refs: []
confidence: high|medium|low|unknown
publication_state: internal_only|official|provisional|range_only|blocked
implementation_authorized: false
implementation_authorization_ref: null
review_state: ALLOW|REVIEW|HALT
approval_state: proposed|approved|deferred|blocked|rejected|complete
decision_owner: ""
decision_date: YYYY-MM-DD|null
ledger_refs: []
~~~

Required fields may not be replaced by narrative implication. Approval of the route selects planning ownership; it does not authorize implementation.

## 7. Routing admission rules

A recommendation may route to a canonical package only when package eligibility is eligible and:

- the source finding is governed and traceable
- evidence is admissible and current enough for the decision
- confidence is assigned separately from maturity
- the root condition is explicit
- exactly one canonical primary package directly fits the root condition
- the package ID and name match the registered package version
- scope is proportional to verified need
- prerequisites and dependencies are explicit
- roadmap phase rules are satisfied
- unknowns and blocked conditions are visible
- acceptance criteria are observable
- DecisionLedger references exist
- implementation authorization is recorded separately and defaults to false
- language is executive-safe

Failure of any material gate routes the recommendation to REVIEW, HALT, validation, deferment, or not_routed. Validation work must not be forced into a package.

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
Phase 5 — Optimization and Renewal
```

Phase 0 — Validation and Access is a pre-admission holding state, not a package implementation phase. Phase 5 may reuse an existing governed package for measured optimization or renewal; it does not create a new default package.

Routing rules:

1. Visible critical failures and foundational accuracy work precede expansion.
2. Offer, proof, service, and conversion foundations precede scaled acquisition work.
3. Undefined workflows must be documented before automation.
4. Metric definitions and source systems must exist before reporting implementation.
5. Workflow, data, privacy, review, escalation, logging, and QA controls must pass before Phase 4 AI work.
6. An unresolved `HALT` blocks all dependent routes.
7. Phase assignment may not be accelerated solely by priority score or client preference.
8. A Phase 0 validation state cannot carry implementation scope or implementation authorization.
9. Phase 5 requires measured evidence, a next-cycle decision, and approved new or renewed scope.

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
routing_id: OI-ROUTE-YYYY-NNN
routing_version: ""
supersedes: null
recommendation_id: OI-REC-YYYY-NNN
finding_refs: []
evidence_refs: []
package_registry_version: ""
package_eligibility: eligible|validation_required|blocked|not_applicable
route_state: routed|validation_required|deferred|blocked|not_routed|complete
primary_package_id: null
secondary_routes: []
roadmap_phase: ""
routing_reason: ""
confidence: high|medium|low|unknown
unknowns: []
blocked_conditions: []
publication_state: internal_only|official|provisional|range_only|blocked
implementation_authorized: false
implementation_authorization_ref: null
review_state: ALLOW|REVIEW|HALT
approval_state: proposed|approved|deferred|blocked|rejected|complete
decision_owner: ""
decision_date: YYYY-MM-DD
change_reason: ""
previous_route_ref: null
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
| `PKG-ROUTE-001` | A package-eligible recommendation lacks exactly one canonical primary package. |
| `PKG-ID-001` | Package ID or name conflicts with the canonical registry. |
| `PKG-VERSION-001` | Registry or route version is missing or cannot be resolved. |
| `PKG-AUTH-001` | Route approval is treated as implementation authorization. |
| `PKG-OWNER-001` | More than one package is marked primary. |
| `PKG-SCOPE-001` | Routed scope exceeds the verified root condition. |
| `PKG-PHASE-001` | Roadmap phase bypasses a required prerequisite. |
| `PKG-UNKNOWN-001` | Unknown evidence was treated as implementation evidence. |
| `PKG-TRACE-001` | Required evidence, finding, recommendation, or ledger trace is missing. |
| `PKG-DUP-001` | The same finding or deliverable is owned by multiple packages. |
| `PKG-COMPLETE-001` | Completion lacks acceptance evidence. |

## 17. Blocking errors

The route must be blocked when:

- package eligibility is claimed but no canonical package fits
- a package-eligible recommendation has zero or multiple primary packages
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

~~~yaml
routing_id: OI-ROUTE-2026-001
routing_version: "1.0"
recommendation_id: OI-REC-2026-014
recommendation_class: implementation
finding_refs:
  - OI-FIND-SEO-002
evidence_refs:
  - OI-EV-2026-118
package_registry_version: "framework/recommendation-index.md@v0.1"
package_eligibility: eligible
route_state: routed
primary_package_id: OI-PKG-SEO-001
primary_package_name: Local SEO Expansion Pack
routing_reason: "The verified root condition is inconsistent local citation identity within the reviewed SEO scope."
secondary_routes: []
roadmap_phase: "Phase 2 — Growth Foundation"
prerequisites:
  - approved canonical business name, address, and phone record
unknowns: []
blocked_conditions: []
included_scope:
  - reconcile the approved citation identity across the defined directory sample
  - retain completion evidence for corrected records
excluded_scope:
  - unrelated website redesign
  - paid acquisition
acceptance_criteria:
  - "Every directory in the approved sample matches the canonical business identity record."
confidence: high
publication_state: provisional
implementation_authorized: false
implementation_authorization_ref: null
review_state: ALLOW
approval_state: approved
~~~

This route matches scoring/examples/seo-worked-example.md. Route approval establishes package ownership and roadmap placement only; implementation remains unauthorized.

The AI readiness regression fixture demonstrates the complementary rule: material unknown privacy and escalation controls remain in Phase 0 with no primary package and implementation_authorized: false.

## 20. Governance checklist

Before approving a package route, confirm:

- [ ] Source evidence and finding are traceable.
- [ ] Root condition is explicit.
- [ ] Package eligibility is explicit.
- [ ] Exactly one canonical primary package is assigned when eligible.
- [ ] Validation, monitoring, halt, or blocked work may remain unrouted without package pressure.
- [ ] Secondary packages have defined relationships.
- [ ] Scope is proportional and non-duplicative.
- [ ] Unknowns and blocked conditions are visible.
- [ ] Roadmap prerequisites are satisfied.
- [ ] Acceptance criteria are observable.
- [ ] Unsupported outcome claims are absent.
- [ ] Route approval and implementation authorization are separate.
- [ ] implementation_authorized defaults to false.
- [ ] DecisionLedger record is complete.

## 21. Cross references

- `framework/recommendation-index.md`
- `framework/lifecycle-roadmap-map.md`
- `framework/governance-gate-index.md`
- `framework/findings/`
- `scoring/recommendation-map.md`
- `scoring/examples/seo-worked-example.md`
- `scoring/examples/ai-readiness-worked-example.md`
- `standards/evidence-standard.md`
- `standards/confidence-standard.md`
- `standards/publication-standard.md`
- `standards/recommendation-standard.md`
- `standards/roadmap-standard.md`
- `standards/decision-ledger-standard.md`
- `standards/quality-control-standard.md`
- `scoring/category-sheets/`
