# Architecture assessment

Use this playbook before recommending a structural redesign. The outcome is an
evidence-based description of the current architecture and a proportionate
recommendation.

## Procedure

1. Map components, responsibilities, dependencies, data flow, and boundaries.
2. Inspect the implementation, tests, build system, deployment model, and
   repository guidance.
3. Identify which constraints are intentional and which are accidental.
4. State the concrete forces motivating change: failure modes, scaling limits,
   maintenance cost, or new requirements.
5. Compare preserving, extending, and replacing the current design.
6. Recommend the smallest architecture change that addresses those forces.
7. Describe migration, compatibility, verification, and rollback concerns.

Do not propose a redesign solely because another pattern is more fashionable.
Use [`migration.md`](migration.md) when the approved outcome requires moving
existing behavior.
