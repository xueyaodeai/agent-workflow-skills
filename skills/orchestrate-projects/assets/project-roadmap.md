# Project Roadmap: <project name>

<!-- Write content in the user's language; retain supported field labels for
validation. Remove guidance and unused optional sections before delivery. Lead
with the outcome and current decision; keep detailed execution in task plans. -->

## Outcome and ownership

- Why: <problem or preference, who benefits, expected value, and requirement source>
- Final observable outcome: <what the user can do or receive when the project is complete>

## Current milestone

- Milestone: <link to the active milestone below; its status and contract live there>
- Current result and gap: <brief coordination conclusion: what exists and what is still missing; link to owning detail>
- Current/next action: <one resumable action or smallest required decision, with owner when needed>
- Side-effect boundary: <authorized delivery boundary, such as local commit, merge, deployment, or live acceptance>
- Readiness: `ready | not_ready`
- Readiness blockers: <root decision gaps and dependent work; omit when ready>

## Completion criteria

- [ ] <A1: required outcome, scenario/action, observable pass condition, verification method, and evidence to obtain>
- [ ] <A2: overall flow or deliverable at the authorized delivery boundary, its pass condition, and required evidence>

## Milestones

<!-- Order milestones by delivery and dependency; name each by its observable
outcome. Keep one current contract per milestone; task plans/audits reference it.
For later milestones retain outcome/requirements, necessary inputs, exit checks,
and a named refinement trigger with Readiness: not_ready; omit other detail until
needed. Ready milestones use the full contract below, with accessible inheritance.
Root readiness does not make every milestone ready. -->

### M1: <observable outcome>

- Required happy path: <who does what, and the observable result this milestone must prove>
- Requirements: <R1 or other requirement references>
- Owner/task plan: <owner and link to the current execution plan>
- Status: `not_started | in_progress | ready_for_verification | blocked | complete | deferred | cancelled | superseded`
- Entry conditions/depends on: <required upstream output or no prerequisite>
- Exit criteria: <scenario/action, observable pass condition, verification method, and evidence to obtain; reference project acceptance where useful>
- Why: <specific contribution to the project outcome; reference shared rationale>
- Shortest path: <complete route including verification and delivery, or explicit inheritance>
- Best path: <same route and reason, or a better-supported alternative under current constraints>
- Selected path: <chosen route reference, reason, and consequential tradeoff, if any>
- Readiness: `ready | not_ready`
- Readiness blockers: <decision gap or refinement trigger; omit when ready>
- Current non-goals and accepted deferrals: <excluded work, scope authority, and reconsideration trigger>
- Blocker threshold: <condition that stops this milestone>
- Stop condition: <evidence after which implementation must stop expanding>

<!-- Add observations when available. Completion requires a pass and evidence.
Keep detailed attempts in the task plan or original artifacts. -->

- Last observed: <date/time when facts can drift>
- Exit result: `pass | fail | blocked | pending`
- Exit evidence: <conclusion and versioned evidence link; pending until checked>

## Approach

<!-- When paths coincide, describe the route once and use short references in
other fields. Milestones inherit this approach and explain only their differences. -->

- Shortest path: <fastest complete route through the milestones, including verification and delivery>
- Best path: <same route and reason, or the best-supported time/cost/risk/lifecycle alternative>
- Selected path: <chosen route reference and reason>

## Requirements and coverage

<!-- Omit this table if milestone/completion references already give clear coverage. -->

| Requirement | Required behavior | Source | Owning milestone/task | Final acceptance criterion |
|---|---|---|---|---|
| R1 | <scenario and observable result> | <user request or authoritative constraint> | <M1/task path> | <A1> |

## Constraints and non-goals

- In scope: <authorized behaviors and deliverables>
- Constraint: <consequential hard boundary; reference shared rules instead of copying them>
- Non-goal: <explicitly excluded work, distinct from required work still unfinished>

## Workstreams and dependencies

<!-- Include only cross-task dependencies not already represented by milestones
or task plans. Omit otherwise; do not duplicate their state here. -->

| Workstream | Owner/task plan | Depends on | Produces | Status |
|---|---|---|---|---|
| <name> | <owner/path> | <input> | <output> | not_started |

## Blockers and required decisions

| Blocker | Impact | Owner and smallest required action | Status |
|---|---|---|---|
| <blocker> | <dependent work affected> | <owner/action> | <open/resolved> |

## Decisions

<!-- Keep effective decisions here. Update affected current contracts when a
choice changes; preserve the superseded decision in History or a fixed revision. -->

| ID/date | Decision | Authority | Reason/evidence | Affected work |
|---|---|---|---|---|
| <D1/date> | <current decision> | <user/policy owner> | <reason> | <scope> |

## Evidence index

<!-- Include evidence for project-level conclusions; link to task plans and
original artifacts for detailed measurements and individual attempts. -->

| Subject/version | Evidence | Observed at | Result | Location |
|---|---|---|---|---|
| <artifact/revision/environment> | <test/review/source> | <date/time> | <result> | <path/link> |

## Maintenance

- Coordinating task/owner: <single roadmap writer>
- Roadmap update authority: <owner>
- Last reconciled: <date/time and evidence scope>

## History

<!-- Omit when unused. Preserve material changes and original results with links,
not an activity log. Do not reuse current state/contract field labels. -->

- <date>: <earlier decision/result, what superseded it, and historical evidence or fixed revision/path>

## Project closeout

<!-- Omit until a closeout decision exists. -->

- Final status: `complete | blocked | deferred | cancelled | superseded`
- Completion result: `pass | fail | blocked | pending`
- Completion evidence: <subject and location>
- Residual risks: <none or material gap with owner>
- Deferred follow-ups: <authorized deferral, owner, and reconsideration trigger>
- Final reconciliation: <task plans and roadmap agree on the outcome and remaining work>
