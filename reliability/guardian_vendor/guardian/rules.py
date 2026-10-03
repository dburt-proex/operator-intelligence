"""First CASA-enforcing rule set for agent actions.

Each rule inspects a proposed Action and returns a RuleResult. A rule either
matches (its verdict applies) or not. The engine merges matched verdicts by
taking the most restrictive one.

Rule tiers:
    HALT   — R1 irreversible destruction, R2 financial transfer, R3 exposed secret
    REVIEW — R4 public broadcast, R5 data mutation
    ALLOW  — R6 read-only
"""
from __future__ import annotations

import re
from typing import Callable

from .models import Action, RuleResult, Verdict

Rule = Callable[[Action], RuleResult]


def _result(rule, verdict, matched, reason="", fix="") -> RuleResult:
    return RuleResult(rule=rule, verdict=verdict, matched=matched,
                      reason=reason, suggested_fix=fix)


def _any(patterns, text) -> bool:
    return any(p.search(text) for p in patterns)


# ----------------------------------------------------------------------------
# R1 — Irreversible destruction → HALT
# ----------------------------------------------------------------------------
_R1_TYPES = {
    "delete_database", "drop_table", "wipe", "purge", "destroy",
    "factory_reset", "delete_all",
}
_R1_PATTERNS = [re.compile(p) for p in [
    r"rm\s+-rf",
    r"\brm\s+(?:-[a-z]+\s+)*-[a-z]*r[a-z]*\b",
    r"\bremove-item\b[\s\S]{0,512}\s-recurse\b",
    r"\brmdir\s+/s\b",
    r"drop\s+table",
    r"drop\s+database",
    r"truncate\s+table",
    r"delete\s+from\b[\s\S]{0,512}\bwhere\s+1\s*=\s*1",
    r"format\s+[\s\S]{0,512}\bdrive\b",
    r"\bgit\s+reset\s+[^\n]{0,128}--hard\b",
    r"\bgit\s+clean\s+[^\n]{0,128}(?:-[a-z]*f[a-z]*\b|--force\b)",
]]


def r1_irreversible_destruction(a: Action) -> RuleResult:
    rid = "R1_IRREVERSIBLE_DESTRUCTION"
    hit = a.type in _R1_TYPES or _any(_R1_PATTERNS, a.searchable_text())
    argv = a.params.get("argv", [])
    if type(argv) is list and all(type(arg) is str for arg in argv):
        tokens = [arg.lower() for arg in argv]
        hit = hit or _any(_R1_PATTERNS, " ".join(tokens))
        if tokens and tokens[0] in {"git", "git.exe"}:
            tokens = tokens[1:]
        if tokens:
            hit = hit or (tokens[0] == "reset" and "--hard" in tokens)
            hit = hit or (tokens[0] == "clean" and any(
                arg == "--force" or (arg.startswith("-") and not arg.startswith("--") and "f" in arg)
                for arg in tokens[1:]))
    if hit:
        return _result(rid, Verdict.HALT, True,
                       "Action performs irreversible data destruction.",
                       "Require explicit human approval and a verified backup before proceeding.")
    return _result(rid, Verdict.HALT, False)


# ----------------------------------------------------------------------------
# R2 — Financial transfer → HALT
# ----------------------------------------------------------------------------
_R2_TYPES = {
    "transfer_funds", "payment", "withdraw", "wire_transfer",
    "send_money", "charge_card", "crypto_transfer",
}
_R2_PATTERNS = [re.compile(p) for p in [
    r"\b(transfer|wire|withdraw)\b[\s\S]{0,512}\b(amount|usd|btc|eth)\b",
    r"\b(transfer|wire|withdraw)\b[\s\S]{0,512}\$\s*\d",
    r"\bsend\b[\s\S]{0,512}\b(usd|btc|eth)\b",
]]


def r2_financial_transfer(a: Action) -> RuleResult:
    rid = "R2_FINANCIAL_TRANSFER"
    hit = a.type in _R2_TYPES or _any(_R2_PATTERNS, a.searchable_text())
    if hit:
        return _result(rid, Verdict.HALT, True,
                       "Action moves funds or financial value.",
                       "Route to a human approver with transaction limits and out-of-band confirmation.")
    return _result(rid, Verdict.HALT, False)


# ----------------------------------------------------------------------------
# R3 — Exposed secret → HALT  (case-sensitive; uses raw_text)
# ----------------------------------------------------------------------------
_R3_PATTERNS = [re.compile(p, re.IGNORECASE) for p in [
    r"sk-[a-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"password\s*[:=]",
    r"api_key\s*[:=]",
    r'["\']?(?:password|passwd|api[_-]?key|access[_-]?token|secret)["\']?\s*[:=]',
    r"\bbearer\s+[a-z0-9._~+/=-]{8,}",
    r"github_pat_[a-z0-9_]{20,}",
    r"ghp_[a-z0-9]{20,}",
    r"xox[baprs]-[a-z0-9-]+",
]]


def r3_exposed_secret(a: Action) -> RuleResult:
    rid = "R3_EXPOSED_SECRET"
    hit = _any(_R3_PATTERNS, a.raw_text())
    if hit:
        return _result(rid, Verdict.HALT, True,
                       "Action payload contains a credential/secret pattern.",
                       "Strip the secret; load from a secrets manager or env var at runtime.")
    return _result(rid, Verdict.HALT, False)


# ----------------------------------------------------------------------------
# R4 — Public broadcast → REVIEW (default) | HALT (KING-file strict mode)
# Diffwall v1 shipped R4 as REVIEW; the Guardian KING file specifies HALT.
# R4_TIER makes the tier an explicit, auditable configuration constant.
# ----------------------------------------------------------------------------
R4_TIER = Verdict.REVIEW

_R4_TYPES = {
    "post_public", "publish", "send_email", "send_sms",
    "tweet", "social_post", "press_release",
}


def r4_public_broadcast(a: Action) -> RuleResult:
    rid = "R4_PUBLIC_BROADCAST"
    if a.type in _R4_TYPES:
        return _result(rid, R4_TIER, True,
                       "Action broadcasts content externally.",
                       "Have a human review recipients and content before sending.")
    return _result(rid, R4_TIER, False)


# ----------------------------------------------------------------------------
# R5 — Data mutation → REVIEW
# ----------------------------------------------------------------------------
_R5_TYPES = {
    "db_write", "file_write", "update_record", "create_record",
    "config_change", "deploy",
    "shell", "shell_command", "tool_call", "git", "git_operation",
}


def r5_data_mutation(a: Action) -> RuleResult:
    rid = "R5_DATA_MUTATION"
    if a.type in _R5_TYPES:
        return _result(rid, Verdict.REVIEW, True,
                       "Action mutates persistent state.",
                       "Confirm scope and ensure the change is reversible or backed up.")
    return _result(rid, Verdict.REVIEW, False)


# ----------------------------------------------------------------------------
# R6 — Read-only → ALLOW
# ----------------------------------------------------------------------------
_R6_TYPES = {
    "read_file", "query", "fetch", "list", "search",
    "get", "describe", "summarize",
}


def r6_read_only(a: Action) -> RuleResult:
    rid = "R6_READ_ONLY"
    # Generic query/fetch/get names do not establish read-only behavior.
    ambiguous = a.type in {"query", "fetch", "get"}
    mutation = bool(re.search(r"\b(insert|update|delete|alter|create|merge|replace|grant|revoke)\b", a.searchable_text()))
    if a.type in _R6_TYPES and (ambiguous or mutation):
        return _result(rid, Verdict.REVIEW, True,
                       "Read-only behavior is ambiguous or mutation text is present.",
                       "Use an explicitly scoped read-only tool and review the request.")
    if a.type in _R6_TYPES and not ambiguous and not mutation:
        return _result(rid, Verdict.ALLOW, True,
                       "Action is read-only / non-mutating.")
    return _result(rid, Verdict.ALLOW, False)


RULES: tuple[Rule, ...] = (
    r1_irreversible_destruction,
    r2_financial_transfer,
    r3_exposed_secret,
    r4_public_broadcast,
    r5_data_mutation,
    r6_read_only,
)
