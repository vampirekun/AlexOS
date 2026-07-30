# AlexOS

AlexOS is a portable operating system for AI-assisted software engineering. It
separates durable engineering judgment from task procedures, local context, and
tool integrations so that the same body of knowledge can be used by Codex,
Claude Code, Cursor, Gemini CLI, or a future agent without rewriting its core.

This repository is the canonical source. Agent-specific files may eventually
load or adapt AlexOS, but they must not become competing sources of truth.

## Start here

An agent or maintainer should read only what the current task requires:

1. Read [`kernel/README.md`](kernel/README.md) to understand the invariant
   mission, principles, and operating cycle.
2. Read [`policies/README.md`](policies/README.md) and select policies that
   constrain the work.
3. Read [`context/README.md`](context/README.md) and load only the relevant
   person, environment, or project context.
4. Select a procedure from [`playbooks/README.md`](playbooks/README.md).
5. Use [`docs/README.md`](docs/README.md) when maintaining AlexOS itself.

This is progressive disclosure by design. Loading every document would waste
context, blur priorities, and become increasingly harmful as the repository
grows.

## Repository map

| Directory | Responsibility | Stability |
| --- | --- | --- |
| [`kernel/`](kernel/README.md) | Universal identity, reasoning principles, and execution lifecycle | Highest |
| [`policies/`](policies/README.md) | Cross-cutting rules and quality constraints | High |
| [`playbooks/`](playbooks/README.md) | Triggered procedures for recurring engineering work | Medium |
| [`context/`](context/README.md) | Replaceable facts about people, environments, and projects | Variable |
| [`docs/`](docs/README.md) | Architecture and maintenance rules for AlexOS itself | High |

The repository intentionally does not create empty top-level categories. New
categories such as `knowledge/`, `adapters/`, `examples/`, `schemas/`, or
`tools/` should appear only with their first production-quality artifact and an
accompanying README. Their intended roles and admission criteria are documented
in [`docs/architecture.md`](docs/architecture.md).

## Architectural rules

- Organize by responsibility, not file format or model vendor.
- Keep the kernel small; most additions belong elsewhere.
- Store facts separately from instructions so facts can change without
  rewriting behavior.
- Write a playbook around a triggering situation and a verifiable outcome, not
  around the wording of a prompt.
- Keep one canonical home for each rule. Link to it instead of copying it.
- Prefer relative Markdown links and plain text formats.
- Treat directory READMEs as local interfaces: they define boundaries and
  provide curated navigation.
- Add structure in response to real content, not anticipated content.

## How to change AlexOS

Before adding or moving a document, follow the placement decision in
[`docs/architecture.md`](docs/architecture.md) and the authoring contract in
[`docs/content-model.md`](docs/content-model.md). For broader structural
changes, use the evolution process in [`docs/evolution.md`](docs/evolution.md).

AlexOS is not a single prompt, and this README is not a prompt template. It is
the stable entry point into a versionable engineering knowledge system.
