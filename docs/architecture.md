# Repository architecture

This document defines the canonical component model for AlexOS. Directory
READMEs index their contents; they do not redefine these boundaries.

## Design constraints

AlexOS must remain useful across programming languages, repository sizes, and
agent products. Its structure therefore favors stable responsibilities,
one-way dependencies, selective loading, and ordinary files that remain
readable without proprietary tooling.

The framework stores reusable engineering guidance only. User profiles,
project facts, organization rules, runtime state, and specialized technologies
have different owners and release cycles. Keeping them in core would turn a
framework into one installation's configuration.

## Content layers

### Kernel

The kernel defines behavior expected in every engineering task: mission,
epistemic discipline, decision rules, execution lifecycle, and conflict
handling. It is small enough to load as a unit.

The kernel has no semantic dependency on another content layer. A kernel
document may use ordinary engineering terms, but another layer must not be
required to interpret its requirements.

### Policies

Policies are mandatory constraints shared by multiple tasks. A policy narrows
acceptable action without prescribing a full workflow. Policies depend on the
kernel.

### Knowledge

Knowledge contains durable descriptive models. It explains systems and risks
without requiring an action. Knowledge has no dependency on policies,
heuristics, or playbooks.

### Heuristics

Heuristics are conditional shortcuts for directing attention or choosing an
investigation order. They are explicitly fallible and must state applicability
and limits. Heuristics may use knowledge models but cannot create policy.

### Playbooks

Playbooks are procedures selected by a recognizable trigger. They define an
outcome, inputs, method, completion evidence, and failure modes. Playbooks may
compose the kernel, policies, knowledge, and heuristics.

### System documentation

`docs/` governs AlexOS as a repository: architecture, content contracts,
information lifecycle, and evolution. It is maintenance documentation, not an
execution layer.

## Dependency direction

```text
playbooks ──> policies ──> kernel
    │
    ├───────> heuristics ──> knowledge
    └──────────────────────> knowledge

docs governs the graph but is not loaded for ordinary tasks.
```

Dependencies in the reverse direction are prohibited. In particular:

- the kernel cannot require a policy, playbook, heuristic, or knowledge file;
- knowledge and heuristics cannot require the playbooks that consume them;
- policies cannot depend on task procedures;
- core content cannot depend on an external project or adapter.

Navigation links are not automatically semantic dependencies. A link becomes a
dependency when the target defines meaning or requirements needed by the
source.

## Placement decision

Classify new material by its single canonical responsibility:

1. Universal behavior belongs in `kernel/`.
2. A mandatory cross-cutting constraint belongs in `policies/`.
3. A durable explanatory model belongs in `knowledge/`.
4. Conditional guidance with known limits belongs in `heuristics/`.
5. A triggered procedure with a verifiable outcome belongs in `playbooks/`.
6. Governance of AlexOS belongs in `docs/`.
7. Installation-specific material remains external.

If one document matches multiple categories, it contains multiple
responsibilities. Split it at the boundary and link from the consumer to the
dependency.

## External composition

AlexOS composes with three external sources.

**Repository and runtime context** includes local instructions, code,
configuration, current state, and task evidence. It remains owned by the active
repository or work system.

**Overlays** contain durable user, organization, environment, or project facts.
They should be versioned separately when versioning is appropriate. Core
playbooks may request relevant context but cannot assume a specific overlay
layout.

**Extensions** provide specialized policies, knowledge, heuristics, or playbooks
for a technology or workflow. Extensions depend on the core, never the reverse.

**Adapters** map the loading model to a named agent product. They may select and
package canonical documents, but cannot duplicate or alter their semantics.

No overlay, extension, or adapter directory is created in core until the
repository owns a real implementation. Empty integration taxonomy would add
navigation cost without capability.

## Loading and scale

Every directory README is a curated index and boundary summary. At 500
documents, discovery remains local: start at the root, select a layer, then
select one relevant document. An integration may build a generated catalog, but
the repository must remain navigable without it.

Create a child directory only when a stable subject boundary is more useful
than a flat catalog. File count alone is not a boundary. A child directory must
contain substantive material, have a README, and appear in its parent index.

## Invariants

- Every document has one canonical responsibility.
- Every normative rule has one canonical owner.
- Dependency direction is stable and acyclic.
- Core contains no user, project, vendor, or technology assumptions.
- Runtime evidence is not committed as permanent framework truth.
- Every existing directory has a maintained README.
- Structural rules are validated where objective validation is possible.
