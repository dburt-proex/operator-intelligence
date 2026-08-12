"""Command-line replay surface for the bounded evidence graph."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .runner import DEFAULT_POLICY, replay_fixture


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--ledger-outbox", type=Path)
    parser.add_argument(
        "--policy",
        type=Path,
        default=DEFAULT_POLICY,
        help="Publication policy. Defaults to the policy bundled with this package.",
    )
    parser.add_argument(
        "--standards-root",
        type=Path,
        required=True,
        help="External Operator Intelligence repository root used to verify policy sources.",
    )
    args = parser.parse_args()
    result = replay_fixture(
        args.fixture,
        args.database,
        ledger_path=args.ledger_outbox,
        policy_path=args.policy,
        standards_root=args.standards_root,
    )
    print(json.dumps(result.model_dump(mode="json"), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
