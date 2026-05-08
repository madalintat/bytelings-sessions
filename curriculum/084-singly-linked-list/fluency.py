"""Rung 2: Fluency drill — fix the broken Node walks.

Topic: traversing a singly linked list, off-by-one bugs.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def length(head: Node | None) -> int:
    """Return how many nodes are in the list starting at `head`.

    An empty list (head is None) has length 0.
    """
    # TODO: this loop counts wrong (off-by-one on the empty case).
    n = 1
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next
    return n


def values(head: Node | None) -> list:
    """Return the list's values in order, as a Python list."""
    # TODO: this also reads cur.next.value (one ahead) — fix it.
    out = []
    cur = head
    while cur is not None and cur.next is not None:
        out.append(cur.next.value)
        cur = cur.next
    return out
