import re
from datetime import datetime
from pathlib import Path
from typing import Any

from .io import load_json


class SchemaValidationError(ValueError):
    pass


def _type_matches(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(expected, False)


def validate(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    expected = schema.get("type")
    if expected is not None:
        types = expected if isinstance(expected, list) else [expected]
        if not any(_type_matches(instance, item) for item in types):
            raise SchemaValidationError(f"{path}: expected {types}, got {type(instance).__name__}")

    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaValidationError(f"{path}: {instance!r} is not in enum")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        missing = [key for key in required if key not in instance]
        if missing:
            raise SchemaValidationError(f"{path}: missing required fields {missing}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unexpected = sorted(set(instance) - set(properties))
            if unexpected:
                raise SchemaValidationError(f"{path}: unexpected fields {unexpected}")
        for key, value in instance.items():
            if key in properties:
                validate(value, properties[key], f"{path}.{key}")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            raise SchemaValidationError(f"{path}: requires at least {schema['minItems']} items")
        if schema.get("uniqueItems"):
            rendered = [repr(item) for item in instance]
            if len(rendered) != len(set(rendered)):
                raise SchemaValidationError(f"{path}: items must be unique")
        item_schema = schema.get("items")
        if item_schema:
            for index, value in enumerate(instance):
                validate(value, item_schema, f"{path}[{index}]")

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            raise SchemaValidationError(f"{path}: string is too short")
        pattern = schema.get("pattern")
        if pattern and not re.fullmatch(pattern, instance):
            raise SchemaValidationError(f"{path}: does not match {pattern}")
        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(instance.replace("Z", "+00:00"))
            except ValueError as exc:
                raise SchemaValidationError(f"{path}: invalid date-time") from exc

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise SchemaValidationError(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            raise SchemaValidationError(f"{path}: above maximum {schema['maximum']}")


def load_and_validate(instance: Any, schema_path: Path) -> None:
    validate(instance, load_json(schema_path))


def validate_schema_document(schema: dict[str, Any], path: str) -> None:
    required = {"$schema", "$id", "title", "description", "type", "properties", "required"}
    missing = sorted(required - set(schema))
    if missing:
        raise SchemaValidationError(f"{path}: schema document missing {missing}")
    if schema["type"] != "object" or not isinstance(schema["properties"], dict):
        raise SchemaValidationError(f"{path}: canonical schemas must describe an object")
