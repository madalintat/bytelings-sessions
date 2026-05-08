"""Rung 4: Solo — solved version.

`tally` accumulates counts from both positional `tags` and keyword `counts`:
  1. Validate: no positional tag may start with '_'. Raise ValueError if any does.
  2. Build a result dict by counting each tag from `*tags`.
  3. Add/merge the `**counts` keyword arguments.

Using `Counter` simplifies both steps:
  - `Counter(tags)` counts occurrences of each positional tag.
  - Adding two Counters merges counts: `c1 + c2` (or `c1.update(c2)`).
  - Convert to a plain dict before returning.

Validation must happen before accumulation to raise early.
"""
from collections import Counter


def tally(*tags: str, **counts: int) -> dict[str, int]:
    for tag in tags:
        if tag.startswith("_"):
            raise ValueError(f"tag may not start with '_': {tag!r}")
    result = Counter(tags)
    result.update(counts)
    return dict(result)
