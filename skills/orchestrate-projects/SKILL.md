---
name: orchestrate-projects
description: Coordinate long-running projects across multiple Codex tasks, sessions, milestones, worktrees, branches, or environments while keeping plans, progress, decisions, blockers, handoffs, verification evidence, task-scoped commits, temporary initiative integration branches, and master promotion gates synchronized in durable project files. Use when the user asks to organize or continue a multi-session project, maintain a plan or roadmap, prepare a next-round roadmap from current carryover work and multi-round user alignment, preserve planning discussions as durable notes, coordinate parallel work, manage feature or integration branches, reduce repeated master review churn, split work into tasks or subagents, resume work from another conversation, audit milestone completion, or establish a reusable long-running Codex workflow. Keep simple one-session tasks lightweight.
---

# Orchestrate Projects

Turn long-running work into a documented control loop without burdening simple tasks. Preserve the user's existing repository conventions and treat project files—not chat history—as the durable cross-task source of truth.

## Operating principles

1. Inspect before organizing. Read applicable instructions, existing plans, repository state, and current evidence before creating new artifacts.
2. Use the smallest sufficient structure. Do not create a project roadmap for a simple, self-contained task.
3. Separate project state from task execution detail.
4. Record verified facts, decisions, blockers, and evidence; do not invent progress.
5. Keep one clearly identified current milestone for the coordinating task.
6. Require evidence before declaring a task or milestone complete.
7. Preserve analysis-only, review-only, implementation, and publication boundaries from the user's request.
8. Never assume separate tasks share chat context. Persist cross-task facts in project files.
9. Treat an implementation task with repository changes as complete only after its intended changes are committed without unrelated work.
10. Use integration branches to stage and verify an initiative, never to bypass required master review or create a permanent second trunk.
11. Build a next-round roadmap from verified carryover work and durable user-alignment notes, never directly from unpersisted chat context.

## 1. Classify the work

Choose one of these levels after inspecting the workspace.

### Level A: single-task execution

Use one task plan only when all are true:

- the work is expected to fit in one task or session;
- there is one primary outcome;
- no independent workstream needs separate continuation;
- no cross-environment handoff is required;
- completion evidence can be collected in the same task.

Use the existing plan format when one exists. Otherwise copy `assets/task-plan.md` and adapt it.

### Level B: multi-task project

Add a project roadmap when any condition holds:

- work will span two or more tasks or sessions;
- multiple milestones or parallel workstreams exist;
- one task produces input for another;
- work spans repositories, branches, worktrees, machines, or environments;
- the user needs a durable global status view;
- the project is likely to continue for days or be resumed later.

Use the repository's established roadmap file if present. Otherwise copy `assets/project-roadmap.md`. Do not rename existing artifacts merely to match this skill.

### Level C: coordinated long-running project

Use the Level B structure plus explicit milestone audits when the project includes meaningful parallelism, high-risk changes, multiple validation surfaces, or changing requirements. Add a separate dashboard only when the roadmap is no longer a usable status view; do not create one by default.

Add a temporary initiative integration branch only when multiple dependent milestones need a shared pre-master baseline, intermediate states are not independently safe for master, combined integration validation is required, or repeated master review creates material coordination cost. Prefer direct master integration—usually behind feature flags—when milestones can remain independently releasable and the repository expects trunk-based development.

## 2. Establish sources of truth

Maintain two operational layers. When preparing a successor roadmap, add one temporary alignment layer until the new roadmap is approved.

### Project roadmap

Store only global state:

- final outcome and project completion criteria;
- constraints and non-goals;
- current milestone;
- milestone and workstream status;
- branch topology, master baseline, integration head, feature identities, and promotion checkpoints when applicable;
- cross-task decisions and blockers;
- links or paths to task plans and evidence;
- links to alignment notes and carryover disposition when this is a successor roadmap;
- next milestone entry criteria.

Do not copy detailed command logs, code exploration, or every failed attempt into the roadmap.

### Task plan

Store task-local execution state:

- task objective, scope, and non-goals;
- upstream inputs and assumptions;
- ordered work and current progress;
- decisions made in this task;
- validation commands and results;
- branch, worktree, intended change set, and delivery commit;
- blockers and required user decisions;
- downstream handoff and remaining work;
- closeout status.

Make every task plan independently readable by a new task. Include exact paths, identifiers, and verified current state when useful.

### Next-round alignment notes

Use one alignment-notes file for each roadmap transition. It is the durable planning source between the current roadmap and its successor:

- current roadmap, milestone audits, open plans, live repository state, unresolved reviews, and external-task state used as inputs;
- every residual item and its evidence-backed current status;
- each discussion round with user decisions, agent proposals, rejected or deferred alternatives, and remaining questions;
- consolidated decisions and the readiness gate for generating the successor roadmap;
- the resulting roadmap path after the notes are consumed.

Default to a repository path such as `docs/roadmap/discussions/<date>-<initiative>-next-round-alignment.md`, but preserve an established local convention. Append rounds to the same file as `R1`, `R2`, and so on; do not create a new file for every chat turn unless independent workstreams require separate ownership. Summarize material decisions instead of copying the chat transcript, and never persist secrets or irrelevant conversational detail.

## 3. Select the execution unit

Use this decision order:

1. Keep work in the current task when it is directly necessary for the current outcome and shares the same context.
2. Use a subagent only for bounded work that can be independently described and summarized, such as read-only investigation, focused testing, classification, or an isolated implementation. Delegate only when the user has requested delegation or parallel work and higher-priority instructions permit it.
3. Recommend an independent task when work must remain visible for later continuation, requires its own goal or review history, or should be isolated from the coordinator. Create or fork a task only when the user explicitly asks.
4. Use a side task only for temporary status questions or supplemental guidance. Do not store durable implementation state there.
5. Use a separate local task for validation that depends on login state, desktop applications, device permissions, Xcode, simulators, or other machine-local state.
6. Use a dedicated branch and separate worktree before editing when independent tasks will write to the same repository concurrently. Do not let two worktrees check out the same branch.
7. For an initiative integration workflow, branch each milestone or fix from the current integration baseline and target it back to that integration branch. Do not branch from another feature unless the dependency is intentionally stacked and documented.

For every delegated unit, specify:

- objective;
- allowed scope;
- read-only or write authorization;
- constraints and non-goals;
- required evidence;
- expected return format;
- destination for durable findings.

Require summaries to return: conclusion, changes, evidence, risks, and recommended next step.

## 4. Manage initiative integration branches

Use this section only when the Level C decision explicitly enables an integration branch.

### Bootstrap and protect the integration branch

- Follow repository naming conventions; otherwise use `integration/<initiative>`.
- Create it from a verified master commit and record the baseline SHA before accepting feature work.
- Make it initiative-scoped, temporary, and owned by the coordinating task.
- Prohibit direct implementation commits. Merge implementation through reviewed feature or fix branches.
- Keep formal master CR, required CI, human approval, and repository protection intact. Internal review reduces churn; it does not waive policy.
- Record whether the platform permits feature-to-integration review requests. If not, retain equivalent review evidence in the roadmap.

### Gate feature or milestone integration

Require this sequence for every feature or milestone branch:

1. Create a dedicated feature branch and worktree from the recorded integration baseline.
2. Complete task-scoped implementation, verification, and commits without unrelated changes.
3. Synchronize the latest integration branch before final review and re-run affected checks.
4. Launch a fresh independent subagent to review the exact `integration...feature` diff when agent delegation is available and permitted. Otherwise use a separate read-only review task or the required human review, and record the substitution.
5. Record the reviewed feature-head SHA, findings, fixes, verification, and final verdict. Any post-review code change invalidates the verdict and requires re-review.
6. Merge only the exact reviewed SHA into the integration branch. Preserve a traceable feature identity through a merge commit or a repository-approved one-feature-one-commit strategy.
7. Record the feature SHA, reviewed SHA, integration merge SHA, and evidence in the task plan and roadmap.
8. Run integration checks after the merge. Repair failures through a separate fix branch and the same review gate; do not patch the shared integration branch directly.

### Synchronize branch direction and identity

- Synchronize `master -> integration` periodically and before every master promotion.
- Do not rebase or rewrite a shared integration branch. Rebase or merge feature branches onto the latest integration baseline before final review according to repository policy.
- Promote `integration -> master` only through an explicit promotion gate.
- Preserve four identities: feature head, reviewed SHA, integration head/merge SHA, and master-candidate SHA.
- If master review forces squash and breaks ancestry, recreate the next-stage integration branch from the new master head and explicitly retarget or rebuild active feature branches.

### Plan master promotion checkpoints

Do not promote every small milestone and do not defer everything into one unreviewable final change. Define candidate checkpoints in the roadmap and reassess them from evidence.

Use a checkpoint when one or more conditions hold:

- a backward-compatible foundation or shared contract is stable and needed downstream;
- the first complete vertical slice is runnable and independently verifiable;
- multiple milestones form a coherent, deployable, or reversible unit;
- the initiative is about to enter a riskier phase and the current result should be secured;
- divergence from master creates material conflict, review, or validation risk;
- the final initiative candidate is ready.

Before promotion:

1. Freeze and record the integration candidate SHA.
2. Synchronize the latest master and resolve conflicts in the integration workflow.
3. Run the required integration and full-regression suite against the candidate.
4. Run an independent audit of the accumulated delta since the previous promotion and verify the feature/review/merge identity chain.
5. Confirm no blocking findings, missing milestone evidence, or policy exceptions remain.
6. Use `assets/promotion-gate.md` or the repository's equivalent record.
7. Open or update the formal integration-to-master CR only when authorized; merge only after its required approvals and checks pass.
8. Record the resulting master SHA and post-merge validation. A commit, internal merge, or agent review does not authorize push, CR creation, or master merge.

After the final promotion, close and delete the temporary integration branch when repository policy and active-task state make that safe.

## 5. Run the coordination loop

Repeat this loop until the project completion criteria are satisfied or a real blocker requires the user.

### A. Orient

- Read the roadmap, active task plan, applicable instructions, and current repository state.
- For Git work, inspect the current branch, worktree, `git status --short`, staged diff, and unstaged diff. Separate pre-existing or other-task changes from the current task's intended change set before editing.
- Reconcile stale checkboxes or claims against live evidence.
- Identify the current milestone and its entry/exit criteria.
- If no roadmap is warranted, continue with the task plan only.

### B. Plan

- Convert the current milestone into bounded tasks.
- Identify dependencies and safe parallel work.
- Define the evidence required for each task.
- Record material assumptions and unresolved decisions.
- Decide whether direct master integration or an initiative integration branch is justified. If using integration, record the baseline, merge strategy, review mechanism, synchronization policy, and candidate promotion checkpoints before parallel implementation.
- Use built-in Goal mode only when the user explicitly requests a persistent goal; otherwise record the current milestone in the roadmap.

### C. Execute and coordinate

- Perform current-task work directly.
- Delegate only work that meets the execution-unit rules.
- Keep a concrete list of files and, when necessary, hunks owned by the current task. Do not absorb unrelated dirty-worktree changes into the task merely because they are present.
- Keep implementation details in task plans, not the project roadmap.
- Send concise progress updates using `已完成 / 下一步 / 阻塞项` and include evidence when status materially changes.

### D. Integrate

- Verify returned work instead of accepting summaries uncritically.
- Reconcile changes, decisions, and evidence into the task plan.
- Promote only cross-task information into the roadmap.
- Resolve conflicting claims against current files, tests, logs, or environment state.
- Apply the feature-to-integration gate from section 4 when an initiative integration branch is active.

### E. Commit the completed task

For an implementation task that changed a Git repository, create a task-scoped delivery commit before marking the task complete:

1. Finish the task's required verification against the exact working tree to be committed.
2. Inspect `git status --short`, the unstaged diff, and the staged diff.
3. Match changed files and hunks against the task plan's intended change set.
4. Stage only the current task's files or hunks. In a dirty or shared worktree, do not use broad staging such as `git add .` or `git add -A`.
5. Inspect the staged name list and full staged diff. Remove anything unrelated, secret, generated unexpectedly, or owned by another task.
6. Create a concise task-scoped commit that follows the repository's commit convention. Default to one closeout commit; use multiple commits only when the task has independently coherent changes and each commit remains task-local.
7. Record the commit SHA, branch, worktree, committed paths, and verification result in the task plan. Promote the SHA to the roadmap evidence index when downstream tasks depend on it.

If unrelated edits overlap the same file, stage only the current task's hunks when the separation is safe and reviewable. Otherwise, do not commit the whole file, stash, reset, discard, or rewrite another task's changes; leave the task `blocked` or `ready_for_commit` and request the minimum decision needed.

If a commit hook or required check fails, fix the in-scope cause and re-run it. Do not bypass hooks unless the user explicitly authorizes that exception.

Do not create a commit for a read-only analysis/review task, a task with no repository changes, a non-Git workspace, or when the user explicitly requested no commit. Record `commit not required` and the reason. If implementation was authorized and current-task changes remain uncommitted, do not report the task as complete.

A commit is not a push. Push, publish, open a review, deploy, or message others only when separately authorized.

### F. Audit the milestone

Use `assets/milestone-audit.md` or the repository's existing audit format. Check:

- whether the promised outcome exists;
- whether scope and non-goals were respected;
- whether required evidence passed and is attributable to the reviewed version;
- whether implementation tasks delivered isolated commits and whether the reviewed version includes the expected SHAs;
- whether feature review, integration merge, and master-candidate identities are traceable when an integration branch is active;
- whether new findings change later milestones or sequencing;
- whether unresolved risks block entry into the next milestone;
- whether an independent code review or local validation is still required.

Keep roadmap audit and code review conceptually separate: the roadmap audit checks project correctness and sequencing; code review checks implementation defects. For material code changes, run or recommend the applicable review workflow before closing the milestone.

### G. Advance or stop

- Mark a milestone complete only when its exit criteria and evidence are satisfied.
- Update the roadmap's current milestone, status table, decisions, blockers, and next entry criteria.
- Evaluate promotion checkpoint conditions after milestone integration; do not equate milestone completion with automatic master promotion.
- If blocked by a consequential user decision, record the exact decision and stop at that boundary.
- If the project is complete, close the roadmap with final evidence, residual risks, and follow-up ownership.

## 6. Synchronization rules

Apply these rules whenever multiple tasks are involved:

- Chat messages are task-local; project files are durable.
- A task is not synchronized until its relevant conclusion and evidence are written to the agreed project file.
- An implementation task is not delivered until its task-scoped commit SHA is recorded, unless an explicit no-commit exception applies.
- An integration milestone is not delivered until the reviewed feature SHA, integration merge SHA, and post-merge verification are recorded.
- Reference task plans by path instead of duplicating their content.
- Give each decision a date or stable identifier when later tasks may revisit it.
- Record upstream input and downstream handoff in every task plan.
- On resume, trust live repository and evidence over stale document status, then correct the document.
- Do not overwrite unrelated user edits or silently replace established plan structure.

## 7. Closeout contract

Before closing a task, write:

- outcome and current status;
- files or systems changed;
- verification performed and exact result;
- delivery commit SHA, branch, worktree, and committed paths, or the explicit reason no commit was required;
- skipped or unavailable verification;
- unresolved risks and blockers;
- durable decisions produced;
- next task, required inputs, and recommended first action.

Before closing the project, verify:

- all milestone exit criteria are satisfied or explicitly deferred;
- final evidence is linked or recorded;
- deferred items have owners or follow-up destinations;
- task plans and roadmap agree on final state;
- all completed implementation tasks have attributable commits that exclude unrelated work;
- integration initiatives preserve feature, reviewed, integration, and master-candidate identities and complete every required promotion gate;
- temporary integration branches have an explicit continuation or retirement decision;
- no document claims completion that current evidence contradicts.

## 8. Prepare and align the next-round roadmap

Use this workflow when the user asks what should follow the current roadmap, requests a next-round roadmap, or starts aligning future milestones before the current round closes. Do not immediately write a polished successor roadmap.

### A. Build the carryover inventory

Read the current roadmap, task plans, milestone audits, live Git and deployment state, open reviews, and external task trackers that are in scope. Add every residual item to the alignment notes and classify it as:

- `must_continue`: required to finish or safely close an existing commitment;
- `candidate`: useful future work that still needs prioritization;
- `defer`: intentionally postponed with a reason or trigger for reconsideration;
- `drop`: no longer needed, superseded, or rejected;
- `external_dependency`: owned outside the project but able to constrain the next round.

For each item, record its source, evidence, current state, reason it remains, proposed disposition, and whether a user decision is required. Keep unverified claims visibly unverified. Do not silently promote a deferred idea into a committed milestone.

### B. Run the alignment conversation

Start from the carryover inventory, then discuss the additional content that cannot be derived safely from project evidence: desired outcome, new capabilities, removals, constraints, non-goals, sequencing, delivery boundaries, and acceptance evidence. Discuss one coherent decision set at a time rather than presenting an unbounded questionnaire.

After every material user exchange, append a discussion round to the alignment notes before relying on it in later planning. Each round must identify:

- round ID and date;
- topics discussed and evidence reviewed;
- user-confirmed decisions;
- agent proposals that remain proposals;
- rejected, deferred, or superseded options;
- unresolved questions and the next discussion focus.

Do not rewrite prior rounds to make the conversation look linear. When a later decision changes an earlier one, preserve the earlier record and add an explicit superseding decision. A new task or session must resume from the notes, verify drift-prone facts, and continue with the next unresolved decision instead of reconstructing the discussion from chat history.

### C. Gate roadmap generation

Generate the successor roadmap only when:

- every carryover item has a disposition;
- the next-round final outcome and measurable completion criteria are understood;
- constraints, non-goals, removals, and compatibility boundaries are recorded;
- milestone ordering, dependencies, and required evidence are coherent;
- consequential user decisions are resolved or explicitly accepted as open blockers;
- the user-aligned decisions and remaining proposals are distinguishable.

If alignment is incomplete, keep the notes in `alignment_in_progress` and continue the discussion. Create a provisional roadmap only when the user explicitly requests a draft, and label it `draft/unreviewed`; do not treat it as the execution source of truth.

### D. Materialize and verify the successor roadmap

Generate the roadmap from the consolidated decisions in the alignment notes, not directly from chat. Include:

- alignment provenance and the notes path;
- a carryover-disposition table mapping each residual item to a milestone, deferral, drop decision, or external dependency;
- final outcome, boundaries, milestones, exit evidence, dependencies, risks, and unresolved blockers;
- the first milestone entry criteria and recommended first task.

Then compare the roadmap back to the notes. Confirm that no agreed item was lost, no proposal became a decision without approval, no dropped work reappeared, and no milestone claims evidence that does not exist. Mark the notes `aligned` and record the roadmap path only after this reconciliation passes. Later scope changes start a new discussion round and an explicit roadmap decision update; do not silently rewrite planning history.

## Templates

- Copy `assets/project-roadmap.md` for a new multi-task project roadmap.
- Copy `assets/task-plan.md` for a new task-level execution plan.
- Copy `assets/milestone-audit.md` for a milestone gate review.
- Copy `assets/promotion-gate.md` for an integration-to-master promotion decision.
- Copy `assets/roadmap-alignment-notes.md` before discussing or generating a successor roadmap.

Adapt templates to repository conventions. Remove unused sections rather than filling them with invented values.
