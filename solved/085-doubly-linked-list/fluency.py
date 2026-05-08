"""Rung 2: Fluency drill — solved version.

link: both a.next = b AND b.prev = a must be set.
unlink: both directions must be rewired — node.prev.next = node.next
AND node.next.prev = node.prev.
"""
from typing import Optional


class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


def link(a: Node, b: Node) -> None:
    """Wire `a` immediately before `b` in a doubly linked list."""
    a.next = b
    b.prev = a


def unlink(node: Node) -> None:
    """Splice `node` out of its list. Both neighbors should bypass it."""
    node.prev.next = node.next
    node.next.prev = node.prev
