# Milestone Audit: <milestone name>

## Audit scope

- Roadmap: <path>
- Milestone: <identifier>
- Reviewed version: <commit/branch/environment>
- Feature branch/head SHA: <branch and SHA or `not applicable`>
- Reviewed SHA: <SHA or `not applicable`>
- Integration merge SHA: <SHA or pending/not applicable>
- Audit boundary: <read-only review, code review, validation, or combined>

## Exit-criteria assessment

| Exit criterion | Evidence required | Evidence observed | Verdict |
|---|---|---|---|
| <criterion> | <required proof> | <actual proof> | pass/fail/blocked |

## Plan-to-reality reconciliation

- Promised result exists: <yes/no and evidence>
- Scope and non-goals respected: <yes/no and evidence>
- Roadmap status matches live state: <yes/no and corrections>
- New findings change later work: <yes/no and impact>
- Missing milestone or task: <none or details>
- Sequence still valid: <yes/no and reason>

## Review and validation status

- Code review: <completed/not required/pending and evidence>
- Automated tests: <result and version>
- Local or manual validation: <result and environment>
- Task delivery commits: <expected SHAs, branch/worktree, and scope-isolation result>
- Feature-to-integration identity chain: <feature head -> reviewed SHA -> integration merge SHA>
- Post-merge integration validation: <result and evidence>
- Skipped checks: <check, reason, and risk>

## Findings

| Severity | Finding | Evidence | Required action |
|---|---|---|---|
| <blocker/warning/note> | <finding> | <path/log/test> | <action> |

## Gate decision

- Decision: `advance | do_not_advance | user_decision_required`
- Rationale: <evidence-backed reason>
- Required corrections: <none or ordered list>
- All completed implementation tasks committed without unrelated changes: <yes/no/not applicable>
- Exact reviewed SHA was merged without post-review drift: <yes/no/not applicable>
- Next milestone entry criteria: <conditions>

## Roadmap updates required

- <Exact state, decision, blocker, evidence, or sequence update.>
