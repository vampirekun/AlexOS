# Migration

This playbook moves behavior, data, or consumers between implementations while
controlling compatibility and recovery risk.

## Use when

Use it when source and destination must coexist, consumers must transition, or
state must cross a boundary before the old path can be removed.

## Inputs

- Source behavior, contracts, consumers, and invariants.
- Destination behavior and architectural differences.
- Sequencing, compatibility, data, deployment, and rollback constraints.

## Method

1. Establish the behavior that must be preserved and the evidence that defines
   it.
2. Map source and destination with the
   [`system model`](../knowledge/system-model.md).
3. Separate contractual behavior from accidental implementation detail.
4. Evaluate irreversible effects and mixed-version exposure using the
   [`change risk model`](../knowledge/change-risk-model.md).
5. Divide the transition into independently verifiable stages when a single
   cutover would be difficult to diagnose or reverse.
6. Keep translation at explicit boundaries rather than spreading both models
   throughout the system.
7. Verify equivalence, failure handling, observability, and recovery at each
   stage.
8. Remove the obsolete path after consumers have transitioned.

## Completion evidence

- Required behavior is preserved or approved differences are explicit.
- Every stage has entry, verification, and recovery conditions.
- No consumer depends on the retired path.
- Obsolete compatibility code and operational procedures are removed.

## Failure modes

- Migrating implementation details without identifying contracts.
- Assuming code rollback reverses data or external effects.
- Leaving two canonical implementations indefinitely.
- Designing the destination without an executable transition.
