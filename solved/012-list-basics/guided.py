"""Rung 3: Guided — solved version.

`unique_in_order` removes consecutive duplicates without removing all
duplicates (so [1, 1, 2, 1] -> [1, 2, 1], not [1, 2]).

The standard pattern: walk items, append each one only if it differs
from the last thing we appended. The sentinel trick (checking `not out
or out[-1] != x`) handles the empty-result case cleanly.

Alternative using itertools.groupby:
    [key for key, _ in itertools.groupby(items)]
This is even shorter and idiomatic, but the hand-rolled loop is more
transparent for learning purposes.
"""


def unique_in_order(items: list) -> list:
    """Drop consecutive duplicates; keep order.

    >>> unique_in_order([1, 1, 2, 2, 2, 3, 1])
    [1, 2, 3, 1]
    >>> unique_in_order([])
    []
    >>> unique_in_order(['a'])
    ['a']
    >>> unique_in_order(['a', 'a', 'a'])
    ['a']
    """
    out: list = []
    for x in items:
        if not out or out[-1] != x:
            out.append(x)
    return out
