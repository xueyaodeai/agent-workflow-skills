# Initiative Integration Branch

Read this reference only after choosing initiative integration as the delivery topology. Coordination level and delivery topology are independent: a Level 3 audit does not automatically require an integration branch.

## Enable only when justified

Use a temporary initiative integration branch only when one or more conditions materially apply:

- dependent milestones need a shared pre-primary baseline;
- intermediate states are not independently safe or reviewable for the primary branch;
- combined integration validation is required before formal primary-branch review;
- repeated primary-branch review creates demonstrated coordination cost.

Prefer the repository's normal feature-to-primary workflow when milestones remain independently releasable, reversible, and compatible with repository policy. Record the decision, evidence, expected benefit, owner, and retirement condition in the roadmap.

Append `assets/task-plan-git-addon.md` and `assets/task-plan-integration-addon.md` to applicable task plans. Use `assets/promotion-gate.md` for primary-branch promotion.

## Bootstrap and protect the branch

- Discover the repository's primary branch and naming conventions; otherwise use `integration/<initiative>`.
- Create the integration branch from a verified primary-branch revision and record that baseline.
- Make it initiative-scoped, temporary, and owned by the coordinating task.
- Accept implementation only through reviewed feature or fix branches; do not patch the shared integration branch directly.
- Preserve formal review, CI, human approval, and repository protection. Internal review never waives them.
- Determine whether the platform supports feature-to-integration review requests. If not, retain equivalent review evidence in the project artifacts.

Creating, pushing, reviewing, merging, deleting, or rewriting a branch are distinct actions. Perform only those authorized by the user and repository policy.

## Gate each feature or milestone

Use this low-freedom sequence:

1. Create a dedicated feature branch and worktree from the recorded integration baseline.
2. Complete the task-scoped change, verification, and selected Git delivery contract without unrelated work.
3. Synchronize the latest integration branch before final review and rerun affected checks.
4. Review the exact `integration...feature` diff using the single fresh read-only reviewer subagent described in [independent-review.md](independent-review.md). Complete any separately required human review or repository approval without treating it as a substitute for or expansion of the internal review.
5. Record the feature head, reviewed SHA, findings, fixes, verification, and verdict. Any post-review code change invalidates the verdict and requires review again.
6. Merge only the exact reviewed SHA into integration using a traceable repository-approved strategy.
7. Record feature head, reviewed SHA, integration merge SHA, and evidence in the task plan; let the coordinator reconcile global identities into the roadmap.
8. Run integration checks after merge. Repair failures through a separate fix branch and the same gate.

## Preserve identity and branch direction

Preserve four distinct identities:

1. feature head;
2. reviewed SHA;
3. integration head or merge SHA;
4. frozen primary-branch candidate SHA.

Synchronize `primary -> integration` periodically and before promotion. Do not rebase or rewrite a shared integration branch. Update feature branches from the latest integration baseline according to repository policy, then rerun validation and review against the final head.

If primary-branch review requires squash and breaks ancestry, create any next-stage integration branch from the resulting primary head and explicitly retarget or rebuild active features. Do not infer continuity from matching content alone.

## Select promotion checkpoints

Use contextual judgment rather than promoting every milestone or deferring everything into one final review. A checkpoint is justified when evidence shows a coherent boundary such as:

- a stable backward-compatible foundation needed downstream;
- the first runnable and independently verifiable vertical slice;
- a deployable or reversible group of milestones;
- a boundary before a materially riskier phase;
- divergence that creates meaningful conflict, review, or validation risk;
- the final initiative candidate.

## Run the promotion gate

1. Freeze and record the exact integration candidate SHA.
2. Synchronize the latest primary branch and resolve conflicts inside the authorized integration workflow.
3. Run required integration and regression suites against the candidate.
4. Audit the accumulated delta since the previous promotion and verify the complete identity chain.
5. Confirm no blocking finding, missing milestone evidence, or unapproved policy exception remains.
6. Complete `assets/promotion-gate.md`.
7. Open or update a formal review request only when authorized; merge only after required approval and checks.
8. Record the resulting primary SHA and post-merge validation.

After the final promotion, record whether the integration branch continues or retires. Delete local or remote branches only when separately authorized and safe for all active work.
