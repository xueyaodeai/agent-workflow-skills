# Roadmap Cross-Model Review

Use this protocol only as a supplemental, best-effort challenge review for a material roadmap. Keep the normal repository review and approval gates authoritative.

## 1. Availability probe

Complete the probe without making a model request:

1. Locate the installed `agent` binary; accept `cursor-agent` only as its documented compatibility alias. Do not install or upgrade it automatically.
2. Use bounded help/version commands to verify support for non-interactive output, explicit model selection, read-only Ask mode, sandbox enablement, and model listing. A crashing, hanging, or ambiguous CLI is unavailable.
3. Check existing authentication status and retain only a boolean result; do not print or persist account details, tokens, headers, endpoints, or environment values. Do not initiate login or pass an API key in argv.
4. Use the installed CLI's model-list command discovered from its help and require the exact model ID `claude-opus-5-thinking-medium`. Do not guess a renamed model or choose a fallback. Listing models is part of the probe; it must not send a review prompt.
5. Confirm an approved sanitized review packet can be produced and that read-only execution can be enforced. Absence of data-egress authorization is an unavailable prerequisite, not implied consent.

Classify availability independently from review status:

- `available_in_executor`: every prerequisite is positively verified in the current execution environment;
- `available_host_only`: the current executor is blocked specifically by sandbox, Keychain, or equivalent host-bound access, while fresh host-terminal evidence verifies the same CLI version, authentication, exact model, and read-only flags;
- `unavailable`: binary, authentication, exact model, read-only enforcement, approved input, or trustworthy host evidence is absent or unverified.

On `unavailable`, report the failed prerequisite and continue the base roadmap workflow. Do not mark the roadmap blocked, do not retry without an environment change, and do not substitute an internal GPT reviewer while calling it cross-model review.

Do not treat copied or stale host output as permanent capability. Record its date, CLI version, exact model ID, and source. Recheck on a later task when the CLI, account, model catalog, or environment may have changed.

## 2. Outside-sandbox authorization

For `available_host_only`, request a one-time outside-sandbox execution authorization only after the sanitized snapshot is frozen. The approval request must state:

- the exact Cursor executable and model `claude-opus-5-thinking-medium`;
- the snapshot path, allowlisted files, and content hashes;
- that approved content will be transferred to Cursor and may incur model cost;
- `--mode ask --sandbox enabled`, no write authorization, and no unnecessary MCP/network access;
- that approval applies to one command and one snapshot only.

Do not request a reusable broad `agent` prefix or persistent sandbox bypass. Do not use `--force`, `--yolo`, `--trust`, or `--approve-mcps`. A decline, unavailable approval mechanism, or failed outside-sandbox launch yields `outside_sandbox_authorization=declined|unavailable` and `external_review_status=unavailable`; explain it and continue the base roadmap workflow.

Host availability is not data-egress authorization. Do not request outside-sandbox execution until the user has also approved the review packet and external model call. A prior login, model-list check, or unrelated Cursor approval grants neither.

## 3. Review packet

Build an isolated read-only snapshot with an explicit allowlist. Include only what the reviewer needs:

- applicable `AGENTS.md` and architecture constraints;
- alignment notes and the candidate roadmap;
- selected source, tests, fixtures, baselines, SDK metadata, or deployment evidence needed to verify feasibility;
- base/head identity or content hashes.

Exclude prior review reports, remediation plans, chat transcripts, model conclusions, secrets, credentials, private raw payloads, unrelated source, `.cursor` MCP configuration, and user/global memory. The first pass must not see expected findings.

Run from the isolated snapshot with Ask mode and sandbox explicitly enabled. Never use `--force`, `--yolo`, `--trust`, or `--approve-mcps`; deny write permissions and unnecessary shell, MCP, or network tools. Verify the snapshot hashes before and after the run.

## 4. Reviewer contract

Start a fresh session and explicitly select `claude-opus-5-thinking-medium`. Prefer stream JSON so the coordinator can record the observed model and session ID. Reject the result as inconclusive if the observed model differs.

Use the installed CLI's equivalent of this invocation after the probe succeeds:

```text
agent --print --mode ask --sandbox enabled \
  --model claude-opus-5-thinking-medium \
  --output-format stream-json \
  --workspace <isolated-review-snapshot> \
  <de-anchored-review-prompt>
```

Ask the reviewer to challenge, with repository evidence:

1. whether every Exit can pass while the promised user value remains unavailable;
2. when each fact is produced, where its authority lives, and how immutable snapshots are combined;
3. whether a format or directory change creates a new privacy, trust, or data-egress decision;
4. whether claimed SDK/model/platform capabilities are implemented, typed, permissioned, or require a real probe;
5. whether hard dependencies and project closure semantics unnecessarily couple independent work;
6. whether service/process structure violates repository architecture limits;
7. whether Exit criteria imply external writes or authority not granted by the roadmap;
8. whether cleanup or migration rewrites historical audit evidence.

Require this result shape in the assistant result:

```json
{
  "verdict": "GO | CONDITIONAL_GO | NO_GO",
  "reviewed_artifact_hashes": {},
  "findings": [
    {
      "id": "XR-001",
      "severity": "error | blocking_warning | warning",
      "promise": "",
      "failure_scenario": "",
      "repository_evidence": ["path:line"],
      "recommended_disposition": ""
    }
  ],
  "unverified_claims": [],
  "required_probes": []
}
```

Do not request hidden reasoning or persist chain-of-thought. Persist only the result, evidence references, model/session identity, hashes, duration/usage when available, and disposition.

## 5. Disposition and re-review

The coordinating agent must reproduce or inspect each finding before accepting it. Record accepted, rejected, narrowed, and user-decision findings separately; an external reviewer is not an authority by itself.

Accepted blocking findings prevent a GO verdict until fixed or explicitly resolved under repository policy. Resume the same Cursor session for targeted re-review of the exact fixes and finding IDs. Record both the requested and observed model, session ID, reviewed hashes, and final verdict. Any post-review roadmap change invalidates the verdict.

Treat timeout, transport failure, malformed output, missing evidence, model mismatch, or an unreproducible report as `completed_inconclusive`. Explain it and continue the base workflow; do not silently promote it to GO and do not turn reviewer infrastructure failure into a roadmap blocker.
