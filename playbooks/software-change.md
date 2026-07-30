# Software change

Use this playbook when modifying an existing repository and no more specialized
playbook fully covers the task. The outcome is a focused, convention-compatible
change with proportionate verification.

## Procedure

1. Establish the requested behavior and scope.
2. Search for existing implementations, abstractions, and repository guidance.
3. Read the relevant code and tests before selecting an approach.
4. Identify compatibility requirements and unrelated work that must remain
   untouched.
5. Prefer extending an existing pattern over introducing a parallel one.
6. Keep the implementation localized while completing the full behavior.
7. Run the most relevant tests, static checks, or targeted manual validation.
8. Explain why the change was needed, what changed, risks, and validation.

For a defect with an unknown cause, use
[`debugging.md`](debugging.md). All steps remain subject to the kernel
[`operating-principles.md`](../kernel/operating-principles.md).
