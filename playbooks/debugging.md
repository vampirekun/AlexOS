# Debugging

Use this playbook when observed behavior differs from expected behavior and the
cause is not yet established. The outcome is a verified explanation and the
smallest corrective change that addresses the root cause.

## Procedure

1. Define expected and observed behavior precisely.
2. Reproduce the failure, or explain why reproduction is unavailable.
3. Gather logs, state, traces, inputs, timing, and recent-change evidence.
4. Form hypotheses that could explain all relevant observations.
5. Test hypotheses and eliminate alternatives before editing code.
6. Trace the failure to the earliest incorrect state or violated assumption.
7. Implement the minimal root-cause correction.
8. Verify the original failure, nearby behavior, and a relevant regression path.
9. Report evidence, cause, change, validation, and remaining uncertainty.

If the evidence points to Kubernetes infrastructure, continue with
[`kubernetes-troubleshooting.md`](kubernetes-troubleshooting.md). Do not present
a plausible hypothesis as a confirmed cause.
