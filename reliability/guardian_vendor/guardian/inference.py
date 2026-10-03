"""Explicit host-authorized inference profile; generic policy stays fail closed."""
from .models import Action, RuleResult, Verdict, most_restrictive
from .pipeline import GuardianAgent
from .validation import snapshot


class AuthorizedInferenceGuardian(GuardianAgent):
    """Admit one exact outbound-inference action verified by trusted host code.

    The constructor is an authority boundary, never a model-controlled API.
    Network confinement and credential handling remain executor responsibilities.
    """

    def __init__(self, ledger_path, *, authorized_action, evidence_verifier):
        expected = Action.from_dict(authorized_action)
        params = expected.params
        required = {
            "scope": "AR-001", "data_class": "SYNTHETIC_EXPERIMENT_EVIDENCE",
            "network": "api.openai.com", "credential": "OPENAI_API_KEY",
            "mutation": False, "authorization": "ALLOW_TO_RUN_PILOT",
            "evaluated_agent_tool_count": 0, "automatic_inference_retries": 0,
            "store": False,
        }
        if (expected.type != "external_model_execution" or
                expected.target != "https://api.openai.com/v1/responses" or
                any(type(params.get(k)) is not type(v) or params[k] != v
                    for k, v in required.items()) or
                type(params.get("argv")) is not list or not params["argv"] or
                any(type(arg) is not str or not arg for arg in params["argv"])):
            raise ValueError("Unsupported authorized inference contract")
        if not callable(evidence_verifier):
            raise ValueError("Trusted inference evidence verifier required")
        self._authorized_action = snapshot(vars(expected))
        self._host_verifier = evidence_verifier
        super().__init__(ledger_path, evidence_verifier=self._verify_inference,
                         require_verified_evidence=True)

    def _verify_inference(self, envelope):
        return (vars(Action.from_dict(envelope["action"])) == self._authorized_action
                and self._host_verifier(snapshot(envelope)) is True)

    def _policy_report(self, action):
        report = super()._policy_report(action)
        if vars(action) == self._authorized_action:
            rule = RuleResult("R7_AUTHORIZED_INFERENCE", Verdict.ALLOW, True,
                              "Exact host-authorized synthetic AR-001 inference contract.")
            report.results.append(rule)
            matched = [r for r in report.results if r.matched]
            report.verdict = most_restrictive(r.verdict for r in matched)
            report.triggered_by = [r.rule for r in matched if r.verdict == report.verdict]
        return report
