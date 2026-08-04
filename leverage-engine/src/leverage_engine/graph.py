from typing import Any


def build_run_edges(
    opportunities: list[dict[str, Any]], run_id: str, created_at: str
) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for opportunity in sorted(opportunities, key=lambda item: item["opportunity_id"]):
        for signal_id in sorted(opportunity["supporting_signals"]):
            edges.append({
                "from": signal_id,
                "to": opportunity["opportunity_id"],
                "type": "supports",
                "provenance": [signal_id, run_id],
                "created_at": created_at,
                "creator": "leverage-engine:0.1.0",
                "confidence": opportunity["confidence"],
            })
        for asset_id in sorted(opportunity["target_assets"]):
            edges.append({
                "from": opportunity["opportunity_id"],
                "to": asset_id,
                "type": "targets",
                "provenance": [opportunity["opportunity_id"], run_id],
                "created_at": created_at,
                "creator": "leverage-engine:0.1.0",
                "confidence": opportunity["confidence"],
            })
    return edges
