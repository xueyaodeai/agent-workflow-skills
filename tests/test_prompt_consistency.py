"""Static drift checks only: these assertions do not measure model behavior."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('plan-outcomes', 'orchestrate-projects', 'prepare-agent-handoff',
          'dispatch-dida365-agent-tasks', 'triage-dida365-inbox', 'organize-dida365')
EXPLICIT = ('dispatch-dida365-agent-tasks', 'triage-dida365-inbox', 'organize-dida365')


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


class PromptConsistencyTests(unittest.TestCase):
    def test_common_and_codex_readiness_sections_match(self):
        sections = [read(f'templates/{host}/AGENTS.md').split('## Execution readiness\n', 1)[1].split('## Act\n', 1)[0]
                    for host in ('common', 'codex')]
        self.assertEqual(*sections)

    def test_common_and_codex_minimum_complexity_sections_match(self):
        sections = [read(f'templates/{host}/AGENTS.md').split('## Minimum Complexity\n', 1)[1].split('## Verify\n', 1)[0]
                    for host in ('common', 'codex')]
        self.assertEqual(*sections)
        self.assertIn('--git-common-dir', sections[0])
        self.assertIn('out of version control by default', sections[0])

    def test_skills_keep_process_ledgers_out_of_git_by_default(self):
        for path in ('skills/orchestrate-projects/SKILL.md',
                     'skills/orchestrate-projects/references/git-delivery.md',
                     'skills/plan-outcomes/SKILL.md',
                     'skills/prepare-agent-handoff/SKILL.md'):
            text = read(path)
            with self.subTest(path=path):
                self.assertIn('--git-common-dir', text)

    def test_each_standalone_skill_has_the_semantic_guard(self):
        # Intentional small overlap: standalone installs cannot depend on siblings.
        for skill in SKILLS:
            text = read(f'skills/{skill}/SKILL.md').lower()
            with self.subTest(skill=skill):
                for term in ('why', 'shortest', 'best', 'acceptance', 'direct', 'ready', 'do not invent', 'reuse'):
                    self.assertIn(term, text)
                self.assertNotIn('../', text)

    def test_explicit_only_skills_remain_explicit(self):
        for skill in EXPLICIT:
            text = read(f'skills/{skill}/SKILL.md')
            header = text.split('---', 2)[1]
            self.assertIn('disable-model-invocation: true', header)
            self.assertIn('allow_implicit_invocation: false', read(f'skills/{skill}/agents/openai.yaml'))

    def test_dispatch_default_does_not_force_reselection(self):
        text = read('skills/dispatch-dida365-agent-tasks/agents/openai.yaml')
        self.assertIn('only when my selection is unclear', text)
        self.assertNotIn('and ask which ones to start.', text)

    def test_primary_templates_have_contract_fields(self):
        for path in ('skills/plan-outcomes/assets/outcome-plan.md',
                     'skills/orchestrate-projects/assets/task-plan.md',
                     'skills/orchestrate-projects/assets/project-roadmap.md'):
            text = read(path)
            with self.subTest(path=path):
                for label in ('Why', 'Shortest path', 'Best path', 'Selected path', 'Readiness'):
                    self.assertRegex(text, rf'(?m)^- {re.escape(label)}:')

    def test_behavior_cases_are_isolated_specifications(self):
        suite = json.loads(read('tests/behavior_cases.json'))
        self.assertEqual(suite['status'], 'specification_not_executed')
        cases = suite['cases']
        self.assertGreaterEqual(len(cases), 12)
        ids = [case['id'] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            with self.subTest(case=case['id']):
                self.assertTrue(case['subject_input'])
                self.assertIsInstance(case['context'], dict)
                self.assertTrue(case['allowed_mock_tools'])
                self.assertGreaterEqual(len(case['expected']), 3)
                for path in case['skills']:
                    self.assertTrue((ROOT / path).is_file(), path)

    def test_readme_distinguishes_prompt_checks_from_model_evals(self):
        text = read('README.md')
        self.assertIn('not real model behavior', text)
        self.assertIn('does not install a universal rule', text)
        self.assertIn('not a tool-level permission enforcement system', text)

    def test_metadata_names_match_directories(self):
        for skill in SKILLS:
            text = read(f'skills/{skill}/SKILL.md')
            self.assertTrue(text.startswith('---\n'))
            header = text.split('---', 2)[1]
            self.assertIn(f'\nname: {skill}\n', header)
            self.assertRegex(header, r'(?m)^description: \S')


if __name__ == '__main__':
    unittest.main()
