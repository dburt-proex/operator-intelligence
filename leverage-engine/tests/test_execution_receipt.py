import unittest

from leverage_engine.io import load_json
from leverage_engine.paths import ROOT, SCHEMA_DIR
from leverage_engine.schema_validation import (
    SchemaValidationError,
    load_and_validate,
    validate_schema_document,
)


class ExecutionReceiptTests(unittest.TestCase):
    def fixture(self, name: str):
        return ROOT / "fixtures" / name / "receipt.json"

    def schema_path(self):
        return SCHEMA_DIR / "execution-receipt.schema.json"

    def test_execution_receipt_schema_is_canonical_and_valid_fixture_passes(self):
        schema_path = self.schema_path()
        validate_schema_document(load_json(schema_path), "execution-receipt")
        load_and_validate(load_json(self.fixture("execution-receipt-valid")), schema_path)

    def test_retained_live_receipts_validate(self):
        receipts = sorted((ROOT / "receipts").glob("*.json"))
        self.assertTrue(receipts, "at least one retained execution receipt is required")
        for receipt_path in receipts:
            with self.subTest(receipt=receipt_path.name):
                load_and_validate(load_json(receipt_path), self.schema_path())

    def test_completed_receipt_without_completion_evidence_is_rejected(self):
        invalid = load_json(self.fixture("execution-receipt-invalid-missing-evidence"))
        with self.assertRaises(SchemaValidationError):
            load_and_validate(invalid, self.schema_path())

    def test_halt_cannot_be_completed(self):
        receipt = load_json(self.fixture("execution-receipt-valid"))
        receipt["gate_result"] = "HALT"
        with self.assertRaises(SchemaValidationError):
            load_and_validate(receipt, self.schema_path())

    def test_next_improvement_requires_review_flag(self):
        receipt = load_json(self.fixture("execution-receipt-valid"))
        del receipt["next_improvement"]["requires_review"]
        with self.assertRaises(SchemaValidationError):
            load_and_validate(receipt, self.schema_path())

    def test_next_improvement_requires_supporting_evidence(self):
        receipt = load_json(self.fixture("execution-receipt-valid"))
        receipt["next_improvement"]["evidence_refs"] = []
        with self.assertRaises(SchemaValidationError):
            load_and_validate(receipt, self.schema_path())

    def test_reusable_learning_requires_supporting_evidence(self):
        receipt = load_json(self.fixture("execution-receipt-valid"))
        receipt["reusable_learnings"][0]["evidence_refs"] = []
        with self.assertRaises(SchemaValidationError):
            load_and_validate(receipt, self.schema_path())


if __name__ == "__main__":
    unittest.main()
