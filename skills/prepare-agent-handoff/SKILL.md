---
name: prepare-agent-handoff
description: Prepare the smallest runnable context-delta contract when work must continue across an agent task, session, worktree, environment, recurring automation, external model, or evaluation. Use for handoff, delegation, operationalization, scheduling, or reusable prompt and evaluation packaging when the destination cannot reliably continue from the context it already receives. Do not use as a prerequisite for work that can be completed in the current task.
---

# Prepare an Agent Handoff

Package only the context a destination lacks. A handoff is self-contained when the destination can act from inherited context or named accessible sources without hidden chat history; it need not copy the history itself.

## Minimum contract

Include a detail only when removing it could change the destination's action, source selection, authority, or completion decision.

For a cold execution context, include this semantic core. References may replace repeated content only when the destination can access them:

```text
Why: <problem or preference, beneficiary, expected value, and basis>
Outcome: <required result>
Paths: <shortest complete path; best path under current constraints; chosen path and reason; they may be identical>
Resume from: <authoritative source, revision or recheck, and necessary current state>
Remaining work: <work the destination owns>
Bounds: <consequential scope or authority limits>
Done when: <full acceptance scenarios, pass conditions, verification method, evidence, and delivery boundary>
```

Before handing off implementation, confirm why, what, shortest/best paths and selection, and complete acceptance. Direct assignments follow the same readiness check. Both paths must meet the same criteria. Missing consequential decisions block dependent implementation; never defer them to an implementation agent just to launch it. A separately authorized clarification task may instead resolve a bounded uncertainty using its own ready contract. Reuse settled answers without repeated approval and do not invent answers. Unrelated ready, authorized work may continue.

Treat the destination as routing metadata. Include it only when the artifact may be reused or misrouted.

## Workflow

### 1. Size the context gap

If no execution boundary exists and the work is authorized here, perform the work instead of manufacturing a handoff.

When the destination already inherits sufficient context, send only a task delta:

```text
Task: <bounded objective>
Return: <deliverable>
Bounds: <only consequential limits>
```

Add any missing core field only when inherited context does not already make it reliable.

For a recurring schedule, external prompt, or evaluation case, read only the matching section of [references/contract-templates.md](references/contract-templates.md) and add its specialized fields to the core.

### 2. Inspect and extract

Read supplied material, applicable project files, current evidence, and authorized live state before asking the user to restate anything. For long-running work, cite durable plans, audits, repository paths, revisions, identifiers, or recheck instructions instead of copying history.

Add completed work, decisions, non-goals, dependencies, a first action, validation detail, retry or stop behavior only when they can change execution. When facts, decisions, proposals, assumptions, or unresolved items coexist, label only the distinctions that matter.

Ask one concise group of questions only when an undiscoverable user-only answer would materially change purpose, scope, path selection, authority, selected data, deliverable, or acceptance. Otherwise:

- discover the fact with a safe read;
- preserve it as a blocker and assign only a bounded clarification task when authorized;
- record a low-risk assumption only when the user delegated the choice.

Never silently invent permissions, facts, business rules, source priority, metric definitions, credentials, dates, or acceptance thresholds.

### 3. Emit and check

Default to returning one compact contract in chat. Write or update a durable file only when the user requested it, an established project workflow requires it, or another authorized task needs a stable path. Preserve repository conventions and link to existing evidence rather than creating a second source of truth.

Before returning it, verify that:

- the destination can recover all four readiness points using inherited context or named accessible sources; inaccessible references are gaps, not inherited answers;
- drift-prone state has a revision, identifier, timestamp, or recheck instruction;
- the contract narrows or preserves applicable authority and never expands it;
- completion is observable;
- no secret, unnecessary personal information, stale detail, unsupported claim, or behavior-neutral boilerplate remains.

Lead with the contract, use the destination's language, and omit empty sections. If a consequential user-only decision is still missing, return the smallest blocking question. Do not execute the handed-off work unless the user separately authorized it here.
