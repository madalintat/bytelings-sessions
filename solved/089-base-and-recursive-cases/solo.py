"""Rung 4: Solo — solved version.

Trees are dicts here; the "is this a file or a subdirectory" decision
is `isinstance(value, dict)`. A subdirectory contributes its own
recursive count; a file contributes 1.

The base case (empty dict) returns 0 because `for k, v in {}.items()`
is empty — the sum is 0 by initialization. No explicit base-case
guard needed; the for-loop's emptiness IS the base case.

Patterns: P-28 (memoize-recursive) — applies to recursion in general,
though this particular tree walk doesn't have overlapping subproblems
so memoization wouldn't speed it up.
"""


def count_files(tree: dict) -> int:
    total = 0
    for value in tree.values():
        if isinstance(value, dict):
            total += count_files(value)
        else:
            total += 1
    return total
