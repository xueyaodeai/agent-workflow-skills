#!/usr/bin/env python3
"""Check supported Markdown contracts; never certify evidence or authorize actions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BASE_STATES = {
    "not_started",
    "in_progress",
    "ready_for_verification",
    "blocked",
    "complete",
    "deferred",
    "cancelled",
    "superseded",
}
TERMINAL_STATES = {"complete", "blocked", "deferred", "cancelled", "superseded"}
ALIGNMENT_STATES = {"inventory", "alignment_in_progress", "aligned", "superseded"}
GENERATION_STATES = {"not_ready", "draft_unreviewed", "reconciled"}
AUDIT_DECISIONS = {"advance", "do_not_advance", "user_decision_required"}
FINDING_SEVERITIES = {"blocker", "warning", "note"}
FINDING_STATUSES = {"unresolved", "resolved"}
EXIT_VERDICTS = {"pass", "fail", "blocked"}
CONTRADICTORY_CELLS = {"fail", "blocked", "open", "pending", "no"}
ROADMAP_CONTRACT_LABELS = {
    "Required happy path",
    "Exit criteria",
    "Current non-goals and accepted deferrals",
    "Blocker threshold",
    "Stop condition",
}
AUDIT_CONTRACT_LABELS = {"Frozen milestone contract", "Scope-change authority"}
EXIT_CRITERIA_HEADER = (
    "exit criterion",
    "evidence required",
    "evidence observed",
    "verdict",
)
FINDINGS_HEADER = (
    "severity",
    "finding",
    "contract, rule, or protected behavior violated",
    "current-flow or candidate-change evidence",
    "disposition",
    "status",
)

PLACEHOLDER_RE = re.compile(r"<(?!https?://)[^<>\n]+>")
STATE_RE = re.compile(
    r"^- (?P<label>Status|Final status|Generation status):[ \t]*(?P<value>[^\n]*)$",
    re.MULTILINE,
)
FINAL_COMPLETE_RE = re.compile(r"^- Final status:\s*`?complete`?\s*$", re.MULTILINE)
DECISION_RE = re.compile(
    r"^- Decision:[ \t]*(?P<value>[^\n]*)$",
    re.MULTILINE,
)
UNCHECKED_RE = re.compile(r"^[ \t]*[-*] \[ \] ", re.MULTILINE)


def artifact_kind(text: str) -> str:
    first_line = text.lstrip("\ufeff\r\n").splitlines()[0] if text.strip("\ufeff\r\n") else ""
    if first_line.startswith("# Outcome Plan:"):
        return "outcome"
    if first_line.startswith("# Task Plan:"):
        return "task"
    if first_line.startswith("# Project Roadmap:"):
        return "roadmap"
    if first_line.startswith("# Next-Round Roadmap Alignment Notes:"):
        return "alignment"
    if first_line.startswith("# Milestone Audit:"):
        return "audit"
    return "custom"


def missing_labels(text: str, labels: set[str]) -> list[str]:
    return sorted(
        label
        for label in labels
        if not re.search(rf"^- {re.escape(label)}:[ \t]*[^\s]", text, re.MULTILINE)
    )


def section_table_rows(text: str, heading: str) -> list[list[str]]:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return []
    rows: list[list[str]] = []
    for line in match.group("body").splitlines():
        if not line.startswith("|"):
            continue
        rows.append(
            [cell.strip().strip("`").lower() for cell in line.strip("|").split("|")]
        )
    return rows


def is_separator_row(row: list[str]) -> bool:
    return bool(row) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in row)


def validated_table_rows(
    text: str,
    heading: str,
    expected_header: tuple[str, ...],
) -> tuple[list[list[str]], list[str]]:
    rows = section_table_rows(text, heading)
    if not rows:
        return [], [f"missing {heading} table"]
    if rows[0] != list(expected_header):
        return [], [f"invalid {heading} table header"]
    if len(rows) < 2 or not is_separator_row(rows[1]):
        return [], [f"missing {heading} table separator"]

    data_rows: list[list[str]] = []
    errors: list[str] = []
    for index, row in enumerate(rows[2:], start=1):
        if len(row) != len(expected_header):
            errors.append(
                f"{heading} table row {index} has {len(row)} columns; "
                f"expected {len(expected_header)}"
            )
            continue
        data_rows.append(row)
    return data_rows, errors



READY_STATES = {"ready", "not_ready"}
EXECUTING_STATES = {"in_progress", "ready_for_verification", "complete"}
UNFINISHED_STATES = {"not_started", "in_progress", "ready_for_verification", "blocked"}
PATH_LABELS = {"Why", "Shortest path", "Best path", "Selected path"}
TASK_LABELS = PATH_LABELS | {"Observable result", "Requirement basis", "In scope", "Acceptance checks"}
OUTCOME_LABELS = PATH_LABELS | {"Final result", "Scope and delivery boundary"}
ROOT_LABELS = PATH_LABELS | {"Final observable outcome", "In scope", "Side-effect boundary"}
MILESTONE_LABELS = PATH_LABELS | ROADMAP_CONTRACT_LABELS | {"Requirements", "Entry conditions/depends on"}
UNRESOLVED_RE = re.compile(
    r"^(?:pending|tbd|todo|unknown|unresolved|awaiting|not[ _-]+(?:yet[ _-]+)?(?:run|verified|checked)|"
    r"待验证|待确认|未验证|未运行)(?:\b|[ :：—-]|$)", re.IGNORECASE
)


def clean(value: str) -> str:
    return value.strip().strip("`").strip()


def without_examples(text: str) -> str:
    """Ignore fenced examples and HTML comments, not actual contract fields."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    lines: list[str] = []
    fence = ""
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if not fence:
                fence = token
                continue
            if token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
                continue
        if not fence:
            lines.append(line)
    return "\n".join(lines)


def values(text: str, label: str) -> list[str]:
    return [clean(v) for v in re.findall(rf"^- {re.escape(label)}:[ \t]*(.*)$", text, re.MULTILINE)]


def value(text: str, label: str) -> str:
    found = values(text, label)
    return found[0] if found else ""


def unusable(content: str) -> bool:
    return (not content or content.casefold() in {"none", "n/a", "not applicable", "-", "—"}
            or bool(UNRESOLVED_RE.match(content)))


def require_fields(text: str, labels: set[str]) -> list[str]:
    errors: list[str] = []
    for label in sorted(labels):
        found = values(text, label)
        if len(found) != 1:
            errors.append(f"expected one {label} field; found {len(found)}")
        elif unusable(found[0]) and not (found[0].casefold() == "none" and label in {"Current non-goals and accepted deferrals", "Entry conditions/depends on"}):
            errors.append(f"{label} is empty or unresolved")
    return errors


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}[ \t]*$\n?(.*?)(?=^## |\Z)",
                      text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def require_section(text: str, heading: str) -> list[str]:
    body = section(text, heading)
    if not body:
        return [f"missing or empty {heading} section"]
    if body.startswith("|"):
        rows = section_table_rows(text, heading)
        if len(rows) < 3 or not is_separator_row(rows[1]):
            return [f"{heading} table has no valid data rows"]
        if any(not cell for row in rows[2:] for cell in row):
            return [f"{heading} table contains empty cells"]
    return []


def readiness_errors(text: str, labels: set[str], *, force: bool = False,
                     executing: bool = False) -> list[str]:
    found = values(text, "Readiness")
    if len(found) != 1 or found[0] not in READY_STATES:
        return ["expected one Readiness field: ready or not_ready"]
    ready = found[0] == "ready"
    errors: list[str] = []
    if not ready:
        if force or executing:
            errors.append("not_ready contract cannot be used for selected or executing work")
        blockers = values(text, "Readiness blockers")
        if len(blockers) != 1 or not blockers[0] or blockers[0].casefold() in {"none", "pending", "tbd", "unknown"}:
            errors.append("not_ready contract needs named Readiness blockers")
    else:
        if values(text, "Readiness blockers"):
            errors.append("ready contract must remove resolved Readiness blockers")
        errors.extend(require_fields(text, labels))
    return errors


def evidence_errors(text: str, result_label: str, evidence_label: str) -> list[str]:
    errors = require_fields(text, {evidence_label})
    if values(text, result_label) != ["pass"]:
        errors.append(f"completion requires one {result_label}: pass")
    return errors


def table_states(text: str, heading: str) -> list[str]:
    """Read each current table under matching headings, including template add-ons.

    Stop at the next heading so historical subsections do not become current
    evidence. Each table owns its columns; separate tables may differ in shape.
    """
    states: list[str] = []
    active = False
    header: list[str] | None = None
    columns: list[int] = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6} (.+?)[ \t]*$", line)
        if match:
            active = match.group(1) == heading
            header = None
            columns = []
            continue
        if not active or not line.startswith("|"):
            header = None
            columns = []
            continue
        row = [clean(cell).lower() for cell in line.strip("|").split("|")]
        if header is None:
            header = row
            columns = [i for i, name in enumerate(header)
                       if name in {"status", "result", "verdict"}]
        elif not is_separator_row(row):
            states.extend(row[i] for i in columns if i < len(row))
    return states


def contract_errors(text: str, kind: str, require_ready: bool) -> list[str]:
    errors: list[str] = []
    if kind == "task":
        status = value(text, "Status")
        if len(values(text, "Status")) != 1:
            errors.append("task requires exactly one current Status")
        errors.extend(readiness_errors(text, TASK_LABELS, force=require_ready,
                                       executing=status in EXECUTING_STATES))
        final = value(text, "Final status")
        if len(values(text, "Final status")) > 1:
            errors.append("duplicate Final status")
        if final and final != status:
            errors.append("current Status contradicts Final status")
        if status == "complete" and final != "complete":
            errors.append("completed task requires Final status: complete")
        if status == "complete" or final == "complete":
            errors.extend(evidence_errors(text, "Verification result", "Verification"))
            errors.extend(require_fields(text, {"Result", "Delivery boundary"}))
    elif kind == "outcome":
        errors.extend(readiness_errors(text, OUTCOME_LABELS, force=require_ready))
        if value(text, "Readiness") == "ready":
            errors.extend(require_section(text, "Acceptance criteria"))
            errors.extend(require_fields(text, {"Final acceptance of required outcomes", "Overall result verification", "Delivery boundary", "Tasks ready to start"}))
        if values(text, "Final status"):
            errors.append("Outcome Plan defines planned acceptance, not implementation closeout")
    elif kind == "roadmap":
        body = section(text, "Milestones")
        matches = list(re.finditer(r"^### (.+)$", body, re.MULTILINE))
        milestones: list[tuple[str, str]] = []
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
            milestones.append((match.group(1).split(":", 1)[0].strip(), body[match.end():end]))
        root = re.sub(r"^## Milestones[ \t]*$\n?.*?(?=^## |\Z)", "", text,
                      flags=re.MULTILINE | re.DOTALL)
        active = any(value(block, "Status") in EXECUTING_STATES for _, block in milestones)
        errors.extend(readiness_errors(root, ROOT_LABELS, force=require_ready, executing=active or value(root, "Final status") == "complete"))
        if value(root, "Readiness") == "ready":
            errors.extend(require_section(root, "Completion criteria"))
        if not milestones:
            errors.append("roadmap has no scoped milestone records")
        names = [name for name, _ in milestones]
        if len(names) != len(set(names)):
            errors.append("duplicate milestone identifiers")
        current = value(root, "Milestone")
        final = value(root, "Final status")
        # Template references use a plain ID or a Markdown link beginning with it.
        current_id = re.match(r"\[?([A-Za-z]+\d+)\b", current)
        selected = current_id.group(1) if current_id else ""
        if require_ready and final != "complete" and selected not in names:
            errors.append("selected readiness check requires a resolvable current Milestone ID")
        for name, block in milestones:
            status = value(block, "Status")
            local = readiness_errors(block, MILESTONE_LABELS,
                                     force=require_ready and name == selected,
                                     executing=status in EXECUTING_STATES)
            if len(values(block, "Status")) != 1:
                local.append("milestone requires exactly one Status")
            if status == "complete":
                local.extend(evidence_errors(block, "Exit result", "Exit evidence"))
                if UNCHECKED_RE.search(block):
                    local.append("completed milestone has unchecked criteria")
            if final == "complete" and status in UNFINISHED_STATES:
                local.append("project is complete while milestone is unfinished")
            errors.extend(f"{name}: {error}" for error in local)
        if len(values(root, "Final status")) > 1:
            errors.append("duplicate Final status")
        if final == "complete":
            errors.extend(evidence_errors(root, "Completion result", "Completion evidence"))
            errors.extend(require_section(root, "Evidence index"))
        workstream_states = table_states(root, "Workstreams and dependencies")
        for state in workstream_states:
            if state not in BASE_STATES:
                errors.append(f"invalid workstream status '{state}'")
            elif final == "complete" and state in UNFINISHED_STATES:
                errors.append(f"project is complete while workstream is {state}")
    elif require_ready:
        errors.append("--require-ready supports only Task Plans, Outcome Plans, and Project Roadmaps")
    return errors


def validate(path: Path, *, require_ready: bool = False) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read UTF-8 Markdown: {exc}"]

    text = without_examples(text)
    kind = artifact_kind(text)
    if kind == "custom":
        return ["unsupported artifact type; use a supported template or review its custom schema separately"]
    errors.extend(contract_errors(text, kind, require_ready))
    placeholders = PLACEHOLDER_RE.findall(text)
    if placeholders:
        preview = ", ".join(placeholders[:3])
        suffix = "..." if len(placeholders) > 3 else ""
        errors.append(f"unresolved placeholders: {preview}{suffix}")

    for label in ("Verification result", "Exit result", "Completion result"):
        for result in values(text, label):
            if result not in {"pass", "fail", "blocked", "pending"}:
                errors.append(f"invalid {label} '{result}'")

    for match in STATE_RE.finditer(text):
        label = match.group("label")
        state = clean(match.group("value"))
        if label == "Generation status":
            allowed = GENERATION_STATES
        elif kind == "alignment" and label == "Status":
            allowed = ALIGNMENT_STATES
        elif label == "Final status":
            allowed = TERMINAL_STATES
        else:
            allowed = BASE_STATES
        if state == "partial":
            errors.append("'partial' is not a valid terminal state")
        elif state not in allowed:
            errors.append(f"invalid {label.lower()} '{state}'")

    if kind == "audit":
        missing = missing_labels(text, AUDIT_CONTRACT_LABELS)
        if missing:
            errors.append("missing audit contract fields: " + ", ".join(missing))

        exit_rows, exit_table_errors = validated_table_rows(
            text,
            "Exit-criteria assessment",
            EXIT_CRITERIA_HEADER,
        )
        errors.extend(exit_table_errors)
        if not exit_rows:
            errors.append("exit-criteria assessment has no data rows")
        exit_verdicts = [row[-1] for row in exit_rows]
        invalid_verdicts = sorted(set(exit_verdicts) - EXIT_VERDICTS)
        if invalid_verdicts:
            errors.append("invalid exit verdict: " + ", ".join(invalid_verdicts))

        finding_rows, finding_table_errors = validated_table_rows(
            text,
            "Findings",
            FINDINGS_HEADER,
        )
        errors.extend(finding_table_errors)
        invalid_severities = sorted(
            {row[0] for row in finding_rows if row[0] not in FINDING_SEVERITIES}
        )
        if invalid_severities:
            errors.append("invalid finding severity: " + ", ".join(invalid_severities))
        invalid_statuses = sorted(
            {row[-1] for row in finding_rows if row[-1] not in FINDING_STATUSES}
        )
        if invalid_statuses:
            errors.append("invalid finding status: " + ", ".join(invalid_statuses))
        unresolved_blockers = [
            row
            for row in finding_rows
            if row[0] == "blocker" and row[-1] == "unresolved"
        ]

        decision_match = DECISION_RE.search(text)
        if not decision_match:
            errors.append("missing gate decision")
        else:
            decision = clean(decision_match.group("value"))
            if decision not in AUDIT_DECISIONS:
                errors.append(f"invalid gate decision '{decision}'")
            else:
                failed_exit_verdicts = sorted(
                    set(exit_verdicts) & {"fail", "blocked"}
                )
                if decision == "advance" and unresolved_blockers:
                    errors.append("gate advances while unresolved blockers remain")
                if decision == "advance" and failed_exit_verdicts:
                    errors.append(
                        "gate advances while failed or blocked evidence remains: "
                        + ", ".join(failed_exit_verdicts)
                    )
                if decision == "do_not_advance" and not unresolved_blockers:
                    errors.append("gate does not advance without an unresolved blocker")

    if FINAL_COMPLETE_RE.search(text):
        if UNCHECKED_RE.search(text):
            errors.append("final status is complete while unchecked criteria remain")
        # Only current state/result columns contradict closeout. Requirements and
        # historical evidence may legitimately describe failures or pending cases.
        for heading in ("Current state", "Closeout", "Project closeout", "Blockers and required decisions", "Verification evidence"):
            contradictions = sorted(set(table_states(text, heading)) & CONTRADICTORY_CELLS)
            if contradictions:
                errors.append(f"completion contradicts {heading}: " + ", ".join(contradictions))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check materialized orchestrate-projects Markdown artifacts."
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--require-ready", action="store_true",
                        help="require a ready selected contract, not only a valid draft")
    args = parser.parse_args()

    failed = False
    for path in args.files:
        errors = validate(path, require_ready=args.require_ready)
        if errors:
            failed = True
            print(f"[FAIL] {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[VALID] {path} (structure only; verify evidence, readiness, and authority separately)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
