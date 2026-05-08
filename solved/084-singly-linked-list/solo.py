"""Rung 4: Solo implement — solved version.

Classic three-pointer in-place reversal. prev starts as None; each
step saves cur.next, points cur.next back to prev, advances both.
Return prev (the new head) when cur falls off the end.
"""
from typing import Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def reverse(head: Optional[Node]) -> Optional[Node]:
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
