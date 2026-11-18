# Writing Project Records

Read this reference when creating, resuming, or updating a roadmap, task plan, milestone audit, or progress page.

## Record ownership and sources

| Record | Owns | Writer |
| --- | --- | --- |
| Progress or index page | A brief current result, next action, and link to active work | Its existing owner |
| Task plan | Selected approach, work and dependencies, exact acceptance checks, evidence, current state, and next action | Task owner |
| Project roadmap | Final outcome and completion criteria, scope and non-goals, current milestone contract, downstream dependencies, decision ledger, accepted deferrals, risk owners and links to task evidence | Coordinator |
| Milestone audit | Required flow, exit criteria, evidence, blockers and verdict for the specific gate | Designated audit owner |

Keep one writer per shared artifact. Workers return changes, evidence, risks, and next steps to the coordinator instead of editing the roadmap concurrently. The user or named policy owner is authoritative for scope, exclusions and deferrals. Obtain code identity from the live repository, test or review results from their producing system, and external status from its owning system. Bind evidence to a revision, environment, or time where it matters. Reconcile stale records before resuming. Keep commands, attempts and local experiments with task evidence, and link rather than copying them into the roadmap.

Use the [storage rules](../SKILL.md#store-durable-records). Check the repository remote before choosing a project tracker. For Level 1, record or link the execution contract and next action. For Levels 2 and 3, also record the current milestone's required flow, exit criteria, exclusions, accepted deferrals, blocker threshold, and stop condition. Keep the roadmap owner, last reconciliation point, next milestone entry criteria, and closeout state visible.

## Progress and readiness

Use `not_started -> in_progress -> ready_for_verification -> complete` for tasks, milestones, and projects. Use `blocked` when a named condition meets the applicable blocker threshold, `deferred` with an owner or reconsideration trigger, `cancelled` for an authorized stop, and `superseded` with a replacement reference. A blocked unit may return to `in_progress`. Keep unfinished work in an active or explicit side state rather than closing it as partial.

Track execution readiness separately with `Readiness: ready | not_ready` and named gaps when not ready. Readiness records the contract. Progress, permission, and prerequisites each have their own evidence. Record only transitions that affect a decision, blocker, dependency, delivery identity, or resumable action. Batch routine progress and add observation times for drift-prone facts.

## Reading order

Write in the user's language. Open with the problem and intended outcome, then what exists, what is still missing, the next action or required decision, and the delivery boundary. Keep this opening brief and tied to the current records; do not create a separate summary file. Explain technical terms where they first affect a decision and name milestones by observable outcomes, retaining IDs for references.

## Compact contracts

Preserve why, what, path choice, and acceptance without repeating the same explanation at every level. Reference accessible parent requirements and boundaries, then describe the task or milestone's specific contribution and differences. When shortest and best paths coincide, explain the route and reason once; in template-shaped documents keep the supported field labels with short references. In custom prose they may share one sentence. Keep distant milestones at outcome, dependency, exit, and refinement-trigger detail until needed.

## Current and historical content

Keep historical records out of current state/contract fields parsed by the validator. A top note saying “the latest decision overrides the following” does not reconcile obsolete instructions. Preserve unresolved requirements and evidence gaps when reorganizing; readability is not authority to weaken acceptance or erase history.

Use tables for comparisons, dependencies, or repeated acceptance scenarios when they help scanning. Avoid dense paragraphs or table cells that combine several decisions. Label implementation, functional verification, measured improvement, and deployment acceptance directly instead of adding disclaimers about what a status does not mean. Keep planned checks separate from observed results. Retain the established machine-readable states and field labels when using the supported templates; custom repository formats keep their own conventions.

## Closeout readability

At closeout, check that a new reader can identify the outcome, current result and gap, next action, and delivery boundary from the opening; that an executor can find the single current plan and full acceptance without interpreting historical overrides; and that links lead to the owning detail and summaries agree with it. Repair ambiguity in the existing artifacts without adding an approval stage or treating length limits as proof of readability.
