# Confidence Standard

Version: v0.1 governance foundation  
Stage alignment: Stage 4 — `standards/`  
Folder alignment: `standards/`  
Status: Draft foundation for commercial v1.0

## 1. Purpose

This standard governs confidence assignment across Operator Intelligence criteria, categories, findings, recommendations, publication states, and DecisionLedger records.

Confidence describes how strongly admissible evidence supports an interpretation. It does not describe business performance and must never alter the underlying maturity score.

## 2. Core rules

1. Confidence and maturity are separate fields.
2. Confidence must derive from admissible evidence, not evaluator intuition.
3. Low confidence does not reduce a maturity score.
4. Strong evidence does not increase a maturity score.
5. `unknown` is not a weaker form of `low`; it means no defensible score can be selected.
6. Missing access is `unknown` or `blocked`, never negative evidence by default.
7. Public absence may prove non-visibility on tested surfaces, not internal nonexistence.
8. Confidence affects uncertainty, assertion strength, validation priority, and publication state.
9. Findings and recommendations require an explicit confidence assignment.
10. High-impact, low-confidence conditions route to validation, `REVIEW`, or `HALT`, not automatic implementation.

## 3. Approved confidence levels

| Level | Use when | Prohibited use |
|---|---|---|
| `high` | Direct, current, attributable evidence covers required scope with no material conflict | Assigning high confidence from one narrow screenshot, unsupported client claim, or tool presence |
| `medium` | Multiple consistent records or observations support the pattern, but one material gap remains | Treating medium confidence as complete verification |
| `low` | Evidence is indirect, narrow, stale, interview-led, partially accessible, or materially incomplete | Converting uncertainty into a negative score |
| `unknown` | Evidence cannot support a defensible score or interpretation | Assigning a numeric score and calling it unknown |

`blocked` is a criterion state, not a confidence level. A blocked criterion normally carries `confidence: unknown` plus a documented blocking condition.

## 4. Confidence dimensions

Evaluate all applicable dimensions before assigning confidence:

- directness
- source integrity
- recency
- scope coverage
- test completeness
- source agreement
- applicability certainty
- internal-record reliability
- sample adequacy
- competitor comparability where relevant

A material weakness in any required dimension may cap confidence below `high`.

## 5. Assignment rules

### High

Assign `high` only when:

- evidence is admissible under `standards/evidence-standard.md`
- required evaluation scope is complete
- source authority and recency are appropriate
- relevant tests were completed when testing is required
- no unresolved material conflict exists
- the observation can be independently reviewed

### Medium

Assign `medium` when the condition is supported but one material limitation remains, such as:

- incomplete internal validation
- partial sample coverage
- one unresolved but bounded source discrepancy
- direct public evidence without full operating context
- useful but variable search or competitor evidence

### Low

Assign `low` when the interpretation depends materially on:

- client recollection
- a narrow sample
- stale evidence
- indirect inference
- incomplete system access
- uncertain applicability
- unverified process claims

Low-confidence evidence may support a bounded finding only when its limitations are explicit and the business impact is phrased cautiously.

### Unknown

Assign `unknown` when:

- no maturity anchor can be defended
- evidence is absent, rejected, or materially conflicting
- absence cannot be distinguished from inaccessibility
- authorization prevents required review or testing
- the criterion state is `unknown` or `blocked`

## 6. Evidence-strength mapping

Evidence strength informs but does not mechanically determine confidence.

| Evidence condition | Normal confidence ceiling |
|---|---|
| Direct system access, current complete records, authorized safe test | High |
| Multiple corroborating screenshots, partial export, verified interview | Medium |
| Single screenshot, uncorroborated interview, stale or incomplete record | Low |
| Unsupported assumption, vendor claim, missing access interpreted as failure | Unknown; reject scoring use |

Exceptions require a documented rationale and reviewer approval.

## 7. Mixed and conflicting evidence

When evidence differs:

1. retain all material records
2. identify the conflict
3. prefer the most authoritative, current, and direct source
4. record unresolved limitations
5. lower confidence when the conflict could change the selected anchor or finding
6. route high-materiality unresolved conflicts to `REVIEW` or `HALT`

Do not average contradictory evidence into false certainty.

## 8. Confidence and scoring

A criterion score uses only approved maturity anchors. Confidence is stored separately.

```yaml
criterion_id: OI-EXAMPLE-001
criterion_state: scored
score: 50
confidence: medium
evidence_refs:
  - OI-EV-2026-001
limitations:
  - "One internal validation source remains unavailable."
```

Prohibited:

```text
Adjusted maturity score = maturity score × confidence factor
```

Confidence factors may be used only for confidence indexes and uncertainty calculations defined in `scoring/confidence-adjusted-scoring.md`.

## 9. Findings and recommendations

A finding requires confidence that reflects the evidence supporting the observation and interpretation.

| Finding confidence | Allowed treatment |
|---|---|
| High | May support direct report language and package routing when all other gates pass |
| Medium | May support bounded report language and package routing with disclosed validation needs |
| Low | Normally routes to validation first; implementation routing requires documented rationale and low-risk scope |
| Unknown | Cannot support a finding or recommendation |

A recommendation may not have stronger confidence than its underlying finding and evidence chain.

## 10. Publication effects

Confidence affects publication, not maturity.

| Condition | Publication effect |
|---|---|
| Strong coverage and confidence, no material unknowns | `official` may be allowed |
| Adequate coverage with disclosed confidence limitations | `provisional` may be allowed |
| Material low-confidence or unknown conditions widen interpretation | `range_only` |
| Evidence conflict, authorization failure, or control boundary prevents defensible output | `blocked` |

Threshold calculations remain governed by `scoring/confidence-adjusted-scoring.md` and the calculator specification.

## 11. Executive-safe language

Use:

- `verified with high confidence`
- `supported by the reviewed sample`
- `partially confirmed`
- `confidence is limited by unavailable internal records`
- `validation is required before implementation`
- `not visible on tested public surfaces`

Avoid:

- `definitely`
- `always`
- `never`
- `proven` when evidence is incomplete
- `losing leads`, `losing revenue`, or quantified impact without direct evidence
- presenting low-confidence interpretation as established fact

## 12. DecisionLedger requirements

Every material score, finding, recommendation, or publication decision must retain:

```yaml
confidence: high|medium|low|unknown
confidence_basis: ""
evidence_refs: []
limitations: []
validation_required: []
publication_effect: none|provisional|range_only|blocked
review_state: ALLOW|REVIEW|HALT
reviewed_by: ""
ledger_ref: OI-DL-YYYY-NNN
```

Confidence changes after evidence review must create or update an auditable ledger decision. Do not silently overwrite a published confidence assignment.

## 13. Validation rules

### Blocking errors

- `CONF-EVID-001`: confidence lacks admissible evidence references
- `CONF-SCORE-001`: confidence was used to alter maturity score
- `CONF-UNKNOWN-001`: unknown or blocked criterion received a numeric score
- `CONF-PUB-001`: publication state conflicts with material confidence limitations
- `CONF-DL-001`: material confidence decision lacks DecisionLedger traceability
- `CONF-CONFLICT-001`: unresolved material evidence conflict was omitted

### Warnings

- `CONF-SAMPLE-001`: confidence depends on a narrow sample
- `CONF-STALE-001`: source recency may not support current-state language
- `CONF-INTERVIEW-001`: conclusion depends materially on uncorroborated interview evidence
- `CONF-COVER-001`: high confidence is reported despite incomplete category coverage
- `CONF-ROUTE-001`: low-confidence finding is routed directly to implementation

## 14. Worked examples

### Visible public condition

A warranty statement is absent from all required tested pages.

```yaml
score: 0
confidence: high
observation: "No warranty statement was visible on the tested homepage, service pages, or contact page."
limitation: "This does not establish that no internal warranty exists."
```

### Internal process without access

The evaluator cannot inspect lead-assignment rules.

```yaml
criterion_state: unknown
score: null
confidence: unknown
validation_required:
  - "Review CRM assignment rules or approved workflow documentation."
```

### Interview-led workflow finding

The owner reports that estimate follow-up depends on memory, but records were not supplied.

```yaml
score: 25
confidence: low
publication_effect: provisional
validation_required:
  - "Review recent estimate records and follow-up task history."
```

## 15. Completion checklist

Before finalizing confidence, confirm:

- evidence is admissible and referenced
- confidence is separate from maturity
- required scope and sample are documented
- unknown and blocked states remain unscored
- public absence is not used to infer internal absence
- evidence conflicts are retained and resolved or disclosed
- low-confidence, high-impact conditions route to validation
- report language matches confidence strength
- publication state reflects material uncertainty
- DecisionLedger traceability is complete

## 16. v1.0 connection

This standard creates one repository-wide confidence grammar for scoring, findings, recommendation routing, publication controls, and executive reporting. It reduces evaluator drift while preserving honest uncertainty and auditable decisions required for commercial v1.0.