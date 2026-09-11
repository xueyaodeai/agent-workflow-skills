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

## Align only unresolved choices

Apply the planning procedure in [SKILL.md](../SKILL.md#plan) to the carryover inventory and new requirements. This transition adds disposition and provenance, not another requirements interview. Record material decisions in the authorized alignment notes, or return proposed entries in chat for read-only work. Preserve the distinction between verified facts, policy constraints, user decisions, and agent proposals; a superseding decision must reference the prior record rather than erase it. Do not manufacture discussion rounds when the necessary decisions are already current.

## Gate roadmap generation

Generate a reconciled successor roadmap when the level-appropriate planning contract is established and every carryover item has an authorized disposition. Reconciliation below must preserve that mapping, including outstanding obligations and explicit blockers.

If alignment is incomplete, produce a provisional roadmap within the authorized planning scope; the user need not separately request a draft. Label it `draft_unreviewed`, identify unresolved decisions and dependent work, and do not treat it as an execution ledger. Keep alignment notes `alignment_in_progress`. Return the draft in chat for read-only planning; write it only when durable output is authorized.

## Materialize and reconcile

Generate the roadmap from the reconciled records: authorized durable notes or decisions explicitly listed in the current chat. A standalone roadmap must include the necessary decisions or link accessible records; do not make its interpretation depend on hidden chat history. Include:

- predecessor roadmap and alignment provenance;
- carryover mapping to milestones, deferrals, drops, or external owners;
- the planning contract in the existing roadmap format, with the first milestone and task identified.

Compare the roadmap back to the alignment records. Confirm that no agreed item disappeared, no proposal became a decision, no dropped work reappeared, and no milestone claims nonexistent evidence. Mark the notes `aligned` and record the successor path only after reconciliation passes.

Later scope changes create a new dated record and explicit roadmap decision update. Do not rewrite planning history to make it appear linear.
