"""Rung 2: Fluency drill — fix the O(n^2) dedupe.

Topic: list lookups vs set lookups.

`unique_preserve_order(items)` should return items with duplicates
removed, in the original order they first appeared.

It works correctly. But on 100K items, it crawls — `seen` is a list,
so each `not in` walks the whole thing. Switch `seen` to a set.

The tests include a perf bound: a 50K-item input must complete in
under a second. With `seen = []` it won't.
"""


def unique_preserve_order(items: list) -> list:
    out: list = []
    seen: list = []  # TODO: change to set()
    for x in items:
        if x not in seen:
            seen.append(x)  # TODO: seen.add(x) once it's a set
            out.append(x)
    return out
