import argparse
import json
import sys
from pathlib import Path

from .io import canonical_json, write_json
from .paths import resolve_fixture
from .runner import run_fixture


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the advisory-only Leverage Engine fixture cycle.")
    parser.add_argument("--fixture", required=True, help="Fixture directory, run.json path, or fixture name")
    parser.add_argument("--ledger", help="Optional append-only JSONL ledger path")
    parser.add_argument("--output", help="Optional JSON output path")
    parser.add_argument("--verify-determinism", action="store_true", help="Replay in memory and fail if outputs differ")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        fixture = resolve_fixture(args.fixture)
        ledger = Path(args.ledger) if args.ledger else None
        result = run_fixture(fixture, ledger)
        if args.verify_determinism:
            replay = run_fixture(fixture, ledger)
            first = dict(result)
            second = dict(replay)
            first["ledger_receipt"] = {**first["ledger_receipt"], "appended": False}
            second["ledger_receipt"] = {**second["ledger_receipt"], "appended": False}
            if canonical_json(first) != canonical_json(second):
                raise RuntimeError("determinism verification failed")
        if args.output:
            write_json(Path(args.output), result)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "HALT", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
