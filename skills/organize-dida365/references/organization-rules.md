# Dida365 organization rules

## Contents

1. Project, task, and tag decision table
2. Project rules
3. Tag rules
4. Task splitting rules
5. Dates and priorities
6. Lifecycle states
7. Agent delegation lifecycle
8. Habits and recurring tasks
9. Cleanup and verification examples

## 1. Project, task, and tag decision table

| Need | Use | Test |
|---|---|---|
| A durable outcome or responsibility containing several actions | Project | Would this still be a useful container after one task finishes? |
| One checkable result owned by one person | Task | Can completion be judged without interpreting a broad theme? |
| A cross-project retrieval dimension | Tag | Will the same label usefully group tasks from at least two projects? |
| A temporary sequence under one result | Subtasks/checklist | Do the steps share one owner and one completion boundary? |
| A recurring behavior measured over time | Habit | Is success regular repetition rather than delivery of an artifact? |

Do not use a project merely because several tasks share a noun. Do not use a tag to replace ownership, lifecycle state, date, or priority.

## 2. Project rules

Create or keep a project when all of these are true:

- it represents a stable responsibility, product, initiative, or outcome;
- it normally contains multiple independent actions;
- the user benefits from reviewing it as a unit;
- it has a meaningful active-to-finished lifecycle.

Merge projects when they serve the same outcome and separation creates duplicate planning. For example, a product implementation, its website, and its independent-developer operations can be one project when the website and operations exist only to serve that product. Before merging, preserve useful sections or parent tasks that represent distinct workstreams.

Avoid projects for:

- a month such as “7月”;
- a priority such as “P0”;
- a generic method such as “AI”;
- a single small task;
- a status such as “暂停” unless the user intentionally uses one holding project as a workflow mechanism;
- a person who merely receives delegated work.

Archive a project when it has no active owned outcomes and its historical tasks remain useful. Do not archive it while active children remain unresolved. If a parent task moves to a pause project, move its children with it unless the user explicitly splits their lifecycle.

## 3. Tag rules

Use tags for stable, cross-project facets such as a testing perspective, knowledge-library work, review type, platform, or a planning horizon. A good tag answers a retrieval question such as “show all knowledge-base tasks across work projects.”

Prefer one canonical spelling and language. Treat case, punctuation, and near-synonyms as one concept unless they have documented meanings. Examples of likely duplicates include `计费agent` versus `计费-agent`, or broad chains such as `AI`, `agent`, and a more precise domain tag applied to the same work.

Avoid tags that duplicate native fields:

- `p0`, `p1`, `p2` when Dida365 priority is sufficient;
- `7月` when start/due dates or a planning filter express the period;
- `暂停`, `完成`, or `放弃` when project placement or task status expresses lifecycle;
- a project name applied to every task already inside that project;
- implementation vocabulary such as `design`, `metrics`, or `e2e` when used once and not part of an intentional taxonomy.

Before deleting a tag definition:

1. count active and historical task use where available;
2. inspect parent and child tags;
3. identify a canonical replacement when the concept is still needed;
4. retag tasks first;
5. delete only exact confirmed redundant definitions;
6. re-list tags and verify the expected count and absence set.

A zero-use tag is a candidate, not automatic proof. Retain empty taxonomy parents or deliberately reserved tags when the user confirms future use.

## 4. Task splitting rules

Write a task as a verb plus a concrete result. Prefer “完成 X 的回归测试并记录结论” over “X 测试”。

Keep one task when:

- one person owns it;
- it produces one observable result;
- its steps must move through the same lifecycle together;
- it can reasonably be completed in one focused session or a small number of sessions.

Split a task when any of these apply:

- it contains two independently valuable deliverables joined by “和/以及”；
- different people own parts of it;
- one part can finish while another is paused or abandoned;
- it spans discovery, decision, implementation, and verification as separately reviewable outcomes;
- it lasts several days without a visible next action;
- progress cannot be stated more precisely than a percentage.

Use a parent task plus subtasks when the aggregate outcome is meaningful. Use a project when the workstream will continue to receive new independent tasks. Use a checklist only for short mechanical steps that do not need their own dates, priorities, tags, or lifecycle.

For an uncertain product idea, create an analysis/continue-or-stop decision task first. Do not preload implementation tasks before the decision. For obsolete language-learning or content-selection plans, abandon the old execution tasks and create one new planning task rather than editing incompatible plans in place.

## 5. Dates and priorities

Assign a date only when it represents one of:

- an external deadline;
- a genuine commitment;
- a planned start window the user intends to protect;
- a dependency boundary;
- a recurring schedule.

Clear dates from backlog, paused work, or reading options that are not current commitments. Preserve a current book's deadline while clearing unrelated book dates. For sequential reading, encode the real sequence: finish the current book by its deadline, then start the next book on the agreed date for the agreed duration.

Use exact dates and the user's timezone. Translate phrases such as “8月初”“8月中下旬”“月底” into dates only after the user accepts the planning interpretation or when an existing convention makes the mapping unambiguous.

Use native priority:

- high: near-term deadline, blocking dependency, or explicitly critical outcome;
- medium: committed work for the current planning horizon;
- low or none: useful backlog without a current commitment.

Do not mark every H2 objective high. Priority should distinguish what receives attention first, not express general importance.

## 6. Lifecycle states

| State | Meaning | Typical evidence |
|---|---|---|
| Complete | The user's required result exists | implementation delivered, note written, decision recorded |
| Pause | The user still owns the outcome but cannot act now | capacity unavailable, waiting to align, deliberately deferred |
| Abandon | The user no longer intends or needs to deliver it | obsolete plan, task transferred to a colleague, evaluated as not worth doing |
| Archive project | No active work remains, but history should be retained | H1 project closed after all children are resolved |

“Partially complete” is not complete when the missing acceptance condition remains material. Record the completed evidence in task content and leave the remaining outcome active or split it into a new task. A result delegated to someone else should normally be abandoned from the user's owned list, not completed, unless the task was explicitly “delegate and confirm ownership.”

When the user says “挂起/暂停”, preserve the task and remove misleading urgency or dates as appropriate. When the user says “不需要了/放弃”, use abandoned status rather than deletion so the decision remains auditable.

## 7. Agent delegation lifecycle

Use the single `agent委派` tag as the delegation queue marker. An active tagged task is waiting for user selection and launch. A completed tagged task represents successful delegation only when its title or content truthfully defines the Dida365 outcome as delegation and it records a valid independent Codex task reference.

The destination Codex task owns implementation and delivery. Do not keep the Dida365 task active to mirror Agent progress or reopen it from later Agent outcomes. This delegation completion boundary does not apply to a task whose stated outcome is still the delivered fix, feature, analysis, or other work result.

The whole-system organizer may audit these lifecycle facts but must not select or start Agent work unless the user explicitly invokes the dispatch workflow and chooses the tasks.

## 8. Habits and recurring tasks

Use a habit for repeated behavioral training such as early rising, reading practice, or distinct exercise goals. Retain separate habits when they train genuinely different behaviors, even if they occur in the same domain.

Merge or remove a separate recurring task when it is only another representation of the same habit. For example, keep a “阅读20分钟” behavior and fold “听书” into it when listening is merely an allowed mode, but keep separate exercise habits when their training targets differ.

Stopping one behavior does not imply stopping its paired behavior. Apply exact intent, such as stopping “早睡” while retaining “早起”。

## 9. Cleanup and verification examples

### Project versus tag

- “自动化” can be a project when it owns a backlog and deliverables.
- “知识库” can be a tag when knowledge work appears across multiple projects.
- “H2” can be a temporary planning tag if it supports a deliberate half-year review; remove it later when the review horizon is no longer useful.

### Parent and children

If a parent task and its child tasks are all waiting for the same cross-team alignment, move the whole tree to pause. If only one child is blocked, keep the parent active and pause only that child.

### Transferred work

If another colleague now owns the problem, mark the user's task abandoned and optionally record the transfer in its content. Do not keep a dated active task that the user can no longer complete.

### Verification summary

After a cleanup, report at least:

- affected task and project counts;
- tag count before and after tag-definition cleanup;
- exact removed and retained ambiguous labels;
- unresolved items requiring future alignment;
- checks skipped because the connector does not expose historical or destructive operations.
