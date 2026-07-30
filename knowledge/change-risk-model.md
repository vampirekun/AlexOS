# Change risk model

Engineering risk is the possibility that a change produces an undesirable
outcome. Diff size is an incomplete proxy. A more useful model considers
consequence, uncertainty, exposure, and recoverability.

## Consequence

Consequence is the severity of a plausible failure. Data loss, security breach,
financial error, and prolonged unavailability require more control than a
cosmetic defect. Consequence includes technical and human impact: operational
load, customer confusion, compliance, and damaged trust.

## Uncertainty

Uncertainty is how little is known about the system, requirement, or behavior.
It rises with unfamiliar code, weak tests, implicit contracts, nondeterminism,
unclear ownership, and changes that have no close precedent.

Uncertainty can often be reduced before implementation through investigation,
experiments, targeted tests, or smaller stages. Treating uncertainty as
confidence does not reduce it; it only removes the warning label.

## Exposure

Exposure describes how widely and how long a failure can act before detection
or containment. Consider the number of consumers, deployment scope, data
volume, execution frequency, privilege, and time to observable impact.

Feature controls, staged rollout, isolation, and monitoring can reduce exposure
without changing the defect probability.

## Recoverability

Recoverability is the ability to return to an acceptable state. Code rollback
is only one part. A change may be easy to revert while its data mutation,
external notification, or contractual effect is irreversible.

Assess rollback time, data restoration, forward-fix options, compatibility
during mixed versions, and the evidence needed to know recovery succeeded.

## Using the model

The dimensions are not a numerical formula. They structure judgment:

- High consequence calls for stronger prevention and independent verification.
- High uncertainty calls for investigation, experiments, and smaller changes.
- High exposure calls for staged rollout, containment, and early detection.
- Low recoverability calls for rehearsal, backups, migration discipline, and
  explicit approval.

Controls should target the dominant dimension. Adding more unit tests may reduce
some uncertainty but does little for an irreversible data migration without a
recovery plan.

The [`change safety policy`](../policies/change-safety.md) turns this model into
requirements. The
[`change-surface heuristic`](../memory/heuristics/change-surface-as-risk-signal.md)
provides an early, deliberately imperfect signal for where risk may be hiding.
