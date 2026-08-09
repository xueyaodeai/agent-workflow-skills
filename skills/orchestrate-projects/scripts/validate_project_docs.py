#!/usr/bin/env python3
"""Validate materialized orchestrate-projects Markdown artifacts."""

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

PLACEHOLDER_RE = re.compile(r"<[^<>\n]+>")
STATE_RE = re.compile(
    r"^- (?P<label>Status|Final status|Generation status):\s*`?(?P<value>[a-z_]+)`?\s*$",
    re.MULTILINE,
)
FINAL_COMPLETE_RE = re.compile(r"^- Final status:\s*`?complete`?\s*$", re.MULTILINE)
DECISION_RE = re.compile(
    r"^- Decision:\s*`?(?P<value>[a-z_]+)`?\s*$",
    re.MULTILINE,
)
UNCHECKED_RE = re.compile(r"^- \[ \] ", re.MULTILINE)


def artifact_kind(text: str) -> str:
    first_line = text.splitlines()[0] if text else ""
    if first_line.startswith("# Task Plan:"):
        return "task"
    if first_line.startswith("# Project Roadmap:"):
        return "roadmap"
    if first_line.startswith("# Next-Round Roadmap Alignment Notes:"):
        return "alignment"
    if first_line.startswith("# Milestone Audit:"):
        return "audit"
    return "custom"


def markdown_cells(text: str) -> list[str]:
    cells: list[str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells.extend(cell.strip().strip("`").lower() for cell in line.strip("|").split("|"))
    return cells


def missing_labels(text: str, labels: set[str]) -> list[str]:
    return sorted(
        label
        for label in labels
        if not re.search(rf"^- {re.escape(label)}:\s*\S", text, re.MULTILINE)
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


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read UTF-8 Markdown: {exc}"]

    kind = artifact_kind(text)
    placeholders = PLACEHOLDER_RE.findall(text)
    if placeholders:
        preview = ", ".join(placeholders[:3])
        suffix = "..." if len(placeholders) > 3 else ""
        errors.append(f"unresolved placeholders: {preview}{suffix}")

    for match in STATE_RE.finditer(text):
        label = match.group("label")
        value = match.group("value")
        if label == "Generation status":
            allowed = GENERATION_STATES
        elif kind == "alignment" and label == "Status":
            allowed = ALIGNMENT_STATES
        elif label == "Final status":
            allowed = TERMINAL_STATES
        else:
            allowed = BASE_STATES
        if value == "partial":
            errors.append("'partial' is not a valid terminal state")
        elif value not in allowed:
            errors.append(f"invalid {label.lower()} '{value}'")

    if kind == "roadmap":
        missing = missing_labels(text, ROADMAP_CONTRACT_LABELS)
        if missing:
            errors.append(
                "missing frozen milestone contract fields: " + ", ".join(missing)
            )

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
            decision = decision_match.group("value")
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
        contradictions = sorted(set(markdown_cells(text)) & CONTRADICTORY_CELLS)
        if contradictions:
            errors.append(
                "final status is complete while contradictory table states remain: "
                + ", ".join(contradictions)
            )
        if kind == "task" and not (
            "## Verification evidence" in text or re.search(r"^- Verification:\s*\S", text, re.MULTILINE)
        ):
            errors.append("completed task has no verification evidence")
        if kind == "roadmap" and "## Evidence index" not in text:
            errors.append("completed roadmap has no evidence index")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check materialized orchestrate-projects Markdown artifacts."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    failed = False
    for path in args.files:
        errors = validate(path)
        if errors:
            failed = True
            print(f"[FAIL] {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[PASS] {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
