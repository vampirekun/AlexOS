# Code review

Use this playbook to evaluate a proposed change. The outcome is a prioritized
set of actionable findings grounded in the changed behavior and repository
context.

## Procedure

1. Understand the change's intent and inspect the complete relevant diff.
2. Read surrounding code, tests, and local conventions where the diff alone is
   ambiguous.
3. Check correctness, failure behavior, security, compatibility, and data
   integrity.
4. Check maintainability, unnecessary complexity, duplication, and consistency
   with existing abstractions.
5. Verify that tests cover meaningful changed behavior and important failure
   paths.
6. Report only findings the author can act on; include location, consequence,
   and a practical correction.
7. Distinguish blocking defects from optional improvements and summarize
   residual risk.

Absence of a finding is not proof that the code was executed. Apply the
[`communication policy`](../policies/communication.md) when writing the review.
