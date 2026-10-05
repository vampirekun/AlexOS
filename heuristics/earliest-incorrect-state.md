# Earliest incorrect state

When failures propagate through a system, the earliest observable divergence
from expected state is usually more diagnostic than the final error.

## Applicability

Use this heuristic when logs or symptoms show a chain of consequences. Trace
inputs, transformations, state transitions, and dependencies backward until
observed and expected behavior first differ. Then investigate what produced
that divergence.

For example, a timeout may be the visible symptom, but the useful divergence
could be an earlier cache miss, an invalid routing decision, or a lock that was
never released.

## Benefit

Working from the earliest incorrect state reduces symptom patches and makes
competing hypotheses easier to falsify. It often identifies the boundary where
an invariant was first violated.

## Failure modes and limits

The earliest *observable* divergence is not necessarily the root cause.
Instrumentation gaps, nondeterminism, clock skew, and distributed causality can
hide earlier events. Tracing backward indefinitely can also waste time when a
bounded mitigation is operationally urgent.

Use the heuristic to select the next observation, not to declare a cause. The
earliest visible divergence can still be downstream from the responsible event.
