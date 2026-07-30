# Change surface as a risk signal

The number and kind of boundaries affected by a change are often a better early
risk signal than the number of edited lines.

## Applicability

Use this heuristic while scoping a change or choosing verification. Count
meaningful boundaries: public contracts, persisted data, concurrency, security
trust zones, deployment units, external dependencies, and independently owned
components.

A ten-line protocol change can carry more risk than a thousand-line internal
refactor because the former crosses a compatibility boundary. Conversely, a
large mechanical rename inside a closed module may have broad textual impact
but limited behavioral risk.

## Benefit

The heuristic directs design and testing effort toward consequences rather than
diff size. It also exposes apparently small changes that require migration,
coordination, observability, or rollback planning.

## Failure modes and limits

Boundary count is not a risk score. A local arithmetic error can still be
critical, and a well-managed boundary change may be safe. Familiarity can also
hide boundaries: configuration formats, metrics, and operational procedures are
contracts even when a type system cannot see them.

Use the heuristic to ask better questions, not to avoid analysis. The
[`change risk model`](../knowledge/change-risk-model.md) provides the broader
descriptive model.
