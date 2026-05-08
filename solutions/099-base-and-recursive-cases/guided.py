"""Rung 3: Guided implement — sum a nested list.

Topic: recursion shines on tree-shaped data

`nested_sum` takes a list that may contain ints OR more lists (which
may themselves contain ints or lists). Return the total of all ints
no matter how deep.

>>> nested_sum([1, [2, [3, 4]], 5])
15
>>> nested_sum([])
0
>>> nested_sum([[[[7]]]])
7

Hints:
- Base case: empty list → 0.
- For each item, ask: is this an int (add it) or a list (recurse on it)?
- `isinstance(item, list)` will tell you which.
"""


def nested_sum(items: list) -> int:
    # TODO: implement using recursion. No flatten() and no for-loop tricks
    # that hide the recursion — the recursive call is the point.
    raise NotImplementedError
