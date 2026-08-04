## Git isolation and delivery add-on

- Repository: <path>
- Worktree/branch/baseline: <only identities needed for isolation or resume>
- Delivery contract: `uncommitted_change_set | task_commit | externally_managed`
- Authorized delivery package: <for example edit + verify + commit + push, or local only>
- Intended scope and unrelated changes to preserve: <paths/hunks>

### Git delivery record

- Delivered identity and paths: <commit/diff plus exact scope>
- Verification: <subject and result>
- External delivery completed or pending: <only actions in the authorized package>
