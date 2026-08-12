---
name: triage-dida365-inbox
description: Sort Dida365/TickTick Inbox tasks into existing personal, learning, work, or side-project destinations; distinguish user-owned work from agent-ready work; collect only consequential context; and tag agent-ready items `agent委派` without launching agents. Use only when the user explicitly invokes `$triage-dida365-inbox`. Do not trigger from ordinary task or planning conversation, audit the whole account, group agent work, create roadmaps, or start Codex tasks.
---

# Triage Dida365 Inbox

Use the Inbox as a capture boundary. Turn each captured item into either an active user-owned task or an active task in the Agent delegation queue without turning triage into project planning or execution.

## Establish authority

- Treat “分析”“看看” and equivalent wording as read-only.
- Treat “整理收集箱”“执行整理” and equivalent wording as authority for the exact task moves, edits, and `agent委派` tag creation or removal required by this workflow.
- Do not delete tasks, projects, tags, or history. Do not infer authority to start a Codex task from permission to organize the Inbox.

## Read only the intake surface

Read the user timezone, project groups, active destination projects, the exact active Inbox tasks, and relevant tags. Paginate when needed. Inspect additional task or source details only when they can change routing or make a task executable; do not inventory the whole account, completed history, habits, or unrelated projects.

## Classify two independent dimensions

Classify each task by:

1. **Area:** personal daily life, learning, work, or side project. Express the area through placement in an existing owning project or project group, not a duplicate area tag.
2. **Handler:** user-owned or Agent-ready. Treat handler as independent from area; a personal or learning task may also be suitable for an Agent.

Use an established specific project when one clearly owns the outcome. If no current project is a safe fit, leave the item in the Inbox and return the smallest routing question. Do not create a project merely to empty the Inbox.

## Gather the minimum executable context

Inspect task content, links, attachments, and safely discoverable sources before asking the user.

- For a user-owned task, make the title a verb plus one observable result. Preserve or add a date, reminder, or priority only when it represents a real commitment, start window, deadline, or dependency.
- For an Agent-ready task, capture only the desired observable outcome, authoritative source or discoverable location, consequential scope or authority limits, and completion evidence. Let the destination Agent inspect ordinary repository or system detail later.
- Use repair, new behavior, refactor, data analysis, and error diagnosis only as temporary routing judgments. Do not create persistent subtype tags unless the user explicitly requests a taxonomy for repeated retrieval.
- Ask only when missing user-only information would materially change the outcome, source, permission, external side effect, or acceptance decision. Do not require a fixed intake template.

## Apply the routing

- Move a clear user-owned task to its owning project, keep it active, and remove `agent委派` if it was incorrectly applied.
- Move a clear Agent-ready task to its owning project, keep it active, and apply the single canonical tag `agent委派`. When execution is authorized, create that exact tag if it does not exist; do not add handler or Agent subtype tags.
- Preserve unrelated fields, including content, checklist items, parent, dates, timezone, reminders, recurrence, priority, and retained tags.
- Do not group Agent-ready tasks, decide whether they need a roadmap, start an Agent, rename them as dispatched, or complete them. `$dispatch-dida365-agent-tasks` owns that boundary.

Process unambiguous items without blocking on unrelated ambiguous ones when the user authorized batch organization. Leave unresolved items unchanged and return one compact question covering only the decisions still needed.

## Verify and report

Re-read every affected task. Verify its project, active state, exact `agent委派` presence or absence, retained fields, dates, and timezone. Report counts for user-owned tasks moved, Agent-ready tasks queued, unchanged ambiguous tasks, and failed changes. Do not claim completion from write responses alone.
