# Optional GPT-5.6 Prompt Guidance

Source: OpenAI, [Prompting guidance for GPT-5.6 Sol](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6), checked 2026-07-16.

Read this reference only when the handoff target is explicitly GPT-5.6. The destination contract remains model-independent; apply these points only where they materially improve the external prompt or evaluation case.

- State the outcome and observable completion criteria more precisely than the procedure.
- Name authoritative context, available tools, validation, and stopping behavior.
- Preserve user autonomy and approval boundaries for external writes or consequential actions.
- Prefer compact decision rules over duplicated examples and broad absolute language.
- Include workflow order only for dependencies, handoffs, fragile operations, or safety boundaries.
- Separate source-backed facts from creative or inferred content.
- Define retry, fallback, clarification, and abstention behavior when failures or missing evidence are realistic.
- Specify reasoning effort only when configuring an API or evaluation and evidence justifies changing the existing baseline.

Do not add model-specific headings or boilerplate merely to make a prompt look comprehensive.
