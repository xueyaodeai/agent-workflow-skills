# Milestone Audit: <milestone name>

## Audit scope

- Roadmap: <path>
- Milestone: <identifier>
- Audit owner: <owner>
- Reviewed subject: <artifact/revision/environment>
- Observation time: <date/time>
- Audit boundary: <roadmap correctness, validation, code review, or combined>
- Frozen milestone contract: <roadmap section or versioned decision>
- Scope-change authority: <user or named policy owner>

## Exit-criteria assessment

| Exit criterion | Evidence required | Evidence observed | Verdict |
|---|---|---|---|
| <criterion> | <required proof> | <versioned proof> | <pass/fail/blocked> |

## Plan-to-reality reconciliation

- Promised result exists: <yes/no and evidence>
- Scope and non-goals respected: <yes/no and evidence>
- Roadmap state matches authoritative live state: <yes/no and corrections>
- Task plans and roadmap agree: <yes/no and corrections>
- New findings remain within the frozen contract or are routed to later work: <yes/no and impact>
- Sequence remains valid: <yes/no and reason>

## Review and validation status

- Independent code review: <not required with trigger assessment/completed by one fresh read-only reviewer subagent/pending or unavailable and evidence>
- Automated tests: <subject, result, and evidence>
- Local or manual validation: <subject, environment, and result>
- Delivery boundaries: <expected and observed identities>
- Skipped checks: <check, reason, risk, and owner>

## Findings

Classify findings with the blocker criteria in the `orchestrate-projects` independent-review reference. Route other findings to warnings, notes, or deferred follow-ups; the auditor must not expand the active milestone.

| Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |
|---|---|---|---|---|---|
| <blocker/warning/note> | <finding> | <criterion/rule/behavior or later-work classification> | <path/log/test and material effect> | <required correction or deferred owner/trigger> | <unresolved/resolved> |

## Gate decision

`do_not_advance` requires at least one unresolved blocker above. A scope-expansion proposal alone cannot fail the gate.

- Decision: `advance | do_not_advance | user_decision_required`
- Assessment authority: <auditor>
- Scope-change authority: <user or named policy owner>
- Rationale: <evidence-backed reason>
- Required corrections: <unresolved blockers only>
- Next milestone entry criteria: <conditions>

## Roadmap reconciliation

- Required updates: <state, decision, blocker, evidence, or sequence changes>
- Coordinator acknowledgement: <owner and date>
