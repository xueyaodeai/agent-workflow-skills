from __future__ import annotations

import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    REPOSITORY_ROOT
    / "skills"
    / "orchestrate-projects"
    / "scripts"
    / "validate_project_docs.py"
)
SPEC = importlib.util.spec_from_file_location("validate_project_docs", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def validate_text(text: str) -> list[str]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "artifact.md"
        path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")
        return VALIDATOR.validate(path)


class MilestoneAuditValidationTests(unittest.TestCase):
    def audit(self, decision: str, verdict: str = "pass", finding: str = "") -> str:
        return f"""
            # Milestone Audit: M1

            ## Audit scope

            - Frozen milestone contract: roadmap.md#current-milestone
            - Scope-change authority: project owner

            ## Exit-criteria assessment

            | Exit criterion | Evidence required | Evidence observed | Verdict |
            |---|---|---|---|
            | happy path | integration test | run-123 | {verdict} |

            ## Findings

            | Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |
            |---|---|---|---|---|---|
            {finding}

            ## Gate decision

            - Decision: `{decision}`
        """

    def test_advance_accepts_passing_audit_without_blockers(self) -> None:
        self.assertEqual(validate_text(self.audit("advance")), [])

    def test_advance_rejects_unresolved_blocker(self) -> None:
        finding = (
            "| blocker | regression | public contract | diff and test | fix parser | unresolved |"
        )
        errors = validate_text(self.audit("advance", finding=finding))
        self.assertIn("gate advances while unresolved blockers remain", errors)

    def test_advance_rejects_failed_exit_criterion(self) -> None:
        errors = validate_text(self.audit("advance", verdict="fail"))
        self.assertIn(
            "gate advances while failed or blocked evidence remains: fail",
            errors,
        )

    def test_audit_requires_exit_criteria_data(self) -> None:
        errors = validate_text(
            """
            # Milestone Audit: M1

            ## Audit scope

            - Frozen milestone contract: roadmap.md#current-milestone
            - Scope-change authority: project owner

            ## Findings

            | Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |
            |---|---|---|---|---|---|

            ## Gate decision

            - Decision: `advance`
            """
        )
        self.assertIn("missing Exit-criteria assessment table", errors)
        self.assertIn("exit-criteria assessment has no data rows", errors)

    def test_audit_rejects_invalid_exit_verdict(self) -> None:
        errors = validate_text(self.audit("advance", verdict="failed"))
        self.assertIn("invalid exit verdict: failed", errors)

    def test_audit_rejects_legacy_five_column_findings_table(self) -> None:
        text = self.audit("advance").replace(
            "| Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |\n"
            "            |---|---|---|---|---|---|",
            "| Severity | Finding | Contract or rule violated | Evidence | Disposition |\n"
            "            |---|---|---|---|---|",
        ).replace(
            "            \n\n            ## Gate decision",
            "            | blocker | regression | public contract | evidence | resolved |\n\n"
            "            ## Gate decision",
        )
        errors = validate_text(text)
        self.assertIn("invalid Findings table header", errors)

    def test_audit_rejects_invalid_finding_severity(self) -> None:
        finding = (
            "| critical | regression | public contract | diff and test | fix parser | unresolved |"
        )
        errors = validate_text(self.audit("user_decision_required", finding=finding))
        self.assertIn("invalid finding severity: critical", errors)

    def test_do_not_advance_requires_unresolved_blocker(self) -> None:
        errors = validate_text(self.audit("do_not_advance"))
        self.assertIn("gate does not advance without an unresolved blocker", errors)

    def test_do_not_advance_accepts_unresolved_blocker(self) -> None:
        finding = (
            "| blocker | regression | public contract | diff and test | fix parser | unresolved |"
        )
        self.assertEqual(
            validate_text(self.audit("do_not_advance", finding=finding)),
            [],
        )

    def test_audit_requires_frozen_contract_reference_and_scope_authority(self) -> None:
        errors = validate_text(
            """
            # Milestone Audit: M1

            ## Gate decision

            - Decision: `advance`
            """
        )
        self.assertTrue(
            any(error.startswith("missing audit contract fields:") for error in errors)
        )


class RoadmapContractValidationTests(unittest.TestCase):
    def test_roadmap_requires_frozen_contract_fields(self) -> None:
        errors = validate_text(
            """
            # Project Roadmap: Demo

            - Status: `in_progress`
            """
        )
        self.assertTrue(
            any(
                error.startswith("missing frozen milestone contract fields:")
                for error in errors
            )
        )

    def test_roadmap_accepts_complete_frozen_contract(self) -> None:
        errors = validate_text(
            """
            # Project Roadmap: Demo

            - Status: `in_progress`
            - Required happy path: sample.json to report.csv
            - Exit criteria: end-to-end test passes
            - Current non-goals and accepted deferrals: remote upload deferred by owner
            - Blocker threshold: required flow or protected behavior regresses
            - Stop condition: exit evidence is complete
            """
        )
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
