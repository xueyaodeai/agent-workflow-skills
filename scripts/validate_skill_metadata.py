#!/usr/bin/env python3
"""Validate this repository's skill metadata and host invocation policies."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPLICIT_ONLY = {
    'dispatch-dida365-agent-tasks', 'organize-dida365', 'triage-dida365-inbox',
}
FRONTMATTER_KEYS = {
    'name', 'description', 'license', 'allowed-tools', 'metadata',
    'disable-model-invocation',
}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently accepting the last policy."""


def unique_mapping(loader, node):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise ValueError('metadata keys must be strings')
        if key in result:
            raise ValueError(f'duplicate key: {key}')
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping,
)


def mapping(text: str) -> dict:
    result = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(result, dict):
        raise ValueError('expected a YAML mapping')
    return result


def validate(skill: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = (skill / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.DOTALL)
        if not match:
            return ['missing YAML frontmatter']
        header = mapping(match.group(1))
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        return [f'SKILL.md: {exc}']

    unknown = set(header) - FRONTMATTER_KEYS
    if unknown:
        errors.append('unknown frontmatter fields: ' + ', '.join(sorted(unknown)))
    name = header.get('name')
    if (not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)
            or len(name) > 64 or name != skill.name):
        errors.append('name must match the directory and be kebab-case, at most 64 characters')
    description = header.get('description')
    if (not isinstance(description, str) or not description.strip()
            or len(description) > 1024 or '<' in description or '>' in description):
        errors.append('description must be nonempty text, at most 1024 characters, without angle brackets')
    for key in ('license', 'allowed-tools'):
        if key in header and not isinstance(header[key], str):
            errors.append(f'{key} must be a string')
    if 'metadata' in header and (not isinstance(header['metadata'], dict)
            or any(not isinstance(v, str) for v in header['metadata'].values())):
        errors.append('metadata must map strings to strings')
    if 'disable-model-invocation' in header and type(header['disable-model-invocation']) is not bool:
        errors.append('disable-model-invocation must be a boolean')
    explicit = skill.name in EXPLICIT_ONLY
    if explicit and header.get('disable-model-invocation') is not True:
        errors.append('explicit-only skill requires disable-model-invocation: true')

    config_path = skill / 'agents' / 'openai.yaml'
    if not config_path.exists() and not explicit:
        return errors
    try:
        config = mapping(config_path.read_text(encoding='utf-8'))
        unknown = set(config) - {'interface', 'policy', 'dependencies'}
        if unknown:
            errors.append('unknown openai.yaml fields: ' + ', '.join(sorted(unknown)))
        policy = config.get('policy', {})
        if not isinstance(policy, dict):
            errors.append('policy must be a mapping')
        else:
            unknown = set(policy) - {'allow_implicit_invocation'}
            if unknown:
                errors.append('unknown policy fields: ' + ', '.join(sorted(unknown)))
            if 'allow_implicit_invocation' in policy and type(policy['allow_implicit_invocation']) is not bool:
                errors.append('allow_implicit_invocation must be a boolean')
            if explicit and policy.get('allow_implicit_invocation') is not False:
                errors.append('explicit-only skill requires policy.allow_implicit_invocation: false')
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        errors.append(f'openai.yaml: {exc}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*', type=Path, help='skill directories; defaults to this repository')
    args = parser.parse_args()
    skills = args.skills or sorted((ROOT / 'skills').iterdir())
    failed = False
    for skill in skills:
        errors = validate(skill)
        failed |= bool(errors)
        print(f"[{'FAIL' if errors else 'PASS'}] {skill.name}")
        for error in errors:
            print(f'  - {error}')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
