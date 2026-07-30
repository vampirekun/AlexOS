# Engineering playbooks

Playbooks are procedures selected by a recognizable task. They compose lower
layers into a method that produces verifiable evidence.

## Contains

- [`software-change.md`](software-change.md) — general changes to an existing
  software repository.
- [`architecture-assessment.md`](architecture-assessment.md) — evaluation of a
  structural change.
- [`code-review.md`](code-review.md) — risk-focused review of a proposed
  change.
- [`debugging.md`](debugging.md) — causal investigation and correction of
  unexpected behavior.
- [`migration.md`](migration.md) — controlled movement between implementations
  or contracts.
- [`documentation.md`](documentation.md) — creation or revision of durable
  technical documentation.
- [`progress-reporting.md`](progress-reporting.md) — concise communication of
  work state, direction, and impediments.

## Excludes

- Universal principles and cross-cutting policy.
- Explanatory material with no task sequence.
- Conditional shortcuts without a complete procedure.
- Technology-, vendor-, organization-, or project-specific workflows.
- Output templates without reasoning or completion criteria.

## Contract

Every playbook defines:

- when it applies;
- inputs needed to begin;
- a method with decision points;
- evidence that establishes completion;
- common failure modes.

Select one primary playbook by task outcome. Supporting playbooks should be
used only when the work crosses a real task boundary; chaining playbooks by
default recreates an oversized universal workflow.
