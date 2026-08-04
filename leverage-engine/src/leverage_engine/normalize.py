import re
from copy import deepcopy
from typing import Any


INJECTION_PATTERNS = (
    r"ignore (all |any )?(previous|prior) instructions",
    r"system prompt",
    r"reveal (a |the )?(secret|credential|token)",
    r"bypass (the )?(policy|approval|gate)",
)


def normalize_signal(signal: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(signal)
    result["title"] = " ".join(result["title"].split())
    result["summary"] = " ".join(result["summary"].split())
    untrusted_text = f"{result['title']} {result['summary']}".lower()
    detected = any(re.search(pattern, untrusted_text) for pattern in INJECTION_PATTERNS)
    result["untrusted_instruction_detected"] = detected
    if detected and result["validation_state"] == "validated":
        result["validation_state"] = "validation_required"
    return result
