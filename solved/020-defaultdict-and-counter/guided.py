"""Rung 3: Guided — solved version.

`index_by` is the canonical "group records by a field" pattern:
  - Use `defaultdict(list)` to avoid the `if key not in d` dance.
  - Skip records that don't have the `key` field (guard with `if key in r`).
  - Convert to a plain `dict` before returning so that accessing a missing
    group raises KeyError instead of silently creating an empty list.

This is the same pattern as `group_by_first_letter` from fluency, just
applied to dicts-of-dicts instead of words.
"""
from collections import defaultdict


def index_by(records: list[dict], key: str) -> dict:
    """Group records by the value of `records[i][key]`."""
    groups: dict = defaultdict(list)
    for r in records:
        if key in r:
            groups[r[key]].append(r)
    return dict(groups)
