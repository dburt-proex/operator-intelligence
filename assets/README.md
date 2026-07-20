# Operator Intelligence Asset Registry

Version: v1.0 commercial asset registry  
Stage alignment: Stage 9 — `assets/`  
Folder alignment: `assets/`  
Status: Canonical production-asset index

## 1. Purpose

Register the visual, report, score, roadmap, diagram, and brand specifications required for commercial v1.0 output.

These files define asset behavior and governance. Production implementations may use PDF, HTML, presentation, or design tools only when they preserve these contracts.

## 2. Registry

| Asset specification | Governed purpose |
|---|---|
| `design-system.md` | Palette, typography, spacing, components, visualization, accessibility, and asset governance |
| `operator-score-gauge.md` | Official, provisional, range-only, blocked, and internal-only score visualization |
| `report-layout.md` | Executive and contractor report page/section/export structure |
| `roadmap-visual-spec.md` | Phase 0 and phases 1–5, dependencies, eligibility, authorization, and completion visuals |
| `diagram-specs.md` | Architecture, gate, buyer journey, routing, lifecycle, and publication-state diagrams |
| `brand-rules.md` | Naming, voice, visual identity, claims, mark use, synthetic, client, and version rules |

## 3. Production order

```text
Governed source objects
→ Design-system tokens
→ Score / roadmap / diagram components
→ Report layout
→ Export QA
→ Publication review
```

## 4. Shared controls

- visual design never overrides evidence or publication state
- blocked scores display no numeric gauge
- provisional and range-only states display uncertainty prominently
- unknown is not visualized as zero
- package eligibility precedes package promotion
- Phase 0 is visually distinct from implementation
- QC, publication, proposal, and implementation authorization remain separate
- completion and realized value remain separate
- diagrams have textual equivalents
- synthetic and confidential labels remain prominent

## 5. Commercial v1.0 connection

This registry converts the methodology and templates into a production-ready visual system without allowing design to create unsupported certainty.