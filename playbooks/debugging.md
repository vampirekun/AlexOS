# Debugging

This playbook investigates unexpected behavior until a supported cause and
proportionate response are established.

## Use when

Use it when observed behavior differs from expected behavior and the
responsible cause is not yet known.

## Inputs

- A precise expected and observed behavior.
- Reproduction conditions or evidence explaining why reproduction is
  unavailable.
- Relevant code, configuration, runtime state, logs, traces, and recent
  changes.

## Method

1. Reproduce or bound the failure.
2. Build the relevant causal path using the
   [`system model`](../knowledge/system-model.md).
3. Separate observations, inferences, assumptions, and hypotheses under the
   [`epistemic discipline`](../kernel/epistemic-discipline.md).
4. Form competing falsifiable hypotheses.
5. Trace toward the
   [`earliest incorrect state`](../heuristics/earliest-incorrect-state.md)
   while accounting for instrumentation gaps.
6. Run tests that distinguish the hypotheses.
7. Correct the cause at the responsible boundary or identify a containment
   measure explicitly as temporary.
8. Reproduce the original path and check a relevant regression boundary.

## Completion evidence

- The explanation accounts for the material observations.
- Evidence distinguishes the selected cause from credible alternatives.
- The original failure no longer occurs under equivalent conditions.
- Remaining uncertainty and untested conditions are reported.

## Failure modes

- Editing code to test an unfalsifiable guess.
- Stopping at the loudest downstream symptom.
- Calling a plausible hypothesis a root cause.
- Expanding the fix beyond the boundary supported by evidence.
