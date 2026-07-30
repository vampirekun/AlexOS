# Repository architecture

## Design goals

AlexOS must remain understandable to humans, consumable by different agents,
and maintainable when it contains hundreds of documents. Its architecture
therefore optimizes for:

- clear ownership of every idea;
- selective loading instead of one enormous instruction file;
- minimal coupling between durable rules and volatile facts;
- ordinary Markdown and relative links;
- expansion without empty taxonomy or duplicated content;
- change review using the same discipline as a software project.

## Layer model

AlexOS uses five active layers.

### 1. Kernel

The kernel contains the smallest set of universal operating semantics: mission,
reasoning principles, and the execution cycle. It answers, "How does an
engineering agent behave regardless of the current task?"

The kernel may depend on nothing else. It can point readers toward policies or
playbooks, but its meaning must remain valid when no project context is loaded.
See [`../kernel/README.md`](../kernel/README.md).

### 2. Policies

Policies express cross-cutting constraints and quality bars. They answer, "What
must remain true across multiple kinds of work?" A policy can refine a kernel
principle but should not prescribe a long task sequence.

Policies may depend on the kernel. They must not depend on a specific person,
project, or agent vendor. See [`../policies/README.md`](../policies/README.md).

### 3. Playbooks

Playbooks are executable procedures selected because a situation has occurred.
They answer, "What sequence helps reach a verifiable outcome for this class of
task?"

Playbooks may reference the kernel and policies. They may name context fields an
agent should look for, but they must still make sense when a particular context
overlay is absent. See [`../playbooks/README.md`](../playbooks/README.md).

### 4. Context

Context contains facts and preferences that change independently from the
operating model. It answers, "What is true about the person, environment, or
project involved in this run?"

Context can narrow or configure a playbook, but it cannot weaken the kernel or
policies. Conflicts are resolved in favor of the more stable layer unless a
human explicitly authorizes an exception. See
[`../context/README.md`](../context/README.md).

### 5. System documentation

`docs/` governs AlexOS as a repository. It defines boundaries, document
contracts, and evolution rules. It is read by maintainers, not loaded by
default for ordinary engineering tasks.

## Dependency direction

Dependencies should point from volatile or specialized material toward stable,
general material:

```text
context ─────┐
             ├──> playbooks ───> policies ───> kernel
specialized ─┘

docs governs the structure; it is not an execution dependency.
```

Avoid reverse dependencies. In particular, the kernel must not know about Alex,
M5, Windows, Kubernetes, or a named coding agent. A project context may say
which playbooks are common, but a playbook must not embed that project's facts.

## Placement decision

Classify a proposed document using the first matching question:

1. Does it govern the AlexOS repository? Put it in `docs/`.
2. Is it an invariant behavior required for almost every task? Put it in
   `kernel/`, after proving the kernel needs to grow.
3. Is it a rule that constrains many different workflows? Put it in `policies/`.
4. Is it a repeatable response to a recognizable trigger with an outcome? Put
   it in `playbooks/`.
5. Is it a replaceable fact or preference about a person, environment, or
   project? Put it in the matching `context/` namespace.
6. Is it durable explanatory knowledge rather than an instruction? Introduce or
   use `knowledge/` as described below.
7. If none applies, reconsider whether the material belongs in AlexOS.

When one document would answer several questions, split it at the boundary and
link the pieces. Do not solve ambiguity by copying the same rule into multiple
layers.

## Loading model

An integration should start at the root [`README.md`](../README.md), then load:

1. all kernel documents, because the kernel is intentionally small;
2. policies relevant to the risk and artifact being changed;
3. context selected by the active person, environment, and project;
4. one primary playbook, plus only directly referenced supporting material;
5. optional knowledge or examples when needed.

This loading order is advisory, not a vendor-specific protocol. An adapter can
translate it into imports, include directives, symlinks, or generated
instructions, but the canonical Markdown remains vendor-neutral.

## Scaling to hundreds of documents

Each directory README is both a boundary contract and a curated index. When a
directory becomes difficult to scan, split it by domain or lifecycle rather
than by arbitrary document counts. Every new child directory receives its own
README and appears in its parent's index.

Cross-cutting discovery should rely on stable relative links and the document
metadata described in [`content-model.md`](content-model.md). A future generated
catalog may read that metadata, but generated navigation must supplement rather
than replace local READMEs. This preserves usefulness in a plain file browser.

Large subjects should use a hub document that explains scope and links to
focused documents. A hub is not permission to duplicate their contents.

## Optional extension directories

These directories are part of the architectural vocabulary but are not created
until substantive content exists:

- `knowledge/`: durable technical or domain explanations used by several
  playbooks. It must not contain instructions masquerading as reference notes.
- `examples/`: complete, reviewed examples that demonstrate desired decisions
  or outputs. Fragments such as "Yesterday: ..." are not examples.
- `adapters/`: thin integrations for named agent products. Adapters may point to
  canonical content but must not fork it.
- `schemas/`: machine-readable contracts used by actual validation or
  generation tooling.
- `tools/`: scripts that validate, index, package, or publish AlexOS.
- `decisions/`: architecture decision records when decisions become numerous
  enough that a chronological log improves maintenance.

Creating an optional directory requires its first real artifact, a detailed
README defining its boundary, and links from the root and relevant parent
indexes.

## Architectural invariants

- There is one canonical source for every rule.
- Vendor adapters never own universal behavior.
- Context configures behavior but cannot silently redefine policy.
- Playbooks have triggers and outcomes; policies have constraints.
- Every directory is navigable without a proprietary tool.
- Empty taxonomy is forbidden.
- Moving a document includes updating all inbound links.
