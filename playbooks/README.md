# Playbooks

Playbooks are repeatable operating procedures for recognizable engineering
situations. Each one specializes the kernel's operating cycle toward a concrete,
verifiable outcome.

## Why this directory exists

Task instructions need to evolve faster than universal principles and often
apply only when a trigger is present. Keeping them here allows an agent to load
one relevant workflow without absorbing every procedure in AlexOS.

## What belongs here

- Procedures with a clear trigger and intended outcome.
- Investigation sequences and decision checkpoints.
- Required inputs, evidence, and verification for a recurring task.
- Links to policies that constrain the procedure.
- Branches for common conditions within the same class of task.

Current playbooks:

- [`software-change.md`](software-change.md) — general repository change work.
- [`architecture-assessment.md`](architecture-assessment.md) — evaluating an
  existing architecture before recommending change.
- [`code-review.md`](code-review.md) — reviewing a change for actionable risk.
- [`debugging.md`](debugging.md) — finding and correcting a root cause.
- [`migration.md`](migration.md) — moving behavior between architectures while
  preserving intended semantics.
- [`kubernetes-troubleshooting.md`](kubernetes-troubleshooting.md) — diagnosing
  Kubernetes workloads using cluster evidence.
- [`documentation.md`](documentation.md) — producing maintainable technical
  documentation.
- [`jira-update.md`](jira-update.md) — communicating work state in a ticket.
- [`scrum-update.md`](scrum-update.md) — communicating daily progress and
  blockers.

## What must never belong here

- A universal behavioral rule with no task trigger; use
  [`../kernel/`](../kernel/README.md) or
  [`../policies/`](../policies/README.md).
- Facts about a particular person, machine, organization, or repository; use
  [`../context/`](../context/README.md).
- A phrase intended to manipulate a specific model.
- A one-line request such as "write good documentation." A playbook must contain
  enough procedure and verification to guide work.
- Complete sample outputs; future reviewed samples belong in `examples/` under
  the criteria in
  [`../docs/architecture.md`](../docs/architecture.md#optional-extension-directories).

## Organization and growth

Select playbooks by trigger, not by technology mentioned in the request. Use
the general software-change playbook as a base when no specialized playbook
fits. A specialized playbook should link to shared policies and knowledge
rather than repeat them.

When this list becomes crowded, introduce stable namespaces such as
`delivery/`, `diagnostics/`, or `communication/`. Do not create a hierarchy
based only on the current number of files. Every child directory must have a
README and must be indexed here according to
[`../docs/content-model.md`](../docs/content-model.md#directory-readmes).
