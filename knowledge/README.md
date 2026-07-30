# Engineering knowledge

This directory contains durable explanatory models used to reason about
software systems. Knowledge explains how to see a problem; policies constrain
decisions, and playbooks prescribe a procedure.

## Why this directory exists

An engineering operating system needs more than rules. Agents also need stable
conceptual models for understanding systems, changes, and failures. Embedding
those models inside individual playbooks duplicates reasoning and makes it
difficult to improve the model independently.

## What belongs here

- Technology-independent models of software behavior and change.
- Definitions and distinctions reused across policies or playbooks.
- Explanations of tradeoffs, failure modes, and related concepts.
- Durable technical knowledge expected to remain useful across projects.

Current knowledge:

- [`system-model.md`](system-model.md) defines the dimensions used to understand
  an unfamiliar software system.
- [`change-risk-model.md`](change-risk-model.md) defines how consequence,
  uncertainty, exposure, and recoverability shape engineering risk.

## What must never belong here

- Mandatory requirements; use [`../policies/`](../policies/README.md).
- Ordered task procedures; use [`../playbooks/`](../playbooks/README.md).
- User, environment, or project facts; use [`../memory/`](../memory/README.md).
- Conditional rules learned from experience; use
  [`../memory/heuristics/`](../memory/heuristics/README.md).
- Vendor documentation copied for convenience.
- Facts likely to decay without a clear ownership and review mechanism.

## Organization and use

Load knowledge documents when their model is needed for the current decision;
they are not startup instructions. As the corpus grows, group documents by
stable engineering concern such as systems, change, reliability, or delivery.
Each child directory must have a boundary README and must be indexed here.

Knowledge is descriptive, not authoritative merely because it is durable.
Current system evidence can reveal that a model does not fit. Improvements
follow the document quality rules in
[`../docs/content-model.md`](../docs/content-model.md).
