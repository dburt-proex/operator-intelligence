# Governed Roadmap Visual Specification

Version: v1.0 commercial asset specification  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Canonical roadmap visualization contract

## 1. Purpose

Define how Phase 0 validation, phases 1–5, dependencies, package eligibility, ownership, gates, authorization, completion, and renewal are represented visually.

The visual must show decision sequence, not imply guaranteed timing or implementation progress.

## 2. Required input fields

```yaml
roadmap_id: OI-ROAD-YYYY-NNN
roadmap_version: ""
items:
  - item_id: OI-RM-YYYY-NNN
    recommendation_ref: null
    package_eligibility: eligible|validation_required|blocked|not_applicable
    primary_package_id: null
    roadmap_phase: 0|1|2|3|4|5
    dependencies: []
    owner: ""
    decision_authority: ""
    review_state: ALLOW|REVIEW|HALT
    implementation_authorized: false
    status: proposed|validation_required|approved|blocked|authorized|in_progress|complete|monitoring|deferred|rejected|cancelled
    acceptance_evidence: []
```

## 3. Phase architecture

| Phase | Label | Visual meaning |
|---:|---|---|
| 0 | Validation and Access | Evidence/authority/control work; never implementation progress |
| 1 | Quick Wins | Bounded verified correction |
| 2 | Growth Foundation | Service, local, trust, message, and conversion foundations |
| 3 | Automation and Reporting | Workflow, ownership, data, automation, and dashboards |
| 4 | Governed AI Enablement | AI only after readiness and control gates |
| 5 | Optimization and Renewal | Measurement, maintenance, renewal, optimization, or closure |

Phase 0 must use a distinct visual lane and cannot be merged into Phase 1.

## 4. Item card

Every card displays:

- item ID and action
- recommendation/validation ref
- package eligibility
- primary package or `None`
- owner
- review state
- authorization state
- status
- dependency marker
- acceptance-evidence indicator

Do not display a package logo/card for validation-required or blocked items.

## 5. Dependency visualization

- Use directional connectors from prerequisite to dependent item.
- Label dependency type: evidence, access, workflow, data, package, governance, approval, or measurement.
- HALT connectors use a stop boundary, not an arrow suggesting future progress.
- Avoid crossing connectors where a grouped dependency list is clearer.
- Priority rank does not change connector order.

## 6. Time representation

Permitted:

- planning window
- target review period
- dependency-driven order
- milestone or gate sequence

Prohibited unless contractually fixed:

- guaranteed completion date
- percentage complete based solely on elapsed time
- speed claims unsupported by capacity/access evidence

Use `Planning window` and include assumptions.

## 7. State treatment

| State | Required treatment |
|---|---|
| Validation required | Phase 0 lane, neutral/REVIEW styling, no progress percentage |
| Eligible / proposed | Package ID shown; no start indicator |
| Authorized | Authorization badge plus reference |
| In progress | Only after authorization passes |
| Complete | Acceptance-evidence marker required |
| Monitoring | Phase 5 or post-completion state |
| Blocked / HALT | Strong boundary and blocking reason |
| Deferred | Neutral paused state and re-entry condition |

Color is secondary to labels, borders, and icons.

## 8. Recommended views

### Executive roadmap

- six phase lanes
- 3–7 priority items
- major dependencies
- owner and gate
- no implementation detail overload

### Delivery roadmap

- full item register
- prerequisites, owners, authorization, acceptance evidence
- change-control and status information

### Package roadmap

Group by phase, not by product. Primary package appears as item metadata rather than the dominant visual hierarchy.

## 9. Validation rules

The visual must fail or flag REVIEW when:

- an eligible implementation item lacks a primary package
- validation/blocked work has a primary package
- an item is `in_progress` without authorization
- a Phase 4 item lacks readiness gate refs
- a complete item lacks acceptance evidence
- Phase 5 outcome claims lack measurement evidence
- a dependency target is missing
- roadmap version or ledger ref is absent

## 10. Prohibited patterns

- funnel graphics implying inevitable progression
- Phase 0 shown as implementation
- all items shown green because roadmap is approved
- package-first grouping that hides root condition
- progress percentages without defined denominator/evidence
- AI shown as the final automatic stage
- complete state without acceptance evidence
- renewal presented as mandatory upsell

## 11. Commercial v1.0 connection

This specification makes the implementation roadmap clear and sellable while preserving validation, dependency, authorization, and acceptance controls.

## 12. References

- `standards/roadmap-standard.md`
- `templates/roadmap.md`
- `assets/design-system.md`