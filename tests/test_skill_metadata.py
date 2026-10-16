"""Repository metadata validation, including both explicit-invocation policies."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/validate_skill_metadata.py'
SPEC = importlib.util.spec_from_file_location('validate_skill_metadata', SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class SkillMetadataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.skill = Path(self.tmp.name) / 'organize-dida365'
        (self.skill / 'agents').mkdir(parents=True)
        self.header = 'name: organize-dida365\ndescription: Organize tasks on explicit request.\ndisable-model-invocation: true\n'
        self.config = 'policy:\n  allow_implicit_invocation: false\n'

    def check(self, header=None, config=None):
        (self.skill / 'SKILL.md').write_text('---\n' + (self.header if header is None else header) + '---\nInstructions.\n')
        (self.skill / 'agents/openai.yaml').write_text(self.config if config is None else config)
        return validator.validate(self.skill)

    def test_repository_skills(self):
        for skill in sorted((ROOT / 'skills').iterdir()):
            with self.subTest(skill=skill.name):
                self.assertEqual(validator.validate(skill), [])

    def test_both_explicit_configurations_pass(self):
        self.assertEqual(self.check(), [])

    def test_unknown_frontmatter_is_rejected(self):
        self.assertIn('unknown frontmatter fields: disable-model-invocaton',
                      self.check(self.header + 'disable-model-invocaton: true\n'))

    def test_unknown_policy_field_is_rejected(self):
        self.assertTrue(any('unknown policy fields' in e for e in self.check(config=self.config + '  allow_implicit_invocaton: false\n')))

    def test_unknown_config_field_is_rejected(self):
        self.assertTrue(any('unknown openai.yaml fields' in e for e in self.check(config=self.config + 'polciy: {}\n')))

    def test_host_fields_require_boolean_types(self):
        for literal in ('"true"', '"false"', '0', '1', 'null', '[]', '{}'):
            with self.subTest(literal=literal):
                self.assertIn('disable-model-invocation must be a boolean', self.check(self.header.replace('true', literal)))
                self.assertIn('allow_implicit_invocation must be a boolean', self.check(config=self.config.replace('false', literal)))

    def test_claude_policy_cannot_be_removed_or_disabled(self):
        for header in (self.header.replace('disable-model-invocation: true\n', ''), self.header.replace('true', 'false')):
            self.assertIn('explicit-only skill requires disable-model-invocation: true', self.check(header))

    def test_codex_policy_cannot_be_removed_or_enabled(self):
        for config in ('{}\n', 'policy: {}\n', self.config.replace('false', 'true')):
            self.assertIn('explicit-only skill requires policy.allow_implicit_invocation: false', self.check(config=config))

    def test_all_three_skills_require_both_policies(self):
        for name in validator.EXPLICIT_ONLY:
            with self.subTest(name=name):
                dest = self.skill.with_name(name)
                self.skill.rename(dest)
                self.skill = dest
                header = f'name: {name}\ndescription: Test.\n'
                errors = self.check(header, '{}\n')
                self.assertIn('explicit-only skill requires disable-model-invocation: true', errors)
                self.assertIn('explicit-only skill requires policy.allow_implicit_invocation: false', errors)

    def test_missing_config_is_rejected_for_explicit_skill(self):
        self.check()
        (self.skill / 'agents/openai.yaml').unlink()
        self.assertTrue(any('openai.yaml:' in e for e in validator.validate(self.skill)))

    def test_duplicate_keys_are_rejected(self):
        self.assertTrue(any('duplicate key' in e for e in self.check(self.header + 'disable-model-invocation: false\n')))
        self.assertTrue(any('duplicate key' in e for e in self.check(config=self.config + '  allow_implicit_invocation: true\n')))

    def test_malformed_yaml_and_non_mapping_policy(self):
        for config in ('policy: [', '[]', 'policy: false', 'policy: null'):
            with self.subTest(config=config):
                self.assertTrue(self.check(config=config))

    def test_required_core_fields(self):
        for header in (self.header.replace('name: organize-dida365', 'name: wrong-name'),
                       self.header.replace('description: Organize tasks on explicit request.', 'description: null')):
            self.assertTrue(self.check(header))

    def test_ordinary_skill_can_omit_host_policies(self):
        dest = self.skill.with_name('ordinary-skill')
        self.skill.rename(dest)
        self.skill = dest
        self.assertEqual(self.check('name: ordinary-skill\ndescription: Ordinary task.\n', '{}\n'), [])
        (self.skill / 'agents/openai.yaml').unlink()
        self.assertEqual(validator.validate(self.skill), [])

    def test_cli_reports_failure_and_success(self):
        self.check()
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.skill)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('[PASS]', result.stdout)
        self.check(config=self.config.replace('false', 'true'))
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.skill)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn('[FAIL]', result.stdout)
