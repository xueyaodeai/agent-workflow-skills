# Project Roadmap: <project name>

## Outcome and ownership

- Final observable outcome: <result the project must produce>
- Coordinating task/owner: <single roadmap writer>
- Roadmap update authority: <owner>
- Last reconciled: <date/time and evidence scope>

## Completion criteria

- [ ] <required outcome reference, observable pass condition, verification method, and evidence to obtain>
- [ ] <overall flow or deliverable passes at the authorized delivery boundary; define its check and required evidence>

## Requirements and coverage

| Requirement | Required behavior | Source | Owning milestone/task | Final acceptance criterion |
|---|---|---|---|---|
| R1 | <scenario and observable result> | <user request or authoritative constraint> | <M1/task path> | <completion criterion reference> |

Keep implementation assumptions separate from requirements. Record consequential unresolved choices under Blockers and required decisions, including the dependent work they block. Planned evidence is not an observed pass.

## Constraints and non-goals

- Constraint: <hard boundary>
- Non-goal: <explicitly excluded work>
- Side-effect boundary: <write, publication, deployment, or external authority>

## Current milestone

- Milestone: <link to the active milestone below; state and criteria live there>
- Current/next action: <one resumable statement>

## Milestones

Keep one record per milestone. Reference its criteria from task plans and audits rather than restating them. For later milestones, retain only outcome, requirements, necessary inputs, exit checks, and the trigger for detailing the remaining contract.

### M1: <name>

- Requirements: <R1 or other requirement references>
- Owner/task plan: <owner and path>
- Entry conditions/depends on: <necessary input or no prerequisite>
- Status: `not_started | in_progress | ready_for_verification | blocked | complete | deferred | cancelled | superseded`
- Required happy path: <smallest end-to-end flow this milestone must prove>
- Exit criteria: <observable pass conditions, verification method, and evidence to obtain>
- Current non-goals and accepted deferrals: <excluded work, authority, and reconsideration trigger>
- Blocker threshold: <what may stop this milestone>
- Stop condition: <evidence after which implementation must stop expanding>
- Last observed: <date/time>
- Exit evidence: <observed result and evidence-index reference; pending until checked>

## Workstreams and dependencies

Include only when independently owned workstreams have cross-task dependencies not already represented by milestones or task plans. Otherwise omit this section; reference existing records instead of duplicating their state.

| Workstream | Owner/task plan | Depends on | Produces | Status |
|---|---|---|---|---|
| <name> | <owner/path> | <input> | <output> | not_started |

## Decisions

| ID/date | Decision | Authority | Reason/evidence | Affected work |
|---|---|---|---|---|
| <D1/date> | <decision> | <user/policy owner> | <reason> | <scope> |

## Blockers and required decisions

| Blocker | Impact | Owner and smallest required action | Status |
|---|---|---|---|
| <blocker> | <impact> | <owner/action> | <open/resolved> |

## Evidence index

| Subject/version | Evidence | Observed at | Result | Location |
|---|---|---|---|---|
| <artifact/revision/environment> | <test/review/source> | <date/time> | <result> | <path/link> |

## Recent material updates

- <date>: <owner, state-changing update, and evidence>

## Project closeout

- Final status: `complete | blocked | deferred | cancelled | superseded`
- Completion evidence: <subject and location>
- Residual risks: <none or explicit list with owner>
- Deferred follow-ups: <owner and reconsideration trigger>
- Final reconciliation: <task plans and roadmap agreement>
