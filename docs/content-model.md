# Content model

This document defines the contract for files and indexes in AlexOS. Layer
semantics belong to [`architecture.md`](architecture.md); change procedures
belong to [`evolution.md`](evolution.md).

## One responsibility

Every document must have one responsibility expressible in one sentence. Its
path and title should make that responsibility predictable. A document that
mixes a rule, explanatory model, task procedure, and installation fact must be
split because those parts have different owners and lifecycles.

Documents must remain understandable when reached directly. They may depend on
explicitly linked lower layers but cannot assume that the entire repository was
loaded.

## Required structure

Every Markdown document has:

- exactly one level-one heading;
- an opening paragraph defining purpose or scope;
- headings that expose its major concepts;
- relative links for internal references;
- no empty sections, unresolved placeholders, or implied missing content.

Layer-specific requirements:

- Policies define scope, rules, rationale, tradeoffs, and failure modes.
- Knowledge documents define a model, its use, and its limits.
- Heuristics define applicability, benefit, and counterexamples.
- Playbooks define when to use them, inputs, method, completion evidence, and
  failure modes.

Metadata is not required until a real consumer needs it. Decorative metadata
becomes another stale source of truth.

## Directory READMEs

Every existing directory has a `README.md` that provides:

- the directory's single responsibility;
- a catalog of current contents;
- explicit exclusions;
- selection or maintenance rules.

The README summarizes boundaries from
[`architecture.md`](architecture.md); it does not redefine them. Every
non-README document in a directory must appear in that directory's catalog.

## Naming

- Use lowercase `kebab-case.md` for documents.
- Reserve `README.md` for directory indexes.
- Name policies and knowledge by subject.
- Name heuristics by the signal or inference they express.
- Name playbooks by the task they perform.
- Use sequence prefixes only when chronology is part of the document's
  identity.
- Keep vendor and technology names out of core filenames.

## References

Link from a consumer to its dependency. A playbook may link to a policy or
knowledge model; a knowledge model should not link back to every playbook that
uses it.

Use links rather than copied rules. A short orientation summary is acceptable
when it cannot be edited to change the referenced rule's meaning.

External sources may establish provenance, but a core operating rule cannot
depend on an unstable external page for its interpretation.

## Examples

An example must be complete enough to demonstrate a decision or outcome.
Sentence fragments and ellipses are placeholders, not examples. Examples
should be introduced only when they clarify material that remains ambiguous
after the rule or procedure is stated.

## Review questions

- Does the path match the document's responsibility?
- Does another document own the same rule or explanation?
- Does every internal link follow the allowed dependency direction?
- Is the material reusable across projects and agent products?
- Does the local README list the document?
- Could the document be removed without making an unrelated layer incomplete?
