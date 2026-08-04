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
CONTRADICTORY_CELLS = {"fail", "blocked", "open", "pending", "no"}

PLACEHOLDER_RE = re.compile(r"<[^<>\n]+>")
STATE_RE = re.compile(
    r"^- (?P<label>Status|Final status|Generation status):\s*`?(?P<value>[a-z_]+)`?\s*$",
    re.MULTILINE,
)
FINAL_COMPLETE_RE = re.compile(r"^- Final status:\s*`?complete`?\s*$", re.MULTILINE)
UNCHECKED_RE = re.compile(r"^- \[ \] ", re.MULTILINE)


def artifact_kind(text: str) -> str:
    first_line = text.splitlines()[0] if text else ""
    if first_line.startswith("# Task Plan:"):
        return "task"
    if first_line.startswith("# Project Roadmap:"):
        return "roadmap"
    if first_line.startswith("# Next-Round Roadmap Alignment Notes:"):
        return "alignment"
    return "custom"


def markdown_cells(text: str) -> list[str]:
    cells: list[str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells.extend(cell.strip().strip("`").lower() for cell in line.strip("|").split("|"))
    return cells


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
