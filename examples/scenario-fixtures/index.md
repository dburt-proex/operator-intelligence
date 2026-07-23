# Operator Intelligence Scenario Fixture Index

Version: v0.2 post-v1 assurance suite  
Folder alignment: `examples/scenario-fixtures/`  
Status: Governed regression-fixture registry

## Purpose

Register compact engagement scenarios that prove Operator Intelligence preserves evidence, scoring, routing, authorization, publication, and realized-value controls under non-happy-path conditions.

## Fixture contract

Each fixture directory contains exactly four governed records:

```text
scenario-brief.md
input-records.md
expected-decision.md
validation-record.md
```

The top-level companion Markdown file remains a concise human-readable scenario summary. Fixtures are synthetic, contain no client data, do not alter canonical scoring, and must produce deterministic control outcomes.

| Fixture ID | Directory | Primary control under test | Expected result |
|---|---|---|---|
| OI-FIX-001 | `unknown-heavy/` | Unknown is not zero; publication gating | `REVIEW`, Phase 0 validation |
| OI-FIX-002 | `conflicting-evidence/` | Contradictions remain visible | `REVIEW`, confidence constrained |
| OI-FIX-003 | `g4-control-boundary/` | G4 authority/privacy boundary | `HALT` |
| OI-FIX-004 | `package-ineligible/` | Package eligibility before assignment | `ALLOW` finding, no package |
| OI-FIX-005 | `low-confidence-high-impact/` | Impact does not erase uncertainty | `REVIEW`, validation first |
| OI-FIX-006 | `recommendation-declined/` | Client decision without history manipulation | `ALLOW` closure record |
| OI-FIX-007 | `completion-without-realized-value/` | Completion is not outcome proof | `ALLOW`, `not_measured` |
| OI-FIX-008 | `multi-location-scope/` | Scope and evidence ownership by location | `REVIEW` until separated |

## Validation rules

- Unknown and blocked states never carry numeric zeroes.
- Confidence never modifies performance.
- One weighted owner applies to every criterion.
- Findings cannot be invented to fit a scenario.
- Package assignment requires eligibility.
- Publication, proposal acceptance, and implementation authorization remain separate.
- Completion and realized value remain separate.
- Material decisions require DecisionLedger references.
- Every expected decision must be reproducible from the listed inputs and governing authorities.

## Usage

Use these fixtures as acceptance tests for future calculators, report assembly, registry validation, profile extensions, and evaluator calibration. The four-record fixture envelope is the test authority; the companion summary is orientation only.
