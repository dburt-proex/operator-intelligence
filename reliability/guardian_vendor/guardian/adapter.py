"""Governed tool runner — Guardian as a drop-in pre-tool hook.

Wraps any agent framework's tool-execution step. Framework-agnostic and
stdlib-only; the Anthropic tool_use block shape is supported directly.

    runner = GovernedToolRunner(tools={"read_file": read_file, ...},
                                agent=GuardianAgent("audit.jsonl"))
    result = runner.run("wire_transfer", {"amount": "$12,000"}, signal=ctx)
    # -> {"verdict": "HALT", "blocked": True, ...}; tool never called

Mapping law: tool name -> Action.type (override via type_map), tool input
-> Action.params/payload. Governance verdict decides:
    ALLOW  -> tool executes, output returned
    REVIEW -> tool NOT executed; pending record returned for a human queue
    HALT   -> tool NOT executed; blocked record returned
Every call is ledgered before any execution (KING-file law).
"""
from __future__ import annotations

import json
import uuid
from typing import Callable, Dict, Optional

from .models import Verdict
from .pipeline import GuardianAgent
from .validation import snapshot, text
from types import MappingProxyType
import inspect
from .engine import validate
from .models import Action

# Fallback signal for callers that supply no context. Deliberately weak:
# it routes to CLARIFY -> HALT, so ungrounded tool calls fail safe instead
# of sneaking through on a neutral score.
_NO_SIGNAL = {"content": "", "source": "unknown", "signal_score": 0.0}


class GovernedToolRunner:
    def __init__(self, tools: Dict[str, Callable], agent: GuardianAgent,
                 type_map: Optional[Dict[str, str]] = None,
                 default_signal: Optional[dict] = None):
        if type(tools) is not dict or any(type(k) is not str or not callable(v) for k, v in tools.items()):
            raise ValueError("tools must map names to callables")
        self.tools = MappingProxyType(dict(tools))
        if any(inspect.iscoroutinefunction(v) or inspect.isasyncgenfunction(v) for v in tools.values()):
            raise ValueError("Async tools require a synchronous execution wrapper")
        self.agent = agent
        mappings = snapshot({} if type_map is None else type_map)
        if type(mappings) is not dict:
            raise ValueError("type_map must be an object")
        self.type_map = MappingProxyType(mappings)
        rank = {Verdict.ALLOW: 0, Verdict.REVIEW: 1, Verdict.HALT: 2}
        for name, kind in self.type_map.items():
            original = validate(Action("registration", name))
            mapped = validate(Action("registration", kind))
            if (original.triggered_by != ["DEFAULT_FAIL_SAFE"] and
                    rank[mapped.verdict] < rank[original.verdict]):
                raise ValueError("type_map cannot weaken a recognized tool policy")
        self.default_signal = snapshot(default_signal)

    def _envelope(self, tool_name: str, tool_input: dict,
                  signal: Optional[dict], call_id: str) -> dict:
        return {
            "signal": signal if signal is not None else (
                self.default_signal if self.default_signal is not None else _NO_SIGNAL),
            "action": {
                "id": call_id,
                "type": self.type_map.get(tool_name, tool_name),
                "target": text(tool_input.get("target",
                               tool_input.get("path", tool_input.get("to", ""))), "target"),
                "payload": json.dumps(tool_input, sort_keys=True),
                "params": tool_input,
            },
        }

    def run(self, tool_name: str, tool_input: dict,
            signal: Optional[dict] = None,
            call_id: Optional[str] = None) -> dict:
        """Govern one tool call. Returns a JSON-safe result dict; the wrapped
        tool runs only on ALLOW."""
        call_id = call_id if call_id is not None else f"tool-{uuid.uuid4().hex}"
        try:
            text(tool_name, "tool_name", required=True)
            text(call_id, "call_id", required=True)
            if len(tool_name) > 64 or len(call_id) > 128:
                raise ValueError("Tool identifier exceeds limit")
            tool_input = snapshot(tool_input)
            if type(tool_input) is not dict:
                raise ValueError("tool_input must be an object")
            envelope = self._envelope(tool_name, tool_input, signal, call_id)
        except (ValueError, TypeError, OverflowError, RecursionError):
            return self._reject()

        tool = self.tools.get(tool_name)
        if tool is None:
            # Unknown tool: still govern + ledger, never execute.
            envelope["action"]["type"] = "unknown_tool"
            d = self.agent.govern(envelope)
            return self._out(d, call_id, tool_name,
                             error="unknown tool")

        d = self.agent.govern_and_execute(
            envelope, lambda a, _t=tool: _t(**a.params))
        return self._out(d, call_id, tool_name)

    def handle_tool_use_block(self, block: dict,
                              signal: Optional[dict] = None) -> dict:
        """Accept a bounded tool_use block; return its correlated tool_result.

        Malformed blocks are recorded as HALT before raising ValueError.
        Audit failures propagate; no successful rejection receipt is invented.
        """
        try:
            block = snapshot(block)
            if (type(block) is not dict or set(block) != {"type", "id", "name", "input"} or
                    block["type"] != "tool_use" or type(block["input"]) is not dict):
                raise ValueError("Invalid block shape")
            text(block["id"], "id", required=True)
            text(block["name"], "name", required=True)
            if len(block["id"]) > 128 or len(block["name"]) > 64:
                raise ValueError("Tool identifier exceeds limit")
        except (ValueError, TypeError, OverflowError, RecursionError):
            self._reject()
            raise ValueError("Invalid tool_use block; rejected action recorded") from None
        out = self.run(block["name"], block["input"],
                       signal=signal, call_id=block["id"])
        return {
            "type": "tool_result",
            "tool_use_id": block["id"],
            "is_error": out["verdict"] != Verdict.ALLOW.value or not out["executed"] or bool(out["error"]),
            "content": json.dumps(out),
        }

    def _reject(self):
        decision = self.agent.govern({})
        return self._out(decision, "invalid", "invalid", error="invalid tool request")

    @staticmethod
    def _out(decision, call_id: str, tool_name: str, error: str = "") -> dict:
        return {
            "call_id": call_id,
            "tool": tool_name,
            "verdict": decision.verdict.value,
            "executed": decision.executed,
            "output": decision.execution_result,
            "pending_review": decision.verdict is Verdict.REVIEW,
            "blocked": decision.verdict is Verdict.HALT,
            "reasons": decision.reasons,
            "entry_hash": decision.entry_hash,
            "error": error or decision.execution_error,
            "attempted": decision.attempted,
            "decision_hash": decision.decision_hash,
            "action_hash": decision.action_hash,
            "evidence_verified": decision.evidence_verified,
        }
