# Kernel

The kernel is the smallest stable core of AlexOS. It defines the universal
mission, epistemic discipline, decision framework, and execution lifecycle of
an engineering agent. Its meaning is independent of model vendor, user,
project, and technology stack.

## Why this directory exists

Agents need a consistent operating model before they can choose a specialized
procedure or apply local context. Keeping that model small and isolated makes
it portable and prevents frequently changing project facts from destabilizing
the whole system.

## What belongs here

- The engineering mission shared by every AlexOS run.
- Invariant reasoning and change principles.
- Rules for evidence, uncertainty, and intellectual honesty.
- A framework for proportionate engineering decisions.
- The top-level operating cycle and authority model.

Current kernel:

- [`mission.md`](mission.md) defines the role and desired engineering outcome.
- [`operating-principles.md`](operating-principles.md) defines durable
  decision-making constraints.
- [`epistemic-discipline.md`](epistemic-discipline.md) defines how claims,
  hypotheses, and uncertainty are handled.
- [`decision-framework.md`](decision-framework.md) defines how options, risk,
  reversibility, and tradeoffs are evaluated.
- [`operating-cycle.md`](operating-cycle.md) defines the lifecycle from
  understanding through explanation.
- [`authority-and-conflicts.md`](authority-and-conflicts.md) defines how AlexOS
  interacts with current instructions, repository rules, evidence, and host
  constraints.

All kernel documents are intended to be loaded together. If that becomes
expensive, the kernel has grown too large and should be decomposed into policies
or playbooks.

## What must never belong here

- Personal preferences or names; use
  [`../memory/user/`](../memory/user/README.md).
- Machine, organization, or repository facts; use
  [`../memory/`](../memory/README.md).
- Step-by-step procedures for a particular task; use
  [`../playbooks/`](../playbooks/README.md).
- Detailed quality rules that constrain a class of work; use
  [`../policies/`](../policies/README.md).
- Explanatory engineering models; use
  [`../knowledge/`](../knowledge/README.md).
- Vendor syntax, model-specific prompting tricks, or integration files.

## Change discipline

Kernel changes have the widest possible blast radius. An addition must apply
across projects, tasks, and agents, must not fit a policy or knowledge document,
and must provide a capability that an existing principle cannot express.

Kernel brevity is a safety property. A large kernel consumes attention on every
task and makes conflicts more likely. Changes follow the structural review
process in [`../docs/evolution.md`](../docs/evolution.md).
