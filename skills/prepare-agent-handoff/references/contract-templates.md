# Handoff Contract Templates

Use the smallest matching template. Omit fields that cannot change execution and add a field only when the destination needs it.

## Execution handoff

```text
Destination: <task, agent, session, worktree, or environment>

Objective:
<user-visible outcome>

Why now:
<dependency or reason for the handoff, when useful>

Sources of truth:
- <durable path, revision, identifier, evidence, and recheck instruction>

Current state:
- Verified facts: <facts and evidence>
- Completed: <work already delivered>
- Remaining: <work the destination owns>

Decisions:
- Confirmed: <user-confirmed or authoritative decisions>
- Proposals: <unapproved recommendations, if any>
- Assumptions: <explicitly delegated assumptions, if any>
- Unresolved: <question, owner, and impact>

Scope and authority:
- In scope: <allowed work>
- Non-goals: <excluded work>
- Allowed side effects: <read, edit, commit, message, publish, deploy, etc.>
- Approval boundaries: <actions requiring the user>

Deliverables and completion evidence:
- <artifact or outcome> — <observable acceptance evidence>

Validation and stop rules:
- <checks, fallback, escalation, and stopping behavior>

First action:
<one concrete orientation or execution step>
```

Gate only what the next execution context needs to resume: current state, remaining ownership, consequential authority limits, observable completion, and first action.

## Schedule contract

```text
Job: <stable name>
Outcome: <what each run achieves>

Trigger:
- Cadence or event: <schedule or event>
- Timezone: <IANA timezone>
- Lookback/window: <included period and boundary behavior>

Inputs and sources of truth:
- <system, query, file, project state, or API>

Run procedure:
1. <read and orient>
2. <bounded processing>
3. <validation>
4. <delivery>

State and idempotency:
- <deduplication key, checkpoint, replay behavior, and concurrency rule>

Output and delivery:
- <artifact/message destination, format, recipients, and no-op behavior>

Failure behavior:
- <retry limit, partial-failure handling, escalation, and stop condition>

Authority:
- <allowed writes and actions requiring approval>
```

Schedule gate: confirm trigger, timezone when time-based, window boundaries, idempotency/concurrency, no-op delivery, and failure/retry behavior. Do not invent a cron expression when the platform accepts a human-readable schedule. Confirm business-day semantics only when they change execution.

## External prompt

```text
Goal: <outcome>

Success criteria:
- <observable completion conditions>

Context and evidence:
- <inputs, authoritative sources, and missing-evidence behavior>

Constraints and authority:
- <scope, non-goals, permissions, safety, privacy, time, and resource limits>

Tools and routing:
- <available tools, prerequisites, exclusions, and fallbacks>

Workflow:
- <only order-dependent or fragile steps>

Validation:
- <checks and acceptance evidence>

Output:
- <audience, language, format, and required content>

Stop rules:
- <clarify, retry, abstain, escalate, or finish conditions>
```

Add role or personality only when it materially changes judgment or user-facing behavior.

External-prompt gate: keep authoritative context, tool limits, observable success, output, and stop behavior; omit role, workflow, or formatting detail that does not change behavior.

## Evaluation case

```text
Behavior under test: <capability or decision rule>
Task input: <self-contained user input or artifact reference>
Allowed context and tools: <what the subject may use>
Forbidden context: <information that would leak the intended answer>

Expected behavior:
- <observable requirements>

Grading:
- Pass: <evidence-backed criteria>
- Inconclusive: <missing evidence or invalid setup>
- Fail: <violated requirements>

Reproducibility:
- <model/configuration, revision, fixtures, and environment facts>
```

Keep the case independent of the diagnosis being tested. Do not embed the suspected defect, intended fix, or hidden ground truth unless the evaluation explicitly measures their use.

Evaluation gate: verify allowed/forbidden context, observable grading, inconclusive behavior, and reproducibility identity; schedule and delivery fields do not apply.
