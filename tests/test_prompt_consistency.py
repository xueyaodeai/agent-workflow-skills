"""Static drift checks only: these assertions do not measure model behavior."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('plan-outcomes', 'orchestrate-projects', 'prepare-agent-handoff', 'report-acceptance',
          'dispatch-dida365-agent-tasks', 'triage-dida365-inbox', 'organize-dida365')
EXPLICIT = ('dispatch-dida365-agent-tasks', 'triage-dida365-inbox', 'organize-dida365')

# Each installed skill keeps its own readiness guard, so these points are checked per skill
# rather than in a shared file that the installer may omit.
READINESS_POINTS = {
    'why': r'\bwhy\b',
    'outcome': r'\bwhat\b|\boutcome\b',
    'paths': r'\bshortest\b[^.]{0,80}?\bbest\b',
    'acceptance': r'\bacceptance\b|\bpass condition',
    'no-invention gate': r'\binvent\b',
}
MISSING_CONNECTOR = ('If the connector or required tools are unavailable, stop and report the limitation '
                     'instead of inferring or fabricating task state.')


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def missing_readiness_points(text):
    """Return the readiness points a skill body never states."""
    return sorted(point for point, pattern in READINESS_POINTS.items()
                  if not re.search(pattern, text, re.I))


def paths_unbound(text):
    """True when no shortest/best path statement sits with an acceptance statement."""
    blocks = [block for block in text.split('\n\n') if re.search(r'\bshortest\b', block, re.I)]
    return not any(re.search(r'\bacceptance\b', block, re.I) for block in blocks)


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

    def test_common_and_codex_communicate_sections_match(self):
        sections = [read(f'templates/{host}/AGENTS.md').split('## Communicate\n', 1)[1]
                    for host in ('common', 'codex')]
        self.assertEqual(*sections)
        self.assertIn('Bound claims positively with exact subjects, scope, and labels', sections[0])
        self.assertIn('不代表', sections[0])

    def test_standalone_skills_define_coordination_storage(self):
        for path in ('skills/orchestrate-projects/SKILL.md',
                     'skills/plan-outcomes/SKILL.md',
                     'skills/prepare-agent-handoff/SKILL.md',
                     'skills/report-acceptance/SKILL.md'):
            text = read(path)
            with self.subTest(path=path):
                self.assertIn('--git-common-dir', text)

    def test_each_standalone_skill_states_the_bound_readiness_guard(self):
        # Intentional small overlap: standalone installs cannot depend on siblings.
        for skill in SKILLS:
            text = read(f'skills/{skill}/SKILL.md')
            with self.subTest(skill=skill):
                self.assertEqual(missing_readiness_points(text), [])
                self.assertFalse(paths_unbound(text))
                self.assertNotIn('../', text)

    def test_readiness_guard_check_rejects_unbound_boilerplate(self):
        scattered = ('Reuse settled answers and stay ready. The best option is obvious, and why ask twice? '
                     'Direct requests are fine.')
        self.assertEqual(missing_readiness_points(scattered),
                         ['acceptance', 'no-invention gate', 'outcome', 'paths'])
        unbound = ('Why: because. The outcome and acceptance are clear. Never invent facts.\n\n'
                   'Take the shortest and best path.')
        self.assertEqual(missing_readiness_points(unbound), [])
        self.assertTrue(paths_unbound(unbound))
        self.assertFalse(paths_unbound('The shortest and best path meets the acceptance criteria.'))

    def test_dida365_skills_stop_when_the_connector_is_missing(self):
        for skill in EXPLICIT:
            with self.subTest(skill=skill):
                self.assertIn(MISSING_CONNECTOR, read(f'skills/{skill}/SKILL.md'))

    def test_explicit_only_skills_remain_explicit(self):
        for skill in EXPLICIT:
            text = read(f'skills/{skill}/SKILL.md')
            header = text.split('---', 2)[1]
            self.assertIn('disable-model-invocation: true', header)
            self.assertIn('allow_implicit_invocation: false', read(f'skills/{skill}/agents/openai.yaml'))

    def test_dispatch_default_does_not_force_reselection(self):
        text = read('skills/dispatch-dida365-agent-tasks/agents/openai.yaml')
        self.assertIn('只启动我明确选择的就绪任务', text)
        self.assertIn('仅在我的选择不明确时询问', text)
        self.assertNotIn('请选择要启动的任务', text)

    def test_interface_prompts_use_the_same_language(self):
        for skill in SKILLS:
            prompt = re.search(r'(?m)^  default_prompt: "(.+)"$',
                               read(f'skills/{skill}/agents/openai.yaml'))
            with self.subTest(skill=skill):
                self.assertIsNotNone(prompt)
                self.assertRegex(prompt.group(1), '[\u4e00-\u9fff]')
                self.assertIn(f'${skill}', prompt.group(1))

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
