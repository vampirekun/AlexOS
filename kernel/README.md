# Kernel

The kernel defines the universal operating semantics of AlexOS. It is the only
content layer intended to load for every engineering task.

## Contains

- [`mission.md`](mission.md) — the outcome and responsibilities of engineering
  agency.
- [`operating-principles.md`](operating-principles.md) — universal constraints
  on investigation and change.
- [`epistemic-discipline.md`](epistemic-discipline.md) — claims, evidence,
  uncertainty, and falsification.
- [`decision-framework.md`](decision-framework.md) — proportionate engineering
  decisions under constraints.
- [`operating-cycle.md`](operating-cycle.md) — the lifecycle from framing
  through communication.
- [`authority-and-conflicts.md`](authority-and-conflicts.md) — interaction among
  host constraints, current instructions, repository rules, and evidence.

## Excludes

- Cross-cutting standards that apply only to some work.
- Descriptive engineering models.
- Conditional heuristics.
- Task-specific procedures.
- User, project, technology, or agent product information.

## Dependency rule

Kernel documents may depend only on other kernel documents. This keeps the
always-loaded core complete and prevents optional layers from becoming hidden
prerequisites.

Kernel brevity is a safety property. An addition must apply across projects,
languages, tasks, and agent products, and must not fit an existing kernel
responsibility.
