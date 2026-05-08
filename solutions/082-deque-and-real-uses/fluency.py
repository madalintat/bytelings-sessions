"""Rung 2: Fluency drill — fix two deque idioms.

Topic: maxlen and extendleft surprises.
"""
from collections import deque


def make_ring(n: int) -> deque:
    """Return an empty deque that holds at most `n` items (oldest evicted)."""
    # TODO: this deque is unbounded — give it a max length.
    return deque()


def left_extend_in_order(d: deque, items: list) -> None:
    """Push every item from `items` onto the LEFT of `d`, preserving the
    same order as `items`.

    For example:
        d = deque([10])
        left_extend_in_order(d, [1, 2, 3])
        # d should be deque([1, 2, 3, 10])

    Note: deque.extendleft REVERSES order — that's the trap.
    """
    # TODO: this uses extendleft naively, so the order ends up reversed.
    d.extendleft(items)
