from copy import deepcopy
from pathlib import Path
from typing import Any

from .context import compile_context_package, load_context_relations
from .deduplicate import group_duplicate_signals, suppress_duplicate_opportunities
from .directive import build_directive, ledger_record_id
from .executor_routing import route_executor
from .experience import load_validated_receipts
from .graph import build_run_edges
from .io import load_json
from .ledger import append_idempotent
from .normalize import normalize_signal
from .paths import CONFIG_DIR, SCHEMA_DIR
from .profiles import validate_policy_profile, validate_scoring_profile
from .retrieval import retrieve_candidates
from .route import route_opportunity
from .schema_validation import load_and_validate, validate_schema_document
from .score import score_opportunity


def _load_control_files() -> dict[str, dict[str, Any]]:
    files = {
        "sources": CONFIG_DIR / "source-registry.yaml",
        "repositories": CONFIG_DIR / "repository-registry.yaml",
        "scoring": CONFIG_DIR / "scoring-profile.yaml",
        "policy": CONFIG_DIR / "policy-profile.yaml",
    }
    controls = {key: load_json(path) for key, path in files.items()}
    validate_scoring_profile(controls["scoring"])
    validate_policy_profile(controls["policy"])
    return controls


def _validate_canonical_schemas() -> None:
    for name in (
        "signal",
        "repository-state",
        "opportunity",
        "directive",
        "outcome",
        "execution-receipt",
        "context-package",
        "context-relations",
        "routing-decision",
        "candidate-retrieval",
        "improvement-patterns",
        "improvement-analysis",
    ):
        path = SCHEMA_DIR / f"{name}.schema.json"
        validate_schema_document(load_json(path), str(path))


def _validate_registries(fixture: dict[str, Any], controls: dict[str, dict[str, Any]]) -> None:
    enabled_sources = {item["source_id"] for item in controls["sources"]["sources"] if item["enabled"]}
    unknown_sources = sorted({item["source_id"] for item in fixture["signals"]} - enabled_sources)
    if unknown_sources:
        raise ValueError(f"unregistered sources: {unknown_sources}")
    registered_repositories = {item["repository_id"] for item in controls["repositories"]["repositories"]}
    unknown_repositories = sorted({item["repository_id"] for item in fixture["repository_states"]} - registered_repositories)
    if unknown_repositories:
        raise ValueError(f"unregistered repositories: {unknown_repositories}")


def _rank_key(opportunity: dict[str, Any]) -> tuple[Any, ...]:
    eligibility = {"ALLOW": 0, "REVIEW": 1, "HALT": 2}[opportunity["gate_result"]]
    return (
        eligibility,
        -opportunity["leverage_index"],
        -opportunity["confidence_factor"],
        -opportunity["evidence_quality"],
        opportunity["friction_score"],
        opportunity["opportunity_id"],
    )


def run_fixture(fixture_path: Path, ledger_path: Path | None = None) -> dict[str, Any]:
    fixture = load_json(fixture_path)
    controls = _load_control_files()
    _validate_canonical_schemas()
    _validate_registries(fixture, controls)

    reuse_scope = fixture.get("experience_scope", [])
    experience_project_id = fixture.get("experience_project_id") or fixture.get("target_system", "unspecified")
    routing_config = fixture.get("executor_routing", {})
    routing_enabled = bool(routing_config.get("enabled", False))
    retrieval_config = fixture.get("candidate_retrieval", {})
    retrieval_query = str(retrieval_config.get("query", "")).strip()
    retrieval_enabled = bool(retrieval_config.get("enabled", False) and retrieval_query)
    retained_receipts = load_validated_receipts() if (reuse_scope or routing_enabled or retrieval_enabled) else []
    context_relations = load_context_relations()

    retrieval_result = None
    retrieved_item_ids: set[str] = set()
    if retrieval_enabled:
        retrieval_result = retrieve_candidates(
            retained_receipts,
            run_timestamp=fixture["run_timestamp"],
            project_id=experience_project_id,
            query=retrieval_query,
            relations=context_relations,
            max_candidates=int(retrieval_config.get("max_candidates", 24)),
        )
        retrieved_item_ids = {item["item_id"] for item in retrieval_result["candidates"]}

    context_budget = fixture.get("context_budget", {})
    compiled_context = compile_context_package(
        retained_receipts if (reuse_scope or retrieval_enabled) else [],
        run_timestamp=fixture["run_timestamp"],
        project_id=experience_project_id,
        reuse_scope=reuse_scope,
        relations=context_relations,
        retrieved_item_ids=retrieved_item_ids,
        max_items=int(context_budget.get("max_items", 12)),
        max_chars=int(context_budget.get("max_chars", 6000)),
        max_age_days=int(context_budget.get("max_age_days", 90)),
    )
    reused_experience = compiled_context["included"]
    experience_refs = sorted({f"experience:{item['source_execution_id']}" for item in reused_experience})
    effective_fixture = deepcopy(fixture)
    effective_fixture["evidence_refs"] = sorted(
        set(fixture.get("evidence_refs", []) + experience_refs)
    )

    routing_decision = None
    if routing_enabled:
        routing_decision = route_executor(
            retained_receipts,
            as_of=fixture["run_timestamp"],
            project_id=experience_project_id,
            min_samples=int(routing_config.get("min_samples", 3)),
            tie_tolerance=float(routing_config.get("tie_tolerance", 0.02)),
        )

    signals = [normalize_signal(item) for item in deepcopy(fixture["signals"])]
    for signal in signals:
        load_and_validate(signal, SCHEMA_DIR / "signal.schema.json")
    repository_states = deepcopy(fixture["repository_states"])
    for snapshot in repository_states:
        load_and_validate(snapshot, SCHEMA_DIR / "repository-state.schema.json")

    opportunities = deepcopy(fixture["opportunities"])
    suppressed = suppress_duplicate_opportunities(opportunities)
    signals_by_id = {item["signal_id"]: item for item in signals}
    scored: list[dict[str, Any]] = []
    for candidate in opportunities:
        missing = sorted(set(candidate["supporting_signals"]) - set(signals_by_id))
        if missing:
            raise ValueError(f"{candidate['opportunity_id']}: missing signal references {missing}")
        result = score_opportunity(candidate, controls["scoring"])
        gate, reasons = route_opportunity(
            result,
            signals_by_id,
            repository_states,
            controls["policy"],
            fixture["run_timestamp"],
        )
        result["gate_result"] = gate
        result["gate_reasons"] = reasons
        load_and_validate(result, SCHEMA_DIR / "opportunity.schema.json")
        scored.append(result)

    ranked = sorted(scored, key=_rank_key)
    selectable = [item for item in ranked if item["gate_result"] == "ALLOW" and item["state"] != "duplicate"]
    tie_candidates: list[str] = []
    if len(selectable) > 1:
        delta = abs(selectable[0]["leverage_index"] - selectable[1]["leverage_index"])
        if delta <= controls["policy"]["tie_tolerance"]:
            top_score = selectable[0]["leverage_index"]
            tied = [item for item in selectable if abs(item["leverage_index"] - top_score) <= controls["policy"]["tie_tolerance"]]
            tie_candidates = [item["opportunity_id"] for item in tied]
            for item in tied:
                item["gate_result"] = "REVIEW"
                item["gate_reasons"] = sorted(set(item["gate_reasons"] + ["LE-GATE-MATERIAL-TIE"]))
            ranked = sorted(scored, key=_rank_key)
    selected = None if tie_candidates else (selectable[0] if selectable else None)
    if selected:
        selected["state"] = "selected"
        directive = build_directive(effective_fixture, selected)
        load_and_validate(directive, SCHEMA_DIR / "directive.schema.json")
        selection: dict[str, Any] = {"result": "DIRECTIVE", "directive": directive}
        decision_rationale = (
            f"{selected['opportunity_id']} ranked first among policy-eligible candidates "
            f"with Leverage Index {selected['leverage_index']}. ALLOW means human review eligibility only."
        )
        selected_id = selected["opportunity_id"]
    else:
        selection = {"result": "NO_ACTION", "directive": None}
        decision_rationale = (
            f"Top candidates {', '.join(tie_candidates)} are tied and require human review."
            if tie_candidates
            else "No candidate cleared evidence, confidence, freshness, duplication, and authority gates."
        )
        selected_id = None

    ranking = [
        {
            "rank": index,
            "opportunity_id": item["opportunity_id"],
            "leverage_index": item["leverage_index"],
            "confidence": item["confidence"],
            "evidence_quality": item["evidence_quality"],
            "friction_score": item["friction_score"],
            "risk_score": item["risk_score"],
            "gate_result": item["gate_result"],
            "gate_reasons": item["gate_reasons"],
            "state": item["state"],
        }
        for index, item in enumerate(ranked, 1)
    ]
    record_id = ledger_record_id(fixture["run_id"], selected_id)
    ledger_record = {
        "record_id": record_id,
        "run_id": fixture["run_id"],
        "recorded_at": fixture["run_timestamp"],
        "policy_version": controls["policy"]["version"],
        "scoring_version": controls["scoring"]["version"],
        "source_registry_version": controls["sources"]["version"],
        "repository_registry_version": controls["repositories"]["version"],
        "selection_result": selection["result"],
        "selected_opportunity_id": selected_id,
        "context_id": compiled_context["context_id"],
        "retrieval_id": retrieval_result["retrieval_id"] if retrieval_result else None,
        "routing_id": routing_decision["routing_id"] if routing_decision else None,
        "experience_refs": experience_refs,
        "ranking": ranking,
        "rationale": decision_rationale,
        "rejected_alternatives": [item["opportunity_id"] for item in ranked if item["opportunity_id"] != selected_id],
    }
    receipt = append_idempotent(ledger_path, ledger_record)
    return {
        "run_id": fixture["run_id"],
        "run_timestamp": fixture["run_timestamp"],
        "versions": {
            "fixture": fixture["fixture_version"],
            "policy": controls["policy"]["version"],
            "scoring": controls["scoring"]["version"],
            "source_registry": controls["sources"]["version"],
            "repository_registry": controls["repositories"]["version"],
        },
        "coverage": {
            "signal_count": len(signals),
            "repository_snapshot_count": len(repository_states),
            "opportunity_count": len(opportunities),
            "partial": fixture.get("partial_coverage", False),
        },
        "duplicate_signal_groups": group_duplicate_signals(signals),
        "suppressed_opportunities": suppressed,
        "graph_edges": build_run_edges(scored, fixture["run_id"], fixture["run_timestamp"]),
        "tie_candidates": tie_candidates,
        "ranking": ranking,
        "selection": selection,
        "rationale": decision_rationale,
        "assumptions": fixture.get("assumptions", []),
        "evidence_refs": effective_fixture["evidence_refs"],
        "candidate_retrieval": retrieval_result,
        "compiled_context": compiled_context,
        "reused_experience": reused_experience,
        "routing_decision": routing_decision,
        "ledger_receipt": receipt,
        "execution_authorized": False,
    }
