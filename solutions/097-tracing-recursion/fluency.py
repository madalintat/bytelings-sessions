"""Rung 2: Fluency drill — fix the broken trace functions.

Topic: pre-order vs post-order recursion

Each function should produce a specific list. Right now they're
returning the wrong thing because the work-vs-recurse order is
backwards. Swap the two lines so the tests pass.
"""


def forward(n: int) -> list[int]:
    """Return [1, 2, ..., n]. Should count UP."""
    if n == 0:
        return []
    # TODO: the order of these two operations is wrong for "count up"
    rest = forward(n - 1)
    return [n] + rest


def backward(n: int) -> list[int]:
    """Return [n, n-1, ..., 1]. Should count DOWN."""
    if n == 0:
        return []
    # TODO: the order of these two operations is wrong for "count down"
    rest = backward(n - 1)
    return rest + [n]
