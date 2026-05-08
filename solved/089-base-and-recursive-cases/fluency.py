"""Rung 2: Fluency — solved version.

Two missing base cases. The recursive cases are correct; without a
guard the calls run forever (well, until Python's recursion-limit
sentinel: RecursionError around depth ~1000).

For factorial, 0 and 1 both return 1 (the empty product). The
combined check `n <= 1` covers both cleanly. For length, the empty
list is the natural floor — once `items[1:]` is `[]`, we return 0.
"""


def factorial(n: int) -> int:
    """Return n! (n factorial). 0! is 1."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def length(items: list) -> int:
    """Return the number of items, computed recursively."""
    if not items:
        return 0
    return 1 + length(items[1:])
