"""Rung 4: Solo implement — solved version.

Push all chars onto a deque, then peel from both ends while there are
at least two remaining. If left != right at any point, return False.
An odd-length string leaves one character in the middle — that's fine.
"""
from collections import deque


def is_palindrome(s: str) -> bool:
    d: deque[str] = deque(s)
    while len(d) >= 2:
        if d.popleft() != d.pop():
            return False
    return True
