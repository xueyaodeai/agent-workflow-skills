# Primary-Branch Promotion Gate: <initiative and gate>

## Candidate identity

- Primary branch/current SHA: <branch and SHA>
- Previous promotion primary SHA: <SHA or none>
- Integration branch: <branch>
- Frozen integration candidate SHA: <SHA>
- Candidate scope: <milestones/features included>
- Merge strategy: <repository policy>

## Included identity chain

| Feature/milestone | Delivery identity | Reviewed SHA | Integration merge SHA | Review evidence | Integration validation |
|---|---|---|---|---|---|
| <feature> | <commit/diff> | <SHA> | <SHA> | <path/link> | <result> |

## Promotion preconditions

| Gate condition | Required evidence | Observed evidence | Verdict |
|---|---|---|---|
| Latest primary synchronized | <merge/sync proof> | <SHA/evidence> | <pass/fail/blocked> |
| Candidate identity frozen | <exact SHA> | <SHA> | <pass/fail/blocked> |
| Required regression complete | <suite> | <subject/result> | <pass/fail/blocked> |
| Accumulated-diff audit complete | <review scope> | <result> | <pass/fail/blocked> |
| Identity chain traceable | <identity matrix> | <result> | <pass/fail/blocked> |
| Blocking findings resolved | <finding ledger> | <result> | <pass/fail/blocked> |
| Formal review requirements known | <policy/checks> | <result> | <pass/fail/blocked> |
| Rollback or revert boundary defined | <procedure> | <result> | <pass/fail/blocked> |

## Promotion decision

- Decision: `promote | do_not_promote | user_decision_required`
- Authority: <owner>
- Rationale: <evidence-backed reason>
- Required corrections: <none or ordered list>
- Formal review request authorized: <yes/no/pending>

## Review and merge record

- Review request: <link/id or not created>
- Approved candidate SHA: <SHA>
- Resulting primary SHA: <SHA or pending>
- Post-merge validation: <subject/result/evidence>
- Integration branch next state: <continue/recreate/retire>
- Branch deletion authorization: <scope or pending>
- If squash broke ancestry: <new baseline and active-feature retarget plan>
