"""Guardian Agent — deterministic AI governance runtime.

Composes VIL (signal gate), CASA policy via Diffwall rules (action gate),
and a hash-chained audit ledger behind one govern() call.
"""
from .models import Action, Verdict
from .pipeline import Decision, GuardianAgent, ExecutionAuditError
from .audit import AuditError
from .vil import Route, Signal

__version__ = "1.1.0"
__all__ = ["Action", "Verdict", "Decision", "GuardianAgent", "Route", "Signal",
           "AuditError", "ExecutionAuditError"]
