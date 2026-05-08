"""Rung 3: Guided — solved version.

`is` checks *identity* — whether two names refer to the same object
in memory. `==` checks *equality* — whether two objects compare equal,
which for lists means same length AND all elements equal.

The docstring's whole point is the difference:

  same_list(x, x)     → True   (same identity)
  same_list([1,2], [1,2]) → False  (equal values, different objects)

`a == b` would return True for the second case, which is wrong for
this function. Use `is`.
"""


def same_list(a, b) -> bool:
    """
    >>> x = [1, 2]
    >>> same_list(x, x)
    True
    >>> same_list([1, 2], [1, 2])
    False
    """
    return a is b
