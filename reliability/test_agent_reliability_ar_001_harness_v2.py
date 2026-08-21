#!/usr/bin/env python3
"""Deterministic tests for the AR-001 Stage A v2 metadata correction."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from reliability import agent_reliability_ar_001_harness as v1
from reliability import agent_reliability_ar_001_harness_v2 as v2
from reliability.test_agent_reliability_ar_001_harness import valid_output


RUN_ID = "AR001-STAGEA-V2-TEST-RUN-001"
TRACE_ID = "AR001-STAGEA-V2-TEST-TRACE-001"


class V2MetadataCorrectionTests(unittest.TestCase):
    def test_request_supplies_exact_model_identifier_without_changing_frozen_inputs(self) -> None:
        before = v1.CONFIGURATION_ID
        request = v2.build_request(RUN_ID, TRACE_ID)
        self.assertEqual(v1.CONFIGURATION_ID, before)
        self.assertEqual(request["model"], v2.MODEL)
        self.assertEqual(request["reasoning"], {"effort": "high", "context": "current_turn"})
        self.assertNotIn("tools", request)
        self.assertIs(request["store"], False)
        envelope = json.loads(request["input"])
        self.assertEqual(envelope["configuration_id"], "AR-001-CONFIG-002")
        self.assertEqual(envelope["model_identifier"], "gpt-5.6-terra")
        self.assertEqual(envelope["input_packet_sha256"], v2.INPUT_SHA256)
        self.assertEqual(envelope["instruction_sha256"], v2.INSTRUCTION_SHA256)
        self.assertFalse(envelope["admitted_input"]["oracle_fields_included"])

    def test_v1_authorization_cannot_authorize_v2(self) -> None:
        with self.assertRaises(v2.HarnessError):
            v2.validate_execution_authorization(
                Path("reliability/authorizations/ar-001-pilot-v1.json")
            )

    def test_v2_authorization_is_exactly_two_runs_and_cohort_closed(self) -> None:
        data = v2.validate_execution_authorization(
            Path("reliability/authorizations/ar-001-pilot-v2.json")
        )
        self.assertEqual(data["authorization_version"], "2.0.0")
        self.assertEqual(data["configuration_id"], "AR-001-CONFIG-002")
        self.assertEqual(data["authorized_runs"], 2)
        self.assertIs(data["cohort_execution_authorized"], False)
        self.assertIs(data["metadata_correction_only"], True)

    def test_v2_receipt_contract_is_schema_valid_when_model_identity_is_supplied(self) -> None:
        output = valid_output(RUN_ID, TRACE_ID)
        output["receipt"]["configuration_id"] = v2.CONFIGURATION_ID
        output["receipt"]["model_identifier"] = v2.MODEL
        result = v2.validate_output(output, RUN_ID, TRACE_ID)
        self.assertTrue(result.valid, result.errors)
        self.assertFalse(result.safety_halt)

    def test_v2_validation_does_not_mutate_v1_configuration(self) -> None:
        before = v1.CONFIGURATION_ID
        output = valid_output(RUN_ID, TRACE_ID)
        output["receipt"]["configuration_id"] = v2.CONFIGURATION_ID
        output["receipt"]["model_identifier"] = v2.MODEL
        v2.validate_output(output, RUN_ID, TRACE_ID)
        self.assertEqual(v1.CONFIGURATION_ID, before)


if __name__ == "__main__":
    unittest.main()
