# Independent Review

Read this reference only when independent review is required by the trigger rules in `SKILL.md`. It defines how to perform that review; it does not add review requirements.

## Reviewer and snapshot

When independent review is required, use one fresh read-only reviewer subagent distinct from the implementer when subagents are available and higher-priority instructions permit it. Give it sourced requirements, implementation assumptions, the exact acceptance-ready snapshot, relevant evidence, and blocker threshold. Keep it read-only and do not prescribe a verdict or fix. Recheck assumptions using current evidence; freezing the snapshot does not make inherited architecture a requirement. If such a subagent cannot be started, record the review gate as pending or unavailable instead of treating self-review as independent.

When review is required, consolidate it around one acceptance-ready semantic snapshot. Do not split preflight, implementation, each operation, and result checking into repeated independent reviews. After blocking findings, use the same reviewer for a targeted recheck; widen it only if the fix changes another material boundary.

## Blocking findings

Apply the core complexity rule to new and inherited mechanisms within the reviewed scope. Unsupported complexity is a finding when a simpler solution satisfies the requirements at lower total cost; assess whether it blocks completion using the criteria below.

Current reachability alone does not make a finding blocking. A blocker must identify the declared acceptance or exit criterion, non-deferable higher-priority rule, or protected existing behavior it violates; evidence linking the violation to the required current flow or candidate change; the material effect on truthful completion; and why existing controls do not cover it.

Treat technically valid findings outside the frozen contract as warnings, notes, or deferred follow-ups only when the candidate change neither introduces nor materially worsens them and no non-deferable rule applies. Candidate-introduced regressions in a public contract, security or sensitive-data boundary, production or irreversible side effect, or critical fail-closed behavior remain blocking even when the affected behavior is outside the milestone happy path. A reviewer may recommend a later scope change, but only the named scope authority may add it to the active task or milestone.

## Historical evidence

Preserve historical review and audit records, but do not inherit their gates into later tasks without a current trigger.
