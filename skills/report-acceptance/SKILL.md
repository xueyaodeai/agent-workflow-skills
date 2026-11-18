---
name: report-acceptance
description: Map agreed acceptance criteria to existing evidence in a standalone offline HTML report. Use when the user asks for an HTML acceptance report or a separate acceptance report artifact.
metadata:
  version: 1.0.1
---

# Report Acceptance

Show a reader, in one page, which agreed criteria are met, which are not, and the evidence behind each verdict. The page reports evidence; it never creates it.

For a verification summary in chat, answer from the available evidence within the current task's scope. Write an HTML file only when the request or explicit skill invocation calls for the report artifact and the active write scope permits it. Honor any requested output format and read-only scope.

## 1. Establish the contract

Reuse the acceptance criteria from the user's request, the current plan, or the task contract. Each criterion needs a scenario, expected behavior, and the evidence that would prove it. Direct requests follow the same readiness check: know why the report is wanted, what scope and delivery boundary it covers, the shortest and best paths to gather its evidence, and what makes the report done. The report is ready to write once those points are known. When criteria are missing or ambiguous, do not invent them to fill the page; list them under open items or ask one concise question if the gap changes the verdict.

A request for the report artifact authorizes reading existing evidence and writing that artifact within the active permissions. Collect new evidence only when the request or existing authority includes that work.

## 2. Classify each criterion

Inspect the actual evidence before assigning a status:

| Status | Use when |
| --- | --- |
| `pass` | Current evidence directly shows the expected behavior for the stated subject and environment. |
| `fail` | Evidence shows the behavior is wrong or the check failed. |
| `missing` | No evidence, stale or mismatched evidence (other revision, environment, or build), or a skipped or empty run. |
| `manual` | Only a human judgment can decide it and none has been recorded. |

- Record the subject identity behind each verdict: revision or build, environment, and observation time. Historical evidence keeps its own time and revision; do not attribute it to the current revision.
- State the exact check and environment in each row (for example, local unit test, build, or live deployment); mark installation or deployment criteria pass only with their own evidence.
- Link native reports, logs, and screenshots by path or URL rather than pasting full logs. Quote a short excerpt only when it explains the verdict.
- The overall verdict is `pass` only when every required criterion is `pass`. Otherwise state which required criteria block it.

## 3. Write the page

Copy [assets/acceptance-report.html](assets/acceptance-report.html) and fill its placeholders. Repeat a criterion row per criterion and remove unused sections. Keep the page offline: no remote scripts, fonts, or images. Embed a screenshot only when it is small and relevant; otherwise link it. HTML-escape any text that comes from logs, test names, or user data.

Save the report outside version control by default: `$(git rev-parse --git-common-dir)/agent/` in Git repositories, or an existing authorized local location outside Git. Write into the project only when the user asks for a tracked report.

## 4. Check and deliver

Before replying, confirm that the summary counts match the rows, every non-`pass` row says what is missing or failed, every evidence link resolves, and no placeholder remains. Open the page in a browser when one is available; otherwise state that it was not rendered.

Reply with the overall verdict, the blocking criteria, and the report path. Do not restate the whole table in chat.
