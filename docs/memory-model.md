# Memory model

AlexOS separates knowledge by lifecycle and authority so that useful experience
can accumulate without converting transient observations into permanent rules.
Each document has one primary memory class. Cross-references connect classes;
documents must not blend them.

## Classes

### Permanent knowledge

Permanent knowledge is expected to remain valid across users, projects, and
tools. It includes the kernel, policies, playbooks, explanatory knowledge, and
repository governance. “Permanent” describes intended durability, not
infallibility; corrections remain possible and should be deliberate.

Permanent knowledge is stored in [`../kernel/`](../kernel/README.md),
[`../policies/`](../policies/README.md),
[`../playbooks/`](../playbooks/README.md),
[`../knowledge/`](../knowledge/README.md), and `docs/`.

Promotion into this class requires evidence that the material generalizes
beyond the event or project that produced it. A local workaround does not meet
that standard.

### User knowledge

User knowledge records confirmed preferences and relevant professional context.
It is durable for one person but has no authority over other users or universal
engineering rules. It belongs in [`../memory/user/`](../memory/user/README.md).

### Project knowledge

Project knowledge records stable facts, vocabulary, relationships, and
constraints for a bounded project. Its authority ends at that project and
current repository evidence can supersede it. It belongs in
[`../memory/projects/`](../memory/projects/README.md). Environment facts with a
similar lifecycle belong in
[`../memory/environments/`](../memory/environments/README.md).

### Temporary context

Temporary context supports an active task, incident, or conversation. It is not
committed to AlexOS by default. It stays in the owning work system or runtime
context until discarded or reviewed for promotion. The handling protocol is
defined in [`../memory/temporary-context.md`](../memory/temporary-context.md).

### Historical lessons

Historical lessons preserve what a real event taught, including evidence and
limits. They do not become universal solely because the event was memorable.
They belong in [`../memory/lessons/`](../memory/lessons/README.md).

### Engineering heuristics

Heuristics are conditional, evidence-informed rules of thumb. They are more
general than a project fact but less authoritative than a policy. They belong in
[`../memory/heuristics/`](../memory/heuristics/README.md) and must state where
they fail.

## Authority is not retention

Durability and authority are separate. A permanent explanatory model can be
descriptive rather than mandatory. A fresh observation can be highly relevant
to the current incident without being durable. A policy is authoritative
because of its normative role, not because its file is old.

When information conflicts:

1. Current direct evidence outranks stale descriptive memory.
2. Normative policy constrains action until an authorized exception is made.
3. Specific project facts refine general descriptive knowledge within scope.
4. Heuristics suggest investigation; they do not settle factual questions.
5. Historical lessons inform risk but do not prove that events will repeat.

Conflicts should be surfaced and resolved at the canonical record. Appending a
contradictory note creates ambiguity rather than memory.

## Promotion and demotion

Information moves between classes only through review:

```text
temporary observation
    ├── discard
    ├── project or user fact
    ├── historical lesson
    └── heuristic ──> policy, playbook, or permanent knowledge
```

Promotion requires provenance, demonstrated reuse, explicit scope, and a
canonical destination. The broader the claimed scope, the stronger the
evidence required.

Demote or retire information when its scope was overstated, its evidence no
longer holds, or its maintenance cost exceeds its value. Historical facts are
corrected rather than rewritten to imply the original event did not occur.

## Failure modes

- **Memory inflation:** retaining every observation makes relevant knowledge
  harder to find.
- **Scope leakage:** a project preference becomes a universal rule.
- **Stale authority:** an old summary overrides current repository evidence.
- **Anecdotal policy:** one incident creates a mandatory rule without broader
  analysis.
- **Orphaned context:** copied facts lose their authoritative source.
- **Secret retention:** operational access data enters long-lived documentation.

Directory boundaries and review requirements exist to make these failures
visible before they become system behavior.
