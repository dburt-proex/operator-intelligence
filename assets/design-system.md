# Operator Intelligence Design System

Version: v1.0 commercial asset specification  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Production visual-system authority

## 1. Purpose

Define the reusable visual language for Operator Intelligence reports, scorecards, roadmaps, diagrams, proposals, and supporting materials.

The design system must improve comprehension, hierarchy, traceability, and executive usability. It must never hide uncertainty, compress material limitations, or visually elevate a recommendation beyond its evidence or authorization state.

## 2. Design principles

1. Evidence before decoration.
2. Decision hierarchy before visual novelty.
3. One visual meaning per token.
4. Text and symbols accompany every color-coded state.
5. Uncertainty is visible, not minimized.
6. Tables and diagrams preserve source IDs and control states.
7. Client-safe language remains primary; visual emphasis cannot create unsupported claims.
8. Printed, exported, and screen versions must remain legible.

## 3. Core palette

| Token | Hex | Use |
|---|---|---|
| `oi-ink` | `#111318` | Primary text, dark surfaces |
| `oi-paper` | `#F7F6F2` | Primary light background |
| `oi-white` | `#FFFFFF` | Cards and negative space |
| `oi-silver-700` | `#555B66` | Secondary text |
| `oi-silver-400` | `#AEB4BE` | Borders, inactive structure |
| `oi-silver-150` | `#E4E7EB` | Dividers and table bands |
| `oi-gold` | `#B18A42` | Brand accent and selected emphasis |
| `oi-blueprint` | `#335C81` | System maps, reference paths, neutral data emphasis |
| `oi-allow` | `#2F6B4F` | ALLOW state |
| `oi-review` | `#94651B` | REVIEW state |
| `oi-halt` | `#982F34` | HALT or blocking state |
| `oi-unknown` | `#666F7D` | Unknown or unavailable state |

Rules:

- Gold is brand emphasis, not a success signal.
- ALLOW, REVIEW, HALT, and unknown always include the state word or icon.
- Score magnitude and gate state use different encodings.
- Background/text combinations must maintain strong legibility in screen and print output.

## 4. Typography roles

| Role | Use |
|---|---|
| Display | Cover title, section dividers, major score label |
| Heading 1 | Primary report sections |
| Heading 2 | Subsystems, categories, or decisions |
| Heading 3 | Finding/recommendation detail |
| Body | Client narrative and interpretation |
| Data | Tables, scores, IDs, dates, calculations |
| Caption | Source, limitation, publication, or evidence notes |

Rules:

- Use no more than two type families in one artifact.
- Use tabular numerals for scores, coverage, bounds, and IDs when available.
- Minimum body size must remain readable in exported PDF and printed letter/A4 output.
- Do not use condensed or decorative fonts for evidence, limitations, or tables.

## 5. Spacing and layout tokens

Base spacing unit: `4`.

| Token | Size | Use |
|---|---:|---|
| `space-1` | 4 | Tight metadata grouping |
| `space-2` | 8 | Table/cell padding |
| `space-3` | 12 | Card internals |
| `space-4` | 16 | Standard component gap |
| `space-6` | 24 | Section subgroup |
| `space-8` | 32 | Major content transition |
| `space-12` | 48 | Section opening |
| `space-16` | 64 | Cover or divider spacing |

Use a consistent grid and generous margins. Dense tables may reduce horizontal padding but not body legibility.

## 6. Component system

### 6.1 Release-control banner

Required fields:

- artifact ID and version
- methodology version
- evidence snapshot
- publication state
- QC state/ref
- implementation authorization state

Blocked or internal-only artifacts display the state at the top of every distributed page or screen.

### 6.2 Decision card

Structure:

```text
Decision / Gate
Rationale
Evidence refs
Confidence and limitations
Owner / Authority
Next gate
```

### 6.3 Finding card

- Finding ID and title
- observation
- evidence refs
- interpretation
- business impact
- confidence
- limitation/unknown
- report-use state

Do not embed the recommendation in the finding title.

### 6.4 Recommendation card

- recommendation ID/class
- source finding refs
- action
- priority and confidence shown separately
- package eligibility
- primary package only when eligible
- phase
- authorization state
- acceptance evidence

### 6.5 Status chip

Allowed labels:

- `ALLOW`
- `REVIEW`
- `HALT`
- `UNKNOWN`
- `OFFICIAL`
- `PROVISIONAL`
- `RANGE ONLY`
- `BLOCKED`
- `INTERNAL ONLY`

A chip never replaces the full decision rationale.

### 6.6 Evidence reference

Use compact resolvable labels such as `OI-EV-2026-014`. Hover/footnote/detail view may show source, date, and scope. Never expose credentials or sensitive source locations.

## 7. Data visualization rules

- Show units, denominator, time period, source, and definition.
- Use direct labels rather than legend-only interpretation where possible.
- Show unknown and blocked values as distinct states, not zero-length bars.
- Display uncertainty ranges where material.
- Do not truncate axes to exaggerate small differences.
- Do not use decorative 3D charts.
- Do not visualize synthetic examples as real client data.
- Do not visualize modeled ROI as realized value.

## 8. Score visual rules

- The Operator Score visual must include publication state.
- Official, provisional, range-only, blocked, and internal-only use different structures, not merely colors.
- A provisional score shows the point indicator plus range, evidence coverage, and confidence.
- A range-only result emphasizes the range and validation requirements; no central score is visually dominant.
- A blocked result displays `NOT PUBLISHABLE` or `BLOCKED`, not a gauge needle.
- Category unknowns remain visible in the scorecard.

## 9. Accessibility and resilience

- Meaning cannot depend on color alone.
- Provide text equivalents for icons and diagrams.
- Preserve logical reading order.
- Use sufficient contrast and spacing.
- Tables include headers and avoid merged-cell ambiguity where possible.
- PDF exports include selectable text and bookmarks when supported.
- Diagrams include a textual description and source IDs.
- Monochrome printing must preserve states through labels, patterns, and borders.

## 10. Asset governance

```yaml
asset_id: OI-ASSET-YYYY-NNN
asset_type: component|layout|diagram|icon|chart|template
version: ""
source_authority: ""
intended_artifacts: []
publication_states_supported: []
accessibility_review: pass|review|fail
governance_review: ALLOW|REVIEW|HALT
owner: ""
ledger_ref: null
```

Material visual changes affecting interpretation, score state, gate state, or authorization require review and supersession.

## 11. Prohibited design patterns

- visualizing an unofficial score as definitive
- hiding limitations in low-contrast footnotes
- using green to imply realized business value
- merging priority and confidence into one color
- displaying an ineligible package as a recommended product
- representing Phase 0 as implementation progress
- labeling proposal acceptance as “project started”
- using alarmist revenue-leakage graphics without validated amounts
- decorative complexity that obscures source IDs or ownership

## 12. Commercial v1.0 connection

This specification turns the completed methodology into a consistent premium consulting-report system while preserving evidence, uncertainty, gates, and authority boundaries.

## 13. References

- `assets/operator-score-gauge.md`
- `assets/report-layout.md`
- `standards/publication-standard.md`
- `templates/executive-report.md`