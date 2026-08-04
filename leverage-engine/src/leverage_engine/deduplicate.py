import hashlib
import re
from collections import defaultdict
from typing import Any


def _plain(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def signal_fingerprint(signal: dict[str, Any]) -> str:
    basis = "|".join([_plain(signal["title"]), *sorted(signal["affected_assets"])])
    return hashlib.sha256(basis.encode()).hexdigest()[:16]


def group_duplicate_signals(signals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for signal in signals:
        groups[signal_fingerprint(signal)].append(signal["signal_id"])
    return [
        {"fingerprint": fingerprint, "signal_ids": sorted(ids)}
        for fingerprint, ids in sorted(groups.items())
        if len(ids) > 1
    ]


def opportunity_fingerprint(opportunity: dict[str, Any]) -> str:
    basis = "|".join([_plain(opportunity["objective"]), *sorted(opportunity["target_assets"])])
    return hashlib.sha256(basis.encode()).hexdigest()[:16]


def suppress_duplicate_opportunities(opportunities: list[dict[str, Any]]) -> list[dict[str, str]]:
    seen: dict[str, str] = {}
    suppressed: list[dict[str, str]] = []
    for opportunity in sorted(opportunities, key=lambda item: item["opportunity_id"]):
        fingerprint = opportunity_fingerprint(opportunity)
        if fingerprint in seen:
            opportunity["state"] = "duplicate"
            opportunity["duplicates"] = sorted(set(opportunity["duplicates"] + [seen[fingerprint]]))
            suppressed.append({"duplicate_id": opportunity["opportunity_id"], "canonical_id": seen[fingerprint]})
        else:
            seen[fingerprint] = opportunity["opportunity_id"]
    return suppressed
