# AlexOS

AlexOS is a portable framework for engineering agents. It provides a shared
operating discipline without depending on a programming language, repository
layout, agent product, or tool-specific instruction format.

The framework is deliberately smaller than the environment in which it runs.
Project rules, user preferences, runtime observations, and technology-specific
procedures remain owned by their source systems or by external extensions.

## Framework map

| Layer | Responsibility | Load when |
| --- | --- | --- |
| [`kernel/`](kernel/README.md) | Universal reasoning and execution semantics | Every engineering task |
| [`policies/`](policies/README.md) | Cross-cutting constraints | The policy governs the task or artifact |
| [`knowledge/`](knowledge/README.md) | Durable explanatory models | The model helps interpret the system |
| [`heuristics/`](heuristics/README.md) | Conditional rules of thumb | Its applicability conditions are present |
| [`playbooks/`](playbooks/README.md) | Procedures for recurring tasks | The task matches the playbook trigger |
| [`docs/`](docs/README.md) | Governance of AlexOS itself | Maintaining or integrating the framework |

These layers are not equal kinds of authority. The kernel defines universal
behavior, policies constrain it, knowledge explains, heuristics suggest, and
playbooks sequence work. The distinction is defined in
[`docs/architecture.md`](docs/architecture.md).

## Loading

An integration should load the kernel first, then select only the policies,
knowledge, heuristics, and playbook relevant to the current task. Loading the
entire repository defeats the architecture: irrelevant guidance consumes
attention and makes conflicts harder to detect.

AlexOS does not own the active repository's instructions or facts. Integrations
compose those external inputs with the framework under the conflict rules in
[`kernel/authority-and-conflicts.md`](kernel/authority-and-conflicts.md).

## Portability

Canonical documents use Markdown, relative links, and model-neutral language.
An adapter may translate the loading model into a product's native mechanism,
but it must not fork or redefine framework semantics. Technology-specific
guidance belongs in an extension rather than the core.

The framework boundary and extension rules are documented in
[`docs/architecture.md`](docs/architecture.md#external-composition).

## Maintaining AlexOS

Repository changes follow:

- [`docs/content-model.md`](docs/content-model.md) for document responsibilities,
  naming, and references;
- [`docs/information-lifecycle.md`](docs/information-lifecycle.md) for facts,
  runtime context, history, and promotion;
- [`docs/evolution.md`](docs/evolution.md) for structural changes, migration,
  and deprecation.

Run `python tools/validate.py` before proposing a change. The validator checks
objective repository contracts; engineering quality still requires review.
