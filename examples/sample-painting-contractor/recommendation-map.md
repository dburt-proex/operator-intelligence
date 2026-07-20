# Northstar Painting Co. — Synthetic Recommendation Map

Version: v1.0 sample recommendation set  
Stage alignment: Stage 7 — `examples/`  
Status: Synthetic governed recommendations

## 1. Register control

```yaml
assessment_id: OI-ASSESS-2026-EX001
register_version: "1.0"
methodology_version: commercial-v1.0
publication_state: provisional
implementation_authorized: false
ledger_ref: OI-DL-2026-EX010
```

## 2. Priority formula

```text
Priority Score = ((Impact × 0.40) + (Evidence Strength × 0.20) + (Effort Inverse × 0.15) + (Strategic Fit × 0.25)) × 20
```

Confidence remains a separate gate and does not modify priority.

## 3. Recommendation register

| Recommendation ID | Class | Finding refs | Action | Confidence | Impact | Evidence strength | Effort inverse | Strategic fit | Priority | Eligibility | Primary package | Phase | State |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|
| `OI-REC-2026-EX001` | implementation | CONV-EX001 | Add painting-specific project qualification and test the estimate path | high | 4 | 5 | 4 | 5 | 89 | eligible | `OI-PKG-WEB-001` | 1 | proposed |
| `OI-REC-2026-EX002` | implementation | SEO-EX001 | Create a verified cabinet-painting service path with internal links and approved CTA | high | 3 | 5 | 3 | 4 | 73 | eligible | `OI-PKG-SEO-001` | 2 | proposed |
| `OI-REC-2026-EX003` | implementation | TRUST-EX001 | Add service, scope, location, and result context to approved project proof | medium | 3 | 4 | 4 | 4 | 72 | eligible | `OI-PKG-TRUST-001` | 2 | proposed |
| `OI-REC-2026-EX004` | validation | AUTO-EX001 | Map inquiry routing, ownership, stages, next-action rules, follow-up cadence, and exceptions | medium | 5 | 3 | 4 | 5 | 89 | validation_required | None | 0 | validation_required |
| `OI-REC-2026-EX005` | validation | ANALYTICS-EX001 | Define source, service, estimate, job-outcome, owner, and reconciliation requirements | medium | 3 | 3 | 3 | 4 | 65 | validation_required | None | 0 | validation_required |

## 4. Recommendation details

### `OI-REC-2026-EX001` — Improve painting estimate qualification

**Observed condition:** The working estimate form collects contact details but not structured project context.

**Action:** Add only the project fields the team confirms it uses: service type, property type, approximate scope, desired timing, surface/repair context, and optional photos. Test mobile completion, validation, confirmation, and safe routing.

**Included scope**

- approved form fields and labels
- mobile/desktop form behavior
- confirmation message
- bounded routing test
- event requirement for successful submission

**Excluded scope**

- CRM redesign
- automated pricing
- conversion-rate guarantee
- AI assessment of photos

**Eligibility:** eligible  
**Primary package:** `OI-PKG-WEB-001` Website Conversion Fix Pack  
**Dependencies:** Phase 0 must identify the form owner and approved routing destination before live release.  
**Acceptance evidence:** screenshots, test submission, routing receipt, approved field map.  
**Authorization:** false; separate proposal and start authorization required.  
**Ledger:** `OI-DL-2026-EX011`

### `OI-REC-2026-EX002` — Build the verified cabinet-painting service path

**Action:** Create one cabinet-painting service page grounded in the verified service inventory, approved process, authentic project proof, service area, and estimate CTA.

**Included scope:** page brief/copy, metadata, heading structure, internal links, proof and CTA placement.  
**Excluded scope:** ranking guarantee, unsupported warranty/durability claims, fabricated local pages.  
**Eligibility:** eligible  
**Primary package:** `OI-PKG-SEO-001` Local SEO Expansion Pack  
**Phase:** 2  
**Acceptance evidence:** published URL, link checks, indexability review, claim approval.  
**Ledger:** `OI-DL-2026-EX012`

### `OI-REC-2026-EX003` — Structure painting project proof

**Action:** Add service type, project scope, approved location context, problem/process/result description, and permission record to selected project examples.

**Included scope:** proof inventory, context fields, placement map for cabinet/interior/exterior pages.  
**Excluded scope:** fabricated outcomes, unsupported customer claims, new photography.  
**Eligibility:** eligible  
**Primary package:** `OI-PKG-TRUST-001` Trust Proof System  
**Dependency:** Cabinet proof placement follows the approved cabinet page structure.  
**Phase:** 2  
**Acceptance evidence:** source-to-placement register and published examples.  
**Ledger:** `OI-DL-2026-EX013`

### `OI-REC-2026-EX004` — Validate lead ownership and follow-up workflow

**Action:** Document intake sources, routing destination, owner, stages, required fields, next-action rules, follow-up cadence, lost reasons, exceptions, and escalation.

**Class:** validation  
**Eligibility:** validation_required  
**Primary package:** None  
**Phase:** 0  
**Decision enabled:** determine whether `OI-PKG-CRM-001` is eligible and define its bounded scope.  
**Acceptance evidence:** approved current-state workflow, field/stage dictionary, owner matrix, controlled test plan.  
**Authorization:** false; validation is not implementation.  
**Ledger:** `OI-DL-2026-EX014`

### `OI-REC-2026-EX005` — Validate measurement and reconciliation requirements

**Action:** Define each decision metric, source, field, owner, baseline state, reconciliation method, review cadence, and limitation.

**Class:** validation  
**Eligibility:** validation_required  
**Primary package:** None  
**Phase:** 0  
**Dependencies:** lead workflow and source fields from EX004.  
**Decision enabled:** determine whether `OI-PKG-DASH-001` is eligible.  
**Acceptance evidence:** approved metric dictionary and source map.  
**Ledger:** `OI-DL-2026-EX015`

## 5. Blocked route

```yaml
condition: AI-assisted painting intake
package_candidate: OI-PKG-AI-001
package_eligibility: blocked
primary_package_id: null
roadmap_phase: 0
control_gate: HALT
reason: privacy, retention, escalation, logging, human-review, and QA controls are incomplete
implementation_authorized: false
validation_ref: OI-BLK-2026-EX002
ledger_ref: OI-DL-2026-EX016
```

This is a blocked route, not a sellable package recommendation.

## 6. Routing checks

- [x] Every recommendation traces to a governed finding.
- [x] Priority inputs reproduce.
- [x] Confidence remains separate.
- [x] Exactly one primary package exists only for eligible work.
- [x] Validation work remains unrouted in Phase 0.
- [x] Dependencies and exclusions are explicit.
- [x] AI implementation is halted.
- [x] No recommendation claims guaranteed financial or demand outcomes.
- [x] Implementation authorization remains false.

## 7. Commercial v1.0 connection

This fixture demonstrates package eligibility, primary ownership, validation-first routing, canonical priority, and a blocked AI route in one coherent recommendation set.