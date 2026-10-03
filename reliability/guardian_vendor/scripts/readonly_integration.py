"""Runnable scoped integration using only local fixtures and temporary storage.

After installing the wheel, run: python -I scripts/readonly_integration.py
The trusted host approves one exact request. This demonstrates the verifier
contract; it supplies no production authentication, identity or compliance claim.
"""
import copy
import json
import tempfile
from pathlib import Path

from guardian import GuardianAgent
from guardian.adapter import GovernedToolRunner
from guardian.validation import snapshot


def main():
    with tempfile.TemporaryDirectory(prefix="guardian-integration-") as directory:
        root = Path(directory)
        report = root / "weekly-kpi.csv"
        report.write_text("metric,value\nfixture_count,1\n", encoding="utf-8")
        signal = {
            "content": "Read the local fixture report for this integration test. "
                       "The host restricts the tool to a fixed file and approves "
                       "only the exact request defined here.",
            "source": "local-fixture-authority", "signal_score": 9,
            "source_pointers": ["fixture-request", "fixture-scope", "fixture-evidence"],
            "metadata": {"mode": "local fixture", "request": "fixture-read-1",
                         "scope": "weekly-kpi", "operation": "read", "tenant": "fixture"},
        }
        approved = snapshot({"signal": signal, "action": {
            "id": "fixture-read-1", "type": "read_file", "target": "weekly-kpi",
            "payload": json.dumps({"target": "weekly-kpi"}, sort_keys=True),
            "params": {"target": "weekly-kpi"},
        }})

        def verify_exact_request(envelope):
            # This approval comes from trusted host code, never model metadata.
            # A real host must authenticate its request authority and requester.
            return envelope == approved

        calls = []

        def scoped_read(target):
            if target != "weekly-kpi":
                raise ValueError("unsupported target")
            calls.append(target)
            return report.read_text(encoding="utf-8")

        agent = GuardianAgent(root / "audit.jsonl", require_verified_evidence=True,
                              evidence_verifier=verify_exact_request)
        runner = GovernedToolRunner({"read_kpi": scoped_read}, agent,
                                    type_map={"read_kpi": "read_file"})
        allowed = runner.run("read_kpi", {"target": "weekly-kpi"},
                             signal=signal, call_id="fixture-read-1")
        modified_signal = copy.deepcopy(signal)
        modified_signal["metadata"]["tenant"] = "different-tenant"
        modified = runner.run("read_kpi", {"target": "weekly-kpi"},
                              signal=modified_signal, call_id="fixture-read-1")
        changed_target = runner.run("read_kpi", {"target": "../outside"},
                                   signal=signal, call_id="fixture-read-1")
        intact, _ = agent.ledger.verify(expected_head=changed_target["entry_hash"])
        if (not allowed["executed"] or not allowed["evidence_verified"] or
                modified["verdict"] != "HALT" or changed_target["verdict"] != "HALT" or
                len(calls) != 1 or not intact):
            raise RuntimeError("Scoped integration acceptance failed")
        result = {"mode": "local fixture", "allowed": allowed["verdict"],
                  "modified": modified["verdict"], "changed_target": changed_target["verdict"],
                  "calls": len(calls), "audit_intact": intact}
        print(json.dumps(result))
        return result


if __name__ == "__main__":
    main()
