"""Rung 2: Fluency — solved version.

Three linear-search bugs:
  1. contains: uses `is` (identity) instead of `==` (equality). `is` only
     works for interned objects (small ints, None, certain strings). For
     general values use `==`.
  2. find_first: returns `None` on a miss instead of -1. The docstring
     specifies -1 as the sentinel for "not found."
  3. count_matches: increments the counter for every item instead of only
     for items where `predicate(x)` is truthy. Add the predicate check.
"""


def contains(items: list, target) -> bool:
    """Return True iff `target` appears in `items`. Linear search by hand."""
    for x in items:
        if x == target:
            return True
    return False


def find_first(items: list, target) -> int:
    """Return the index of the first occurrence of `target`, or -1 if absent."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def count_matches(items: list, predicate) -> int:
    """Count items for which predicate(item) is truthy."""
    count = 0
    for x in items:
        if predicate(x):
            count += 1
    return count
