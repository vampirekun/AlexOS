# Evolution and governance

AlexOS evolves like a software system: changes should preserve clear contracts,
avoid parallel implementations, and remain reversible when uncertainty is high.

## Change classes

### Content correction

A correction improves accuracy without changing a document's responsibility or
consumer expectations. Update the canonical document and verify its links.

### Content addition

An addition introduces a new rule, procedure, fact, or explanation. Classify it
with [`architecture.md`](architecture.md#placement-decision), confirm it is not
a duplicate, then add it to the local README.

### Structural change

A structural change creates, removes, renames, or redefines a directory or
moves responsibilities between layers. Document the rationale and migration
map in the change review. Update the root map, affected READMEs, and every
inbound link in the same change.

### Integration change

An integration change affects how a particular agent consumes AlexOS. It must
remain thin and must not alter canonical semantics for the convenience of one
vendor. If the integration exposes a missing universal concept, change the
canonical layer first and adapt it second.

## Adding a directory

Create a directory only when at least one substantive document needs a boundary
that the existing architecture cannot express cleanly. The same change must
include:

- the real document that justified the directory;
- a README satisfying [`content-model.md`](content-model.md#directory-readmes);
- a link from the parent README;
- a statement of dependency direction and selection rules;
- migration of any content that already belongs there.

Empty directories and speculative category trees are architectural debt, not
future-proofing.

## Moving or splitting content

First identify the canonical meaning being preserved. Search for inbound links
and duplicated phrases, move or split the content, then repair references.
Where external consumers may use an old path, an adapter or release process may
provide a compatibility redirect; do not retain a second editable copy.

When a mixed document is split, each resulting document must be independently
coherent and the former relationships must become explicit links.

## Deprecation and removal

Material should be deprecated when consumers need transition time; otherwise
remove obsolete guidance as part of the replacing change. A deprecated document
must state:

- that it is deprecated;
- what supersedes it;
- why it changed;
- when it can be removed, if known.

Do not create an archive directory for content that version control already
preserves. Keep historical material in the active tree only when it remains
operationally relevant.

## Review checklist

- Does the change keep universal behavior independent of vendors and projects?
- Is each idea owned by one layer?
- Are directory boundaries and local indexes still accurate?
- Can an agent load only the relevant subset?
- Are all new documents substantive and free of placeholders?
- Are relative links valid?
- Did the change remove obsolete paths and duplicated sources of truth?
- Would the architecture still be understandable in a plain file browser?

For document-level rules, also apply the quality gate in
[`content-model.md`](content-model.md#quality-gate).
