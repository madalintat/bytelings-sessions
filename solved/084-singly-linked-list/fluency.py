"""Rung 2: Fluency drill — solved version.

length: start n=0 (not 1) and increment inside the loop.
values: read cur.value (not cur.next.value) and advance until cur is None.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def length(head: Node | None) -> int:
    """Return how many nodes are in the list starting at `head`."""
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next
    return n


def values(head: Node | None) -> list:
    """Return the list's values in order, as a Python list."""
    out = []
    cur = head
    while cur is not None:
        out.append(cur.value)
        cur = cur.next
    return out
