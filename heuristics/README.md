# Engineering heuristics

This directory contains reusable but fallible rules of thumb. Heuristics direct
attention when full analysis would be disproportionate; they never settle a
factual question or create a mandatory rule.

## Contains

- [`change-surface-as-risk-signal.md`](change-surface-as-risk-signal.md) —
  affected boundaries as an early risk indicator.
- [`earliest-incorrect-state.md`](earliest-incorrect-state.md) — the first
  observable divergence as a debugging lead.

## Excludes

- Universal behavior and mandatory constraints.
- Descriptive models that do not recommend a shortcut.
- Project-specific conventions and one-off observations.
- Procedures with an ordered method and completion criteria.
- Claims expressed as certainty when their evidence is probabilistic.

## Selection and lifecycle

Load a heuristic only when its applicability conditions match the current
problem. Test it against current evidence. Repeated usefulness is not enough to
promote a heuristic into policy; policy requires a normative reason. Narrow or
retire a heuristic when counterexamples invalidate its stated scope.
