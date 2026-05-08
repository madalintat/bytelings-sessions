"""Rung 4: Solo implement — solved version.

Stream characters into a deque, maintaining a count dict. After the walk,
drain from the front of the deque, skipping any character whose count > 1.
Return the first character with count == 1, or None.
"""
from collections import deque
from typing import Optional


def first_unique_char(s: str) -> Optional[str]:
    counts: dict[str, int] = {}
    q: deque[str] = deque()
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
        q.append(ch)
    while q:
        ch = q.popleft()
        if counts[ch] == 1:
            return ch
    return None
