# Git Delivery

Read this reference only when the task changes a Git repository or its completion depends on a Git delivery identity.

## Select the delivery contract

Choose the contract from the user's request, repository policy, and established project workflow:

- `uncommitted_change_set`: return a reviewed working-tree diff without creating a commit.
- `task_commit`: deliver one or more task-scoped commits.
- `externally_managed`: another authorized owner or system performs the commit or merge.

Do not treat a commit as universally required. Follow the governing Authority rules and record a bounded delivery package only when a durable task plan exists. One explicit request may authorize a normal package such as edit + verify + commit + push; execute included steps without inserting repeated confirmation. Never infer an action outside that package.

Append `assets/task-plan-git-addon.md` only when Git identity or isolation must survive a context boundary, or when dirty/concurrent work makes ownership material. Also append `assets/task-plan-integration-addon.md` only when initiative integration is enabled.

## Orient before editing

Always inspect the repository/worktree, current branch, `git status --short`, target diff, and unrelated changes that must be preserved. Record branch, baseline, target, and path identities only when they are needed for resume, handoff, review, isolation, or a dirty/concurrent worktree.

Use a dedicated branch and separate worktree before concurrent tasks write to the same repository. Do not let two worktrees check out the same branch. Follow repository naming conventions and discover the primary branch instead of assuming `main` or `master`.

## Preserve change ownership

- Keep a concrete list of files and, when necessary, hunks owned by the task.
- Do not absorb unrelated dirty-worktree changes because they are present.
- Do not stash, reset, discard, rewrite, or commit another task's changes.
- If task and unrelated edits overlap one file, stage only separable, reviewable hunks. Otherwise leave the delivery blocked and request the minimum decision.

## Deliver an uncommitted change set

1. Run required verification against the exact working tree being returned.
2. Perform one consolidated scope check of status plus staged/unstaged diff; reject unrelated, secret, or unexpected generated content.
3. Record the working-tree identity only when another context must resume or verify it.
4. Do not report repository delivery complete if the agreed contract required a commit.

## Create a task-scoped commit

Use this low-freedom sequence when `task_commit` is the selected contract:

1. Finish required verification against the exact working tree to be committed.
2. Inspect status once to identify task-owned scope and unrelated changes to preserve.
3. Stage only task-owned files or hunks. Never use broad staging such as `git add .` or `git add -A` in a dirty or shared worktree.
4. Perform one complete pre-commit check of staged names, full staged diff, remaining unstaged changes, secrets, and unexpected generated content.
5. Commit using the repository convention. Prefer one closeout commit; use multiple commits only for independently coherent task-local changes. Return the commit identity; add branch/worktree/baseline details only when they matter for continuation or review.

If a required hook or check fails, fix the in-scope cause and rerun it. Do not bypass hooks without explicit authorization.

## Verify completion

Before closing Git delivery, confirm:

- the delivered diff or commit matches the intended scope;
- verification is attributable to that exact subject;
- unrelated changes remain untouched;
- continuation-critical branch, worktree, baseline, changed paths, and delivery identity are recorded when applicable;
- skipped checks and residual risk are explicit;
- any post-review change to reviewed behavior, contract, security, or critical reliability renewed the prior verdict; identity-only or status-only closeout updates do not.
