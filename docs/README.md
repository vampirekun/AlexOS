# AlexOS documentation

This directory explains how AlexOS itself is designed, maintained, and evolved.
It is the repository's control plane: the other directories contain operating
knowledge, while `docs/` defines how that knowledge is organized.

## Why this directory exists

Without explicit repository governance, a large Markdown system drifts into
duplicated rules, ambiguous folders, broken navigation, and vendor-specific
instructions. This directory makes architectural decisions discoverable and
gives maintainers a consistent way to extend AlexOS.

## What belongs here

- Repository architecture and dependency rules.
- The content model, naming rules, and document contracts.
- Evolution, deprecation, and migration procedures for AlexOS.
- Contributor guidance that applies to this repository as a product.
- Architecture decisions about the knowledge system itself.

Current documents:

- [`architecture.md`](architecture.md) defines layers, dependencies, placement,
  loading, and optional extension points.
- [`content-model.md`](content-model.md) defines how documents and directory
  indexes should be written and named.
- [`evolution.md`](evolution.md) defines how to change the system without
  accumulating incompatible conventions.

## What must never belong here

- General software-engineering guidance; use [`../kernel/`](../kernel/README.md),
  [`../policies/`](../policies/README.md), or
  [`../playbooks/`](../playbooks/README.md).
- Facts about Alex, a workstation, customer, or codebase; use
  [`../context/`](../context/README.md).
- Agent-vendor setup instructions. When real integrations exist, place them in
  an `adapters/` directory governed by
  [`architecture.md`](architecture.md#optional-extension-directories).
- Generated indexes or reports mixed with hand-maintained architecture. If
  generation is introduced, give its outputs a clearly documented boundary.

## Maintenance rules

Documents here may describe all repository layers, but they must not silently
override them. A structural rule that changes how agents operate must be
reflected in the affected directory README and linked from the root
[`README.md`](../README.md). Architectural changes follow
[`evolution.md`](evolution.md), including link validation and migration of
existing content.
