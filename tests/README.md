# Validation and behavioral evaluation

## Deterministic repository checks

Run `python3 -m unittest discover -s tests -v` from the repository root with Python 3.10 or later. Install the test dependency first with `python3 -m pip install -r tests/requirements.txt`. Once PyYAML is installed, checks need no network, provider credentials, or task-system writes. Fixtures use synthetic evidence; their content is not a claim about a real implementation.

The suite covers ready and not-ready contracts, each required field, scoped milestones, completion/evidence contradictions, unsupported formats, command exit codes, prompt consistency, and evaluation-case integrity. Negative completion tests start from otherwise valid new-format contracts: they must fail for the actual contradiction, not merely for missing newly added fields. String-level consistency checks are not model-behavior evaluations.

## Skill metadata validator

Run `python3 scripts/validate_skill_metadata.py` to check all repository skills, or pass specific skill directories. This repository-owned check leaves the installed `skill-creator` untouched. It validates required name/description fields, rejects unknown frontmatter and policy fields and duplicate YAML keys, and checks invocation fields as booleans rather than matching text.

The three explicit-only Dida365 skills must retain both configurations:

- `SKILL.md`: `disable-model-invocation: true` for Claude Code.
- `agents/openai.yaml`: `policy.allow_implicit_invocation: false` for Codex.

The supported frontmatter fields are `name`, `description`, `license`, `allowed-tools`, `metadata`, and the known `disable-model-invocation` extension. This is a repository schema, not a complete validator for every host's extensions or UI/dependency metadata. The bundled OpenAI `quick_validate.py` rejects the Claude Code extension in its current allowlist; that does not establish a runtime failure. Do not delete the extension just to satisfy that generic check. Actual host invocation behavior still requires host-level evaluation.

## Document validator scope

`skills/orchestrate-projects/scripts/validate_project_docs.py` supports the English template-shaped **Task Plan**, **Outcome Plan**, **Project Roadmap**, **Milestone Audit**, and **Next-Round Roadmap Alignment Notes** headings. It is not a general Markdown, translated-schema, or free-form plan validator. Preserve repository conventions and inspect equivalent information manually when a custom schema is used. Unknown formats, including standalone add-ons and promotion gates, return an explicit unsupported error instead of a success.

```bash
python3 skills/orchestrate-projects/scripts/validate_project_docs.py plan.md
python3 skills/orchestrate-projects/scripts/validate_project_docs.py --require-ready plan.md
```

The default check permits an explicit `Readiness: not_ready` draft with named `Readiness blockers` and a non-executing status. Such a draft is structurally valid, not permission to execute. `--require-ready` requires ready contract fields for the selected task/outcome or the roadmap root and current milestone; it does not force detailed future milestones to become ready. Current milestone references start with an ID such as `M1` or `[M1](#m1-export)`.

Readiness is separate from progress, prerequisites, and permission. `ready_for_verification` is a progress state, not execution readiness. A structural result does not establish whether a reason is true, a path is optimal, every requirement is covered, referenced evidence exists or is accessible, dependencies are satisfied, or an action is authorized. The agent must verify these at their sources. These prompts and this script are not a security boundary or a host-enforced action gate.

Completed tasks require matching current and final states, `Verification result: pass`, substantive `Verification`, a result, and a delivery boundary. Completed milestones require their own `Exit result: pass` and `Exit evidence`. Completed roadmaps require `Completion result: pass`, `Completion evidence`, an evidence index, and no unfinished in-scope milestones or workstreams. Current failure/status columns and unchecked criteria contradict closeout; a historical failure in an investigation log does not automatically invalidate later evidence.

### Migrating existing materialized templates

Add `Why`, `Shortest path`, `Best path`, `Selected path`, and `Readiness` to the relevant existing sections rather than creating another ledger. Keep the existing outcome, scope, and acceptance fields. Use explicit accessible references to inherit parent decisions, not hidden chat history. The shortest and best paths may be the same but must share the complete acceptance criteria.

Add `Readiness blockers` only while not ready; name the missing decision and dependent work. Remove the field when resolved. Do not default existing plans to ready. For a roadmap, add readiness and the four-point contract to each ready/executing milestone, not just M1; future milestones may remain not ready with a refinement trigger. Add the structured result fields described above for completion, without fabricating pass results. Remove unresolved angle-bracket placeholders and unused closeout sections from materialized drafts. Unchanged milestone-audit and alignment state protocols remain supported.

The templates are optional. For direct tasks outside a loaded skill, the host must actually load the common or Codex personal defaults; `npx skills add` does not install those files. No skill relies on a sibling skill's files for its readiness guard.

## Live-model behavior protocol

`behavior_cases.json` contains self-contained subject inputs, fixture context, allowed mock tools, and separate grading expectations. **These are evaluation specifications, not recorded model passes.** The deterministic suite validates their format only.

Defensive-programming cases cover established internal contracts, required external-input validation, observable failures, justified bounded recovery, unsupported compatibility and extension points, and implementation handoffs. They also distinguish raw database/config/environment/LLM data from validated SDK results, contrast guaranteed ORM fields with an unvalidated JSON column, and exercise final-diff inspection without syntax blacklists or per-conditional justification. Evaluate the named templates and standalone skills as supplied in each case; do not implicitly add personal defaults. Inspect the resulting code or contract for unnecessary mechanisms as well as preservation of required safeguards. A safe simplification must still satisfy the full acceptance criteria.

Run the same cases against a pinned OpenAI model and a pinned Anthropic model, using the actual host configurations to be evaluated. Run both baseline and candidate revisions, keep tool fixtures and budgets identical, and record model ID/version, effort, host version, loaded instruction paths and revision, case ID, repetitions, transcript, tool-call trace, and resulting artifact/state diff. Do not silently change budgets or add provider-specific instructions between revisions. Keep provider-specific tuning outside the common policy unless measurements justify it.

Pass only `subject_input`, `context`, and the mock-tool descriptions to the subject along with the selected guidance/skills. Keep `expected` and reviewer judgments out of subject context. Start each case in a fresh context. Do not use real task-system accounts, repository pushes, paid services, production data, or other live side effects for fixtures. An evaluation runner or reviewer must inspect both user-visible output and actual tool actions; a promised clarification cannot excuse an implementation write that already occurred.

Grade each expectation as pass, fail, or inconclusive with trace evidence. A false completion, implementation dependent on an unresolved consequential decision, or unauthorized side effect is a failure. A missing tool trace or unavailable fixture is inconclusive, not a pass. For nondeterministic runs, predeclare repetitions (for example, three per case per configuration), report failures and denominators, and do not extrapolate observed zero failures into a guarantee. Separately track unnecessary clarification of already settled tasks, scope shrinkage, and loss of information at handoff.

Do not report live-model improvement, independent review, official `skill-creator` validation, or installer compatibility unless those checks were actually run. Unrun configurations remain untested. Installation discovery, model evaluation, and this deterministic suite are separate checks.
