from typing import Any


def build_run_edges(opportunities: list[dict[str, Any]]) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for opportunity in sorted(opportunities, key=lambda item: item["opportunity_id"]):
        for signal_id in sorted(opportunity["supporting_signals"]):
            edges.append({
                "from": signal_id,
                "to": opportunity["opportunity_id"],
                "type": "supports",
                "confidence": opportunity["confidence"],
            })
        for asset_id in sorted(opportunity["target_assets"]):
            edges.append({
                "from": opportunity["opportunity_id"],
                "to": asset_id,
                "type": "targets",
                "confidence": opportunity["confidence"],
            })
    return edges
