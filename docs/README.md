# System documentation

This directory governs AlexOS as a repository. It is read when maintaining,
reviewing, or integrating the framework, not as part of an ordinary engineering
task.

## Contains

- [`architecture.md`](architecture.md) — content layers, dependency direction,
  external composition, loading, and scale.
- [`content-model.md`](content-model.md) — document responsibilities, naming,
  linking, and local indexes.
- [`information-lifecycle.md`](information-lifecycle.md) — treatment of facts,
  runtime context, history, decisions, and promotion.
- [`evolution.md`](evolution.md) — change classes, migrations, deprecation, and
  review.

## Excludes

- Engineering behavior and normative engineering constraints.
- Explanatory models, heuristics, and task procedures.
- User, project, environment, or runtime information.
- Product-specific adapter instructions.

## Maintenance

Each document in this directory owns one governance concern. Structural changes
must update the architecture first, then migrate affected content and links in
the same change. Historical copies are unnecessary because version control owns
repository history.
