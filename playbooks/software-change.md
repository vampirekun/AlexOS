# Software change

This playbook governs a bounded modification to an existing software
repository.

## Use when

Use it when the requested outcome requires changing code, configuration, tests,
or repository-owned documentation and no narrower playbook owns the primary
task.

## Inputs

- The requested outcome and authorized scope.
- Repository instructions and current working-tree state.
- Relevant implementation, tests, contracts, and validation commands.

## Method

1. Define the behavior that must change and the behavior that must remain.
2. Inspect repository guidance, related implementations, tests, and history.
3. Identify affected contracts and boundaries using the
   [`system model`](../knowledge/system-model.md).
4. Compare a local correction, an extension of an existing abstraction, and
   any credible alternative.
5. Implement the smallest complete change while preserving unrelated work.
6. Verify changed behavior and plausible regressions in proportion to the
   [`change risk model`](../knowledge/change-risk-model.md).
7. Communicate the outcome under the
   [`communication policy`](../policies/communication.md).

If the cause of incorrect behavior is unknown, use
[`debugging.md`](debugging.md) before selecting the implementation.

## Completion evidence

- The requested behavior is demonstrated.
- Relevant checks pass or their absence is reported.
- Compatibility, migration, or operational consequences are addressed.
- The working tree contains no unintended changes.

## Failure modes

- Editing before understanding the responsible boundary.
- Treating few changed lines as low risk.
- Reusing an abstraction that does not own the responsibility.
- Completing the implementation while omitting necessary tests or migration.
