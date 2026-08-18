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


def _resolve_local_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise SchemaValidationError(f"unsupported schema reference {ref!r}")
    current: Any = root_schema
    for token in ref[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or token not in current:
            raise SchemaValidationError(f"unresolvable schema reference {ref!r}")
        current = current[token]
    if not isinstance(current, dict):
        raise SchemaValidationError(f"schema reference {ref!r} does not resolve to an object")
    return current


def _matches(instance: Any, schema: dict[str, Any], path: str, root_schema: dict[str, Any]) -> bool:
    try:
        validate(instance, schema, path, root_schema)
    except SchemaValidationError:
        return False
    return True


def validate(
    instance: Any,
    schema: dict[str, Any],
    path: str = "$",
    root_schema: dict[str, Any] | None = None,
) -> None:
    root_schema = root_schema or schema

    if "$ref" in schema:
        validate(instance, _resolve_local_ref(root_schema, schema["$ref"]), path, root_schema)

    if "const" in schema and instance != schema["const"]:
        raise SchemaValidationError(f"{path}: {instance!r} does not equal const {schema['const']!r}")

    for sub_schema in schema.get("allOf", []):
        validate(instance, sub_schema, path, root_schema)

    if "oneOf" in schema:
        matches = sum(_matches(instance, sub_schema, path, root_schema) for sub_schema in schema["oneOf"])
        if matches != 1:
            raise SchemaValidationError(f"{path}: expected exactly one oneOf branch to match, got {matches}")

    if "not" in schema and _matches(instance, schema["not"], path, root_schema):
        raise SchemaValidationError(f"{path}: matched prohibited schema")

    if "if" in schema:
        branch = "then" if _matches(instance, schema["if"], path, root_schema) else "else"
        if branch in schema:
            validate(instance, schema[branch], path, root_schema)

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
                validate(value, properties[key], f"{path}.{key}", root_schema)

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
                validate(value, item_schema, f"{path}[{index}]", root_schema)
        contains_schema = schema.get("contains")
        if contains_schema is not None:
            matches = sum(
                _matches(value, contains_schema, f"{path}[{index}]", root_schema)
                for index, value in enumerate(instance)
            )
            minimum = schema.get("minContains", 1)
            if matches < minimum:
                raise SchemaValidationError(f"{path}: requires at least {minimum} matching contains item(s)")

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
    schema = load_json(schema_path)
    validate(instance, schema, root_schema=schema)


def validate_schema_document(schema: dict[str, Any], path: str) -> None:
    required = {"$schema", "$id", "title", "description", "type", "properties", "required"}
    missing = sorted(required - set(schema))
    if missing:
        raise SchemaValidationError(f"{path}: schema document missing {missing}")
    if schema["type"] != "object" or not isinstance(schema["properties"], dict):
        raise SchemaValidationError(f"{path}: canonical schemas must describe an object")
