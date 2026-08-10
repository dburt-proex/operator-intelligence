# PR #15 Split Plan — Assessment Evidence Graph

## Context

PR #15 (`feat: add governed assessment evidence graph`) was halted by DiffWall for three reasons:

1. **GitHub Actions workflow changed** — `.github/workflows/validate-registry-and-map.yml`
2. **Dependency manifest changed** — `assessment-evidence-graph/pyproject.toml`
3. **Huge diff size** — 23 files, 3147 additions, 135 deletions

This document describes the three-way split and the exact commands required to create each branch and PR.

---

## Split Summary

| PR | Branch | Files | Lines | DiffWall Risk |
|----|--------|-------|-------|---------------|
| **PR A** (this PR) | `copilot/split-pr-15-changes` | `.github/workflows/validate-registry-and-map.yml` | +6 | Workflow change — merge last |
| **PR B** | `split/pr-15-dependencies` | `assessment-evidence-graph/pyproject.toml` | +19 | Dependency manifest only |
| **PR C** | `split/pr-15-application` | 21 files — all application source, tests, fixtures, registry, generated maps | +3124 | Application code — merge first |

**Merge order:** PR C → PR B → PR A

---

## PR A — Workflow change (this PR)

**Branch:** `copilot/split-pr-15-changes`  
**Merge order:** Last — depends on PR C code being in `main` first.

**Change:** Adds two CI steps (with a `hashFiles` guard so they are skipped if the package is not yet in `main`) to validate the assessment evidence graph:
```yaml
- name: Install assessment evidence graph
  if: hashFiles('assessment-evidence-graph/pyproject.toml') != ''
  run: python -m pip install --disable-pip-version-check -e ./assessment-evidence-graph
- name: Run assessment evidence graph replay and adversarial tests
  if: hashFiles('assessment-evidence-graph/pyproject.toml') != ''
  run: python -m unittest discover -s assessment-evidence-graph/tests -v
```

**Why isolated:** DiffWall flags any GitHub Actions workflow change as high-risk. Isolating it to 4 lines makes the risk surface minimal and reviewable.

---

## PR B — Dependency manifest

**Branch:** `split/pr-15-dependencies`  
**Merge order:** Second — can be merged any time after PR C.

**Change:** Adds `assessment-evidence-graph/pyproject.toml` (19 lines):
- Declares the package name, version, Python requirement, and runtime dependencies
- No lockfile — pip resolves from pyproject.toml

**Why isolated:** DiffWall flags dependency manifest changes. At 19 lines, this is the easiest diff for a security reviewer to audit independently.

**Commands to create this branch:**
```bash
git checkout 87b40f24a1c53d254319d240659598afa7d656ae  # base of PR #15
git checkout -b split/pr-15-dependencies
git checkout origin/agent/ge001-assessment-evidence-graph -- assessment-evidence-graph/pyproject.toml
git commit -m "chore: add assessment-evidence-graph pyproject.toml"
git push origin split/pr-15-dependencies
# Then open a PR: split/pr-15-dependencies → main
```

---

## PR C — Application code (largest, merge first)

**Branch:** `split/pr-15-application`  
**Merge order:** First — foundational; PRs A and B depend on this code being in main.

**Files included:**
- `CHANGELOG.md` — version entry
- `assessment-evidence-graph/.gitignore`
- `assessment-evidence-graph/README.md`
- `assessment-evidence-graph/agentic-graph-blueprint.json`
- `assessment-evidence-graph/config/publication-policy.json`
- `assessment-evidence-graph/fixtures/representative-assessment/run.json`
- `assessment-evidence-graph/src/assessment_evidence_graph/__init__.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/broker.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/canonical.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/cli.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/ledger.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/models.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/policy.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/runner.py`
- `assessment-evidence-graph/src/assessment_evidence_graph/store.py`
- `assessment-evidence-graph/tests/test_vertical_slice.py`
- `generated/repository-map.dot`
- `generated/repository-map.json`
- `generated/repository-map.md`
- `generated/repository-map.mmd`
- `registry/artifacts.yaml`

**Why isolated:** This PR has no workflow files and no dependency manifests. DiffWall will still see a large diff (3124 lines), but it will not trigger the workflow or dependency-manifest halt conditions — only the size condition. Size-only halts are lower governance risk than multi-flag halts.

**Commands to create this branch:**
```bash
git checkout 87b40f24a1c53d254319d240659598afa7d656ae  # base of PR #15
git checkout -b split/pr-15-application
git checkout origin/agent/ge001-assessment-evidence-graph -- \
  CHANGELOG.md \
  assessment-evidence-graph/.gitignore \
  assessment-evidence-graph/README.md \
  assessment-evidence-graph/agentic-graph-blueprint.json \
  assessment-evidence-graph/config/publication-policy.json \
  "assessment-evidence-graph/fixtures/representative-assessment/run.json" \
  assessment-evidence-graph/src/assessment_evidence_graph/__init__.py \
  assessment-evidence-graph/src/assessment_evidence_graph/broker.py \
  assessment-evidence-graph/src/assessment_evidence_graph/canonical.py \
  assessment-evidence-graph/src/assessment_evidence_graph/cli.py \
  assessment-evidence-graph/src/assessment_evidence_graph/ledger.py \
  assessment-evidence-graph/src/assessment_evidence_graph/models.py \
  assessment-evidence-graph/src/assessment_evidence_graph/policy.py \
  assessment-evidence-graph/src/assessment_evidence_graph/runner.py \
  assessment-evidence-graph/src/assessment_evidence_graph/store.py \
  assessment-evidence-graph/tests/test_vertical_slice.py \
  generated/repository-map.dot \
  generated/repository-map.json \
  generated/repository-map.md \
  generated/repository-map.mmd \
  registry/artifacts.yaml
git commit -m "feat: add governed assessment evidence graph application code"
git push origin split/pr-15-application
# Then open a PR: split/pr-15-application → main
```

---

## Why this split

The three DiffWall halt signals map cleanly to the three PRs:

- **Workflow changed** → PR A (1 file, 4 lines, lowest-risk workflow audit)
- **Dependency manifest changed** → PR B (1 file, 19 lines, focused dependency review)
- **Huge diff** → PR C (21 files, application code — cannot avoid size, but removes the other two flags)

Each PR carries at most one DiffWall halt signal. The risk is distributed, the reviewer surface for each PR is coherent, and no partial changes are introduced (every file is complete at each commit boundary).
