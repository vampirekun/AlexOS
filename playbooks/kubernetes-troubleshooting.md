# Kubernetes troubleshooting

Use this playbook when a failure may arise from Kubernetes workload state,
configuration, networking, scheduling, or dependencies. The outcome is a
cluster-evidence-based cause and a verified corrective action.

## Procedure

1. Establish the affected cluster, namespace, workload, time window, and
   expected behavior.
2. Inspect deployment or workload specifications and their recent rollout
   history.
3. Inspect pod status, events, restarts, readiness, resource pressure, and
   scheduling decisions.
4. Inspect current and previous container logs for the relevant instances.
5. Trace services, endpoints, ingress, DNS, configuration, secrets, and external
   dependencies as indicated by the evidence.
6. Compare desired configuration with the live objects before changing either.
7. Identify whether the cause is application, configuration, platform, or an
   interaction between them.
8. Apply the smallest safe correction and verify rollout health and user-facing
   behavior.

Do not guess from a manifest alone when live cluster state is available. Use the
general [`debugging playbook`](debugging.md) for hypothesis discipline.
