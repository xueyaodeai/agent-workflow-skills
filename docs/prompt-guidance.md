# Prompt design basis

Reviewed on 2026-10-16. These sources explain the design choices; they are not extra runtime instructions or evidence that the changes have been benchmarked on a model.

| Official source | Applied here |
|---|---|
| [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Keep task-specific details in the relevant skill or existing artifact. Prefer explicit outcomes and completion boundaries to longer procedural scripts; keep descriptions focused. |
| [Anthropic: Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | State intent, context, constraints, and expected results clearly. Explain why a constraint matters and use concrete, testable behavior rather than vague quality claims. |
| [Anthropic: Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Distinguish a model finishing a turn from completing the authorized task. Retain verification and stop conditions, and test model/host-specific behavior rather than assuming one global configuration. |

The **four-point execution-readiness requirement** comes from the repository owner's request: why, what, shortest/best paths and selection, and complete acceptance, including for direct assignments. It is this project's policy, not a claim that either provider mandates this exact template.

The same acceptance applies to the shortest and best paths; they can coincide. Unknown consequential decisions block only dependent work, while settled tasks continue without repeated approval. Each independently installed skill retains the small guard needed at its boundary. More detailed planning remains in `plan-outcomes`; this is deliberate semantic overlap for standalone installation, not a dependency on a shared file that the installer may omit.

Model IDs, effort settings, and tool adapters belong to the runtime or evaluation configuration, not the common policy. The sources are living pages: reassess the relevant advice against observed behavior when models or hosts change. See [the evaluation protocol](../tests/README.md) for the distinction between structural validation and measured behavior.
