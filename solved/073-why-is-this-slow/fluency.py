"""Rung 2: Fluency drill — solved version.

Change `seen` from a list to a set. Both `not in` and `.add` become
O(1) average instead of O(n), turning the overall algorithm from
O(n^2) to O(n).
"""


def unique_preserve_order(items: list) -> list:
    out: list = []
    seen: set = set()
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
