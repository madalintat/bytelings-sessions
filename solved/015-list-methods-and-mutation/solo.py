"""Rung 4: Solo — solved version.

`dedupe` uses a `seen` set for O(1) membership checks:
  1. Walk items in order.
  2. If the item is not in `seen`, add it to both `seen` and the result.
  3. If it's already in `seen`, skip it.

This is O(n) total because set membership is O(1) average and we
visit each element once. Using a list for `seen` would be O(n^2).

The ordering of items is preserved because we walk the list in order and
only keep first occurrences. `set(items)` would lose order entirely.
"""


def dedupe(items: list) -> list:
    seen: set = set()
    result: list = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
