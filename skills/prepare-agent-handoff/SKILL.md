---
name: prepare-agent-handoff
description: Prepare a self-contained, evidence-backed execution contract when work must cross a context boundary to another Codex task, agent, session, recurring schedule or automation, external model, or evaluation case. Use when the user asks to hand off, delegate, operationalize, schedule, or package current work for reuse. Inspect discoverable context before asking, ask only for consequential user-only decisions, distinguish facts, decisions, proposals, and assumptions, and produce the smallest destination-specific contract. Do not use as a prerequisite for ordinary work that can be executed in the current task.
---

# Prepare an Agent Handoff

Turn current working context into a reliable boundary artifact. A handoff is not a substitute for doing work in the current task; create one only when another execution context needs to continue without relying on hidden chat history.

## Operating principles

1. Inspect before asking. Read supplied material, applicable project files, current evidence, and relevant live state when read access is authorized.
2. Ask only for consequential information that cannot be discovered safely. Do not require the user to restate facts already available.
3. Prefer outcome, authority, evidence, and completion criteria over a long procedure.
4. Separate verified facts, user-confirmed decisions, agent proposals, delegated assumptions, and unresolved questions.
5. Follow applicable user- and repository-level Authority rules. A handoff records only destination-specific narrowing; it never expands authority.
6. Exclude secrets, irrelevant conversation, stale implementation detail, and unsupported claims.
7. Make drift visible. Include the evidence timestamp, revision, branch, identifier, or recheck instruction when later execution could see different state.

## Workflow

### 1. Confirm the boundary

Identify the destination from the request and context:

- another Codex task, agent, session, worktree, or environment;
- a recurring schedule or automation;
- an external model or copyable prompt;
- an evaluation or benchmark case.

If no context boundary exists and the work is authorized in the current task, perform the work instead of manufacturing a handoff.

### 2. Reconstruct the execution state

Gather the smallest runnable core: desired outcome, authoritative inputs/current state, remaining work, consequential scope or authority limits, deliverables, and observable completion evidence. Add rationale, decisions, non-goals, dependencies, validation detail, retry/fallback, or stop behavior only when they can change destination execution.

For a long-running project, use the project's roadmap, task plan, alignment notes, audits, and live repository state as the source of truth. Reference durable paths instead of copying large histories.

### 3. Resolve only real blockers

Ask one concise group of questions only when an answer would materially change the destination's scope, authority, selected data, conclusion, deliverable, or acceptance decision. Otherwise:

- discover the fact with a safe read;
- preserve it as unresolved when the destination can resolve it;
- record a low-risk assumption only when the user delegated the choice.

Never silently invent permissions, facts, business rules, source priority, metric definitions, credentials, dates, or acceptance thresholds.

### 4. Select the contract type

Read [references/contract-templates.md](references/contract-templates.md) and use only the relevant template:

- **execution handoff** for another task, agent, session, worktree, or environment;
- **schedule contract** for recurring or event-driven automation;
- **external prompt** for another model or system;
- **evaluation case** for reproducible behavior testing.

If the target is explicitly GPT-5.6, also read [references/gpt-5-6-guidance.md](references/gpt-5-6-guidance.md). Do not load model-specific guidance otherwise.

### 5. Materialize the handoff

Default to returning one compact contract in chat. Write or update a durable file only when the user requested it, an established project workflow requires it, or another authorized task needs a stable path. Preserve repository conventions and link to existing evidence rather than creating a second source of truth.

Keep the first action concrete so the destination can orient itself before making changes. Include exact paths, identifiers, and revisions when they are known and useful.

### 6. Run the completion gate

Before returning any contract, verify only the universal gate:

- destination, intended outcome, and first action are explicit;
- the contract is runnable without hidden chat context and names authoritative sources or required rechecks;
- facts, decisions, assumptions, proposals, and unresolved items are distinguishable where they coexist;
- consequential scope/authority limits and observable completion evidence are explicit;
- no secret, unnecessary personal information, or behavior-neutral prompt boilerplate is included.

Then apply only the matching template-specific gate in `references/contract-templates.md`; do not apply schedule, external-prompt, or evaluation requirements to other contract types.

If a consequential user-only decision is still missing, return the smallest blocking question instead of an apparently complete contract.

## Output rules

- Lead with the contract, not an explanation of how it was assembled.
- Use the destination's language and terminology.
- Omit empty and irrelevant sections.
- Keep source-backed facts separate from instructions.
- Label unresolved items and identify who can resolve them.
- Do not execute the handed-off work unless the user separately authorized execution in the current task.
