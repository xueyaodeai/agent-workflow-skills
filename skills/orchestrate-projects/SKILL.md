---
name: orchestrate-projects
description: Coordinate projects whose execution must survive multiple tasks, sessions, milestones, worktrees, repositories, or environments. Use when work needs a durable task plan or project roadmap, parallel-work coordination, milestone audits, initiative integration, cross-context resume or handoff, or successor-roadmap alignment. Classify the smallest coordination level first; do not use for a self-contained single-session task unless the user explicitly requests durable project files.
---

# Orchestrate Projects

Keep long-running work resumable and evidence-backed without turning ordinary tasks into project-management exercises.

## Core invariants

1. Use the smallest structure needed for continuation, following the routing below. Respect user and repository authority; record only project-specific limits and the authorized delivery package.
2. Keep scope, decisions, ownership, and coordination state in project files. Verify code, runtime, and external facts at their authoritative sources; bind evidence to a revision, environment, or time when it affects the conclusion.
3. For Level 1, record the objective, acceptance checks, consequential scope boundary, and next action. For Level 2/3, record the milestone’s required flow, exit criteria, exclusions, accepted deferrals, blocker threshold, and stop condition from existing authorization.
4. A frozen contract preserves sourced requirements and authority boundaries, not inherited implementation choices. Recheck technical assumptions against current evidence and revise them within scope without reconfirmation. Only the user or delegated scope owner may change required outcomes or authorized boundaries; workers and reviewers must not invent completion conditions.
5. Choose the simplest complete solution by total implementation and lifecycle cost. Apply this to new and inherited mechanisms within scope; retain complexity only for a current caller, requirement, demonstrated failure, applicable rule, or material risk. Preserve unrelated work.

## 1. Route the request before loading details

Inspect applicable instructions, established project artifacts, and current evidence, then choose the smallest coordination level:

1. **Level 0 — ephemeral execution:** The work can finish and be verified in the current task, with no independent continuation or durable status view. Use the current task's lightweight plan if useful; do not create a project file.
2. **Level 1 — resumable task:** One outcome must survive a task, session, or environment boundary. Use the established task-plan format or copy `assets/task-plan.md`.
3. **Level 2 — multi-task project:** Coordination state must survive across multiple tasks, milestones, repositories, environments, or owners. Add the established roadmap or copy `assets/project-roadmap.md`; merely touching multiple repositories in one self-contained task does not require a roadmap.
4. **Level 3 — audited project:** An explicit milestone gate is required by the user, project rules, or a demonstrated coordination or delivery risk. Add `assets/milestone-audit.md`; parallel work or cross-repository changes alone do not raise the level.

Choose the delivery topology independently from the coordination level:

- Use `not_applicable` for read-only or non-Git work.
- Use the repository's normal feature-to-primary workflow when milestones remain independently reviewable and releasable.
- Use initiative integration only when its explicit gate is satisfied. Then read [references/integration-branch.md](references/integration-branch.md).

Load optional workflows only when their trigger applies:

- For Git changes or task-scoped delivery, read [references/git-delivery.md](references/git-delivery.md).
- When a merged PR/MR must close out issues, deployment evidence, or an existing plan, use the merge-closeout procedure in that Git reference. Do not infer deployment or issue-writing authority from a merge notification.
- For an initiative integration branch or primary-branch promotion, read [references/integration-branch.md](references/integration-branch.md).
- For carryover alignment or a successor roadmap, read [references/next-round-alignment.md](references/next-round-alignment.md).

## 2. Establish fact and artifact ownership

Treat project files as coordination ledgers, not universal factual authorities:

| Information | Authority | Durable record |
|---|---|---|
| User decisions, scope, non-goals, accepted deferrals | User or named policy owner | Roadmap decision ledger |
| Project milestone and dependency state | Coordinating task after reconciliation | Project roadmap |
| Task execution state and local choices | Task owner | Task plan |
| Code and change identity | Live repository | Revision, diff, branch, or delivery record |
| Test or review result | Producing system or reviewer | Evidence tied to subject, time, and environment |
| External status | Authoritative external system | Identifier and last-checked time |

Use these write rules:

- Give each shared artifact one writer. The coordinating task owns the roadmap and shared decision ledger.
- Each worker task owns its task plan. It must not edit the roadmap concurrently; return conclusion, changes, evidence, risks, and next step to the coordinator.
- On resume, recheck drift-prone facts and reconcile stale documents to live evidence.
- Write durable files only when the user requested them or an established, authorized project workflow already requires them.
- Preserve existing repository formats. Reference task plans and evidence by path instead of duplicating their contents.

## 3. Use one state protocol

Use the same base states for tasks, milestones, and projects:

`not_started -> in_progress -> ready_for_verification -> complete`

Use side states deliberately:

- `blocked`: the declared current objective cannot continue or complete until a named condition satisfying the applicable task, milestone, or project blocker threshold changes; it may return to `in_progress`.
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

- final outcome, completion criteria, constraints, and project-level non-goals;
- artifact owner and last reconciliation point;
- current milestone contract and milestone/workstream status;
- cross-task dependencies, decisions, blockers, and risk ownership;
- links to task plans and versioned evidence;
- next-milestone entry criteria and project closeout state.

Do not store command logs, detailed exploration, every failed attempt, or worker-local progress in the roadmap.

### Task plan

Use the Level 1 core defined above, with current state and closeout evidence. Add decisions, ownership, blockers, or handoff details only when they change execution or another context needs them to resume.

Use `assets/task-plan-coordination-addon.md` for cross-task decisions, blockers, or downstream handoff. Use other add-ons only when their trigger applies. Do not fill unused sections with `none` or `not applicable`; omit them.

## 5. Choose execution units

1. Keep work in the current task when it directly serves the current outcome and shares the same context.
2. Delegate bounded exploration, implementation with established interfaces, or verification when the benefit outweighs coordination cost and higher-priority instructions permit it. The main agent owns architecture decisions, integration, and final delivery.
3. Create or fork an independent task only when the user explicitly asks and durable visibility or isolation is required.
4. Run validation in the environment that has the required login, device, simulator, or permissions. If an authorized separate task is needed there, carry over the relevant context and evidence.
5. Isolate concurrent repository writers with dedicated branches and worktrees; never let two worktrees use the same branch.

Give each execution unit its objective, consequential bounds, expected evidence, and return destination. Include only context it does not already inherit; use the independent-review reference for reviewer inputs.

## 6. Run the coordination loop

### Orient

Read the roadmap and active task plan when present, applicable instructions, and authoritative current state. Reconcile stale claims before planning.

### Plan

Identify the current task or milestone, bounded execution units, dependencies, evidence requirements, authority boundaries, and delivery topology. Establish the level-appropriate contract described in the core invariants from existing authorization. Record only material assumptions and unresolved decisions.

Use `plan-outcomes`, when available, to create or revise requirements, work decomposition, and acceptance. Without it, map each sourced requirement to work and a check specifying the scenario, observable pass condition, and evidence to obtain; cover the overall delivery as well as stage results, and mark consequential unresolved decisions as blocking their dependent work. Keep this contract in the existing artifact, or in the chat plan when durable output is not authorized. This skill owns coordination state and completion evidence, not a second planning process.

Check which existing primitives satisfy the required behavior before adding a mechanism. Apply the core rules for scope and complexity when comparing solutions.

Split milestones for independently observable outcomes, hard dependencies, distinct authority or side-effect boundaries, or independently resumable contexts. Use bounded work units for parallel execution without turning each unit into a milestone.

### Execute

Execute or delegate the selected units. Keep worker-local detail out of the roadmap and report only progress that changes the result, next action, or blocker.

### Integrate

Verify returned work rather than accepting summaries uncritically. The coordinator promotes only cross-task conclusions, decisions, blockers, and evidence into the roadmap.

### Verify and close

Apply the level-specific completion conditions in section 3. Level 0/1 does not require roadmap reconciliation, handoff, audit, or template validation unless another active rule requires it. For Level 3, complete the milestone audit without substituting it for any independently required code review or runtime validation. Record only skipped checks that leave material risk.

Verification is always required; independent review is conditional:

- Use executor-owned checks proportional to the acceptance criteria and demonstrated regression risk. Reuse existing evidence; add tests only to prove required behavior, reproduce a defect, or protect a material boundary. After checks pass, repeat or broaden them only for new changes, failures, or unresolved concerns.
- Require independent review when the user or an applicable rule requires it, or when the change materially affects a public contract, security or sensitive data, an irreversible production effect, or critical fail-closed behavior. Coordination level, file count, duration, attempts, and bounded external reads alone do not trigger review.
- When independent review is required, read [references/independent-review.md](references/independent-review.md) for reviewer setup, blocker criteria, and targeted rechecks. Otherwise, use executor preflight for bounded low-risk operations without adding independent approval steps.

### Advance or stop

Advance when required exit evidence and the next entry criteria are satisfied; otherwise record the blocker, owner, and next action. At the agreed completion boundary, close with evidence and any material follow-up ownership.

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

For Level 2/3 artifacts materialized from these templates, run `python3 scripts/validate_project_docs.py <files...>` once before closeout. Level 1 does not require this validator by default; use it only when repository policy or a strict template workflow requires it. The validator checks required template fields and tables, unresolved placeholders, state values, and completion contradictions; it does not replace evidence review or support arbitrary custom schemas.
