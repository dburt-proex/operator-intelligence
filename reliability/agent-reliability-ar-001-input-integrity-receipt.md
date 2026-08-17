# AR-001 — Input Integrity Receipt

**Experiment:** AR-001 — Controlled Clone Reproducibility  
**Receipt version:** 0.1  
**Status:** VERIFIED INPUT INTEGRITY  
**Packet:** `reliability/fixtures/ar-001-input-v1.json`  
**Packet version:** 1.0.0

## Purpose

Record the canonical byte-level identity of the oracle-safe AR-001 evaluated-agent input packet. This receipt replaces the prior `validation_required` packet-digest state.

## Verified identity

- canonical encoding: UTF-8
- canonical line endings: LF
- terminal newline: present
- byte length: `2312`
- SHA-256: `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc`
- Git blob SHA: `54d2a000928ddd3d92a886c2e8f01e727a64c2b4`
- creation commit: `d1e26b66a1960885e4fb918f571876dbacec4f23`
- classification: `SYNTHETIC_EXPERIMENT_EVIDENCE`
- oracle fields included: `false`

## Source lineage

The packet was derived only from the admitted scope, evidence requirement, and two synthetic EvidenceArtifact records in:

`assessment-evidence-graph/fixtures/representative-assessment/run.json`

The source fixture's downstream Claim, Finding, ControlGap, Remediation, Verification, governance-disposition, and expected-answer material are deliberately excluded from the evaluated-agent packet.

This separation is mandatory because the representative assessment fixture is suitable as an oracle/reference artifact but is not safe to provide wholesale to evaluated agents without leaking the expected result.

## Run verification rule

Before each AR-001 pilot or cohort execution, the harness must:

1. read the exact packet bytes;
2. calculate SHA-256;
3. compare against `861c2c314fb149def429a078a0181213534ac9490daa793b27abebf216c998cc`;
4. verify byte length `2312`;
5. verify the configured packet version is `1.0.0`;
6. HALT before inference on any mismatch.

No normalization, reformatting, key reordering, newline conversion, or regenerated JSON is permitted after the digest check.

## Governance disposition

**EVD-001 experiment-scoped pre-code integrity requirement: PASS.**

This receipt proves packet identity only. It does not authorize harness implementation or experiment execution and does not satisfy unrelated owner-controlled requirements.

## Supersession rule

Any material packet change requires a new packet version, new digest, new integrity receipt, and renewed pre-code review. This receipt must remain immutable evidence for v1.0.0 of the packet.
