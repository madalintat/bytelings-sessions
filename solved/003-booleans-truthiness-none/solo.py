"""Rung 4: Solo — solved version.

`sum(1 for x in items if x)` reads as "count the truthy ones." The
implicit truthiness check inside `if` is exactly what the function
asks for — empty strings, 0, [], None, False all count as falsy and
get filtered out.

Equivalent expressions: `sum(bool(x) for x in items)` (less readable),
`len([x for x in items if x])` (allocates an intermediate list).
The generator-with-implicit-bool is the idiom.
"""


def count_truthy(items: list) -> int:
    return sum(1 for x in items if x)
