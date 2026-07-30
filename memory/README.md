# Memory

Memory contains knowledge learned about users, environments, projects, prior
outcomes, and recurring engineering patterns. It gives future work continuity
without allowing volatile observations to become permanent truth by accident.

## Why this directory exists

Memory has a different lifecycle from the operating system itself. The kernel
defines how engineering work is performed; memory records what has been learned
about a subject. Mixing them causes local preferences to masquerade as
universal principles and stale project facts to influence unrelated work.

The memory model therefore separates information by authority, scope, and
retention. The governing classification is defined in
[`../docs/memory-model.md`](../docs/memory-model.md).

## What belongs here

- Confirmed user preferences relevant to engineering collaboration.
- Stable facts about development or execution environments.
- Project-specific vocabulary, constraints, and repository relationships.
- Engineering heuristics whose applicability remains conditional.
- Historical lessons grounded in a real event and supported by evidence.
- The durable protocol for handling temporary run context.

Current namespaces and documents:

- [`user/`](user/README.md) contains Alex's confirmed collaboration profile.
- [`environments/`](environments/README.md) contains environment-specific facts.
- [`projects/`](projects/README.md) contains project and repository-family
  knowledge.
- [`heuristics/`](heuristics/README.md) contains conditional rules of thumb.
- [`lessons/`](lessons/README.md) contains evidence-backed historical lessons.
- [`temporary-context.md`](temporary-context.md) defines how short-lived context
  is handled without committing it as durable memory.

## What must never belong here

- Universal behavior or decision rules; use
  [`../kernel/`](../kernel/README.md).
- Normative quality requirements; use
  [`../policies/`](../policies/README.md).
- Generic task procedures; use [`../playbooks/`](../playbooks/README.md).
- Durable explanatory engineering models; use
  [`../knowledge/`](../knowledge/README.md).
- Secrets, credentials, private keys, access tokens, or unnecessary personal
  information.
- Unverified guesses, transient incident state, or conclusions without
  provenance.

## Authority and selection

Memory informs a decision; it does not outrank evidence from the system
currently being examined. Load only the user, environment, project, heuristic,
or lesson relevant to the active task. When memory conflicts with current
evidence, investigate the discrepancy and update or retire the stale memory.

A more specific memory record may refine a broader one, but no memory can
silently weaken the kernel or a policy. An explicit current instruction can
authorize an exception where the host environment permits it; the exception
does not automatically become permanent memory.

## Maintenance

Every record must identify its subject and distinguish fact from inference.
Project facts should link to their authoritative source when one exists.
Heuristics must state their limits. Lessons must retain enough event context to
explain how the conclusion was derived.

Create new namespaces only when substantive records require a distinct
lifecycle. Follow the admission process in
[`../docs/evolution.md`](../docs/evolution.md#adding-a-directory).
