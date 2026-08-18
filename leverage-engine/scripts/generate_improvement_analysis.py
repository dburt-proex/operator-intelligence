#!/usr/bin/env python3
"""Generate a deterministic governed environment-improvement analysis."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from leverage_engine.experience import load_validated_receipts
from leverage_engine.improvement import generate_improvement_analysis, load_improvement_patterns


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Leverage Engine improvement analysis")
    parser.add_argument("--as-of", required=True, help="ISO-8601 analysis cutoff timestamp")
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--min-distinct-executions", type=int, default=2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    analysis = generate_improvement_analysis(
        load_validated_receipts(),
        generated_at=args.as_of,
        project_id=args.project_id,
        pattern_document=load_improvement_patterns(),
        min_distinct_executions=args.min_distinct_executions,
    )
    rendered = json.dumps(analysis, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
