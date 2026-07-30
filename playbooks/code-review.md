# Code review

This playbook evaluates a proposed change for defects and material engineering
risk.

## Use when

Use it for a diff, commit, or pull request whose behavior and consequences must
be reviewed before acceptance.

## Inputs

- The change and its stated intent.
- Relevant surrounding code, tests, contracts, and repository rules.
- Available validation evidence.

## Method

1. Establish the intended behavior and inspect the complete relevant diff.
2. Read surrounding code when the diff does not establish ownership or
   contracts.
3. Check correctness, failure behavior, security boundaries, data integrity,
   compatibility, and operational effects.
4. Use the [`change risk model`](../knowledge/change-risk-model.md) to direct
   attention beyond diff size.
5. Evaluate tests against changed behavior and important failure paths.
6. Report actionable findings with location, consequence, and correction.
7. Separate blocking defects from optional improvements and describe residual
   risk under the [`communication policy`](../policies/communication.md).

## Completion evidence

- Every reported finding is supported by the reviewed change and context.
- Severity follows consequence rather than reviewer preference.
- Important unreviewed or unexecuted areas are explicit.
- Absence of findings is not represented as proof of correctness.

## Failure modes

- Reviewing style while missing behavior.
- Reporting hypothetical problems without a reachable failure path.
- Demanding a redesign unrelated to the change.
- Treating passing tests as complete behavioral proof.
