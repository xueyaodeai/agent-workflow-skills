---
name: orchestrate-projects
description: Coordinate projects whose execution must survive multiple tasks, sessions, milestones, worktrees, repositories, or environments. Use when work needs a durable task plan or project roadmap, parallel-work coordination, milestone audits, initiative integration, cross-context resume or handoff, or successor-roadmap alignment. Classify the smallest coordination level first; do not use for a self-contained single-session task unless the user explicitly requests durable project files.
---

# Orchestrate Projects

Keep long-running work resumable and evidence-backed. Help a human understand the outcome, current gap, and next action before reading execution detail.

## Core invariants

1. Use the smallest structure needed for continuation, following the routing below. Respect user and repository authority; record only project-specific limits and the authorized delivery package.
2. Keep scope, decisions, ownership, and coordination state in coordination artifacts (`$(git rev-parse --git-common-dir)/agent/` for local cross-session/worktree state, or the repository host's native Issue/Milestone/PR-or-MR for shared delivery: check whether the repository is on GitHub first, otherwise use the project's own host), not as tracked commits in the repository unless the user explicitly asks to version-control them. Verify code, runtime, and external facts at their authoritative sources; bind evidence to a revision, environment, or time when it affects the conclusion.
3. At every level, including Level 0 and direct assignments, establish why, what, the shortest and best complete paths with the selected approach, and complete acceptance. Both paths meet the same criteria and may be identical. Reuse settled answers; missing consequential decisions block dependent implementation, not independently ready authorized work. Do not invent answers or require repeated approval. For Level 1, record or reference this contract and the next action. For Level 2/3, also record the milestone’s required flow, exit criteria, exclusions, accepted deferrals, blocker threshold, and stop condition.
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

Use these write and storage rules:

- Give each shared artifact one writer. The coordinating task owns the roadmap and shared decision ledger.
- Each worker task owns its task plan. It must not edit the roadmap concurrently; return conclusion, changes, evidence, risks, and next step to the coordinator.
- On resume, recheck drift-prone facts and reconcile stale documents to live evidence.
- Default to untracked local storage under `$(git rev-parse --git-common-dir)/agent/` (for example, `.git/agent/roadmap.md` and `.git/agent/tasks/<slug>.md`, shared across worktrees) for local continuation, and use the repository host's native tracker (check the repository remote first: use GitHub Issue/Milestone/PR for GitHub repositories, otherwise the project's own host such as Gongfeng/GitLab Issue/Milestone/MR) for shared contracts, milestones, and closeout evidence. Do not commit `roadmap`, `task-plan`, `milestone-audit`, `PROGRESS.md`, or run-evidence files to the Git repository unless the user explicitly asks to version-control them; the mere existence of legacy `docs/plans/`, `docs/roadmap/`, or `PROGRESS.md` in a repository is not authorization to add or commit more process ledgers.
- Commit only enduring system documentation (architecture, API/tool contracts, operator runbooks) when the task changes current system behavior, and fold those updates into the code commit rather than creating standalone `docs(...)` progress commits.
- Preserve existing formats when updating an explicitly requested artifact. Reference task plans and evidence by path or URL instead of duplicating their contents.

## 3. Use one state protocol

Use the same base states for tasks, milestones, and projects:

`not_started -> in_progress -> ready_for_verification -> complete`

Use side states deliberately:

- `blocked`: the declared current objective cannot continue or complete until a named condition satisfying the applicable task, milestone, or project blocker threshold changes; it may return to `in_progress`.
- `deferred`: removed from the active sequence with an owner or reconsideration trigger.
- `cancelled`: intentionally stopped by an authorized owner.
- `superseded`: replaced by a newer artifact or decision, with a reference to the replacement.

Track execution readiness separately from progress: `Readiness: ready | not_ready`, with named decision gaps when not ready. A ready contract is not permission, satisfied dependencies, completed implementation, or `ready_for_verification`. Each execution unit must own or explicitly inherit why, what, path choice, and acceptance from accessible sources. An unclear root objective blocks dependent implementation; bounded clarification may proceed only with its own ready, authorized contract. Recheck affected readiness after scope or evidence changes.

Do not use `partial` as a terminal state. Keep unfinished work `in_progress` or `blocked`, or explicitly move it to `deferred`, `cancelled`, or `superseded`.

Record only transitions that change a decision, blocker, downstream dependency, delivery identity, or next resumable action. Batch routine step progress; add an observation time only for drift-prone facts.

Scale `complete` to the selected level:

- **Level 0:** the requested result exists and a concise current-task check supports it.
- **Level 1:** the observable objective is satisfied, current evidence supports it, no in-scope blocker remains, and the delivery boundary is explicit.
- **Level 2:** Level 1 plus dependent handoff and roadmap reconciliation are complete where another task relies on them.
- **Level 3:** Level 2 plus the required milestone audit and high-risk gates pass.

Do not add a higher-level condition to a lower-level task merely because the template contains a matching field.

## 4. Keep project and task state separate

### Reading order and information ownership

Write in the user's language. Open with the problem and intended outcome, then what exists, what is still missing, the next action or required decision, and the delivery boundary. Keep this opening brief and tied to the current records below; do not create a separate summary file. Explain technical terms where they first affect a decision and name milestones by observable outcomes, retaining IDs for references.

Give each document a distinct job:

- An existing progress/index page points to the active work with a short conclusion, next action, and link. Do not copy experiment histories or detailed acceptance there.
- The roadmap explains project outcomes, milestone order, dependencies, completion conditions, and consequential decisions.
- The task plan explains the current solution, execution steps, exact acceptance checks, and task evidence.

Keep detailed state at its owning record and link to it. Summarize only conclusions that change project coordination; reconcile those summaries when the owning record changes. Put revisions, hashes, per-attempt counts, commands, and detailed budgets beside the execution or evidence they identify, unless they change the immediate decision.

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

Add the add-ons listed in section 7 only when their trigger applies.

### Compact contracts and current decisions

Preserve why, what, path choice, and acceptance without repeating the same explanation at every level. Reference accessible parent requirements and boundaries, then describe the task or milestone's specific contribution and differences. When shortest and best paths coincide, explain the route and reason once; in template-shaped documents keep the supported field labels with short references. In custom prose they may share one sentence. Keep distant milestones at outcome, dependency, exit, and refinement-trigger detail until needed.

Maintain one unambiguous current plan. When a decision changes, update the affected current approach, steps, acceptance, readiness, and next action together, within the artifact's write ownership. Cross-artifact changes go through the owning writer. Preserve earlier decisions and results in a clearly historical section or a fixed revision with its path; name what supersedes them. Keep historical records out of current state/contract fields parsed by the validator. A top note saying “the latest decision overrides the following” does not reconcile obsolete instructions. Preserve unresolved requirements and evidence gaps when reorganizing; readability is not authority to weaken acceptance or erase history.

Use tables for comparisons, dependencies, or repeated acceptance scenarios when they help scanning. Avoid dense paragraphs or table cells that combine several decisions. State what a status means for the reader and distinguish implementation, functional verification, measured improvement, and deployment acceptance. Keep planned checks separate from observed results. Retain the established machine-readable states and field labels when using the supported templates; custom repository formats keep their own conventions.

## 5. Choose execution units

1. Keep work in the current task when it directly serves the current outcome and shares the same context.
2. Delegate bounded exploration, implementation with established interfaces, or verification when the benefit outweighs coordination cost and higher-priority instructions permit it. The main agent owns architecture decisions, integration, and final delivery.
3. Create or fork an independent task only when the user explicitly asks and durable visibility or isolation is required.
4. Run validation in the environment that has the required login, device, simulator, or permissions. If an authorized separate task is needed there, carry over the relevant context and evidence.
5. Isolate concurrent repository writers with dedicated branches and worktrees; never let two worktrees use the same branch.

Give each execution unit its rationale, objective, shortest/best paths and selected approach, consequential bounds, acceptance and expected evidence, and return destination. Reuse accessible parent contracts instead of duplicating them. Include only context it does not already inherit; use the independent-review reference for reviewer inputs.

## 6. Run the coordination loop

### Orient

Read the roadmap and active task plan when present, applicable instructions, and authoritative current state. Reconcile stale claims before planning.

### Plan

Identify the current task or milestone, bounded execution units, dependencies, evidence requirements, authority boundaries, and delivery topology. Establish the level-appropriate contract described in the core invariants from existing authorization. Record only material assumptions and unresolved decisions.

Use `plan-outcomes`, when available, for requirements, work decomposition, and acceptance. Without it, establish why the work is justified, its observable deliverables and scope, the shortest and best paths under the same acceptance criteria, the chosen approach and reason, and scenario-based checks with pass conditions and required evidence. Mark consequential unresolved decisions as blocking their dependent work; direct assignments do not bypass this check. Keep this contract in the existing artifact, or in the chat plan when durable output is not authorized.

Check which existing primitives satisfy the required behavior before adding a mechanism.

Split milestones for independently observable outcomes, hard dependencies, distinct authority or side-effect boundaries, or independently resumable contexts. Use bounded work units for parallel execution without turning each unit into a milestone.

### Execute

Execute or delegate only units whose contracts are ready, prerequisites satisfied, and actions authorized. Keep worker-local detail out of the roadmap and report only progress that changes the result, next action, or blocker.

### Integrate

Verify returned work rather than accepting summaries uncritically. The coordinator promotes only cross-task conclusions, decisions, blockers, and evidence into the roadmap.

### Verify and close

Apply the level-specific completion conditions in section 3. For Level 3, complete the milestone audit without substituting it for any independently required code review or runtime validation. Record only skipped checks that leave material risk.

Check reading usability in the same closeout: can a new reader identify the outcome, current result and gap, next action, and delivery boundary from the opening? Can an executor find the single current plan and full acceptance without interpreting historical overrides? Do links lead to the owning detail, and do summaries agree with it? Repair ambiguity in the existing artifacts without adding an approval stage or treating length limits as proof of readability.

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

For template-shaped roadmaps, milestone audits, and alignment notes, run `python3 scripts/validate_project_docs.py <files...>` once before closeout. Task and Outcome Plans are also supported, but Level 1 does not require this validator by default. Use `--require-ready` when checking a selected task or a roadmap's current execution scope before starting it. Drafts may remain explicitly not ready; a structural pass never grants execution authority.

The validator checks supported fields, scoped milestone contracts, state values, placeholders, and completion contradictions. Unknown formats are reported as unsupported, not passing; standalone add-ons and promotion gates require their own evidence review. It does not establish the truth or accessibility of cited evidence, semantic completeness, or host-enforced permission. Preserve custom repository formats and review their equivalent contracts rather than renaming them to satisfy this script.
