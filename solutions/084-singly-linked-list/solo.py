"""Rung 4: Solo implement.

Topic: write `reverse(head)` — reverse a singly linked list in place.

Given the head of a singly linked list (Node has `.value` and `.next`),
return the head of the reversed list. Mutate in place — don't allocate
new nodes.

The classic three-pointer trick:
    prev = None
    cur  = head
    while cur:
        nxt      = cur.next
        cur.next = prev
        prev     = cur
        cur      = nxt
    return prev

Spec:
    reverse(None)            -> None
    reverse([1])             -> [1]
    reverse([1, 2, 3, 4])    -> [4, 3, 2, 1]

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-09 (two-pointer-fast-slow).
"""
from typing import Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def reverse(head: Optional[Node]) -> Optional[Node]:
    raise NotImplementedError
