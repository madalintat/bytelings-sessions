"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: dedupe a list while preserving order

Implement `dedupe(items)`:
- Return a new list containing each item only once.
- Preserve the *first occurrence* order.
- Items that aren't hashable should still work — fall back to a
  linear "have I seen this?" check using equality.
- The function must NOT mutate `items`.

Examples:
    dedupe([1, 2, 1, 3, 2])             # [1, 2, 3]
    dedupe([[1], [2], [1]])             # [[1], [2]]    (lists are unhashable)
    dedupe([])                          # []

Hint: try a `set` for fast lookup; if you hit a TypeError on
unhashable items, fall back to a list-based check.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-20 (dataclass-as-record).
"""


def dedupe(items: list) -> list:
    raise NotImplementedError
