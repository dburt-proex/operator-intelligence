"""Bounded, strict JSON input validation shared by every execution boundary."""
import json
import math

MAX_BYTES = 1_048_576


def snapshot(value):
    """Copy plain JSON data; reject coercions, non-finite numbers and deep input."""
    remaining = MAX_BYTES

    def charge(size):
        nonlocal remaining
        remaining -= size
        if remaining < 0:
            raise ValueError("JSON input exceeds size limit")

    def walk(item, depth=0):
        if depth > 32:
            raise ValueError("JSON nesting exceeds limit")
        # Charge a lower bound before serialization. Exact escaping/number sizes
        # are checked below. This bounds traversal and allocation for huge input.
        if type(item) is str:
            charge(len(item) + 2)
            return
        if type(item) is int:
            # Four binary digits require at least one decimal digit. Avoid
            # converting enormous integers even if the host disables its limit.
            charge(max(1, (item.bit_length() - 1) // 4))
            return
        if item is None or type(item) is bool:
            charge(1)
            return
        if type(item) is float and math.isfinite(item):
            charge(1)
            return
        if type(item) is list:
            charge(2 + max(0, len(item) - 1))
            for child in item:
                walk(child, depth + 1)
            return
        if type(item) is dict:
            charge(2 + max(0, len(item) - 1))
            for key, child in item.items():
                if type(key) is not str:
                    raise ValueError("JSON object keys must be strings")
                charge(len(key) + 3)
                walk(child, depth + 1)
            return
        raise ValueError("Input must contain only finite JSON values")

    walk(value)
    encoded = json.dumps(value, allow_nan=False, ensure_ascii=True)
    if len(encoded) > MAX_BYTES:
        raise ValueError("JSON input exceeds size limit")
    return json.loads(encoded)


def fields(data, allowed):
    if type(data) is not dict or set(data) - set(allowed):
        raise ValueError("Expected an object with supported fields")


def text(value, name, required=False):
    if type(value) is not str or (required and not value.strip()):
        raise ValueError(f"{name} must be a nonempty string" if required else
                         f"{name} must be a string")
    return value


def strings(value, name):
    if type(value) is not list:
        raise ValueError(f"{name} must be a string array")
    return [text(item, name, required=True) for item in value]
