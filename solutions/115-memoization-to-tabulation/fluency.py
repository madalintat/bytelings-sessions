"""Rung 2: Fluency drill — convert top-down to bottom-up.

Topic: same recurrence, opposite direction.

`climb_topdown` works (it's yesterday's). `climb_bottomup` is your
job: same answer, but iterative, using a table or two rolling
variables. No recursion.
"""
from functools import cache


@cache
def climb_topdown(n: int) -> int:
    if n <= 1:
        return 1
    return climb_topdown(n - 1) + climb_topdown(n - 2)


def climb_bottomup(n: int) -> int:
    """Iterative version — fill a table or roll two variables."""
    # TODO: same recurrence as above, but iterative
    raise NotImplementedError
