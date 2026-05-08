"""Rung 4: Solo implement.

Topic: dedupe a list while preserving order

Implement `dedupe(items)`:

- Return a NEW list with duplicates removed, keeping each element's
  FIRST occurrence in the original order.
- The elements may be any hashable type (ints, strings, tuples).
- Don't mutate the input.

Examples:
    dedupe([1, 2, 1, 3, 2, 4])     -> [1, 2, 3, 4]
    dedupe(['a', 'b', 'a', 'c'])   -> ['a', 'b', 'c']
    dedupe([])                     -> []

Hint: a `set` of "already seen" gives O(n) total. NOT `set(items)` —
that loses order.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def dedupe(items: list) -> list:
    raise NotImplementedError
