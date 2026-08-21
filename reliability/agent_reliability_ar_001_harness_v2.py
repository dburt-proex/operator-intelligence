#!/usr/bin/env python3
"""AR-001 Stage A v2 metadata-corrected harness.

This wrapper preserves the original v1 harness and evidence unchanged. It makes
one bounded correction only: the evaluated-agent input envelope now includes
the frozen model identifier that the output receipt contract already required.

All assessment semantics, evidence, model, reasoning effort, oracle isolation,
validation rules, safety rules, and governance expectations remain inherited
from the v1 harness.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable

from reliability import agent_reliability_ar_001_harness as base

EXPERIMENT_ID = base.EXPERIMENT_ID
CONFIGURATION_ID = "AR-001-CONFIG-002"
MODEL = base.MODEL
REASONING_EFFORT = base.REASONING_EFFORT
INPUT_SHA256 = base.INPUT_SHA256
INSTRUCTION_SHA256 = base.INSTRUCTION_SHA256
MAX_OUTPUT_TOKENS = base.MAX_OUTPUT_TOKENS
EXPECTED_GATE = base.EXPECTED_GATE
REQUIRED_EVIDENCE = base.REQUIRED_EVIDENCE
HarnessError = base.HarnessError
ValidationResult = base.ValidationResult
RunRecord = base.RunRecord

AUTHORIZATION_VERSION = "2.0.0"
AUTHORIZED_RUNS = 2
SOURCE_STAGE_A_CLOSEOUT_SHA = "2756dd503b763ad07e9dba8b398a45ee74250b3c"


@contextmanager
def _v2_configuration() -> Iterable[None]:
    """Temporarily bind the inherited validator/receipt logic to CONFIG-002."""
    previous = base.CONFIGURATION_ID
    base.CONFIGURATION_ID = CONFIGURATION_ID
    try:
        yield
    finally:
        base.CONFIGURATION_ID = previous


def verify_frozen_artifacts() -> dict[str, str]:
    return base.verify_frozen_artifacts()


def output_json_schema() -> dict[str, Any]:
    return base.output_json_schema()


def build_request(run_id: str, trace_id: str) -> dict[str, Any]:
    """Build the v2 request with explicit model identity in admitted metadata."""
    with _v2_configuration():
        request = base.build_request(run_id, trace_id)
    envelope = json.loads(request["input"])
    if envelope.get("configuration_id") != CONFIGURATION_ID:
        raise HarnessError("v2 request configuration_id was not bound correctly")
    envelope["model_identifier"] = MODEL
    request["input"] = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
    return request


def validate_execution_authorization(path: Path) -> dict[str, Any]:
    """Require a fresh, v2-specific two-run authorization before inference."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HarnessError(f"v2 pilot authorization cannot be loaded: {exc}") from exc

    required = {
        "experiment_id": EXPERIMENT_ID,
        "gate": "ALLOW_TO_RUN_PILOT",
        "decision": "ALLOW",
        "authorization_version": AUTHORIZATION_VERSION,
        "configuration_id": CONFIGURATION_ID,
        "authorized_runs": AUTHORIZED_RUNS,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "input_packet_sha256": INPUT_SHA256,
        "instruction_sha256": INSTRUCTION_SHA256,
        "source_stage_a_closeout_sha": SOURCE_STAGE_A_CLOSEOUT_SHA,
    }
    for key, expected in required.items():
        if data.get(key) != expected:
            raise HarnessError(
                f"v2 pilot authorization mismatch for {key}: {data.get(key)!r} != {expected!r}"
            )
    if data.get("pilot_execution_authorized") is not True:
        raise HarnessError("v2 pilot authorization does not explicitly authorize execution")
    if data.get("cohort_execution_authorized") is not False:
        raise HarnessError("v2 pilot authorization must not authorize the 30-run cohort")
    if data.get("metadata_correction_only") is not True:
        raise HarnessError("v2 authorization is not bounded to the metadata correction")
    return data


def call_openai(
    request_body: dict[str, Any],
    authorization_path: Path,
    api_key: str | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_execution_authorization(authorization_path)
    with _v2_configuration():
        return base.call_openai(request_body, authorization_path, api_key=api_key)


def validate_output(output: Any, run_id: str, trace_id: str) -> ValidationResult:
    with _v2_configuration():
        return base.validate_output(output, run_id, trace_id)


def canonicalize_output(output: dict[str, Any]) -> dict[str, Any]:
    return base.canonicalize_output(output)


def calculate_metrics(records: Iterable[RunRecord]) -> dict[str, float]:
    return base.calculate_metrics(records)


def make_run_receipt(record: RunRecord) -> dict[str, Any]:
    with _v2_configuration():
        receipt = base.make_run_receipt(record)
    receipt["schema_version"] = "ar-001-run-receipt-v2"
    receipt["metadata_correction_only"] = True
    receipt["source_stage_a_closeout_sha"] = SOURCE_STAGE_A_CLOSEOUT_SHA
    return receipt


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Governed AR-001 Stage A v2 reliability harness")
    parser.add_argument("--run-id", default="AR001-STAGEA-V2-DRYRUN-001")
    parser.add_argument("--trace-id", default="AR001-STAGEA-V2-TRACE-001")
    parser.add_argument("--print-request", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--pilot-authorization", type=Path)
    args = parser.parse_args()

    try:
        request_body = build_request(args.run_id, args.trace_id)
        if args.print_request:
            print(json.dumps(request_body, indent=2, sort_keys=True))
        if not args.execute:
            print("AR-001 Stage A v2 local validation: PASS; execution not requested", file=sys.stderr)
            return 0
        if args.pilot_authorization is None:
            raise HarnessError("--execute requires --pilot-authorization")
        if not os.environ.get("OPENAI_API_KEY"):
            raise HarnessError("OPENAI_API_KEY is required only for an authorized execution")
        output, metadata = call_openai(request_body, args.pilot_authorization)
        validation = validate_output(output, args.run_id, args.trace_id)
        record = RunRecord(args.run_id, args.trace_id, output, validation, metadata)
        print(json.dumps({"output": output, "receipt": make_run_receipt(record)}, indent=2, sort_keys=True))
        return 0 if validation.valid else 2
    except HarnessError as exc:
        print(f"AR-001 Stage A v2 HALT: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(_cli())
