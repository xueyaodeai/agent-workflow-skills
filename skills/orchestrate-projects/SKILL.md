---
name: orchestrate-projects
description: Coordinate work that needs a durable task plan, roadmap, or milestone audit. Use to advance or resume that work across tasks, sessions, or environments.
metadata:
  version: 1.1.0
---

# Orchestrate Projects

Keep long-running work resumable through one current plan, clear ownership, and evidence-backed completion.

## Choose the smallest coordination level

- **Level 0 — current task:** If work can finish and be verified here and nobody needs durable status or independent continuation, use a short chat plan if useful. Continue directly to the execution contract below. Create no project record and skip references unless a specific delivery or review requirement calls for one.
- **Level 1 — resumable task:** One outcome must survive a task, session, or environment boundary. Use the existing task plan or [task-plan template](assets/task-plan.md).
- **Level 2 — multi-task project:** Dependencies or ownership must be coordinated across tasks, milestones, repositories, or environments. Use the existing roadmap or [project-roadmap template](assets/project-roadmap.md). Touching multiple repositories in one self-contained task is insufficient by itself.
- **Level 3 — audited project:** Add a [milestone audit](assets/milestone-audit.md) when an explicit milestone gate follows from the request, project rules, or a demonstrated delivery risk. Parallelism or multiple repositories alone do not require an audit.

Load only the references needed for the current action:

| Action | Reference |
| --- | --- |
| Create, resume from, or update a durable record | [Writing project records](references/writing-records.md) for owners, progress states, and record structure |
| Create or close a template-shaped record, or choose add-ons | [Templates and validation](references/templates.md) |
| Execute a task-scoped Git delivery, verify Git identity for continuation, or reconcile a merged PR/MR | [Git delivery](references/git-delivery.md). Follow the active repository instructions for ordinary Level 0 local edits and verification |
| Integrate milestones through a shared branch | [Initiative integration](references/integration-branch.md). Use only when its gate is satisfied. Otherwise prefer normal feature-to-primary delivery when milestones are independently releasable |
| Align carryover or plan a successor roadmap | [Next-round alignment](references/next-round-alignment.md) |
| Coordination genuinely requires separate execution units | [Execution units](references/execution-units.md) |
| Independent review is required under the closeout rules below | [Independent review](references/independent-review.md) |

## Establish the execution contract

For any level and direct assignments, establish why, what, the shortest and best complete paths with the selected approach, and complete acceptance. Both paths must satisfy the same complete acceptance criteria and may be identical. Reuse settled answers and let execution units explicitly inherit accessible decisions. Do not invent answers: a missing consequential decision blocks only dependent work. A bounded clarification can proceed with its own goal, approach, and evidence target. Recheck affected assumptions and readiness when scope or evidence changes.

Confirm authorization and prerequisites before executing. Preserve sourced requirements, authority boundaries, and unrelated work. Revise reversible technical choices using current evidence within scope. Only the user or delegated scope owner can change the required outcome or boundaries. For durable work, reconcile drift-prone facts with their authoritative sources and resume from the active plan or roadmap. If available, use `plan-outcomes` for detailed planning within the existing record, or define observable scenarios, pass conditions, and evidence directly.

If existing in-repo primitives cannot cover a required architecture change or non-trivial mechanism, first search GitHub or other open-source hosts for actively maintained frameworks or libraries. Evaluate candidates before writing custom code. Consider adoption, targeted integration, or adapting proven designs, and implement only the remaining gap.

Choose the simplest complete solution by lifecycle cost. Validate at data boundaries and reuse established internal contracts. Preserve diagnostic failures. Retain extra checks, recovery, compatibility, and extension points only for current requirements, callers, demonstrated failures, applicable rules, or concrete risks. Briefly explain retained exceptions when their basis is unclear.

## Continue and close with evidence

Keep implementation and integration in the current task by default. Continue ready, authorized work through verification and delivery. Validate returned work against current evidence. For durable work, promote only conclusions that change project state or another task's decisions. Advance when exit evidence and next entry criteria are met. Otherwise record the blocker or pending prerequisite, its owner, and the next action.

- **Level 0:** Close when the requested result and its proportionate verification are complete.
- **Level 1:** Also confirm the delivery boundary and reconcile the task record with current evidence.
- **Level 2:** Also reconcile the roadmap and complete any dependent handoff required for continuation.
- **Level 3:** Also pass the required audit and high-risk gates. An audit does not substitute for required code review or runtime evidence.

Verify the exact delivered subject. Keep failed checks, missing or mismatched evidence, and pending human judgments distinct. Link native results and bind evidence to a revision, environment, or time when it affects the verdict. Installation and deployment require their own evidence. Use `report-acceptance` when available for a requested standalone acceptance report.

Reuse sufficient checks. Widen or repeat them for changes, failures, or unresolved concerns. Check that the final diff preserves required safeguards and removes unsupported complexity. Require independent review when the user or a rule requires it, or when a change materially affects a public contract, security or sensitive data, an irreversible production effect, or critical fail-closed behavior. Coordination level, file count, and duration alone do not trigger review.

## Store durable records

For authorized local persistence use `$(git rev-parse --git-common-dir)/agent/` in Git repositories or an existing authorized location accessible to the next context. Use the project's own host for authorized shared records. Keep process records out of version control by default unless the user explicitly requests tracking them. Preserve existing formats and update enduring documentation with related work. Do not commit merely to checkpoint progress or test attempts.
