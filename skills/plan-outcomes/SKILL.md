---
name: plan-outcomes
description: Define requirements, phased work, and verifiable completion criteria for a task or roadmap. Use when creating or revising implementation plans, splitting milestones, clarifying goals and scope, or sharpening vague acceptance criteria. Do not trigger for routine execution status updates.
---

# Plan Outcomes and Acceptance

Turn goals into executable, verifiable plans. Every required outcome needs a source, owning work, and a pass condition. Each stage must identify what it delivers, and final acceptance must prove the overall objective.

Use the user's language for plans, questions, and explanations, regardless of this skill's language.

## Choose the output boundary

- A single task may need only a short plan. Split stages only for independent outcomes, real dependencies, or delivery boundaries, not a fixed stage count or technical layers.
- For a multi-stage roadmap, define the final result first, then work backward to stage outcomes and tasks. Make near-term tasks executable; keep distant work at the level of outcomes, dependencies, acceptance conditions, and a trigger for further detail.
- Fill gaps in the existing plan and maintain one authoritative record. Return the plan in chat when durable files were not requested. Requests for planning only or no changes remain strictly read-only. Planning does not authorize implementation, commits, external task creation, or publication.
- When used with `orchestrate-projects`, this skill owns requirements and acceptance content; that skill owns persistence, state, and coordination. Put the content in its existing task plan or roadmap rather than creating another ledger. This skill also works independently and requires no other skill.

## 1. Establish the goal and its basis

Read the user's requirements, existing plans, and decision-relevant code, documentation, or runtime evidence. Inspect only facts that can change scope, behavior, dependencies, or acceptance.

Distinguish the following instead of treating them all as commitments:

- **Requirements:** who needs which observable result in what scenario; cite the user request or authoritative constraint.
- **Current state:** verified behavior and gaps. Existing code establishes current behavior, not automatically the target behavior.
- **Open decisions:** answers that would change requirements, boundaries, or acceptance and cannot be obtained from existing evidence.
- **Implementation assumptions:** replaceable technical choices or low-risk defaults; state the rationale and when to recheck. Architecture inherited from a plan is not inherently a requirement.

State the beneficiary, target result, scope, and explicit exclusions. Unsupported performance numbers, dates, priorities, or launch requirements are proposals, not confirmed criteria.

## 2. Clarify consequential questions in dependency order

Discover accessible facts before asking for user decisions. Prioritize questions that change downstream branches; defer questions that depend on unsettled answers. Ask only the few questions needed to advance the current decision, explaining their impact and recommended choices.

Continue independent planning while waiting. Leave consequential scope, interface, data, cost, or external-effect decisions open rather than deciding for the user. Low-risk, reversible implementation choices may be provisional with a rationale. Do not keep interviewing to exhaust imagined branches or impose a universal reconfirmation gate.

Give concrete meanings and counterexamples for ambiguous terms that affect acceptance, such as "complete," "account," or "sync succeeded." When entities, relationships, or states matter, use the shortest business flow that explains who acts, how state changes, and which conditions must always hold. Model only concepts that change requirements or acceptance; do not require glossary or ADR files.

Check understanding against concrete scenarios: the happy path and important failure or boundary cases justified by requirements or existing risks. Surface conflicts between terminology, documentation, code, and the user's goal, distinguishing current behavior from intended behavior.

## 3. Work backward from final acceptance to stage tasks

Define pass conditions for each required outcome before deciding what work will establish them. Use stable references such as R1, A1, M1, and T1 for multiple requirements or stages; direct correspondence is sufficient for a simple task.

Each acceptance criterion includes:

- the scenario or preconditions and triggering action;
- the observable expected result, including prohibited outcomes when necessary;
- the verification method, specific pass condition, and expected evidence;
- the associated requirement; add environment, version, data scope, or acceptance owner only when it changes the conclusion.

"Implement the API," "tests pass," or "good user experience" alone do not prove a requirement. Specify the required API behavior, what the tests establish, or a manual check with a decidable result. Reuse suitable existing coverage; not every check needs automation. During planning, record **checks to perform and evidence to obtain**, never fictional passing results. If verification is unavailable, state the evidence gap, its impact, and how to close it.

For each stage, state its independently observable result, associated requirements, necessary inputs, exit criteria, and evidence. Then identify the necessary tasks, each with an action, deliverable, dependencies, and acceptance references. Assign owners only for multiple people or cross-task execution. A stage may serve several requirements and a requirement may span stages, but identify where each requirement receives final acceptance.

Final acceptance checks the complete user flow or overall deliverable and the agreed delivery boundary. Passing stages separately does not automatically prove the whole result. Publication, deployment, or an observation period is required only within the authorized scope. An exploration stage delivers an answer to a specific uncertainty and evidence for a decision; do not precommit to an implementation whose feasibility is unproven.

## 4. Check the plan for completeness

Inspect the following and repair gaps in the current plan:

- Does every required outcome have owning work and a final pass condition? Does every task serve a requirement, necessary verification, or an established constraint?
- Do stage inputs and outputs connect without circular dependencies or tasks that cannot start?
- Have implementation preferences, suggested thresholds, open decisions, or future ideas been mistaken for requirements?
- Is it clear when individual stages and the overall result are complete, and how to proceed while evidence is still missing?
- Are non-goals, deferrals, and unmet requirements distinct? Removing or deferring required work needs the corresponding scope authority; do not downgrade it merely to close the project.

When requirements change, update affected tasks, stage exit criteria, and final acceptance together. Identify invalidated evidence without automatically reopening every stage.

Planning is complete when requirements have a basis, work and acceptance are traceable, dependencies are executable, and consequential open decisions are resolved or explicitly block their dependent portions. A plan may retain blocked branches, but must not describe them as ready to execute. Completing a plan does not mean implementation or acceptance is complete.

Use [assets/outcome-plan.md](assets/outcome-plan.md) when drafting a plan with multiple requirements or stages. Fill gaps in existing formats; cover the same information in a few lines for simple tasks.

## Sources

Inspired by dependency-ordered questions in [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) and terminology and scenario clarification in [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md). This version centers requirements, stage deliverables, and acceptance without adopting exhaustive interviews or automatic domain-document writes.
