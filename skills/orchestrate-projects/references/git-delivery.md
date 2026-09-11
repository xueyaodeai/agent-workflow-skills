# Git Delivery

Read this reference only when the task changes a Git repository or its completion depends on a Git delivery identity.

## Select the delivery contract

Choose the contract from the user's request, repository policy, and established project workflow:

- `uncommitted_change_set`: return a verified working-tree diff without creating a commit.
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

## Reconcile after a PR/MR merges

Use this when the user asks to close out a merged change, check what it solved, or reconcile an existing issue/plan.
A merge notification is a fact to verify, not permission to deploy, close issues, post comments, or start recurring monitoring.
Carry forward any explicit authorization for those actions from the current task.

1. Read the live PR/MR state, target branch, merge commit and linked issues. Check the actual landed code when squash/rebase or later changes affect the conclusion; the old feature-branch tip alone is insufficient.
2. Compare each in-scope issue's required behavior with the merged implementation and relevant validation. Classify it as resolved within the agreed boundary, partially resolved, or not addressed. A plan title or passing generic test suite does not establish issue resolution.
3. Keep code completion and operational recovery separate. For recovery claims, match the deployed version and a new execution's actual checkout/image to the fix. A requested target SHA or an old failing build cannot prove which code ran. Unavailable deployment evidence means unknown, not failed or recovered.
4. Reuse the existing issue for remaining work. Split out shared deployment verification only when it has a distinct owner or verifiable outcome; link the original issues and do not lose their unresolved acceptance criteria.
5. Within the authorized write scope, update issue descriptions/comments/states and the existing plan/progress entry, then read back the affected records. Without that authority, return the proposed changes and evidence. Preserve other tasks' ownership of shared progress files.

Use a small reconciliation table when there are several issues:

| Issue / required result | Landed code and validation | Deployment / new execution evidence | Disposition and remaining work |
|---|---|---|---|
| Preserve the actual issue identity | Evidence for all or part of its requirement | Version and observed result, or unknown | Scope of completion, next owner or trigger |

An issue may close at code merge when that is its agreed completion boundary and operational verification has an explicit linked owner.
If its acceptance requires recovery in the running system, keep it open until that evidence exists. Do not silently change the boundary to clear the issue list.
An existing roadmap can complete with explicitly assigned follow-up work when that is its agreed scope; record the handoff instead of falsely claiming production recovery or reopening unrelated milestones.

When the user requests ongoing follow-up, use a temporary schedule attached to the existing task for the named MR or execution.
Track the MR revision and new comment IDs, or the run/report identity and status; inspect only changes that can alter the decision.
Notify on new actionable feedback, meaningful status changes, completion, or a blocker. Stay quiet while unchanged.
Stop the follow-up when its agreed result is verified, it is cancelled, or the target is superseded; pause it when user input is required.
Use the available scheduling tool to persist these transitions. Do not leave permanent polling for a completed run, start another run automatically, or invent a polling job when no follow-up was requested.

## Verify completion

Before closing Git delivery, confirm:

- the delivered diff or commit matches the intended scope;
- verification is attributable to that exact subject;
- unrelated changes remain untouched;
- continuation-critical branch, worktree, baseline, changed paths, and delivery identity are recorded when applicable;
- skipped checks and residual risk are explicit;
- when independent review was required, any later material change to the reviewed contract, security or sensitive-data boundary, production side effect, critical reliability behavior, milestone exit, or integration gate renewed the relevant verdict; ordinary local fixes and identity-only or status-only closeout updates do not create a review requirement.
