# Template Modules and Document Validation

Read this reference when creating or closing a template-shaped artifact, or when choosing an optional module. The level routing in `SKILL.md` already names the core module for each level.

## Modules

- `assets/task-plan.md`: Level 1 core resumable task plan.
- `assets/task-plan-coordination-addon.md`: cross-task decisions, blockers, and downstream handoff; add only when needed.
- `assets/task-plan-git-addon.md`: Git isolation and delivery identity; use with the Git reference.
- `assets/task-plan-integration-addon.md`: reviewed and integration SHA chain; use only for initiative integration.
- `assets/project-roadmap.md`: core multi-task roadmap.
- `assets/project-roadmap-transition-addon.md`: predecessor and carryover mapping for a successor roadmap.
- `assets/milestone-audit.md`: Level 3 milestone gate.
- `assets/promotion-gate.md`: initiative integration to primary-branch promotion.
- `assets/roadmap-alignment-notes.md`: durable successor-roadmap discussion ledger.

Adapt modules to repository conventions and omit irrelevant sections instead of filling them with `not applicable`. Do not rename an established project artifact merely to match this skill.

## Document validator

For template-shaped roadmaps, milestone audits, and alignment notes, run `python3 scripts/validate_project_docs.py <files...>` once before closeout. Task and Outcome Plans are also supported, but Level 1 does not require this validator by default. Use `--require-ready` when checking a selected task or a roadmap's current execution scope before starting it. Drafts may remain explicitly not ready; a structural pass never grants execution authority.

The validator checks supported fields, scoped milestone contracts, state values, placeholders, and completion contradictions. Unknown formats are reported as unsupported, not passing; standalone add-ons and promotion gates require their own evidence review. It does not establish the truth or accessibility of cited evidence, semantic completeness, or host-enforced permission. Preserve custom repository formats and review their equivalent contracts rather than renaming them to satisfy this script.
