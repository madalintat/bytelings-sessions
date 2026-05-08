"""Rung 4: Solo — solved version.

`most_common` finds the element with the highest count in O(n):
  1. One pass to build a count dict (or Counter).
  2. One pass (or max()) to find the max count.
  3. On ties, the FIRST element with max count wins.

The naive two-pass approach:
  - Build counts in one pass.
  - Walk the original list again, returning the first element whose
    count equals the max count.

This preserves tie-breaking by first-occurrence without sorting.

Alternative: `Counter(items).most_common(1)[0][0]` is shorter but
resolves ties by arbitrary ordering (Counter doesn't guarantee
first-seen on ties). So the two-pass approach is more correct here.
"""


def most_common(items: list):
    if not items:
        raise ValueError("most_common of empty list")
    counts: dict = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    for x in items:
        if counts[x] == max_count:
            return x
