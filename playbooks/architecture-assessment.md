# Architecture assessment

This playbook evaluates whether a software structure should be preserved,
extended, or replaced.

## Use when

Use it before a change that moves responsibilities, alters major dependencies,
introduces a new system boundary, or requires a migration between
architectures.

## Inputs

- The current system and its operational context.
- The force motivating change.
- Known constraints, consumers, and compatibility requirements.

## Method

1. Map responsibilities, contracts, dependencies, state, data flow, time, and
   failure behavior using the [`system model`](../knowledge/system-model.md).
2. Separate intentional constraints from accidental implementation details.
3. State the concrete force for change: failure, scale, maintenance cost, new
   capability, or ownership.
4. Compare preserving, extending, and replacing the design.
5. Evaluate consequence, uncertainty, exposure, and recoverability with the
   [`change risk model`](../knowledge/change-risk-model.md).
6. Select the smallest structural change that addresses the force.
7. Define migration, compatibility, verification, observability, and rollback.

## Completion evidence

- Current and proposed responsibilities are explicit.
- The recommendation traces to observed forces rather than preference.
- Rejected alternatives and decisive tradeoffs are recorded.
- Transition and recovery are credible for the assessed risk.

## Failure modes

- Inferring architecture from directories alone.
- Redesigning because another pattern is fashionable.
- Treating current structure as intentional without evidence.
- Recommending an end state without a viable transition.
