# Operator Intelligence Artifact Registry

Version: v0.1 post-v1 conformance layer  
Folder alignment: `registry/`  
Status: Governed machine-readable authority layer

## Purpose

The registry classifies governed repository artifacts, records explicit authority exceptions, defines dependency and generation rules, and provides the source for repository-map generation and conformance validation.

## Files

- `artifacts.yaml` — JSON-compatible YAML registry.
- `registry-schema.json` — machine-readable contract.
- `validate_registry.py` — fail-closed conformance validator.

## Governance

- Human-readable standards remain the methodology authority.
- This registry records where authority resides; it does not change scoring, findings, packages, publication states, or implementation authorization.
- Explicit artifact entries override governed-root defaults.
- Proposed, experimental, deprecated, superseded, and generated artifacts must never be represented as canonical.
- New governed files must be classified before merge.
- Generated maps are outputs and cannot become methodology authorities.

## Usage

```bash
python registry/validate_registry.py
python tools/generate_repository_map.py
python tools/generate_repository_map.py --check
```

## Post-v1 connection

This layer makes repository drift, shadow authority, stale maps, missing dependencies, and unclassified governed artifacts detectable before they affect delivery or automation.
