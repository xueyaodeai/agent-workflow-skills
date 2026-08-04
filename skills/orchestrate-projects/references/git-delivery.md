# Git Delivery

Read this reference only when the task changes a Git repository or its completion depends on a Git delivery identity.

## Select the delivery contract

Choose the contract from the user's request, repository policy, and established project workflow:

- `uncommitted_change_set`: return a reviewed working-tree diff without creating a commit.
- `task_commit`: deliver one or more task-scoped commits.
- `externally_managed`: another authorized owner or system performs the commit or merge.

Do not treat a commit as universally required. Record the selected contract in the task plan. A commit never authorizes push, review creation, merge, deployment, messaging, or branch deletion.

Append `assets/task-plan-git-addon.md` to the task plan when Git identity or isolation matters. Also append `assets/task-plan-integration-addon.md` only when initiative integration is enabled.

## Orient before editing

Inspect and record:

- repository and worktree path;
- current branch and upstream relationship;
- primary or target branch;
- baseline revision;
- `git status --short`, staged diff, and unstaged diff;
- intended files or bounded hunks;
- pre-existing or other-task changes to preserve.

Use a dedicated branch and separate worktree before concurrent tasks write to the same repository. Do not let two worktrees check out the same branch. Follow repository naming conventions and discover the primary branch instead of assuming `main` or `master`.

## Preserve change ownership

- Keep a concrete list of files and, when necessary, hunks owned by the task.
- Do not absorb unrelated dirty-worktree changes because they are present.
- Do not stash, reset, discard, rewrite, or commit another task's changes.
- If task and unrelated edits overlap one file, stage only separable, reviewable hunks. Otherwise leave the delivery blocked and request the minimum decision.

## Deliver an uncommitted change set

1. Run required verification against the exact working tree being returned.
2. Inspect the complete unstaged and staged diff.
3. Confirm the diff contains only intended files or hunks and no secrets or unexpected generated output.
4. Record the baseline revision, changed paths, verification, and explicit `uncommitted_change_set` delivery boundary.
5. Do not report repository delivery complete if the agreed contract required a commit.

## Create a task-scoped commit

Use this low-freedom sequence when `task_commit` is the selected contract:

1. Finish required verification against the exact working tree to be committed.
2. Reinspect `git status --short`, the unstaged diff, and the staged diff.
3. Match files and hunks against the intended change set.
4. Stage only task-owned files or hunks. Never use broad staging such as `git add .` or `git add -A` in a dirty or shared worktree.
5. Inspect the staged name list and full staged diff. Remove unrelated, secret, or unexpected generated content.
6. Commit using the repository convention. Prefer one closeout commit; use multiple commits only for independently coherent task-local changes.
7. Record commit SHA, branch, worktree, committed paths, and verification result.

If a required hook or check fails, fix the in-scope cause and rerun it. Do not bypass hooks without explicit authorization.

## Verify completion

Before closing Git delivery, confirm:

- the delivered diff or commit matches the intended scope;
- verification is attributable to that exact subject;
- unrelated changes remain untouched;
- branch, worktree, baseline, changed paths, and delivery identity are recorded;
- skipped checks and residual risk are explicit;
- any post-review change invalidated and renewed the prior review verdict.
