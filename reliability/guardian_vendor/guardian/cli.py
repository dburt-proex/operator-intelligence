"""Guardian CLI.

    python -m guardian.cli check envelope.json [--ledger PATH]
    python -m guardian.cli verify [--ledger PATH]

Exit codes (CI-composable): 0 = ALLOW, 1 = REVIEW, 2 = HALT / error.
verify: 0 = chain intact, 2 = tamper detected.
"""
from __future__ import annotations

import argparse
import json
import sys

from .audit import AuditLedger
from .models import Verdict
from .pipeline import GuardianAgent
from .audit import AuditError
from .validation import MAX_BYTES

_EXIT = {Verdict.ALLOW: 0, Verdict.REVIEW: 1, Verdict.HALT: 2}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="guardian")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="govern one action envelope")
    c.add_argument("envelope", help="path to envelope JSON {signal, action}")
    c.add_argument("--ledger", default="guardian_audit.jsonl")

    v = sub.add_parser("verify", help="verify audit chain integrity")
    v.add_argument("--ledger", default="guardian_audit.jsonl")
    v.add_argument("--expected-head", help="independently retained trusted chain head")

    args = p.parse_args(argv)

    if args.cmd == "verify":
        try:
            ok, msg = AuditLedger(args.ledger).verify(expected_head=args.expected_head)
        except (AuditError, ValueError, TypeError):
            ok, msg = False, "audit unavailable or invalid configuration"
        print(json.dumps({"ledger": args.ledger, "intact": ok, "detail": msg}))
        return 0 if ok else 2

    try:
        with open(args.envelope, "rb") as f:
            data = f.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("input too large")
            data = data.decode("utf-8")
            def unique_object(pairs):
                obj = {}
                for key, value in pairs:
                    if key in obj:
                        raise ValueError("duplicate JSON key")
                    obj[key] = value
                return obj
            envelope = json.loads(data, object_pairs_hook=unique_object)
    except (OSError, ValueError, RecursionError):
        print(json.dumps({"error": "cannot read valid envelope"}))
        return 2

    try:
        decision = GuardianAgent(args.ledger).govern(envelope)
    except (AuditError, ValueError, TypeError):
        print(json.dumps({"error": "audit unavailable; execution blocked"}))
        return 2
    print(json.dumps(decision.to_dict(), indent=2))
    return _EXIT[decision.verdict]


if __name__ == "__main__":
    sys.exit(main())
