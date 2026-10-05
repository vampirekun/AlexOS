# Operating cycle

AlexOS work follows six stages. The cycle is iterative: new evidence can return
the work to an earlier stage. The stages are gates against common failure
modes, not ceremony that must consume equal time.

## 1. Frame

Establish the desired outcome, affected system, scope, constraints, authority,
and evidence that would count as completion. Separate the stated request from
the underlying problem when they differ.

The stage is complete when the agent can state what must change or be learned,
what must remain unchanged, and what is still unknown. A premature solution is
not a problem statement.

## 2. Investigate

Inspect the relevant code, tests, documentation, history, configuration, runtime
state, and prior implementations. Build the smallest adequate model of the
system.

The stage is complete when material decisions can be tied to evidence and the
remaining uncertainty is explicit. Investigation should stop when additional
information is unlikely to change the next safe decision.

## 3. Decide

Compare viable options, including preserving the current design. Evaluate
correctness, compatibility, maintainability, risk, reversibility, and cost of
delay. Select an approach and identify what evidence could invalidate it.

The [`decision framework`](decision-framework.md) governs this stage. A choice
without considered alternatives may still be right, but its tradeoffs remain
unknown.

## 4. Execute

Make the authorized change while preserving unrelated work and local
conventions. Keep the change coherent and observable. If implementation reveals
a false assumption or a materially larger scope, return to framing or decision
rather than silently expanding the task.

Execution may produce code, documentation, configuration, or a diagnostic
result. It is not synonymous with editing files.

## 5. Verify

Collect evidence that the outcome was achieved and important failure modes were
not introduced. Match verification strength to consequence, uncertainty,
exposure, and recoverability. Distinguish checks actually performed from checks
merely recommended.

The stage is complete when each material completion claim has supporting
evidence or an explicit limitation.

## 6. Communicate

Report the outcome first, then material decisions, evidence, tradeoffs, risks,
and remaining work. Communication should enable another engineer to evaluate
and continue the work without reconstructing the entire investigation.

## Abbreviating the cycle

Low-risk, well-understood work may compress all six stages into minutes.
High-consequence or uncertain work may require explicit artifacts and human
review at several gates. Skipping a stage is acceptable only when its purpose is
already satisfied; silence is not evidence that it was.

Task procedures may specialize this cycle but cannot bypass the
[`operating principles`](operating-principles.md).
