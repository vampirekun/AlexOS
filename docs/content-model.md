# Content model

This document defines the contract for AlexOS Markdown. It keeps a large
knowledge system consistent without forcing every document into a rigid
template.

## Document responsibilities

Every document must have one primary responsibility that can be stated in a
sentence. Its title and path should make that responsibility predictable. If a
document mixes universal principles, project facts, and a task sequence, split
it according to the layer model in [`architecture.md`](architecture.md).

A production document should provide enough context to be useful when reached
through a direct link. It should not assume that an agent loaded the entire
repository.

## Required properties

Every non-README Markdown document must have:

- one level-one title;
- an opening paragraph that states purpose or scope;
- explicit links for dependencies that affect interpretation;
- headings that expose its structure to both people and agents;
- no unresolved placeholders, ellipses standing in for content, or empty
  sections.

Playbooks additionally define a trigger, intended outcome, prerequisites or
inputs when relevant, a procedure, and verification. Policies state their scope
and the constraints they impose. Context documents identify the subject whose
facts they describe.

YAML front matter is not currently required. It should be introduced only when
real tooling consumes it; decorative metadata quickly becomes stale. If that
time comes, define one schema in `schemas/` and migrate the corpus
systematically.

## Directory READMEs

Every directory has a README once the directory exists. It must explain:

- why the directory exists;
- what belongs there;
- what must never belong there;
- how its contents are organized and selected;
- links to its current documents and relevant neighboring layers.

A README is an interface, not a dumping ground. Operational rules belong in
their canonical documents and are summarized, not duplicated, in indexes.

## Naming

- Use lowercase `kebab-case.md` for documents.
- Use `README.md` for directory indexes.
- Prefer descriptive nouns for policies and context, and task names for
  playbooks.
- Avoid ordering prefixes such as `01-` unless sequence is intrinsic and
  permanent.
- Do not put model, vendor, or editor names in canonical filenames unless the
  file is inside a vendor adapter.
- Choose paths for long-term meaning, not the current team structure.

## Linking and references

Use relative links so a clone remains self-contained. Link to the canonical
document instead of copying paragraphs. Use descriptive link text rather than
"here." Link to a directory's README when referring to the directory as a
concept.

External links are appropriate for authoritative source material, but AlexOS
must not depend on a volatile external page for a core operating rule. Record
the locally relevant conclusion and cite the source where provenance matters.

## Duplication and composition

Some repetition for orientation is acceptable; repeated rules are not. A
document may summarize another layer in one sentence and link to it. If two
documents could independently be edited to change the same rule, the design has
created competing sources of truth.

Prefer composition:

- a playbook links to applicable policies;
- context supplies project-specific commands or constraints;
- knowledge explains a technology;
- an adapter points the agent toward the canonical entry path.

## Quality gate

Before accepting a document:

1. Classify it using the placement decision in
   [`architecture.md`](architecture.md#placement-decision).
2. Confirm it contains substantive, current material.
3. Search for an existing canonical home and extend or link instead of
   duplicating.
4. Add it to its directory README.
5. Validate relative links and heading targets.
6. Check that moving or removing it does not strand inbound references.
7. Review whether its scope leaks vendor-specific or project-specific details
   into a stable layer.

Deprecated material follows [`evolution.md`](evolution.md); it is not left
unmarked beside active guidance.
