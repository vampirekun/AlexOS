# Project memory

This directory holds durable, project-scoped facts shared by a product,
repository family, or bounded engineering domain.

## Why this directory exists

Project-specific vocabulary, compatibility constraints, and common
infrastructure can materially affect an engineering decision but should not
leak into universal playbooks. Project overlays keep those facts close together
and loadable only when the corresponding work is active.

## What belongs here

- The repositories or components that make up a project family.
- Stable domain vocabulary and architectural constraints.
- Project-specific compatibility, rollout, testing, or ownership conventions.
- Links to authoritative project documentation.
- References to relevant generic playbooks and policies.

Current project:

- [`m5.md`](m5.md) describes the M5 repository family and its common engineering
  context.

## What must never belong here

- Source code or a mirror of a project's own documentation.
- Credentials, private access details, or environment secrets.
- Universal engineering procedures copied into each project.
- Active ticket state, transient incident notes, or speculation about current
  production behavior.
- Personal preferences unrelated to the project.

## Selection, scope, and organization

Use one document for a small project context. Split into a child directory only
when multiple substantive documents have distinct owners or update cycles, such
as architecture, delivery, and domain vocabulary. The parent project README
then becomes a curated index.

When local facts change how a procedure is executed, link to the canonical
playbook and document only the project-specific input or constraint.

Load only the active project's memory. Current repository evidence remains more
authoritative than a stored summary. When a fact becomes stale, correct it at
its canonical memory record rather than adding a contradictory note elsewhere.
