"""Static drift checks only: these assertions do not measure model behavior."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('plan-outcomes', 'fix-issue', 'orchestrate-projects', 'prepare-agent-handoff', 'report-acceptance')
OPEN_SOURCE_SURVEY = (
    'If existing in-repo primitives cannot cover a required architecture change or non-trivial mechanism, '
    'first search GitHub or other open-source hosts for actively maintained frameworks or libraries. '
    'Evaluate candidates before writing custom code.'
)

# Each installed skill keeps its own readiness guard, so these points are checked per skill
# rather than in a shared file that the installer may omit.
READINESS_POINTS = {
    'why': r'\bwhy\b',
    'outcome': r'\bwhat\b|\boutcome\b',
    'paths': r'\bshortest\b[^.]{0,80}?\bbest\b',
    'acceptance': r'\bacceptance\b|\bpass condition',
    'no-invention gate': r'do not invent|never\s+(?:silently\s+)?invent',
    'direct assignments': r'\bdirect\b',
    'reuse of settled answers': r'\breus(?:e|es|ed|ing)\b',
    'execution readiness': r'\breadiness\b|\bready\b',
}


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def markdown_section(text, heading):
    """Return the section body, omitting HTML comments and fenced examples."""
    comments_and_fences = (
        r'<!--.*?(?:-->|\Z)'
        r'|^ {0,3}(?P<fence>(?P<marker>`|~)(?P=marker){2,})[^\n]*\n'
        r'.*?(?:^ {0,3}(?P=fence)(?P=marker)*[ \t]*(?:\n|\Z)|\Z)'
    )
    text = re.sub(comments_and_fences, '\n', text, flags=re.M | re.S)
    level = len(heading.split(' ', 1)[0])
    pattern = (
        rf'^ {{0,3}}{re.escape(heading)}(?:[ \t]+#+)?[ \t]*\n'
        rf'(.*?)(?=^ {{0,3}}#{{1,{level}}}(?:[ \t]|$)|\Z)'
    )
    match = re.search(pattern, text, re.M | re.S)
    return match.group(1) if match else ''


def missing_readiness_points(text):
    """Return the readiness points a skill body never states."""
    return sorted(point for point, pattern in READINESS_POINTS.items()
                  if not re.search(pattern, text, re.I))


def paths_unbound(text):
    """True when no block states both path kinds together with acceptance."""
    blocks = [block for block in text.split('\n\n') if re.search(r'\bshortest\b', block, re.I)]
    return not any(re.search(r'\bbest\b', block, re.I) and re.search(r'\bacceptance\b', block, re.I)
                   for block in blocks)


class PromptConsistencyTests(unittest.TestCase):
    def test_single_personal_defaults_template_layout(self):
        templates = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / 'templates').rglob('*.md'))
        self.assertEqual(templates, ['templates/common/AGENTS.md'])
        text = read('templates/common/AGENTS.md')
        self.assertEqual(missing_readiness_points(text), [])
        self.assertFalse(paths_unbound(text))
        environment = markdown_section(text, '## Environment')
        self.assertIn('high-output command filter such as RTK', environment)
        self.assertIn('`rtk proxy`', environment)

    def test_personal_defaults_act_and_delegate_sections(self):
        text = read('templates/common/AGENTS.md')
        act = markdown_section(text, '## Act')
        for phrase in (
            'follow immediate read-only leads one step deeper',
            'change history and actor intent, and visible downstream or metric effects',
            'merely triggering a run or build whose result is needed for the goal',
            'execute in-scope authorized work rather than listing it as “next steps”',
            'Exhaust ordered lists, backlogs, and N-item scopes',
            'never stop after a first batch, top-N subset, or triage/inventory pass to report interim progress',
            'When one item is paused or blocked, record its status and continue independent ready items',
            'multiple logical local commits across large batches do not end the turn',
            'Do not classify an item as blocked or defer it to “next steps” while any safe, authorized local or read-only check can still advance it',
            'pause or stop an item only when no safe, authorized progress remains within current session, worktree-preservation, and verification constraints',
            'Carry authorization, thread goals, and settled decisions forward.',
            'When upstream items or records are incomplete—even in a read-only check—draft the missing content (such as concrete steps, provisional expected checks, or candidate config) from available context, clearly marked provisional/to-confirm',
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, act)
        delegate = markdown_section(text, '## Delegate')
        for phrase in (
            'Keep architecture, implementation, coordination, and delivery in the main agent by default.',
            'Delegate implementation only for parallel units with frozen interfaces, no shared open decisions, and cheap acceptance checks.',
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, delegate)

    def test_personal_defaults_minimum_complexity_verify_and_review_sections(self):
        text = read('templates/common/AGENTS.md')
        complexity = markdown_section(text, '## Minimum Complexity')
        self.assertIn('--git-common-dir', complexity)
        self.assertIn('out of version control by default', complexity)
        self.assertIn('reserve explicit caller-supplied hashes for concurrent-write protection', complexity)
        self.assertRegex(complexity, rf'(?m)^- {re.escape(OPEN_SOURCE_SURVEY)}(?: |$)')
        self.assertIn('regression check fails on the old code', markdown_section(text, '## Verify'))
        self.assertIn('Minimum Complexity violations', markdown_section(text, '## Review'))

    def test_planning_skills_require_open_source_survey_for_uncovered_needs(self):
        for skill, headings in (
            ('plan-outcomes', ('## 3. Define acceptance and compare paths',)),
            ('orchestrate-projects', ('## Establish the execution contract',)),
        ):
            with self.subTest(skill=skill):
                section = read(f'skills/{skill}/SKILL.md')
                for heading in headings:
                    section = markdown_section(section, heading)
                self.assertRegex(
                    section,
                    rf'(?m)(?:\A(?:[ \t]*\n)*|\n[ \t]*\n){re.escape(OPEN_SOURCE_SURVEY)}(?: |$)',
                )

    def test_personal_defaults_communicate_section(self):
        section = markdown_section(read('templates/common/AGENTS.md'), '## Communicate')
        for phrase in (
            'Keep workflow terms from these instructions',
            '`evidence gap`',
            '`contract violation`',
            'Do not recite passed checklist categories unless asked.',
            'Lead with the plain answer',
            'compact verification lines after the main explanation',
            'Bound claims positively with exact subjects, scope, and labels',
            'Whenever findings leave actionable follow-ups, failures, missing inputs, unverified async runs, or scope/metric trade-offs—even on a standalone read-only status or diagnosis check—end with a concrete recommended next step or order of operations',
            'for work outside current turn authorization or paused under safety, worktree-preservation, session, or external-dependency constraints',
            'never end an execution turn with a “next step” you are already authorized and able to perform safely right now—execute it first and report the result.',
            'Omit next-step suggestions only when nothing actionable remains.',
            '不代表',
            'Name the real object and action first; do not lead with abstract capability labels',
            'When explaining a flow, mechanism, or logic defect, connect the steps with plain verbs',
            'trigger → what blocks or misses what at which step → result',
            'Never pack multiple project-internal shorthand terms into one sentence',
            'on first mention of an internal concept, state its actual object or action directly',
            '`发给调查 Agent 的 prompt`',
            '`跑 base/head 对比`',
            '`调查提示`',
            '`双版执行`',
            'Apply the same standard to interim progress updates.',
            'Prefer `对比各代付场景传给询价接口的 UIN；代码看过了，还没发真实请求验证下游` over `把关键行为差异变成可复核的候选，目前还剩实际请求与下游行为的证据缺口`.',
            'Prefer `在容器里跑完同样的检查后，用 git commit --no-verify 提交` over `在隔离容器完成等价检查后，仅对本次提交绕过失效启动器`.',
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, section)

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
        affirmative = ('Why: needed. Outcome: known. Reuse prior results. Be ready for direct work. '
                       'Invent answers. Acceptance: the shortest and best path passes.')
        self.assertEqual(missing_readiness_points(affirmative), ['no-invention gate'])
        self.assertEqual(missing_readiness_points(
            affirmative.replace('Invent answers', 'Do not invent answers')), [])
        unbound = ('Why: needed. Outcome: export. Do not invent answers. Reuse prior results. '
                   'Be ready for direct requests. Acceptance: rows match.\n\n'
                   'Take the shortest and best path.')
        self.assertEqual(missing_readiness_points(unbound), [])
        self.assertTrue(paths_unbound(unbound))
        split_pairs = ('Why: needed. Outcome: export. Do not invent answers. Reuse prior results. '
                       'Be ready for direct requests.\n\nTake the shortest and best path.\n\n'
                       'The shortest path meets acceptance.')
        self.assertEqual(missing_readiness_points(split_pairs), [])
        self.assertTrue(paths_unbound(split_pairs))
        self.assertFalse(paths_unbound('The shortest and best path meets the acceptance criteria.'))

    def test_readiness_guard_keeps_the_canonical_acceptance_binding(self):
        # Shorthand such as "meet the same criteria" was ambiguous about acceptance scope.
        for path in [f'skills/{skill}/SKILL.md' for skill in SKILLS] + ['templates/common/AGENTS.md']:
            with self.subTest(path=path):
                self.assertNotIn('meet the same criteria', read(path))

    def test_orchestrate_projects_loads_template_detail_from_a_reference(self):
        text = read('skills/orchestrate-projects/SKILL.md')
        reference = read('skills/orchestrate-projects/references/templates.md')
        self.assertIn('(references/templates.md)', text)
        self.assertIn('validate_project_docs.py', reference)
        self.assertNotIn('validate_project_docs.py', text)
        for path in ('assets/promotion-gate.md', 'assets/milestone-audit.md'):
            self.assertIn(path, reference)

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
        covered = {path.split('/')[1] for case in cases for path in case['skills'] if path.startswith('skills/')}
        self.assertEqual(sorted(set(SKILLS) - covered), [])

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
