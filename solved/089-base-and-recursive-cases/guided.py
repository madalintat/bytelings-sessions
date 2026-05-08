"""Rung 3: Guided — solved version.

The "for each item, ask is-int-or-list" decomposition is the
canonical recursion shape on tree-shaped data. The base case is the
empty list (sum is 0). The recursive case sums each item's
contribution: an int contributes itself; a list contributes its own
nested_sum (recursive call).

The for-loop here isn't hiding the recursion — it's iterating over
the level we're currently inspecting. The recursion happens only on
nested lists.
"""


def nested_sum(items: list) -> int:
    total = 0
    for item in items:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total
