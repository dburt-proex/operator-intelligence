"""FR-001 contract and adversarial regression tests."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from reliability import field_reliability_validator as validator

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "reliability" / "fixtures"
VALID_CSV = FIXTURES / "field-reliability-contract-valid.csv"
VALID_MANIFEST = FIXTURES / "field-reliability-contract-valid.manifest.json"
INVALID_UNKNOWN = FIXTURES / "field-reliability-contract-invalid-unknown-score.csv"


class FieldReliabilityContractTests(unittest.TestCase):
    def manifest(self) -> dict[str, object]:
        return json.loads(VALID_MANIFEST.read_text(encoding="utf-8"))

    def write_manifest(self, directory: Path, data: dict[str, object]) -> Path:
        path = directory / "manifest.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_valid_synthetic_contract_fixture_routes_review(self) -> None:
        ratings = validator.read_ratings_csv(VALID_CSV)
        manifest = validator.load_manifest(VALID_MANIFEST, VALID_CSV, ratings)
        result = validator.evaluate(ratings, manifest)
        self.assertEqual(result["decision"], "REVIEW")
        self.assertEqual(result["metrics"]["exact_agreement"], 0.5)
        self.assertIn("synthetic contract fixture", result["decision_reason"])

    def test_unknown_with_numeric_score_halts(self) -> None:
        with self.assertRaisesRegex(validator.ValidationError, "must not carry a numeric score"):
            validator.read_ratings_csv(INVALID_UNKNOWN)

    def test_extra_csv_header_halts(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "invalid.csv"
            path.write_text("criterion_id,category,evaluator_id,state,score,notes\n", encoding="utf-8")
            with self.assertRaisesRegex(validator.ValidationError, "header must be exactly"):
                validator.read_ratings_csv(path)

    def test_manifest_hash_substitution_halts(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            copied = directory / "ratings.csv"
            shutil.copy2(VALID_CSV, copied)
            copied.write_text(copied.read_text(encoding="utf-8").replace(",50\n", ",25\n", 1), encoding="utf-8")
            ratings = validator.read_ratings_csv(copied)
            with self.assertRaisesRegex(validator.ValidationError, "ratings_sha256 does not match"):
                validator.load_manifest(VALID_MANIFEST, copied, ratings)

    def test_manifest_evaluator_set_mismatch_halts(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            data = self.manifest()
            data["evaluator_ids"] = ["EV-001", "EV-003"]
            manifest = self.write_manifest(directory, data)
            ratings = validator.read_ratings_csv(VALID_CSV)
            with self.assertRaisesRegex(validator.ValidationError, "must exactly match"):
                validator.load_manifest(manifest, VALID_CSV, ratings)

    def test_unknown_manifest_field_and_duplicate_rating_halt(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            data = self.manifest()
            data["unapproved_field"] = "must not persist"
            manifest = self.write_manifest(directory, data)
            ratings = validator.read_ratings_csv(VALID_CSV)
            with self.assertRaisesRegex(validator.ValidationError, "fields must be exact"):
                validator.load_manifest(manifest, VALID_CSV, ratings)
        duplicate = [
            {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "EV-001", "state": "scored", "score": "50"},
            {"criterion_id": "OI-WEB-001", "category": "website", "evaluator_id": "EV-001", "state": "scored", "score": "50"},
        ]
        with self.assertRaisesRegex(validator.ValidationError, "duplicate rating"):
            validator.read_ratings(duplicate)

    def test_unblinded_human_study_halts(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            data = self.manifest()
            data["record_class"] = "human_field_study"
            data["blinding_status"] = "not_blinded"
            manifest = self.write_manifest(directory, data)
            ratings = validator.read_ratings_csv(VALID_CSV)
            with self.assertRaisesRegex(validator.ValidationError, "requires blinded"):
                validator.load_manifest(manifest, VALID_CSV, ratings)

    def test_unknown_criterion_or_wrong_category_halts(self) -> None:
        rows = [
            {"criterion_id": "OI-WEB-999", "category": "website", "evaluator_id": "EV-001", "state": "scored", "score": "50"},
            {"criterion_id": "OI-WEB-999", "category": "website", "evaluator_id": "EV-002", "state": "scored", "score": "50"},
        ]
        with self.assertRaisesRegex(validator.ValidationError, "unknown canonical criterion"):
            validator.read_ratings(rows)
        rows[0]["criterion_id"] = rows[1]["criterion_id"] = "OI-WEB-001"
        rows[0]["category"] = rows[1]["category"] = "seo"
        with self.assertRaisesRegex(validator.ValidationError, "does not match"):
            validator.read_ratings(rows)

    def test_evaluation_is_order_invariant(self) -> None:
        ratings = validator.read_ratings_csv(VALID_CSV)
        self.assertEqual(validator.evaluate(ratings), validator.evaluate(list(reversed(ratings))))

    def test_human_study_cannot_allow_without_scored_pairs(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            directory = Path(raw)
            csv_path = directory / "states.csv"
            csv_path.write_text(
                "criterion_id,category,evaluator_id,state,score\n"
                "OI-SOC-001,social,EV-001,unknown,\n"
                "OI-SOC-001,social,EV-002,unknown,\n",
                encoding="utf-8",
            )
            data = self.manifest()
            data["record_class"] = "human_field_study"
            data["ratings_sha256"] = hashlib.sha256(csv_path.read_bytes()).hexdigest()
            data["evaluator_ids"] = ["EV-001", "EV-002"]
            data["evaluator_count"] = 2
            data["threshold_profile"] = {
                "profile_id": "REVIEWER-PROFILE-001",
                "version": "1.0",
                "approved_by": "reviewer-ref",
                "decision_authority": "authority-ref",
                "metrics": {"exact_agreement": 0.8},
            }
            manifest_path = self.write_manifest(directory, data)
            ratings = validator.read_ratings_csv(csv_path)
            manifest = validator.load_manifest(manifest_path, csv_path, ratings)
            result = validator.evaluate(ratings, manifest)
            self.assertEqual(result["decision"], "REVIEW")
            self.assertEqual(result["metrics"]["scored_pair_count"], 0)


if __name__ == "__main__":
    unittest.main()
