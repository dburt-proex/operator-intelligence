# Operator Score Gauge Specification

Version: v1.0 commercial asset specification  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Canonical Operator Score visual contract

## 1. Purpose

Define how the Operator Score, category results, evidence coverage, confidence, bounds, and publication state may be visualized.

The gauge is a decision-support component, not a decorative grade. It must not imply more precision, certainty, completeness, or authorization than the score object supports.

## 2. Required input object

```yaml
operator_score_id: OI-OS-YYYY-NNN
observed_score: 0-100|null
lower_bound: 0-100
upper_bound: 0-100
weighted_evidence_coverage: 0-1
operator_confidence_index: 0-1
maturity_tier: null|1|2|3|4|5
publication_state: official|provisional|range_only|blocked|internal_only
validation_messages: []
methodology_version: ""
evidence_snapshot_date: YYYY-MM-DD
qc_ref: null
ledger_ref: OI-DL-YYYY-NNN
```

The component must fail closed when required state fields are missing or inconsistent.

## 3. Publication-state variants

### 3.1 Official

Show:

- point score as the primary numeral
- maturity tier
- evidence coverage
- confidence index
- uncertainty range or exact-state indicator
- `OFFICIAL` label
- evidence snapshot and methodology version

Do not show official styling unless all publication gates pass.

### 3.2 Provisional

Show:

- `PROVISIONAL` label above or adjacent to the score
- point indicator with reduced visual dominance
- range as a visible band
- evidence coverage and confidence
- material validation messages or limitations

Use language such as `Provisional Operator Score indicator`, not `final score`.

### 3.3 Range only

Show:

- range as the primary visual
- no dominant needle or central point score
- `RANGE ONLY` label
- coverage, confidence, and validation priorities

A midpoint may not be implied through marker placement unless it is an approved observed indicator and remains secondary.

### 3.4 Blocked

Show:

```text
OPERATOR SCORE
BLOCKED / NOT PUBLISHABLE
```

Include the blocking validation codes and next gate. Do not render a needle, progress arc, tier, or numerical grade.

### 3.5 Internal only

Show a neutral internal-state banner and watermark. Do not use client-release styling.

## 4. Gauge geometry

Preferred form: horizontal bounded scale or semicircular gauge with an explicit uncertainty band.

Required visual layers:

1. full 0–100 scale
2. maturity-tier regions, labeled textually
3. lower-to-upper uncertainty band
4. observed score marker only when permitted
5. publication-state label
6. coverage and confidence metadata
7. validation marker when material

The uncertainty band must remain legible and cannot be replaced by a small footnote.

## 5. Maturity-tier treatment

Tier labels and thresholds resolve to `scoring/maturity-tiers.md`. The asset does not define or change thresholds.

Rules:

- show tier label and number together
- do not imply a tier when the range spans materially different tiers without qualification
- use `Tier uncertain across range` when required
- blocked results have no tier
- category maturity does not inherit Operator Score tier automatically

## 6. Category scorecard

Each category row includes:

| Field | Required |
|---|---|
| Category name | yes |
| Weight | yes |
| Score or state | yes |
| Evidence coverage | yes |
| Confidence | yes |
| Bounds | when material |
| Publication treatment | yes |
| Validation marker | when applicable |

Unknown and blocked categories use labeled state cells and full-width state markers, not score `0` bars.

## 7. Semantic separation

| Concept | Visual treatment |
|---|---|
| Performance/maturity | neutral magnitude scale |
| Confidence | labeled confidence indicator |
| Evidence coverage | separate percentage/bar |
| Uncertainty | lower–upper band |
| Gate state | ALLOW/REVIEW/HALT chip and text |
| Publication state | official/provisional/range-only/blocked banner |
| Priority | separate recommendation component, never gauge color |
| Authorization | separate status field |

Do not use one color or icon to communicate several concepts.

## 8. Required labels

At minimum:

```text
Operator Score state
Score / range / blocked state
Evidence coverage
Confidence index
Methodology version
Evidence snapshot
Publication state
```

For provisional/range-only/blocked results, include a visible `Why this state` link or note.

## 9. Validation behavior

The component must refuse or downgrade rendering when:

- weights do not total 100%
- observed score is outside 0–100
- lower bound exceeds upper bound
- confidence or coverage is outside 0–1
- publication state conflicts with score fields
- blocked state includes a published point score
- official state lacks required QC/publication refs
- methodology version or evidence snapshot is missing

## 10. Example states

### Synthetic provisional example

```yaml
observed_score: 50
lower_bound: 34
upper_bound: 67
weighted_evidence_coverage: 0.865
operator_confidence_index: 0.779
publication_state: provisional
```

Render:

```text
PROVISIONAL OPERATOR SCORE INDICATOR
50
Range 34–67
Evidence coverage 86.5%
Confidence 0.779
```

### Blocked example

```yaml
observed_score: null
lower_bound: 0
upper_bound: 100
publication_state: blocked
validation_messages: ["OI-VAL-AUTH-001"]
```

Render no numerical gauge.

## 11. Accessibility and export

- All visual information has text equivalents.
- The scale remains understandable in grayscale.
- The score marker, range band, and tier boundaries use shape/pattern differences.
- PDF output retains searchable labels and values.
- Screen-reader order presents publication state before score.

## 12. Prohibited states

- green score arc implying success or realized value
- score-only display without coverage/confidence/state
- hidden or unlabeled unknown categories
- official badge based solely on coverage
- point score for blocked state
- animated movement implying improvement where no comparison exists
- before/after score comparison without matched methodology and evidence scope

## 13. Commercial v1.0 connection

This specification makes the Operator Score visually usable and commercially credible without weakening uncertainty, publication, or governance controls.

## 14. References

- `framework/operator-score.md`
- `scoring/calculator-spec.md`
- `scoring/maturity-tiers.md`
- `scoring/completion-status.md`
- `assets/design-system.md`