---
name: orchestrate-projects
description: Coordinate projects whose execution must survive multiple tasks, sessions, milestones, worktrees, repositories, or environments. Use when work needs a durable task plan or project roadmap, parallel-work coordination, milestone audits, initiative integration, cross-context resume or handoff, or successor-roadmap alignment. Classify the smallest coordination level first; do not use for a self-contained single-session task unless the user explicitly requests durable project files.
---

# Orchestrate Projects

Keep long-running work resumable and evidence-backed without turning ordinary tasks into project-management exercises.

## Core invariants

1. Use the smallest structure that survives the actual context boundaries. Do not create durable project files for a self-contained single-session task unless requested.
2. Persist cross-task decisions, scope, ownership, and coordination state. Verify implementation and runtime facts against their authoritative live sources.
3. Give each shared project artifact one writer. The coordinating task owns roadmap reconciliation; worker tasks update only their own plans or return a handoff.
4. Scale completion evidence to the coordination level. Bind evidence to a revision, environment, or observation time only when that identity can change the conclusion.
5. Follow the applicable user- and repository-level Authority rules. This skill records only project-specific narrowing and the selected delivery package; it never expands authority.
6. Keep every implementation change attributable to one task and preserve unrelated work.
7. Scale independent review to demonstrated risk separately from coordination level. Long duration, multiple files or attempts, and bounded external reads do not make review a default completion step.

## 1. Route the request before loading details

Inspect applicable instructions, established project artifacts, and current evidence, then choose the smallest coordination level:

1. **Level 0 — ephemeral execution:** The work can finish and be verified in the current task, with no independent continuation or durable status view. Use the current task's lightweight plan if useful; do not create a project file.
2. **Level 1 — resumable task:** One outcome must survive a task, session, or environment boundary. Use the established task-plan format or copy `assets/task-plan.md`.
3. **Level 2 — multi-task project:** Coordination state must survive across multiple tasks, milestones, repositories, environments, or owners. Add the established roadmap or copy `assets/project-roadmap.md`; merely touching multiple repositories in one self-contained task does not require a roadmap.
4. **Level 3 — audited project:** Material parallelism or high-risk, irreversible, production, or cross-repository integration changes require an explicit milestone gate. Add `assets/milestone-audit.md`; changing requirements or multiple checks alone do not raise the level.

Choose the delivery topology independently from the coordination level:

- Use `not_applicable` for read-only or non-Git work.
- Use the repository's normal feature-to-primary workflow when milestones remain independently reviewable and releasable.
- Use initiative integration only when its explicit gate is satisfied. Then read [references/integration-branch.md](references/integration-branch.md).

Load optional workflows only when their trigger applies:

- For Git changes or task-scoped delivery, read [references/git-delivery.md](references/git-delivery.md).
- For an initiative integration branch or primary-branch promotion, read [references/integration-branch.md](references/integration-branch.md).
- For carryover alignment or a successor roadmap, read [references/next-round-alignment.md](references/next-round-alignment.md).

## 2. Establish fact and artifact ownership

Treat project files as coordination ledgers, not universal factual authorities:

| Information | Authority | Durable record |
|---|---|---|
| User decisions, scope, non-goals | User or named policy owner | Roadmap decision ledger |
| Project milestone and dependency state | Coordinating task after reconciliation | Project roadmap |
| Task execution state and local choices | Task owner | Task plan |
| Code and change identity | Live repository | Revision, diff, branch, or delivery record |
| Test or review result | Producing system or reviewer | Evidence tied to subject, time, and environment |
| External status | Authoritative external system | Identifier and last-checked time |

Use these write rules:

- The coordinating task is the single writer for the roadmap and shared decision ledger.
- Each worker task owns its task plan. It must not edit the roadmap concurrently; return conclusion, changes, evidence, risks, and next step to the coordinator.
- On resume, recheck drift-prone facts and reconcile stale documents to live evidence.
- Write durable files only when the user requested them or an established, authorized project workflow already requires them.
- Preserve existing repository formats. Reference task plans and evidence by path instead of duplicating their contents.

## 3. Use one state protocol

Use the same base states for tasks, milestones, and projects:

`not_started -> in_progress -> ready_for_verification -> complete`

Use side states deliberately:

- `blocked`: progress cannot continue until a named condition changes; it may return to `in_progress`.
- `deferred`: removed from the active sequence with an owner or reconsideration trigger.
- `cancelled`: intentionally stopped by an authorized owner.
- `superseded`: replaced by a newer artifact or decision, with a reference to the replacement.

Do not use `partial` as a terminal state. Keep unfinished work `in_progress` or `blocked`, or explicitly move it to `deferred`, `cancelled`, or `superseded`.

Record only transitions that change a decision, blocker, downstream dependency, delivery identity, or next resumable action. Batch routine step progress; add an observation time only for drift-prone facts.

Scale `complete` to the selected level:

- **Level 0:** the requested result exists and a concise current-task check supports it.
- **Level 1:** the observable objective is satisfied, current evidence supports it, no in-scope blocker remains, and the delivery boundary is explicit.
- **Level 2:** Level 1 plus dependent handoff and roadmap reconciliation are complete where another task relies on them.
- **Level 3:** Level 2 plus the required milestone audit and high-risk gates pass.

Do not add a higher-level condition to a lower-level task merely because the template contains a matching field.

## 4. Keep project and task state separate

### Project roadmap

Store only global coordination state:

- final outcome, completion criteria, constraints, and non-goals;
- artifact owner and last reconciliation point;
- current milestone and milestone/workstream status;
- cross-task dependencies, decisions, blockers, and risk ownership;
- links to task plans and versioned evidence;
- next-milestone entry criteria and project closeout state.

Do not store command logs, detailed exploration, every failed attempt, or worker-local progress in the roadmap.

### Task plan

For Level 1, default to the core task plan: observable objective, consequential scope boundary, current plan/state, and closeout evidence plus delivery boundary. Add owner, non-goals, assumptions, detailed evidence metadata, decisions, blockers, or handoff only when they change execution or another context must resume the work.

Use `assets/task-plan-coordination-addon.md` for cross-task decisions, blockers, or downstream handoff. Use other add-ons only when their trigger applies. Do not fill unused sections with `none` or `not applicable`; omit them.

## 5. Select execution units conservatively

1. Keep work in the current task when it directly serves the current outcome and shares the same context.
2. Delegate only bounded work when the user requested delegation or parallel work and higher-priority instructions permit it.
3. Create or fork an independent task only when the user explicitly asks and durable visibility or isolation is required.
4. Use a separate local task when validation depends on machine-local login, device, desktop, simulator, or permission state.
5. Isolate concurrent repository writers with dedicated branches and worktrees; never let two worktrees use the same branch.

For a delegated or independently resumable execution unit, specify the objective, allowed scope, consequential authority constraints, expected evidence, and return destination. A current-task or low-risk unit needs only the fields that can change execution.

## 6. Run the coordination loop

### Orient

Read the roadmap and active task plan when present, applicable instructions, and authoritative current state. Reconcile stale claims before planning.

### Plan

Identify the current milestone, bounded execution units, dependencies, evidence requirements, authority boundaries, and delivery topology. Record only material assumptions and unresolved decisions.

### Execute

Perform current-task work directly. Preserve unrelated changes and keep worker-local detail out of the roadmap. Report material progress as completed, next, and blocked, with evidence.

### Integrate

Verify returned work rather than accepting summaries uncritically. The coordinator promotes only cross-task conclusions, decisions, blockers, and evidence into the roadmap.

### Verify and close

Apply the level-specific completion conditions in section 3. Level 0/1 does not require roadmap reconciliation, handoff, audit, or template validation unless another active rule requires it. For Level 3, complete the milestone audit without substituting it for any independently required code review or runtime validation. Record only skipped checks that leave material risk.

Verification is always required; independent review is conditional:

- Default to executor-owned targeted and proportional regression checks for local, reversible changes that do not materially affect a public contract, security or sensitive-data boundary, production or irreversible side effect, critical fail-closed behavior, milestone exit, or cross-repository integration gate.
- Require an independent reviewer only when an applicable rule or the user explicitly requires one, or when one of those material boundaries changes. Coordination level, file count, elapsed time, multiple attempts, model cost, or bounded read-only access alone do not trigger it.
- Use a deterministic executor preflight for bounded low-risk read-only or model operations. Do not insert an independent preflight around each operation unless a demonstrated current risk requires it.
- When review is required, consolidate it around one acceptance-ready semantic snapshot. Do not split preflight, implementation, each operation, and result checking into repeated independent reviews. After blocking findings, use the same reviewer for a targeted recheck; widen it only if the fix changes another material boundary.
- Preserve historical review and audit records, but do not inherit their gates into later tasks without a current trigger.

### Advance or stop

Advance only when exit evidence and the next entry criteria are satisfied. Otherwise record the exact blocker, owner, and smallest required action. Close the project with final evidence, residual risks, and follow-up ownership.

## 7. Use the right template modules

- `assets/task-plan.md`: Level 1 core resumable task plan.
- `assets/task-plan-coordination-addon.md`: cross-task decisions, blockers, and downstream handoff; add only when needed.
- `assets/task-plan-git-addon.md`: Git isolation and delivery identity; use with the Git reference.
- `assets/task-plan-integration-addon.md`: reviewed and integration SHA chain; use only for initiative integration.
- `assets/project-roadmap.md`: core multi-task roadmap.
- `assets/project-roadmap-transition-addon.md`: predecessor and carryover mapping for a successor roadmap.
- `assets/milestone-audit.md`: Level 3 milestone gate.
- `assets/promotion-gate.md`: initiative integration to primary-branch promotion.
- `assets/roadmap-alignment-notes.md`: durable successor-roadmap discussion ledger.

Adapt modules to repository conventions and omit irrelevant sections instead of filling them with `not applicable`. Do not rename an established project artifact merely to match this skill.

For Level 2/3 artifacts materialized from these templates, run `python3 scripts/validate_project_docs.py <files...>` once before closeout. Level 1 does not require this validator by default; use it only when repository policy or a strict template workflow requires it. The validator checks unresolved placeholders, base-state values, and obvious completion contradictions; it does not replace evidence review or support arbitrary custom schemas.
