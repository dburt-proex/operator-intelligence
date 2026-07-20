# Executive Report Layout Specification

Version: v1.0 commercial asset specification  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Canonical report-production layout

## 1. Purpose

Define the page, section, component, and export structure for Operator Intelligence executive and contractor reports.

The layout must preserve the source hierarchy in `templates/executive-report.md` and cannot omit required release, uncertainty, or authorization information for visual simplicity.

## 2. Document formats

Supported:

- screen-first PDF
- print-safe letter and A4 PDF
- presentation-style delivery view
- accessible HTML report using the same content hierarchy

Every format uses the same artifact ID, version, methodology, evidence snapshot, QC, publication, and authorization state.

## 3. Executive report sequence

1. Cover and confidentiality
2. Release-control page
3. Executive conclusion
4. Operator Score and uncertainty
5. Verified strengths
6. Priority constraints
7. Category assessment
8. Recommendation register
9. Roadmap
10. Package decision
11. Executive decision memo
12. Scope, evidence, and method notes
13. Completion/outcome boundary
14. Appendix: evidence, finding, recommendation, and ledger references

## 4. Page architecture

### Cover

- product and report title
- client, date, report ID/version
- publication-state label
- minimal brand mark
- synthetic/confidential marker where applicable

No score appears on the cover unless publication state permits it and the state label is equally prominent.

### Release-control page

Use a full-width structured panel with:

- method and evidence versions
- score type
- coverage and confidence
- QC/publication refs
- implementation authorization
- material limitations and blockers

### Executive pages

Use one dominant conclusion per page/section. Supporting evidence, state, and decision remain adjacent.

### Detail pages

Use stable left-to-right hierarchy:

```text
Identity / State
→ Observation / Result
→ Evidence / Calculation
→ Interpretation / Impact
→ Decision / Next gate
```

## 5. Grid

- 12-column responsive grid for digital layouts
- 6-column equivalent for print spreads
- maximum body line length optimized for reading
- primary narrative width 7–8 columns
- metadata/evidence rail 3–4 columns
- full-width tables only when necessary

Avoid two-column body text for dense technical sections.

## 6. Header and footer

Header may contain report title and section. Footer must contain:

- report ID/version
- publication state
- confidentiality/synthetic label
- page number

Blocked/internal-only artifacts repeat the state on every page.

## 7. Section components

### Executive conclusion panel

- conclusion
- confidence/limitation
- recommended decision
- next gate

### Score panel

Uses `operator-score-gauge.md` without modification.

### Finding panel

- ID/title
- observation
- impact
- confidence
- evidence refs
- limitation

### Recommendation panel

- ID/class
- action
- priority and confidence separately
- eligibility/package/phase
- owner
- acceptance evidence
- authorization state

### Roadmap panel

Uses `roadmap-visual-spec.md`; Phase 0 is visually distinct from implementation phases.

### Decision memo panel

- requested decision
- recommendation
- rationale/evidence
- conditions
- owner/authority
- ledger ref

## 8. Tables

- repeat header rows across pages
- no more than 8–10 essential columns in client view
- move technical identifiers to appendix or evidence rail when necessary
- never remove state, confidence, eligibility, phase, or authorization to reduce width
- unknown and blocked values use text labels

## 9. Executive versus contractor report

The contractor report may reduce narrative density and technical schema detail, but must preserve:

- release controls
- score state/range/coverage/confidence
- findings and unknowns
- package eligibility and phases
- implementation authorization state
- outcome boundary

Both reports derive from the same governed source objects.

## 10. Export QA

- page breaks do not separate a state label from its score or decision
- tables remain readable without clipping
- evidence IDs and hyperlinks remain functional where supported
- diagrams include captions and textual summaries
- fonts are embedded or safely substituted
- no confidential evidence appears in unintended appendices
- publication-state watermark/banner is retained
- screen and print versions use the same values

## 11. Prohibited layout behavior

- burying limitations after recommendations
- placing a package sales card before evidence/findings
- presenting Phase 0 as percentage implementation complete
- using a full-page score without publication state
- visually minimizing HALT or blocked conditions
- omitting IDs and traceability from the appendix
- inserting decorative ROI or revenue-leakage graphics without validated data

## 12. Commercial v1.0 connection

This specification converts the canonical report templates into consistent executive-ready output while preserving every material control.

## 13. References

- `assets/design-system.md`
- `assets/operator-score-gauge.md`
- `assets/roadmap-visual-spec.md`
- `templates/executive-report.md`
- `templates/contractor-report.md`