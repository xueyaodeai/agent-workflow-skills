---
name: dispatch-dida365-agent-tasks
description: Find active Dida365/TickTick tasks tagged `agent委派`, assess readiness and related work, let the user choose which tasks to start, then create user-visible independent Agent tasks and close only the successfully dispatched Dida365 items. Use only when the user explicitly requests this dispatch workflow by name. Do not trigger from ordinary task, Agent, roadmap, or planning conversation, and do not monitor the delegated work to completion.
disable-model-invocation: true
---

# Dispatch Dida365 Agent Tasks

Treat active `agent委派` tasks as a user-controlled launch queue. Help the user select work, choose the smallest execution package, start independent Agent tasks, and then remove the dispatched items from the active Dida365 queue.

## Establish authority

- Listing, analyzing, and recommending tasks are read-only.
- If the user has not selected exact tasks or an unambiguous set such as “all ready high-priority tasks,” show the queue and wait for one selection before creating independent Agent tasks or changing Dida365.
- An explicit selection plus “启动”“委派”“开始” or equivalent wording authorizes creation of the selected independent Agent tasks and the exact Dida365 comments, title updates, and completions required to record successful dispatch. Do not ask again when the user already made an exact selection.
- Create user-visible independent Agent tasks, not hidden subagents. Resolve readiness before launch; subsequent alignment covers only new findings or changed requirements.
- Use the current host's user-visible independent agent or task primitive. Typical equivalents are a Codex task, a Cursor Cloud Agent or new conversation, or a Claude Code session the user can open. If the host has only hidden subagents, stop and report that limitation instead of launching one.

## Read the active queue

Read active tasks carrying the exact `agent委派` tag, their owning projects, parent relationships, content, links, dates, priority, and comments needed to detect an earlier dispatch. Read relevant authoritative project or repository state only when it can change readiness, grouping, or scope.

If an active task already records a valid destination task reference, do not create another task. Reuse the reference and finish only the missing Dida365 closeout after verifying the prior dispatch.

## Assess readiness

A task is ready only when current, accessible context establishes:

- **Why:** the problem or preference, beneficiary, expected value, and basis;
- **What:** one observable outcome, deliverables, scope, and authority limits;
- **Paths:** shortest complete path, best path under current constraints, and selected approach with rationale; both meet the same acceptance and may be identical;
- **Done:** full acceptance scenarios, pass conditions, verification method, required evidence, and delivery boundary.

Also identify authoritative sources, satisfied prerequisites, and a concrete first action. Direct selections and the `agent委派` tag do not bypass readiness. Reuse settled answers and discover safe facts before asking; do not invent answers or ask for repeated approval. Missing consequential decisions block dependent implementation. Dispatch a clarification task only when separately authorized and its own question, scope, paths, and acceptance are clear. Continue independently ready selected work. Do not require exhaustive history or a fixed template.

Present a compact selection view with task number, title, project, real date or priority, readiness, and recommended dispatch unit. Keep non-ready tasks visible but do not start them.

## Choose the smallest dispatch units

Evaluate the selected ready tasks together before creating any independent Agent task.

- Treat a shared Dida365 project, repository, component, or tag only as a grouping clue.
- Group tasks only when they contribute to one observable outcome and can share authoritative sources, authority boundaries, and a coherent acceptance contract.
- Use separate independent Agent tasks for independent outcomes or materially different authority, side-effect, repository-isolation, or lifecycle boundaries.
- Use one merged execution task when the work shares one outcome, context, owner, and completion boundary and can reasonably finish in one task.
- Use one coordinating Agent task with `orchestrate-projects` only when execution must survive multiple tasks, sessions, milestones, repositories, environments, owners, or independently completable dependency stages.
- Inspect existing progress notes, a roadmap, and active task plans before proposing another roadmap. Reconcile into an existing roadmap when it already owns the outcome.
- Do not create a roadmap because tasks are numerous, share a project, touch several files, look difficult, or may take a long time.

Do not persist grouping IDs, roadmap-candidate tags, or dispatch states in Dida365. Multiple source tasks may record the same destination task reference.

## Prepare and start each task

Use `prepare-agent-handoff`, when available, to package each dispatch unit from the readiness assessment and existing sources. Without it, pass all four readiness points, source/recheck instructions, remaining work, authority limits, and completion evidence; add a first action only when it is not discoverable. Do not repeat discovery or clarification already settled during readiness assessment. This step packages context; task creation and Dida365 closeout remain this skill's responsibility.

For a coordinating unit, tell the destination to use `orchestrate-projects`, inspect current project artifacts, and choose the smallest coordination level before creating or changing a roadmap.

Create one independent Agent task per dispatch unit. After creation, wait once for a host-native acceptance signal such as initial progress or a user-input request so the task is known to be accepted; do not follow it to delivery or poll its later status.

## Close the Dida365 dispatch items

For each source task covered by a successfully accepted independent Agent task:

1. Add a comment containing the Agent task title and stable destination task reference.
2. Rewrite the Dida365 title to `委派 Agent：<原可观察目标>` unless it already truthfully describes delegation.
3. Preserve the `agent委派` tag and unrelated fields.
4. Mark the Dida365 task complete.

Complete a Dida365 task only when its recorded objective is delegation and a valid destination reference exists. The destination Agent task owns implementation, validation, review, and final delivery. Do not reopen or update the Dida365 task based on later Agent progress.

If creation or reference writeback fails, leave the affected Dida365 task active and report the exact failure. Do not retry task creation without new evidence.

## Verify and report

Re-read affected Dida365 tasks and confirm title, completion state, retained tag, destination reference, and preservation of unrelated fields; check project and dates when relevant to the changes. Report the resulting dispatch units and destination references, plus any items left active or failed changes. Do not claim dispatch complete from creation or write responses alone.
