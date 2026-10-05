# Engineering policies

Policies define mandatory constraints shared by more than one task. They refine
the kernel without prescribing a complete workflow.

## Contains

- [`communication.md`](communication.md) — requirements for truthful,
  decision-useful engineering communication.

## Excludes

- Universal behavior already owned by the kernel.
- Explanatory models and conditional heuristics.
- Ordered task procedures.
- User preferences, project exceptions, and product-specific conventions.

## Selection and dependency

Load a policy when its scope covers the task or artifact. Policies depend on the
kernel and may make its principles more specific, but they cannot weaken them.
Task procedures depend on policies, never the reverse.

A new policy requires a cross-cutting normative reason. Repeated advice does not
become policy merely because it appears in several documents; first determine
whether those copies should instead depend on one model or heuristic.
