# Specialized Contract Add-ons

Load only the matching section. Add a field to the core contract in `SKILL.md` only when it can change execution.

## Recurring schedule

Add only the relevant fields:

- **Trigger:** cadence or event; add timezone and window boundaries when time affects inclusion.
- **State:** deduplication key, checkpoint, replay, or concurrency behavior when reruns or overlap can duplicate effects.
- **Delivery:** destination, format, recipients, and no-op behavior.
- **Failure:** retry limit, partial-failure handling, escalation, and stop condition when failure is realistic.
- **Procedure:** only order-dependent or fragile steps.

Gate trigger semantics, idempotency when effects can repeat, delivery, failure behavior, and write authority. Do not invent a cron expression when the platform accepts a human-readable schedule.

## External prompt

Add only the relevant fields:

- **Tools and routing:** available tools, prerequisites, exclusions, and fallbacks.
- **Output:** audience, language, format, and required content.
- **Workflow:** only order-dependent or fragile steps.
- **Stop behavior:** clarify, retry, abstain, escalate, or finish conditions when failure or missing evidence is realistic.
- **Role or personality:** only when it changes judgment or user-facing behavior.

Gate authoritative context, tool limits, observable success, output, and realistic stop behavior. Omit prompt formatting that does not change behavior.

When writing the prompt itself, keep the destination contract model-independent and apply these rules only where they change execution:

- State the outcome and observable completion criteria more precisely than the procedure.
- Name authoritative context, available tools, validation, and stopping behavior.
- Preserve user autonomy and approval boundaries for external writes or consequential actions.
- Prefer compact decision rules over duplicated examples and broad absolute language.
- Include workflow order only for dependencies, handoffs, fragile operations, or safety boundaries.
- Separate source-backed facts from creative or inferred content.
- Define retry, fallback, clarification, and abstention behavior when failures or missing evidence are realistic.

Specify reasoning effort only when configuring an API or evaluation and evidence justifies changing the existing baseline. Do not add model-specific headings or boilerplate merely to make a prompt look comprehensive.

## Evaluation case

Add the fields needed to isolate and grade behavior:

- **Task input:** self-contained input or artifact reference.
- **Allowed context and tools:** what the subject may use.
- **Forbidden context:** information that would leak the intended answer.
- **Expected behavior:** observable requirements.
- **Grading:** evidence-backed pass, inconclusive, and fail conditions.
- **Reproducibility:** model or configuration, revision, fixtures, and environment facts that affect results.

Keep the case independent of the diagnosis being tested. Do not embed the suspected defect, intended fix, or hidden ground truth unless the evaluation explicitly measures their use. Gate context isolation, observable grading, inconclusive behavior, and reproducibility identity.
