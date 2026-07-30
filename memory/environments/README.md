# Environment memory

This directory records stable, non-secret facts about environments in which
engineering work is performed or software is executed.

## Why this directory exists

Commands, paths, available tools, and platform behavior vary by environment.
Separating those facts prevents playbooks from assuming one workstation or
deployment target and allows an agent to select only the environment relevant
to the current run.

## What belongs here

- Operating system, shell, and path conventions.
- Available development, build, container, or cluster tools.
- Stable workspace layout and non-secret configuration conventions.
- Constraints that affect how generic playbooks are executed.

Current environment:

- [`local-development.md`](local-development.md) describes Alex's usual local
  development workstation.

## What must never belong here

- Passwords, tokens, certificates, private endpoints, or other secrets.
- A project's architecture or business vocabulary; use
  [`../projects/`](../projects/README.md).
- Generic instructions for using a tool; use a playbook or future `knowledge/`
  directory.
- Short-lived runtime state, incident notes, pod names, or current version
  numbers unless the document is explicitly maintained as a versioned
  compatibility constraint.
- Universal assumptions embedded merely because one environment is common.

## Selection and maintenance

Name documents by the environment's role, not an incidental hostname, unless
the host itself is the stable subject. State facts rather than prescribing
universal behavior. Playbooks may use these facts to choose platform-appropriate
commands while retaining vendor-neutral outcomes.

Load only environments active in the current task. Confirm material facts before
relying on them because installed tools and platform configuration drift.
Corrections follow the memory lifecycle in
[`../../docs/memory-model.md`](../../docs/memory-model.md).
