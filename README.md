# Agent Workflow Skills

Reusable agent skills for durable project coordination, task-system organization, and evidence-backed handoffs.

## Skills

| Skill | Purpose |
| --- | --- |
| `orchestrate-projects` | Coordinate long-running projects across tasks, milestones, branches, worktrees, and roadmap transitions. |
| `organize-dida365` | Audit and reorganize Dida365/TickTick projects, tasks, priorities, dates, tags, and paused work. |
| `prepare-agent-handoff` | Package current context into a self-contained execution, schedule, external-model, or evaluation contract. |

Each skill is self-contained under `skills/<skill-name>/` and includes its own triggering metadata, workflow, and optional references or templates.

## Install

Inspect the available skills:

```bash
npx skills add xueyaodeai/agent-workflow-skills --list
```

Install one skill globally for Codex:

```bash
npx skills add xueyaodeai/agent-workflow-skills --skill orchestrate-projects -g -a codex -y
```

Replace `orchestrate-projects` with another listed skill as needed.

## Optional personal defaults

[`templates/common/AGENTS.md`](templates/common/AGENTS.md) is an opt-in personal
working-agreement for any agent. [`templates/codex/AGENTS.md`](templates/codex/AGENTS.md)
is the Codex variant: the same defaults plus subagent delegation and async
waiting rules. These files are not repository guidance and are not installed
by `npx skills add`.

Review and adapt environment and authority rules before use, especially
RTK availability, language-specific read-only phrases, and the local commit
policy. Copy the generic template into the personal or project `AGENTS.md`
used by the target agent. For Codex, if no global guidance exists yet:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}"
cp templates/codex/AGENTS.md "${CODEX_HOME:-$HOME/.codex}/AGENTS.md"
```

If that file already exists, merge the template manually instead of
overwriting personal guidance.

## Dependencies

- `orchestrate-projects` and `prepare-agent-handoff` are tool-agnostic; they preserve the permissions and tools available in the active agent environment.
- `organize-dida365` requires an available Dida365/TickTick integration or equivalent task-management tools. This repository does not provide account access or credentials.

## Validation

The skills are validated with the official `skill-creator` validator and checked through local `npx skills` discovery before release.

## License

[MIT](LICENSE)
