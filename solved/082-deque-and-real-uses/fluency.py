"""Rung 2: Fluency drill — solved version.

make_ring: pass maxlen=n to the deque constructor.
left_extend_in_order: extendleft reverses order, so pass reversed(items)
to undo the reversal and preserve the original order on the left.
"""
from collections import deque


def make_ring(n: int) -> deque:
    """Return an empty deque that holds at most `n` items (oldest evicted)."""
    return deque(maxlen=n)


def left_extend_in_order(d: deque, items: list) -> None:
    """Push every item from `items` onto the LEFT of `d`, preserving
    the same order as `items`.

    extendleft reverses, so we pass reversed(items) to cancel out.
    """
    d.extendleft(reversed(items))
