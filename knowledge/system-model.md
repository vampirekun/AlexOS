# A model for understanding software systems

An unfamiliar codebase cannot be understood reliably from its directory tree or
framework choices alone. A useful system model explains responsibility,
boundaries, state, behavior over time, and operational consequences.

## Responsibilities and boundaries

Start by identifying what each component owns and what it deliberately leaves
to others. Boundaries appear in public APIs, message schemas, storage formats,
processes, deployment units, trust zones, and team ownership. Some are enforced
by tooling; others exist only as conventions.

The benefit of mapping responsibilities is causal clarity: when behavior is
wrong, the investigation can ask which component owned the decision. The
failure mode is treating the current module layout as intentional architecture.
Directories show placement, not necessarily responsibility.

## Contracts and consumers

A contract is any observable behavior on which another party relies. It
includes types and endpoints, but also error behavior, timing, ordering,
configuration, telemetry names, migration sequences, and operational
procedures.

Contracts should be identified from consumers as well as providers. Provider
code reveals what is produced; consumers reveal what is assumed. Tests are
valuable evidence, but they may encode only a subset of the actual contract.

## State and invariants

State includes persisted data, caches, in-memory objects, queues, external
systems, and derived views. For each important state transition, determine:

- the invariant that should remain true;
- who is allowed to perform the transition;
- whether the operation is atomic, retryable, or idempotent;
- how partial failure is represented and recovered;
- how concurrent observers perceive the transition.

Many defects arise because a local operation is correct while the system-level
invariant is violated between operations.

## Data and control flow

Trace representative requests or events from origin to effect. Data flow shows
how information is transformed; control flow shows who decides what happens
next. They diverge in event-driven, asynchronous, and policy-based systems.

A static call graph is insufficient when runtime configuration, dependency
injection, queues, schedulers, or retries determine behavior. Use code,
configuration, deployment state, and telemetry together.

## Time and concurrency

Time is part of system behavior whenever there are caches, retries, leases,
timeouts, scheduled work, eventual consistency, or multiple writers. Ask what
can happen before, during, and after a transition, and what another actor can
observe at each point.

Ignoring time produces designs that work in a single synchronous trace and fail
under real interleaving. Over-modeling every possible interleaving is also
costly; focus on shared state, irreversible effects, and externally visible
ordering.

## Failure and recovery

Model failures at boundaries: invalid input, dependency failure, partial
completion, resource exhaustion, lost responses, duplicate work, and operator
error. Then identify detection, containment, retry, rollback, reconciliation,
and escalation behavior.

The absence of a documented recovery path does not mean a failure cannot occur.
It means recovery is accidental.

## Operational view

A system is not understood until its behavior can be observed and operated.
Identify deployment topology, health signals, logs, metrics, traces, alerts,
feature controls, and rollback mechanisms. Determine whether those signals
distinguish causes or merely report symptoms.

This model is used by the
[`architecture assessment`](../playbooks/architecture-assessment.md),
[`debugging`](../playbooks/debugging.md), and
[`software change`](../playbooks/software-change.md) playbooks.
