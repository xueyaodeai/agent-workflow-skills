"""Synthetic contract tests; their evidence strings are not real test results."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/orchestrate-projects/scripts/validate_project_docs.py'
SPEC = importlib.util.spec_from_file_location('validate_project_docs', SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

PATHS = '''- Why: Restore the user-requested export behavior for existing callers (R1).
- Shortest path: Fix the current export and verify the agreed scenarios.
- Best path: Same local fix; no new service or migration cost is justified.
- Selected path: Use the existing exporter because it meets all agreed checks.
'''
TASK = '''# Task Plan: Export repair

## Objective
''' + PATHS + '''- Observable result: Export all selected rows exactly once.
- Requirement basis: User request R1.
- Acceptance checks: Select two rows and export; parse the file and compare exact IDs; retain the fixture result.

## Scope
- In scope: Existing exporter and its regression checks only.

## Current state
- Readiness: ready
- Status: in_progress
'''
CLOSEOUT = '''
## Closeout
- Final status: complete
- Result: Fixed exporter in revision abc123.
- Verification result: pass
- Verification: Two-row and empty-selection fixtures pass at abc123; synthetic results.log.
- Delivery boundary: Task-scoped local commit abc123.
'''
DRAFT = '''# Task Plan: Unresolved export request
- Readiness: not_ready
- Readiness blockers: Product owner must decide whether duplicates are retained; implementation depends on that answer.
- Status: not_started
'''
OUTCOME = '''# Outcome Plan: Export repair
''' + PATHS + '''- Readiness: ready
- Final result: User receives an exact export of selected rows.
- Scope and delivery boundary: Existing exporter only; task-scoped commit.
## Acceptance criteria
| Acceptance | Scenario and action | Pass condition | Verification |
|---|---|---|---|
| A1 | Select two distinct rows and export | IDs match exactly | Parse fixture and retain comparison |
## Final completion conditions
- Final acceptance of required outcomes: A1 covers R1.
- Overall result verification: Export and reimport the fixture without lost or duplicate rows.
- Delivery boundary: Verified local commit.
- Tasks ready to start: T1 has the above contract and no prerequisites; implementation still requires authorization.
'''


def milestone(name='M1', state='in_progress'):
    return f'### {name}: Export\n' + PATHS + f'''- Readiness: ready
- Requirements: R1.
- Entry conditions/depends on: Existing fixture available.
- Status: {state}
- Required happy path: Export selected rows and compare their IDs.
- Exit criteria: Exact ID equality in the export fixture; retain the result.
- Current non-goals and accepted deferrals: No new export formats; user request R1.
- Blocker threshold: Required fixture cannot run.
- Stop condition: Agreed scenarios pass and no in-scope blocker remains.
''' + ('- Exit result: pass\n- Exit evidence: Synthetic fixture result at abc123.\n' if state == 'complete' else '')


def roadmap(blocks=None):
    return '''# Project Roadmap: Export
## Outcome and ownership
''' + PATHS + '''- Readiness: ready
- Final observable outcome: Existing callers export selected rows correctly.
## Completion criteria
- [x] A1: Fixture IDs exactly match after export and reimport; keep comparison evidence.
## Constraints and non-goals
- In scope: Existing exporter and required verification.
- Side-effect boundary: Local commit only; no deployment.
## Current milestone
- Milestone: M1
## Milestones
''' + (milestone() if blocks is None else blocks)


class DocumentTests(unittest.TestCase):
    def check(self, text, require_ready=False):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'contract.md'
            path.write_text(text, encoding='utf-8')
            return validator.validate(path, require_ready=require_ready)

    def assert_error(self, text, fragment, **kwargs):
        errors = self.check(text, **kwargs)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_ready_task(self):
        self.assertEqual(self.check(TASK, require_ready=True), [])

    def test_same_shortest_and_best_path_is_valid(self):
        self.assertEqual(self.check(TASK), [])

    def test_minimal_explicit_draft_is_not_an_execution_pass(self):
        self.assertEqual(self.check(DRAFT), [])
        self.assert_error(DRAFT, 'not_ready', require_ready=True)

    def test_missing_task_contract_is_rejected(self):
        self.assert_error('# Task Plan: Empty\n- Status: not_started\n', 'Readiness')

    def test_not_ready_needs_named_gap(self):
        self.assert_error(DRAFT.replace('Product owner must decide whether duplicates are retained; implementation depends on that answer.', 'pending'), 'named Readiness blockers')

    def test_executing_draft_is_rejected(self):
        self.assert_error(DRAFT.replace('not_started', 'in_progress'), 'not_ready')

    def test_ready_contract_requires_each_field(self):
        for label in validator.TASK_LABELS:
            with self.subTest(label=label):
                edited = '\n'.join(line for line in TASK.splitlines() if not line.startswith(f'- {label}:'))
                self.assert_error(edited, label)

    def test_empty_field_does_not_borrow_next_line(self):
        self.assert_error(TASK.replace('Use the existing exporter because it meets all agreed checks.', ''), 'Selected path is empty')

    def test_ready_with_unresolved_path(self):
        self.assert_error(TASK.replace('Use the existing exporter because it meets all agreed checks.', 'pending owner decision'), 'Selected path is empty or unresolved')

    def test_duplicate_field_is_rejected(self):
        self.assert_error(TASK + '- Why: A conflicting reason.\n', 'expected one Why')

    def test_unresolved_readiness_blocker_cannot_be_carried_as_ready(self):
        self.assert_error(TASK + '- Readiness blockers: Waiting for a data-retention decision.\n', 'must remove resolved')

    def test_complete_task_with_current_evidence(self):
        self.assertEqual(self.check(TASK.replace('in_progress', 'complete') + CLOSEOUT), [])

    def test_pending_evidence_is_not_completion_even_with_new_fields(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        for evidence in ('pending', 'pending CI run', 'not run', 'not yet verified', '待验证', ''):
            with self.subTest(evidence=evidence):
                edited = text.replace('Two-row and empty-selection fixtures pass at abc123; synthetic results.log.', evidence)
                self.assert_error(edited, 'Verification is empty or unresolved')

    def test_result_must_be_explicit_pass(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        for result in ('fail', 'blocked', 'pending'):
            with self.subTest(result=result):
                self.assert_error(text.replace('Verification result: pass', f'Verification result: {result}'), 'Verification result: pass')

    def test_blocked_and_complete_contradiction(self):
        self.assert_error(TASK.replace('in_progress', 'blocked') + CLOSEOUT, 'contradicts Final status')

    def test_current_complete_cannot_bypass_closeout(self):
        self.assert_error(TASK.replace('in_progress', 'complete'), 'requires Final status')

    def test_complete_empty_evidence_section_is_not_sufficient(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text = '\n'.join(line for line in text.splitlines() if not line.startswith('- Verification:'))
        self.assert_error(text + '\n## Verification evidence\n', 'expected one Verification')

    def test_unchecked_criteria_block_completion(self):
        self.assert_error(TASK.replace('in_progress', 'complete') + CLOSEOUT + '- [ ] Required fixture.\n', 'unchecked')

    def test_nested_unchecked_criteria_block_completion(self):
        self.assert_error(TASK.replace('in_progress', 'complete') + CLOSEOUT + '  - [ ] Required fixture.\n', 'unchecked')

    def test_invalid_state_is_not_silently_ignored(self):
        for state in ('partial', 'COMPLETE', 'unknown-state', ''):
            with self.subTest(state=state):
                self.assertTrue(self.check(TASK.replace('in_progress', state)))

    def test_unknown_format_is_not_a_pass(self):
        self.assert_error('# Custom ledger\nAll done.\n', 'unsupported artifact')

    def test_bare_outcome_plan_is_not_a_pass(self):
        self.assert_error('# Outcome Plan: Empty\n', 'Readiness')

    def test_ready_outcome_plan(self):
        self.assertEqual(self.check(OUTCOME, require_ready=True), [])

    def test_outcome_requires_actual_acceptance_content(self):
        text = OUTCOME.split('## Acceptance criteria')[0] + '## Acceptance criteria\n'
        self.assert_error(text, 'empty Acceptance criteria')

    def test_outcome_acceptance_header_is_not_coverage(self):
        text = OUTCOME.replace('| A1 | Select two distinct rows and export | IDs match exactly | Parse fixture and retain comparison |\n', '')
        self.assert_error(text, 'no valid data rows')

    def test_outcome_plan_is_not_implementation_closeout(self):
        self.assert_error(OUTCOME + '- Final status: complete\n', 'not implementation closeout')

    def test_each_milestone_needs_its_own_contract(self):
        text = roadmap(milestone() + '\n### M2: Another export\n- Readiness: ready\n- Status: in_progress\n')
        self.assert_error(text, 'M2: expected one Why')
        self.assert_error(text, 'M2: expected one Exit criteria')

    def test_valid_two_milestone_roadmap(self):
        self.assertEqual(self.check(roadmap(milestone() + '\n' + milestone('M2')), require_ready=True), [])

    def test_future_draft_does_not_block_ready_current_milestone(self):
        future = '\n### M2: Later\n- Readiness: not_ready\n- Readiness blockers: Refine after M1 confirms the format decision.\n- Status: not_started\n'
        self.assertEqual(self.check(roadmap(milestone() + future), require_ready=True), [])

    def test_selected_draft_is_rejected(self):
        block = '### M1: Discovery needed\n- Readiness: not_ready\n- Readiness blockers: Owner must decide format.\n- Status: not_started\n'
        self.assert_error(roadmap(block), 'M1: not_ready', require_ready=True)

    def test_unknown_current_milestone_is_rejected_for_start(self):
        self.assert_error(roadmap().replace('- Milestone: M1', '- Milestone: M9'), 'resolvable current', require_ready=True)

    def test_root_not_ready_blocks_executing_milestone(self):
        text = roadmap().replace('- Readiness: ready', '- Readiness: not_ready\n- Readiness blockers: Root acceptance unresolved.', 1)
        self.assert_error(text, 'not_ready')

    def test_duplicate_milestones_are_rejected(self):
        self.assert_error(roadmap(milestone() + milestone()), 'duplicate milestone')

    def test_complete_milestone_needs_pass_and_evidence(self):
        self.assert_error(roadmap(milestone(state='complete').replace('Exit result: pass', 'Exit result: pending')), 'Exit result: pass')

    def test_complete_roadmap(self):
        closeout = '''\n## Evidence index
| Subject/version | Evidence | Observed at | Result | Location |
|---|---|---|---|---|
| abc123 | Synthetic fixture | 2026-10-16 | pass | results.log |
## Project closeout
- Final status: complete
- Completion result: pass
- Completion evidence: Synthetic full-flow check at abc123 in results.log.
'''
        self.assertEqual(self.check(roadmap(milestone(state='complete')) + closeout), [])
        self.assert_error(roadmap() + closeout, 'milestone is unfinished')

    def test_historical_failure_word_is_not_current_failure(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text += '\n## Historical investigation\n| Case | Result |\n|---|---|\n| old snapshot | fail |\n'
        self.assertEqual(self.check(text), [])

    def test_current_failure_table_blocks_closeout(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text += '| Check | Result |\n|---|---|\n| current flow | fail |\n'
        self.assert_error(text, 'completion contradicts Closeout')

    def test_coordination_addon_open_blocker_blocks_completion(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text += """
## Coordination add-on
### Blockers and required decisions
| Blocker | Impact | Owner and smallest required action | Status |
|---|---|---|---|
| Missing fixture | Acceptance incomplete | Owner restores fixture | open |
"""
        self.assert_error(text, 'completion contradicts Blockers and required decisions')
        self.assertEqual(self.check(text.replace('| open |', '| resolved |')), [])

    def test_current_verification_evidence_blocks_completion(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        for level in ('##', '###'):
            for result in ('fail', 'blocked', 'pending'):
                with self.subTest(level=level, result=result):
                    evidence = f'\n{level} Verification evidence\n| Check | Result |\n|---|---|\n| Current acceptance | {result} |\n'
                    self.assert_error(text + evidence, 'completion contradicts Verification evidence')

    def test_historical_subsection_is_not_current_verification(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text += """
## Verification evidence
| Check | Result |
|---|---|
| Current acceptance | pass |
### Historical investigation
| Check | Result |
|---|---|
| Previous revision | fail |
"""
        self.assertEqual(self.check(text), [])

    def test_separate_current_tables_use_their_own_columns(self):
        text = TASK.replace('in_progress', 'complete') + CLOSEOUT
        text += """
## Verification evidence
| Check | Result |
|---|---|
| Unit checks | pass |

| Result | Check |
|---|---|
| fail | Current integration |
"""
        self.assert_error(text, 'completion contradicts Verification evidence')

    def test_fenced_examples_are_not_live_state(self):
        example = '\n```md\n- Status: partial\n- Why: <example>\n- [ ] Not a live check\n```\n'
        self.assertEqual(self.check(TASK + example), [])

    def test_alignment_states_remain_supported(self):
        text = '# Next-Round Roadmap Alignment Notes: Next\n- Status: aligned\n- Generation status: reconciled\n'
        self.assertEqual(self.check(text), [])
        self.assert_error(text, '--require-ready supports only', require_ready=True)

    def test_audit_gate_rules_remain_supported(self):
        text = '''# Milestone Audit: M1
- Frozen milestone contract: roadmap.md M1.
- Scope-change authority: User.
## Exit-criteria assessment
| Exit criterion | Evidence required | Evidence observed | Verdict |
|---|---|---|---|
| A1 | Fixture result | Synthetic pass at abc123 | pass |
## Findings
| Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |
|---|---|---|---|---|---|
## Decision
- Decision: advance
'''
        self.assertEqual(self.check(text), [])
        self.assert_error(text.replace('| pass |', '| fail |'), 'failed or blocked evidence')

    def test_no_dependencies_or_deferrals_is_a_valid_explicit_value(self):
        block = milestone().replace('Existing fixture available.', 'none').replace('No new export formats; user request R1.', 'none')
        self.assertEqual(self.check(roadmap(block)), [])

    def test_url_autolink_is_not_a_placeholder(self):
        self.assertEqual(self.check(TASK.replace('User request R1.', 'User request R1 at <https://example.test/requirements>.')), [])

    def test_invalid_result_state_is_rejected_before_closeout(self):
        self.assert_error(TASK + '- Verification result: MAYBE\n', 'invalid Verification result')

    def test_missing_and_non_utf8_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'missing.md'
            self.assertIn('cannot read', validator.validate(path)[0])
            path.write_bytes(b'\xff')
            self.assertIn('cannot read', validator.validate(path)[0])

    def test_cli_exit_codes_and_structural_label(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'draft.md'
            path.write_text(DRAFT, encoding='utf-8')
            valid = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            rejected = subprocess.run([sys.executable, str(SCRIPT), '--require-ready', str(path)], capture_output=True, text=True)
            self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)
            self.assertIn('[VALID]', valid.stdout)
            self.assertEqual(rejected.returncode, 1)
            self.assertIn('not_ready', rejected.stdout)


if __name__ == '__main__':
    unittest.main()
