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

- Independent code review: <not required with trigger assessment/completed/pending and evidence>
- Automated tests: <subject, result, and evidence>
- Local or manual validation: <subject, environment, and result>
- Delivery boundaries: <expected and observed identities>
- Skipped checks: <check, reason, risk, and owner>

## Findings

A finding is blocking only when it proves that a frozen exit criterion fails, a non-deferable higher-priority rule is violated, or the reviewed candidate introduces or materially worsens a protected existing behavior such as a public contract, security or sensitive-data boundary, production or irreversible side effect, or critical fail-closed behavior. Current reachability alone is insufficient. Route other technically valid findings to warnings, notes, or deferred follow-ups; the auditor must not expand the active milestone.

| Severity | Finding | Contract, rule, or protected behavior violated | Current-flow or candidate-change evidence | Disposition | Status |
|---|---|---|---|---|---|
| <blocker/warning/note> | <finding> | <criterion/rule/behavior or later-work classification> | <path/log/test and material effect> | <required correction or deferred owner/trigger> | <unresolved/resolved> |

## Gate decision

`do_not_advance` requires at least one unresolved blocker above that is linked to the frozen milestone contract, a non-deferable higher-priority rule, or a candidate-introduced protected-behavior regression. A scope-expansion proposal alone cannot fail the gate.

- Decision: `advance | do_not_advance | user_decision_required`
- Assessment authority: <auditor>
- Scope-change authority: <user or named policy owner>
- Rationale: <evidence-backed reason>
- Required corrections: <only unresolved blockers linked to the frozen contract, non-deferable rules, or candidate-introduced protected-behavior regressions>
- Next milestone entry criteria: <conditions>

## Roadmap reconciliation

- Required updates: <state, decision, blocker, evidence, or sequence changes>
- Coordinator acknowledgement: <owner and date>
