# Progress reporting

This playbook communicates the current state of engineering work without
reconstructing the full activity history.

## Use when

Use it for a work-item update, asynchronous status report, or short team
progress update.

## Inputs

- Meaningful outcomes since the previous report.
- Current intended outcome.
- Blockers, dependencies, decisions, risks, and validation that affect others.

## Method

1. Lead with the current outcome or state.
2. Describe completed work by its effect, not as an activity transcript.
3. State the next intended outcome when work remains.
4. Identify blockers or decisions that require action.
5. Include validation or changed risk when it affects confidence.
6. Remove background already owned by the work system unless needed to
   interpret the update.
7. Apply the [`communication policy`](../policies/communication.md).

## Completion evidence

- A reader can determine what changed, what comes next, and whether action is
  required.
- Claims about completion and validation are accurate.
- The update is understandable without unnecessary implementation detail.

## Failure modes

- Listing activity without reporting progress.
- Repeating the entire issue description.
- Hiding a blocker behind optimistic wording.
- Using a fixed ceremony template when the communication channel requires a
  different shape.
