# Skill entry routing baseline

Recorded on 2026-11-18 with Codex CLI `0.167.2`, model `gpt-6.2-astra`, and reasoning effort `low`. The baseline is `15b7724ef95c7578d7590124cc296bab1ac070c4`. The candidate is `ce4cd59410b1d63ce0dfa533aee17d67e238b9b6`. Both use the three [case definitions](../behavior_cases.json) from the candidate revision and the same native Codex host setup described in the [evaluation protocol](../README.md#skill-entry-routing-ab-check). Runs used a workspace-write sandbox, with web search and subagents disabled. Codex was the only host evaluated.

There was one completed sample per case and revision. The first baseline chat-summary attempt timed out after 115.06 seconds with only start events and a model-catalog refresh timeout. It was inconclusive and excluded from the behavior counts. One retry with the same model and fixture and a 145-second timeout completed in 12.43 seconds.

| Case ID | Baseline observation | Candidate observation | Misroutes, baseline → candidate | Distinct unnecessary files, baseline → candidate |
| --- | --- | --- | --- | --- |
| `verification_chat_summary_no_report_artifact` | Reported that 12 unit tests passed on `abc123` and the browser smoke test was unrun. Zero tool commands, no Skill body read or file write. | Same observations. | 0 → 0 | 0 → 0 |
| `fix_issue_default_prompt_preserves_diagnosis_only` | Read the `fix-issue` entrypoint and inspected `pricing.py`. Reproduced `IndexError` with `python3 -B`, identified the unguarded `items[0]` access, and proposed a repair. Git status was clean. | Same diagnosis and clean status. | 0 → 0 | 0 → 0 |
| `orchestration_level_zero_uses_only_current_task` | Opened `references/git-delivery.md` twice in one command. The final Git diff changed only `helpp` to `help` in `docs/help.md`, unstaged and uncommitted. No project record. | Opened the Skill entrypoint and read the target file. No reference file reads. Same final Git diff and delivery state. | 0 → 0 | 1 → 0 |
| **Total** | | | **0/3 → 0/3** | **1 → 0** |

The Level 0 difference is visible in the first file-read command in each trace. Paths below are relative to the temporary workspace.

```sh
# Baseline
cat .agents/skills/orchestrate-projects/{SKILL.md,references/git-delivery.md} >/dev/null; cat .agents/skills/orchestrate-projects/references/git-delivery.md | head -20
# Candidate
cat .agents/skills/orchestrate-projects/SKILL.md
```

The same requested outcomes were delivered in both revisions. The observed reduction is one distinct reference file for the Level 0 case. With one completed sample per cell, misroute rates across future runs remain unmeasured.
