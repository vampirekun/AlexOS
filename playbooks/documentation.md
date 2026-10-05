# Documentation

This playbook creates or revises durable technical documentation.

## Use when

Use it when a reader needs a maintained explanation, procedure, decision, or
reference rather than temporary task communication.

## Inputs

- Intended audience and decision or task.
- Authoritative evidence for the documented behavior.
- Existing documentation ownership and expected lifetime.

## Method

1. Define the reader, purpose, scope, and maintenance owner.
2. Verify behavior against implementation, configuration, tests, or an
   authoritative source.
3. Select one canonical location and identify related documents.
4. Organize around reader decisions rather than discovery order.
5. Explain rationale, tradeoffs, and failure modes where they prevent misuse.
6. Add an example only when it resolves ambiguity and can remain correct.
7. Validate terminology, commands, assumptions, and links.
8. Apply the [`communication policy`](../policies/communication.md).

When the target is AlexOS, also apply the
[`content model`](../docs/content-model.md).

## Completion evidence

- The intended reader can complete the task or evaluate the decision.
- Material claims have a current source.
- The document has one owner and does not duplicate another canonical rule.
- Links and examples are valid.

## Failure modes

- Documenting intended behavior as if it were observed behavior.
- Copying facts from an authoritative source and losing provenance.
- Adding a second canonical explanation for convenience.
- Writing a discovery transcript instead of a reader-oriented document.
