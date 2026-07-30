# Repository tools

This directory contains portable tooling that enforces objective AlexOS
repository contracts.

## Contains

- [`validate.py`](validate.py) — validates directory indexes, names, headings,
  relative links, anchors, and layer-specific document structure.

## Excludes

- Agent product adapters.
- Content generation.
- Semantic scoring of engineering guidance.
- Project or user automation unrelated to maintaining AlexOS.

## Use

Run from any working directory:

```text
python tools/validate.py
```

The script uses the Python standard library and resolves the repository root
from its own location. A successful structural check does not replace
architectural and technical review.
