# Northstar Painting Co. — Synthetic Operator Scorecard

Version: v1.0 regression score run  
Stage alignment: Stage 7 — `examples/`  
Status: Provisional synthetic result

## 1. Score run control

```yaml
score_run_id: OI-SCORE-2026-EX001
assessment_id: OI-ASSESS-2026-EX001
methodology_version: commercial-v1.0
weight_profile: default
criterion_corpus: 140
active_category_weight_percent: 100
evidence_snapshot_date: 2026-07-20
publication_state: provisional
implementation_authorized: false
ledger_ref: OI-DL-2026-EX003
```

## 2. Category results

| Category | Weight | Observed score | Coverage | Confidence | Confidence factor | Lower bound | Upper bound | State |
|---|---:|---:|---:|---|---:|---:|---:|---|
| Website structure and UX | 10% | 60 | 100% | medium | 0.75 | 47.5 | 72.5 | scored |
| Messaging and offer clarity | 10% | 55 | 100% | medium | 0.75 | 42.5 | 67.5 | scored |
| Conversion infrastructure | 15% | 50 | 100% | high | 1.00 | 50.0 | 50.0 | scored |
| Local SEO | 15% | 45 | 90% | medium | 0.75 | 29.25 | 61.75 | scored with unknown weight |
| Google Business Profile | 10% | 65 | 100% | high | 1.00 | 65.0 | 65.0 | scored |
| Reputation and trust | 10% | 58 | 90% | medium | 0.75 | 40.95 | 73.45 | scored with unknown weight |
| Social presence | 5% | unknown | 0% | unknown | 0.00 | 0.0 | 100.0 | unknown |
| Automation maturity | 10% | 35 | 80% | low | 0.50 | 8.0 | 68.0 | scored with blocked weight |
| AI readiness | 5% | 25 | 60% | low | 0.50 | 0.0 | 70.0 | scored; implementation blocked |
| Analytics and reporting | 5% | 40 | 80% | low | 0.50 | 12.0 | 72.0 | scored with unknown weight |
| Competitive position | 5% | 50 | 80% | medium | 0.75 | 30.0 | 70.0 | scored with limited sample |

## 3. Reproducible calculations

### Weighted evidence coverage

```text
(10×1.00) + (10×1.00) + (15×1.00) + (15×0.90)
+ (10×1.00) + (10×0.90) + (5×0.00) + (10×0.80)
+ (5×0.60) + (5×0.80) + (5×0.80)
= 86.5

Weighted Evidence Coverage = 86.5%
```

### Observed normalized Operator Score

The unknown social category is excluded from the observed-score denominator but remains inside evidence coverage and uncertainty bounds.

```text
(60×10) + (55×10) + (50×15) + (45×15) + (65×10)
+ (58×10) + (35×10) + (25×5) + (40×5) + (50×5)
= 4,730

Included observed category weight = 95

4,730 ÷ 95 = 49.789...
Displayed provisional indicator = 50
```

### Operator confidence index

```text
[(10×1.00×0.75) + (10×1.00×0.75) + (15×1.00×1.00)
+ (15×0.90×0.75) + (10×1.00×1.00) + (10×0.90×0.75)
+ (5×0.00×0.00) + (10×0.80×0.50) + (5×0.60×0.50)
+ (5×0.80×0.50) + (5×0.80×0.75)] ÷ 86.5
= 67.375 ÷ 86.5
= 0.7789

Operator Confidence Index = 0.779
```

### Operator uncertainty range

```text
Weighted lower bound = 34.3825
Weighted upper bound = 67.0075
Displayed range = 34–67
```

## 4. Publication decision

```yaml
observed_indicator: 50
operator_lower_bound: 34
operator_upper_bound: 67
weighted_evidence_coverage: 0.865
operator_confidence_index: 0.779
publication_state: provisional
publication_reason:
  - coverage and confidence exceed official numeric thresholds
  - social category remains fully unknown
  - automation, analytics, and AI evidence use limited internal samples
  - AI control blockers materially limit implementation conclusions
score_label: Provisional Operator Score indicator
```

The point indicator is not labeled an official Operator Score. The range, coverage, confidence, limitations, and validation priorities must accompany it.

## 5. Validation messages

| Code | Severity | Condition | Effect |
|---|---|---|---|
| `OI-VAL-2026-EX001` | warning | Social evidence unavailable | Category unknown; broadens range |
| `OI-VAL-2026-EX002` | warning | Form ownership and SLA not verified | Limits automation confidence |
| `OI-VAL-2026-EX003` | error for implementation | AI privacy/escalation/logging/QA controls incomplete | HALT AI package eligibility |
| `OI-VAL-2026-EX004` | warning | Competitive sample is narrow and synthetic | Limits assertion strength |

## 6. Invariants verified

- active category weights total 100%
- unknown is not zero
- blocked behaves as uncertainty plus a governance flag
- confidence does not modify maturity
- observed score and evidence coverage are separate
- the social unknown remains visible
- no score publication decision authorizes implementation
- synthetic data is clearly labeled

## 7. Commercial v1.0 connection

This fixture demonstrates reproducible multi-category scoring, partial coverage, confidence-adjusted uncertainty, a provisional publication decision, and a material implementation block.