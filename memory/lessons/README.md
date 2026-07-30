# Historical lessons

This directory records durable lessons derived from real AlexOS or engineering
events. A lesson preserves enough history to explain why a conclusion should
influence future work without treating the event itself as a universal rule.

## Why this directory exists

History prevents repeated mistakes only when the causal reasoning remains
available. A bare rule loses its evidence; a raw incident timeline contains too
much transient detail. Historical lessons bridge the two by recording context,
outcome, interpretation, and limits.

## What belongs here

- A real event with identifiable context and outcome.
- Evidence that supports the lesson.
- The decision or practice changed as a result.
- Limits on generalization and links to any derived heuristic or policy.

Current lesson:

- [`2026-07-30-repository-rearchitecture.md`](2026-07-30-repository-rearchitecture.md)
  records why AlexOS moved from a prompt-oriented layout to responsibility-based
  operating layers.

## What must never belong here

- Active incident notes or unresolved hypotheses.
- A generic recommendation without a historical event.
- Blame, performance evaluation, or unnecessary personal information.
- Raw logs and artifacts better retained in their owning systems.
- A policy disguised as history; derived requirements belong in
  [`../../policies/`](../../policies/README.md).

## Lifecycle

Lessons are append-only in historical facts but editable in interpretation as
new evidence appears. Material corrections should explain what changed. A
lesson may produce a heuristic, policy, or playbook improvement, but the
derived document must link back rather than copy the event narrative.
