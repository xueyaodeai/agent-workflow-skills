---
name: dispatch-dida365-agent-tasks
description: Find active Dida365/TickTick tasks tagged `agent委派`, assess readiness and related work, let the user choose which tasks to start, then create user-visible independent Agent tasks and close only the successfully dispatched Dida365 items. Use only when the user explicitly invokes `$dispatch-dida365-agent-tasks`. Do not trigger from ordinary task, Agent, roadmap, or planning conversation, and do not monitor the delegated work to completion.
---

# Dispatch Dida365 Agent Tasks

Treat active `agent委派` tasks as a user-controlled launch queue. Help the user select work, choose the smallest execution package, start independent Agent tasks, and then remove the dispatched items from the active Dida365 queue.

## Establish authority

- Listing, analyzing, and recommending tasks are read-only.
- If the user has not selected exact tasks or an unambiguous set such as “all ready high-priority tasks,” show the queue and wait for one selection before creating independent Agent tasks or changing Dida365.
- An explicit selection plus “启动”“委派”“开始” or equivalent wording authorizes creation of the selected independent Agent tasks and the exact Dida365 comments, title updates, and completions required to record successful dispatch. Do not ask again when the user already made an exact selection.
- Create user-visible independent Agent tasks, not subagents. The user owns subsequent alignment in those tasks.

## Read the active queue

Read active tasks carrying the exact `agent委派` tag, their owning projects, parent relationships, content, links, dates, priority, and comments needed to detect an earlier dispatch. Read relevant authoritative project or repository state only when it can change readiness, grouping, or scope.

If an active task already records a valid destination task reference, do not create another task. Reuse the reference and finish only the missing Dida365 closeout after verifying the prior dispatch.

## Assess readiness

A task is ready when the destination can discover or has been given:

- one observable outcome;
- authoritative sources or a safe first place to inspect;
- consequential scope and authority limits;
- observable completion evidence; and
- one concrete first action.

Discover safe facts before asking. Mark a task as needing input only when a user-only decision would materially change execution. Do not require exhaustive repository history, implementation steps, or a fixed handoff template.

Present a compact selection view with task number, title, project, real date or priority, readiness, and recommended dispatch unit. Keep non-ready tasks visible but do not start them.

## Choose the smallest dispatch units

Evaluate the selected ready tasks together before creating any independent Agent task.

- Treat a shared Dida365 project, repository, component, or tag only as a grouping clue.
- Group tasks only when they contribute to one observable outcome and can share authoritative sources, authority boundaries, and a coherent acceptance contract.
- Use separate independent Agent tasks for independent outcomes or materially different authority, side-effect, repository-isolation, or lifecycle boundaries.
- Use one merged execution task when the work shares one outcome, context, owner, and completion boundary and can reasonably finish in one task.
- Use one coordinating Agent task with `$orchestrate-projects` only when execution must survive multiple tasks, sessions, milestones, repositories, environments, owners, or independently completable dependency stages.
- Inspect existing progress notes, a roadmap, and active task plans before proposing another roadmap. Reconcile into an existing roadmap when it already owns the outcome.
- Do not create a roadmap because tasks are numerous, share a project, touch several files, look difficult, or may take a long time.

Do not persist grouping IDs, roadmap-candidate tags, or dispatch states in Dida365. Multiple source tasks may record the same destination task reference.

## Prepare and start each task

Build the smallest runnable execution handoff for each dispatch unit: destination, objective, authoritative sources or required rechecks, remaining ownership, consequential authority limits, deliverables and completion evidence, and first action. Reference durable sources instead of copying long task histories.

For a coordinating unit, tell the destination to use `$orchestrate-projects`, inspect current project artifacts, and choose the smallest coordination level before creating or changing a roadmap.

Create one independent Agent task per dispatch unit. After creation, wait once for initial progress or a user-input request so the task is known to be accepted; do not follow it to delivery or poll its later status.

## Close the Dida365 dispatch items

For each source task covered by a successfully accepted independent Agent task:

1. Add a comment containing the Agent task title and stable destination task reference.
2. Rewrite the Dida365 title to `委派 Agent：<原可观察目标>` unless it already truthfully describes delegation.
3. Preserve the `agent委派` tag and unrelated fields.
4. Mark the Dida365 task complete.

Complete a Dida365 task only when its recorded objective is delegation and a valid destination reference exists. The destination Agent task owns implementation, validation, review, and final delivery. Do not reopen or update the Dida365 task based on later Agent progress.

If creation or reference writeback fails, leave the affected Dida365 task active and report the exact failure. Do not retry task creation without new evidence.

## Verify and report

Re-read affected Dida365 tasks and confirm title, completion state, retained tag, destination reference, project, dates, and unrelated fields. Report selected items, dispatch grouping, created Agent tasks, completed Dida365 tasks, reused prior references, and tasks left active. Do not claim dispatch complete from creation or write responses alone.
