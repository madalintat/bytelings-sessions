"""Rung 2: Fluency drill — fix the broken splice helpers.

Topic: doubly-linked node wiring, prev/next bookkeeping.
"""
from typing import Optional


class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


def link(a: Node, b: Node) -> None:
    """Wire `a` immediately before `b` in a doubly linked list.

    After this call:
        a.next == b
        b.prev == a

    Existing pointers from `a.next` or `b.prev` are simply overwritten
    here — this helper is for use right after creating fresh nodes.
    """
    # TODO: only one of the two pointers is set. Both must be.
    a.next = b


def unlink(node: Node) -> None:
    """Splice `node` out of its list. Both neighbors should bypass it.

    For example, if the list is a <-> b <-> c and we unlink b, then:
        a.next == c
        c.prev == a
        (b's own pointers can be anything — caller is discarding it)

    Assume `node` has both neighbors. Boundary nodes (head/tail) are
    handled by the LinkedList class, not here.
    """
    # TODO: this only fixes one direction.
    node.prev.next = node.next
