# Migration

Use this playbook when moving existing behavior, data, or integration between
architectures. The outcome is preserved intended behavior with explicit
compatibility and verification.

## Procedure

1. Establish the source behavior, consumers, contracts, and invariants.
2. Map architectural differences between source and destination.
3. Separate behavior that must be preserved from accidental implementation
   details.
4. Identify compatibility, sequencing, data, deployment, and rollback risks.
5. Design incremental stages when a single cutover would make failures hard to
   isolate or reverse.
6. Implement translation at explicit boundaries rather than leaking both
   architectures throughout the system.
7. Verify behavioral equivalence, important failure paths, and operational
   observability.
8. Remove obsolete paths after consumers have transitioned; do not leave two
   canonical implementations.

Use [`architecture-assessment.md`](architecture-assessment.md) when the target
architecture itself has not yet been justified.
