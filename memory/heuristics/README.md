# Engineering heuristics

This directory contains conditional rules of thumb learned from recurring
engineering work. Heuristics guide attention and sequencing when complete
analysis would be disproportionate; they do not replace evidence or policy.

## Why this directory exists

Experienced engineering relies on patterns that are useful more often than
not, but not universally true. Encoding those patterns as kernel principles
makes them dangerously absolute. Keeping heuristics separate preserves their
value while requiring the agent to test applicability.

## What belongs here

- Reusable observations supported by more than one situation.
- Shortcuts for prioritizing investigation or reducing change risk.
- A stated rationale, applicability conditions, counterexamples, and failure
  modes.
- Links to historical lessons or external evidence that motivated the rule.

Current heuristics:

- [`change-surface-as-risk-signal.md`](change-surface-as-risk-signal.md) uses
  affected boundaries as an early risk indicator.
- [`earliest-incorrect-state.md`](earliest-incorrect-state.md) guides debugging
  toward the first divergence rather than the loudest symptom.

## What must never belong here

- A mandatory invariant; use [`../../kernel/`](../../kernel/README.md) or
  [`../../policies/`](../../policies/README.md).
- A one-off observation or temporary hypothesis.
- Project-specific behavior; use [`../projects/`](../projects/README.md).
- Anecdotes without a transferable rule and stated limitations.
- Rules expressed as certainty when they are probabilistic.

## Use and evolution

Load a heuristic only when its applicability conditions resemble the current
problem. Validate it against current evidence. A heuristic consistently shown
to be universal may be proposed as a policy; one repeatedly contradicted should
be narrowed or retired. The promotion standard is defined in
[`../../docs/memory-model.md`](../../docs/memory-model.md).
