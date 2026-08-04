## Git isolation and delivery add-on

- Repository: <path>
- Worktree: <path>
- Branch: <task-specific branch>
- Target/primary branch: <branch>
- Baseline revision: <SHA>
- Delivery contract: `uncommitted_change_set | task_commit | externally_managed`
- Intended files/hunks: <exact paths or bounded areas>
- Pre-existing or other-task changes to preserve: <paths/hunks or `none`>

### Git delivery record

- Delivered revision or diff: <commit SHA, diff range, or working-tree identity>
- Delivered paths: <exact path list>
- Verification subject: <revision or exact working tree>
- Staged/full diff reviewed for unrelated changes: <yes/no/not applicable>
- Push/review/merge/deploy authorization: <explicit scope or `not authorized`>
