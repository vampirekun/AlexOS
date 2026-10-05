# Information lifecycle

This document defines where information lives, how long it remains valid, and
what review is required before its scope expands. It does not define content
layer responsibilities; those belong to
[`architecture.md`](architecture.md).

## Framework content

Kernel rules, policies, knowledge, heuristics, playbooks, and governance are
versioned in AlexOS because they are intended for reuse. Their durability does
not make them equally authoritative: policies constrain action, knowledge
describes, and heuristics remain conditional.

Framework inclusion requires evidence that the material generalizes beyond one
user, project, language, tool, or incident.

## External facts

Facts about a user, organization, environment, or project remain outside core.
They may live in an independently versioned overlay, the active repository, or
another authoritative system.

Current evidence outranks a stored descriptive fact. When they conflict, the
consumer should investigate and correct the canonical source rather than append
a contradictory copy.

## Runtime context

Runtime context supports an active task: observations, logs, hypotheses,
working diffs, incident state, and intermediate results. It remains in the
agent session or the system that owns the work.

At task completion, runtime context is:

1. discarded when it has no durable value;
2. retained by its owning issue, repository, or incident system;
3. recorded as an external fact;
4. distilled into a lesson or local heuristic;
5. proposed for framework inclusion after broader evidence.

Automatic retention is prohibited. Runtime state decays quickly and may contain
sensitive or misleading information.

## History and decisions

Project history and decisions belong to the project that produced them. AlexOS
retains its own architectural history through version control and, when
necessary, decision records under `docs/`.

A historical event is evidence, not a universal rule. Its transferable result
may become a heuristic, knowledge improvement, playbook change, or policy only
after its scope and counterexamples are reviewed.

## Heuristic promotion

A local heuristic remains with its source until evidence shows recurring value
across unrelated situations. Promotion into [`../heuristics/`](../heuristics/README.md)
requires:

- a clear applicability condition;
- a mechanism explaining why it tends to work;
- known counterexamples or failure modes;
- value beyond one project or technology.

A heuristic becomes policy only when following it is required across the
policy's stated scope. Frequent usefulness alone is insufficient.

## Correction and retirement

Correct factual errors at the canonical source. Narrow guidance whose scope was
overstated. Remove obsolete framework content when consumers do not need a
transition; use the deprecation process in [`evolution.md`](evolution.md) when
they do.

Secrets, access material, unnecessary personal information, and raw operational
artifacts are never eligible for promotion into AlexOS.

## Common failures

- **Scope leakage:** a local preference becomes a framework rule.
- **Stale authority:** an old summary overrides current evidence.
- **Anecdotal policy:** one successful intervention becomes mandatory guidance.
- **Memory inflation:** retaining every observation obscures useful knowledge.
- **Lost provenance:** copied facts can no longer be checked or corrected.
