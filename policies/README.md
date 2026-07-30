# Policies

Policies define cross-cutting constraints and quality bars that apply across
multiple workflows. They refine the kernel without turning it into a catalog of
special cases.

## Why this directory exists

A mature engineering system needs rules that are broader than one playbook but
more specific than universal operating principles. Giving those rules a
separate layer makes them reusable, independently reviewable, and selectively
loadable according to the work's risks.

## What belongs here

- Communication, security, testing, compatibility, or documentation standards
  that constrain several playbooks.
- Decision rules with a clearly stated scope.
- Quality gates that can be checked across different artifact types.
- Exceptions that are universal to a domain and not tied to one project.

Current policy:

- [`communication.md`](communication.md) governs engineering communication
  across reports, tickets, reviews, and documentation.

As policies grow, group them by stable concern such as `code-quality/`,
`delivery/`, or `security/`, not by agent vendor or current team. Create a child
directory only under the admission rules in
[`../docs/evolution.md`](../docs/evolution.md#adding-a-directory).

## What must never belong here

- The universal mission or lifecycle; use
  [`../kernel/`](../kernel/README.md).
- Ordered procedures triggered by a task; use
  [`../playbooks/`](../playbooks/README.md).
- Personal preferences or project exceptions; use
  [`../context/`](../context/README.md).
- Explanatory technology references; introduce `knowledge/` under
  [`../docs/architecture.md`](../docs/architecture.md#optional-extension-directories).
- Rules copied from another policy. Select one canonical owner and link to it.

## Selection and precedence

Load policies based on the artifact, risk, and playbook involved. Playbooks
should link to their mandatory policies. Context can request stricter behavior
but cannot silently weaken a policy. The kernel remains authoritative when a
policy conflicts with an operating principle.
