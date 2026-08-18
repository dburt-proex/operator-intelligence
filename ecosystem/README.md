# Canonical Ecosystem Registry

This directory is the source of truth for repository lifecycle classification and primitive authority across `dburt-proex`.

## Classification contract

Every repository must be exactly one of:

- `CORE` — canonical authority for one or more ecosystem primitives, or a foundational control surface approved to define primitives.
- `CONSUMER` — active product or operating surface that consumes primitives but may not redefine them.
- `REFERENCE` — proof, evidence, documentation, or integration example; never canonical runtime authority.
- `EXPERIMENT` — bounded prototype or exploration; may not become authority without an explicit registry change.
- `LEGACY` — superseded implementation retained for migration/history only; frozen against new authority claims.
- `ARCHIVED` — inactive/non-strategic repository; must not be used as an architectural dependency.

## Authority invariant

Every ecosystem primitive has exactly one canonical repository authority. A repository may consume, wrap, demonstrate, specialize, or integrate another primitive without inheriting authority over it.

A new primitive or authority transfer requires a registry change that:

1. names the primitive and its bounded purpose;
2. identifies exactly one `CORE` authority repository;
3. updates any supersession relationship;
4. preserves downstream consumer/reference classifications;
5. passes `python ecosystem/validate_registry.py`;
6. receives explicit review before merge.

## Resurrection prevention

Future agents and contributors must treat `LEGACY` and `ARCHIVED` repositories as non-authoritative. They may be inspected for migration evidence or historical context, but new features, new primitives, production dependencies, or architectural claims must route to the canonical authority named in `registry.json`.

`CONSUMER`, `REFERENCE`, and `EXPERIMENT` repositories may not claim ownership of an existing primitive. If their work exposes a genuinely new primitive, the registry must be amended first rather than silently expanding repository scope.

## Registry host boundary

`dburt-proex/operator-intelligence` hosts this registry because it already contains ecosystem conformance and decision-routing machinery. Registry hosting is administrative only and does not transfer authority from CASA, PromptBP, VIL, Cognitive Routing, DiffWall, Runwall, the Governance Harness Toolkit, Mirdexx, or Daxxer.

## Enforcement rollout

Each active repository receives a root `ECOSYSTEM.json` marker containing its registry classification, authority claims, consumed primitives, and supersession state. Repository CI compares that marker with this canonical registry. A mismatch fails the classification gate and must be resolved through an explicit registry decision rather than by editing around the control.
