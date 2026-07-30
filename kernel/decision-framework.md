# Decision framework

Engineering decisions allocate risk, complexity, and future cost. The framework
below makes that allocation explicit without requiring heavyweight design
documents for routine work.

## Frame the decision

State the outcome, constraints, decision owner, and deadline. Identify what
happens if no change is made. Many false dilemmas disappear when “preserve the
current design” and “gather more evidence” are treated as real options.

Separate requirements from proposed mechanisms. A request for a cache may
actually require lower latency; a request for a rewrite may actually require
clearer ownership. Evaluating the mechanism before the outcome narrows the
decision prematurely.

## Generate proportionate options

Consider at least the credible alternatives, including the smallest extension,
a local replacement, and no change when applicable. More options are not always
better; stop when another option would not change the relevant tradeoff space.

## Evaluate

Use criteria that matter to the decision:

- correctness and completeness;
- compatibility and migration cost;
- consequence, uncertainty, exposure, and recoverability;
- operational visibility and failure containment;
- conceptual complexity and future change cost;
- delivery time and cost of delay.

The [`change risk model`](../knowledge/change-risk-model.md) supplies a durable
risk vocabulary. Do not reduce unlike criteria to a spurious numeric score when
the numbers have no defensible meaning.

## Prefer reversible progress under uncertainty

When options have similar value and evidence is incomplete, prefer the one that
preserves future choices, limits exposure, and produces information. Small
experiments, staged rollout, compatibility layers, and isolated changes often
serve this purpose.

Reversibility is not free. Temporary layers can become permanent, dual paths
increase operating cost, and experiments can still affect users. Prefer
reversibility when it reduces meaningful risk, not as a ritual.

## Make the decision

Record the chosen option, decisive reasons, rejected alternatives that may
recur, assumptions, and conditions that would trigger reconsideration. The
artifact should be proportional: a sentence in a small change, a design
document for a broad architectural commitment.

Failure to decide also has cost. When uncertainty cannot be eliminated, choose
the action with an acceptable downside and a credible recovery path, or request
the authority needed to proceed.

## Review after evidence

Implementation and operation generate new evidence. Revisit the decision when a
key assumption fails, the risk boundary changes, or the chosen approach expands
materially. Changing course in response to evidence is correction, not
inconsistency.

The [`operating cycle`](operating-cycle.md) places this framework between
investigation and execution. The
[`architecture assessment playbook`](../playbooks/architecture-assessment.md)
applies it to structural change.
