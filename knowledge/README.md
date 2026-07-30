# Engineering knowledge

This directory contains reusable explanatory models for understanding software
systems. Knowledge describes; it does not require an action or prescribe a task
sequence.

## Contains

- [`system-model.md`](system-model.md) — responsibilities, contracts, state,
  time, failure, and operational behavior.
- [`change-risk-model.md`](change-risk-model.md) — consequence, uncertainty,
  exposure, and recoverability.

## Excludes

- Mandatory constraints.
- Conditional rules of thumb.
- Task procedures.
- Language, framework, vendor, user, or project reference material.
- Facts whose validity depends on current runtime state.

## Dependency rule

Knowledge may refer to other knowledge documents. It does not depend on the
policies, heuristics, or playbooks that consume it. Consumers link to the model
they use, preserving one-way dependency direction.

Add a knowledge document only when its model is reusable and materially
improves reasoning. A collection of facts without a stable explanatory model
does not justify framework inclusion.
