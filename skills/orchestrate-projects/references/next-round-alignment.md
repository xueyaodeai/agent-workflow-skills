# Next-Round Roadmap Alignment

Read this reference when the user asks what should follow the current roadmap, requests a successor roadmap, or starts aligning future milestones before the current round closes.

Use `assets/roadmap-alignment-notes.md` as the temporary decision ledger and append `assets/project-roadmap-transition-addon.md` to the successor roadmap. Write durable notes only when the user requested them or an established authorized project workflow requires them. For read-only planning, return the same structure in chat without changing files.

## Build the carryover inventory

Inspect the current roadmap, task plans, milestone audits, live repository or deployment state, open reviews, and in-scope external trackers. Recheck drift-prone facts.

Classify every residual item:

- `must_continue`: required to finish or safely close an existing commitment;
- `candidate`: useful future work that still needs prioritization;
- `defer`: intentionally postponed with an owner, reason, or reconsideration trigger;
- `drop`: rejected, superseded, or no longer needed;
- `external_dependency`: owned elsewhere but able to constrain the next round.

Record source, verified state, observation time, reason it remains, proposed disposition, evidence, and whether an authorized decision is required. Keep unverified claims visibly unverified. Do not convert a deferred idea into a committed milestone silently.

## Separate facts, authority, and proposals

Keep these record types distinct:

- `verified_fact`: supported by a named source, version, and observation time; it informs but does not authorize a choice.
- `policy_constraint`: imposed by a named policy or authority owner.
- `user_decision`: explicitly decided by the user or delegated decision owner.
- `agent_proposal`: a recommendation that remains unapproved.

Evidence is never a decision authority. When a later decision changes an earlier one, preserve the prior record and add an explicit superseding record.

## Align only unresolved choices

Start from the carryover inventory, then discuss only what cannot be derived safely: desired outcome, new capabilities, removals, constraints, non-goals, sequencing, delivery boundaries, and acceptance evidence.

Discuss one coherent decision set at a time. After each material exchange:

- append a dated round to the authorized notes file; or
- for read-only work, return a proposed round entry in chat.

Each round records evidence reviewed, confirmed decisions, remaining proposals, rejected or deferred options, open questions, and the next focus. Do not manufacture extra discussion rounds when all required decisions are already durable and current.

## Gate roadmap generation

Consolidate carryover into the fewest milestones that preserve independently observable outcomes, hard dependencies, distinct authority or side-effect boundaries, or contexts that must resume independently. Do not create milestones per subsystem, implementation phase, failure code, or test category unless one of those boundaries requires it.

Generate a reconciled successor roadmap only when:

- every carryover item has a disposition;
- the next outcome and measurable completion criteria are understood;
- constraints, non-goals, removals, and compatibility boundaries are recorded;
- milestone order, dependencies, and evidence requirements are coherent;
- consequential decisions are resolved or explicitly accepted as blockers;
- facts, constraints, confirmed decisions, and proposals remain distinguishable.

If alignment is incomplete, keep durable notes in `alignment_in_progress` or return the missing decisions in chat. Create a provisional roadmap only when the user explicitly requests a draft, and label it `draft_unreviewed`; never use it as the execution ledger.

## Materialize and reconcile

Generate the roadmap from consolidated durable records, not hidden chat context. Include:

- predecessor roadmap and alignment provenance;
- carryover mapping to milestones, deferrals, drops, or external owners;
- final outcome, boundaries, milestones, exit evidence, dependencies, risks, and blockers;
- first-milestone entry criteria and recommended first task.

Compare the roadmap back to the alignment records. Confirm that no agreed item disappeared, no proposal became a decision, no dropped work reappeared, and no milestone claims nonexistent evidence. Mark the notes `aligned` and record the successor path only after reconciliation passes.

Later scope changes create a new dated record and explicit roadmap decision update. Do not rewrite planning history to make it appear linear.
