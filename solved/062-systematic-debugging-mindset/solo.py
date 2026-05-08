"""Rung 4: Solo implement — solved version.

Greedy shrink: confirm the full input triggers the predicate, then
trim one item at a time from the start, and then from the end, as
long as the predicate still holds. This is a simple linear shrink;
not globally minimal but deterministic and correct.
"""
from typing import Any, Callable


def minimize(
    inputs: list[Any],
    predicate: Callable[[list[Any]], bool],
) -> list[Any]:
    if not predicate(inputs):
        return []

    result = list(inputs)

    # Trim from the start.
    while len(result) > 1 and predicate(result[1:]):
        result = result[1:]

    # Trim from the end.
    while len(result) > 1 and predicate(result[:-1]):
        result = result[:-1]

    return result
