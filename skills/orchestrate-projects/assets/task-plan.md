# Task Plan: <observable task outcome>

<!-- Use this core for Level 1. Write content in the user's language; retain
supported field labels for validation. Remove guidance and unused optional lines
before delivery. Inherit shared requirements/bounds by a specific accessible
parent reference and explain task differences. Add coordination or Git modules
only when their trigger applies. -->

## Objective

- Why: <problem or preference, beneficiary, value, and source; or accessible parent reference>
- Observable result: <what the user can do or receive when this task is complete>
- Requirement basis: <user request or authoritative constraint; reference shared requirements and distinguish implementation assumptions>

## Current state

- Status: `not_started | in_progress | ready_for_verification | blocked | complete | deferred | cancelled | superseded`
- Current result and gap: <what exists, what remains unverified or unfinished, and an evidence link when available>
- Current/next action: <one resumable action or smallest required decision>
- Boundary: <consequential exclusion and authorized delivery boundary>
- Readiness: `ready | not_ready`
- Readiness blockers: <missing consequential decisions and dependent work; omit when ready>
- Blocker: <only when blocked; name the condition and smallest action or owner needed>

## Acceptance

- Acceptance checks: <scenario/action, observable pass condition, verification method, and evidence to obtain; reference requirements when needed>

<!-- For multiple scenarios, put full checks in a table here and reference it
from Acceptance checks. Keep planned checks separate from observed results.
Check the overall result at the delivery boundary, not just isolated steps. -->

## Current approach

- Shortest path: <fastest route to full acceptance, including verification and delivery>
- Best path: <same route and reason, or the best-supported time/cost/risk/lifecycle alternative>
- Selected path: <chosen route reference, reason, and consequential tradeoff, if any>

<!-- When paths coincide, describe the route once and use short references in
other fields. Put exact inputs, revisions, budgets, and environment details here
when needed to execute or verify; do not expand the opening with them. -->

## Plan and progress

- [ ] <action and deliverable, required input/dependency, and acceptance check it serves>

<!-- Group steps into stages only for independent outcomes or real dependency or
delivery boundaries; name each stage's result and exit checks. Update current
steps when a decision changes so obsolete steps cannot appear executable. -->

## Scope

- In scope: <authorized work; reference shared scope and state task-specific differences>
- Deferred/non-goal: <only when needed; distinguish authorized deferral from unfinished required work>
- Blocker threshold: <only when a specific condition changes whether this task may continue>
- Stop condition: <only when acceptance checks alone do not define when to stop>

## Verification evidence

<!-- Include when checks have run. Record check, exact subject/environment,
observed result, and evidence link. Summarize meaningful outcomes; keep command
logs and repeated attempts in original artifacts. An implementation check alone
does not establish functional success, measured improvement, or deployment. -->

## History

<!-- Omit when unused. Reconcile the current approach, steps, acceptance,
readiness, and next action after a decision changes. Preserve earlier decisions
and results here or at a fixed revision/path, naming their replacement. Do not
reuse current state/contract field labels or require history to interpret the plan. -->

- <date>: <earlier decision/result, what superseded it, and historical evidence link>

## Closeout

<!-- Omit until a closeout decision exists. Reference recorded verification;
do not duplicate experiments or claim planned checks have passed. -->

- Final status: `complete | blocked | deferred | cancelled | superseded`
- Result: <observable result, location, and any material remaining gap>
- Verification result: `pass | fail | blocked | pending`
- Verification: <conclusion and link to check, subject, result, and evidence>
- Delivery boundary: <actual delivered change set, commit, artifact, or external system>
- Residual risk/next action: <only when material; owner or reconsideration trigger>
