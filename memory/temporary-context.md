# Temporary context

Temporary context is information needed for the current task but not yet
appropriate for durable memory. Examples include a failing pod name, an
uncommitted diff, a working hypothesis, a ticket's current status, or an
intermediate test result.

## Why temporary context is separate

Most engineering observations decay quickly. Persisting them without review
creates confident but stale memory: yesterday's deployment state becomes
tomorrow's false premise. Temporary context remains attached to the active run,
issue, or incident until its value and durability are established.

## Handling rules

The agent should keep temporary context close to the work that produced it,
retain its provenance, and distinguish observations from hypotheses. Before the
task ends, temporary information has four possible outcomes:

1. Discard it because it has no value beyond the completed work.
2. Leave it in the owning system, such as an issue, pull request, incident
   record, or repository documentation.
3. Promote a stable project fact into [`projects/`](projects/README.md).
4. Distill an evidence-backed general heuristic or historical lesson into
   [`heuristics/`](heuristics/README.md) or [`lessons/`](lessons/README.md).

Promotion requires review. A repeated observation is not automatically a
general rule, and a successful workaround is not automatically a sound
practice.

## What must not be retained

Secrets and unnecessary personal data must not be stored at any lifecycle.
Speculation must not be promoted as fact. Large logs, source snapshots, and
generated artifacts should remain in systems designed to own them; durable
memory should capture the relevant conclusion and provenance.

The full classification and promotion model is defined in
[`../docs/memory-model.md`](../docs/memory-model.md).
