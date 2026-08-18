from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / "config"
SCHEMA_DIR = ROOT / "schemas"
RECEIPT_DIR = ROOT / "receipts"


def resolve_fixture(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_dir():
        return candidate / "run.json"
    if candidate.is_file():
        return candidate
    named = ROOT / "fixtures" / value / "run.json"
    if named.is_file():
        return named
    raise FileNotFoundError(f"Fixture not found: {value}")
