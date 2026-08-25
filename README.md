# Agent Workflow Skills

Reusable agent skills for durable project coordination, task-system organization, and evidence-backed handoffs.

## Skills

| Skill | Purpose |
| --- | --- |
| `orchestrate-projects` | Coordinate long-running projects across tasks, milestones, branches, worktrees, and roadmap transitions. |
| `organize-dida365` | Audit and reorganize Dida365/TickTick projects, tasks, priorities, dates, tags, and paused work. Explicit invocation only. |
| `triage-dida365-inbox` | Sort the Dida365 Inbox into owning projects and queue agent-ready work. Explicit invocation only. |
| `dispatch-dida365-agent-tasks` | Start user-visible independent Agent tasks from the `agent委派` queue. Explicit invocation only. |
| `prepare-agent-handoff` | Package current context into a self-contained execution, schedule, external-model, or evaluation contract. |

Each skill is self-contained under `skills/<skill-name>/` and includes its own triggering metadata, workflow, and optional references or templates.

Explicit-only skills stay inactive until the user names them, for example `/organize-dida365`, `$organize-dida365`, or `organize-dida365`.

## Install

Inspect the available skills:

```bash
npx skills add xueyaodeai/agent-workflow-skills --list
```

Install one skill globally for a specific agent:

```bash
npx skills add xueyaodeai/agent-workflow-skills --skill orchestrate-projects -g -a cursor -y
```

Replace `orchestrate-projects` with another listed skill as needed. Repeat `-a` for each host (`cursor`, `claude-code`, `codex`). Omit `-a` to let the installer target detected agents.

## Optional personal defaults

[`templates/common/AGENTS.md`](templates/common/AGENTS.md) is an opt-in personal working-agreement for any agent. [`templates/codex/AGENTS.md`](templates/codex/AGENTS.md) is the Codex variant: the same defaults plus Codex subagent delegation and `wait_agent` / `list_agents` waiting rules. Do not copy those Codex tool names into Cursor or Claude Code guidance. These files are not repository guidance and are not installed by `npx skills add`.

Review and adapt environment and authority rules before use, especially high-output command filters, language-specific read-only phrases, and the local commit policy. Copy the generic template into the personal or project `AGENTS.md` used by the target agent. For Claude Code, copy the same content into `CLAUDE.md` when that is the project's guidance file.

For Codex, if no global guidance exists yet:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}"
cp templates/codex/AGENTS.md "${CODEX_HOME:-$HOME/.codex}/AGENTS.md"
```

If that file already exists, merge the template manually instead of overwriting personal guidance.

## Dependencies

- `orchestrate-projects` and `prepare-agent-handoff` are tool-agnostic; they preserve the permissions and tools available in the active agent environment.
- `organize-dida365`, `triage-dida365-inbox`, and `dispatch-dida365-agent-tasks` require an available Dida365/TickTick integration or equivalent task-management tools. This repository does not provide account access or credentials.
- `dispatch-dida365-agent-tasks` also needs a host that can create a user-visible independent agent or task. Hidden subagents are not a substitute.

## Validation

The skills are validated with the official `skill-creator` validator and checked through local `npx skills` discovery before release.

## License

[MIT](LICENSE)
