# Evolution

This document governs changes to AlexOS. It owns migration and deprecation
procedures; document structure and layer boundaries are defined elsewhere.

## Change classes

A **correction** fixes accuracy without changing responsibility or consumer
expectations. Update the canonical document and validate references.

An **addition** introduces a reusable rule, model, heuristic, or procedure.
Classify it with [`architecture.md`](architecture.md#placement-decision), prove
that existing content does not own it, and add it to the local catalog.

A **structural change** moves responsibility, changes dependency direction, or
creates or removes a directory. It requires a migration map and a complete
reference update in the same change.

An **integration change** affects an external overlay, extension, or adapter.
It cannot modify core semantics solely for one product's convenience.

## Adding structure

Create a directory only when substantive content needs a lifecycle or selection
boundary that existing directories cannot express. The change must include real
content, a README, a parent-catalog entry, and migration of existing material
that already belongs there.

File count alone does not justify hierarchy. Empty directories and speculative
category trees increase navigation cost without improving ownership.

## Moving or splitting content

Identify the canonical responsibility before moving a document. Search inbound
references, move or split the content, update indexes and links, then remove the
old editable copy.

Compatibility redirects are appropriate only for released paths with known
external consumers. Version control is sufficient history for internal drafts.

## Deprecation

Deprecate rather than remove when consumers need transition time. A deprecated
document states:

- its replacement;
- why the responsibility moved or changed;
- the transition required;
- the removal condition, when known.

Do not create an archive directory for material already preserved by version
control.

## Review sequence

1. Verify the framework boundary and dependency direction.
2. Verify one canonical responsibility per document.
3. Verify local catalogs and relative links.
4. Run `python tools/validate.py`.
5. Review semantic quality manually; structural validation cannot establish
   correctness.
6. Confirm that removed content remains owned by another system or is genuinely
   obsolete.
