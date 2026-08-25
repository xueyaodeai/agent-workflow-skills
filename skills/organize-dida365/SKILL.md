---
name: organize-dida365
description: Audit, plan, and reorganize an entire Dida365/TickTick task system, including projects, groups, tasks, tags, dates, priorities, lifecycle states, habits, and archives. Use only when the user explicitly invokes `organize-dida365` for a whole-system audit, planning review, item-by-item alignment, cleanup, or an agreed reorganization. Do not trigger from ordinary task planning, routine Inbox triage, or requests to select and start Agent work.
disable-model-invocation: true
---

# Organize Dida365

Turn an overloaded task collection into a small set of owned, executable outcomes. Separate analysis, alignment, mutation, and verification so that ambiguous planning does not become accidental data loss.

Use `triage-dida365-inbox` for routine Inbox routing and `dispatch-dida365-agent-tasks` for the active `agent委派` queue. Do not perform those workflows as part of a general audit unless the user explicitly includes their exact mutations.

## Load the detailed rules

Read [references/organization-rules.md](references/organization-rules.md) before proposing structural changes, splitting tasks, or cleaning tags. It contains the decision tables and examples for projects, tags, task granularity, dates, priorities, and lifecycle states.

## Follow the workflow

### 1. Establish scope

Determine whether the user wants analysis, a proposal, item-by-item alignment, or execution.

- Treat “分析”“看看问题” as read-only.
- Treat “先给方案” as proposal-only.
- Treat “逐项跟我对齐” as an interactive decision log; do not batch undecided changes.
- Treat “执行”“落实到清单中”“清理” as authorization for the agreed exact changes only.
- Do not infer permission to delete tasks, tags, projects, or history from a general request to tidy up.

### 2. Capture a current inventory

Use the Dida365 connector before reasoning from names alone. Collect:

- user timezone;
- active and archived projects plus project groups;
- active tasks, parent-child relationships, status, dates, priority, and tags;
- tag definitions and actual task usage;
- habits when the request includes recurring behavior.

Paginate where supported. Distinguish an empty active project from a project containing only completed or abandoned history. Do not equate a zero-count tag in the sidebar with permanent redundancy; check current task use, hierarchy, and intended future use.

### 3. Diagnose before editing

Classify findings into these buckets:

1. structural: duplicate projects, mixed outcomes, misplaced tasks, oversized tasks;
2. execution: stale dates, missing next actions, unrealistic concurrent commitments;
3. lifecycle: finished H1 work, paused work, transferred ownership, obsolete plans;
4. metadata: synonym tags, one-off tags, date or priority encoded as tags, orphan tag trees;
5. recurring work: habits duplicated as tasks or tasks with incompatible recurrence.

For every proposed change, state the current problem, recommended action, and expected result. Keep uncertain items separate from clearly redundant ones.

### 4. Align decisions

When the user requests item-by-item alignment, maintain one explicit decision per item:

- keep;
- complete;
- pause;
- abandon;
- move;
- merge;
- split;
- clear date;
- reschedule;
- retag;
- archive project.

Carry the decision to children when the parent and children represent the same paused, abandoned, moved, or archived outcome. Ask only when child ownership or intent differs.

### 5. Apply the minimum complete change

Prefer reversible task updates and moves over deletion.

- Mark achieved outcomes completed.
- Mark work no longer needed or transferred away abandoned.
- Move temporarily inactive work into the user's pause holding area without inventing completion.
- Clear speculative dates; retain dates that are commitments or real start windows.
- Move tasks to the project that owns the outcome.
- Remove redundant tags from tasks before deleting tag definitions.
- Archive a project only after resolving all active children and confirming it no longer represents live work.

Preserve unrelated fields when updating a task: title, content or description, checklist items, parent, project, dates, timezone, reminders, recurrence, priority, and retained tags. Use batch operations only for homogeneous, already agreed changes and respect connector limits.

If the connector cannot delete a tag definition, use an authenticated browser only after the user has explicitly authorized the exact deletion set. Verify each target has no remaining task use, delete only exact-name matches, and accept only the corresponding confirmation dialogs.

### 6. Verify against live state

Re-read affected tasks, projects, and tags after mutation. Verify:

- task count and lifecycle state;
- target project and parent-child placement;
- exact dates and timezone;
- retained versus removed tags;
- archived project state;
- absence of deleted tag definitions;
- no unexpected changes outside the agreed set.

Report completed changes, skipped or failed changes, and any remaining decision separately. Never call execution complete from write responses alone.

## Produce concise handoff output

Lead with the resulting task-system state. Include exact counts when available. List only meaningful changes, remaining risks, and user decisions still required. Do not repeat the entire inventory unless requested.
