# Master Promotion Gate: <initiative and gate>

## Candidate identity

- Master branch/current SHA: <branch and SHA>
- Previous promotion master SHA: <SHA or none>
- Integration branch: <branch>
- Frozen integration candidate SHA: <SHA>
- Candidate scope: <milestones/features included>
- Merge strategy: <policy>

## Included feature identity chain

| Feature/milestone | Delivery commit | Reviewed SHA | Integration merge SHA | Review evidence | Integration validation |
|---|---|---|---|---|---|
| <feature> | <SHA> | <SHA> | <SHA> | <path/link> | <result> |

## Promotion preconditions

| Gate condition | Required evidence | Observed evidence | Verdict |
|---|---|---|---|
| Latest master synchronized | <merge/sync proof> | <SHA/evidence> | pass/fail/blocked |
| Candidate identity frozen | <exact SHA> | <SHA> | pass/fail/blocked |
| Full regression complete | <suite> | <result> | pass/fail/blocked |
| Independent accumulated-diff audit complete | <review scope> | <result> | pass/fail/blocked |
| Feature/review/merge identities traceable | <identity matrix> | <result> | pass/fail/blocked |
| Blocking findings resolved | <finding ledger> | <result> | pass/fail/blocked |
| Formal master CR requirements known | <policy/checks> | <result> | pass/fail/blocked |
| Rollback or revert boundary defined | <procedure> | <result> | pass/fail/blocked |

## Promotion decision

- Decision: `promote | do_not_promote | user_decision_required`
- Rationale: <evidence-backed reason>
- Required corrections: <none or ordered list>
- Formal CR authorized: <yes/no/pending>

## Formal CR and merge record

- CR/MR: <link/id or not created>
- Approved candidate SHA: <SHA>
- Resulting master SHA: <SHA or pending>
- Post-merge validation: <result/evidence>
- Integration branch next state: <continue/recreate/retire>
- If squash broke ancestry: <new integration baseline and active-feature retarget plan>
