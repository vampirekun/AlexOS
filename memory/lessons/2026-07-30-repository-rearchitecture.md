# Repository rearchitecture: from prompt files to operating layers

On 2026-07-30, AlexOS was restructured from a flat collection of root-level
profiles, prompt fragments, and examples into a layered engineering knowledge
system.

## Initial condition

The repository grouped task instructions under `PROMPTS/`, kept user and
project facts at the root, and contained several one-line examples. Universal
principles, communication preferences, project facts, and procedures had no
formal dependency or authority boundaries.

That structure was usable at small scale but would fail as the corpus grew.
Folder names described file intent rather than system responsibility, prompt
fragments had no verification contract, and user-specific facts could be
mistaken for universal behavior.

## Change

The material was separated into a small kernel, cross-cutting policies, task
playbooks, memory, and system documentation. Incomplete examples were removed.
Directory READMEs became boundary contracts and curated indexes. Later
refinement introduced explicit permanent, project, temporary, historical, and
heuristic memory classes.

## Lesson

Knowledge systems scale through ownership and lifecycle boundaries, not through
more folders alone. Classification must express why information exists, how
authoritative it is, and when it should be loaded or retired.

The derived architecture is defined in
[`../../docs/architecture.md`](../../docs/architecture.md), and the memory
classification is defined in
[`../../docs/memory-model.md`](../../docs/memory-model.md).

## Limits

This lesson supports responsibility-based organization; it does not prove that
the current taxonomy is final. New boundaries should still be justified by real
content and maintenance pressure rather than analogy to an operating system.
