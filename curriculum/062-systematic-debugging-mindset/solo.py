"""Rung 4: Solo implement.

Topic: minimize a failing input — the "shrinking" idea behind
property-based testing and most automated bug-finders.

You're handed:
  - `inputs`: a list (the failing input — say, a list of orders that
    triggers a bug when processed).
  - `predicate(items) -> bool`: True if `items` still triggers the bug.

Return the SHORTEST contiguous slice of `inputs` for which
`predicate` is still True. If the predicate isn't True for the full
input, return [].

Strategy:
  - First, confirm predicate(inputs) is True; if not, return [].
  - Then greedily shrink: try removing items from the start, then
    from the end, while predicate stays True.
  - Don't reorder. Don't go below length 1 if predicate(item-as-1)
    is True somewhere.

Hidden tests in 04_solo_test.py.
"""
from typing import Any, Callable


def minimize(
    inputs: list[Any],
    predicate: Callable[[list[Any]], bool],
) -> list[Any]:
    raise NotImplementedError
