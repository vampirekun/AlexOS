# User memory

This directory contains confirmed, engineering-relevant knowledge about the
person AlexOS serves. It configures collaboration without converting personal
preferences into universal agent behavior.

## Why this directory exists

Communication style and working preferences belong to the person, not to a
universal agent identity. Keeping them in an overlay lets the kernel remain
portable and makes changes to a person's preferences local and explicit.

## What belongs here

- Preferred level of technical detail and communication style.
- Stable engineering preferences that shape choices among otherwise valid
  approaches.
- Professional role or background when it improves collaboration.
- Accessibility or workflow preferences relevant to agent interactions.

Current user:

- [`alex.md`](alex.md) contains Alex's engineering and communication
  preferences.

## What must never belong here

- Sensitive personal data that is not necessary for engineering collaboration.
- Authentication material or account identifiers.
- Facts about a machine or repository; use [`../environments/`](../environments/README.md)
  or [`../projects/`](../projects/README.md).
- Universal rules that every user should inherit; use
  [`../../kernel/`](../../kernel/README.md) or
  [`../../policies/`](../../policies/README.md).
- Temporary mood, one-off request details, or inferred preferences not confirmed
  by repeated evidence.

## Selection and maintenance

Treat a profile as an explicit configuration overlay, not an imitation persona.
Prefer concrete preferences over stylistic role-play. When a task-specific
instruction conflicts with a stored preference, the explicit current
instruction wins for that task.

Load the active user's profile, not every profile that may exist in the future.
The general behavior for engineering prose remains owned by the
[`communication policy`](../../policies/communication.md). The retention and
correction rules in [`../../docs/memory-model.md`](../../docs/memory-model.md)
apply to every profile.
