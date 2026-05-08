"""Rung 4: Solo implement.

Topic: write `first_unique_char(s)` using a queue.

Given a string, return the first character that appears exactly once.
If none exists, return None.

The classical streaming solution: walk left-to-right, push every
character onto a queue. Also keep a count of how many times you've
seen each character. After the walk, peel from the front of the queue,
discarding any character whose count is > 1, until you find one with
count == 1 (or run out).

Examples:
    first_unique_char("aabbc")  -> "c"
    first_unique_char("abacabad") -> "c"
    first_unique_char("aabb")    -> None
    first_unique_char("")        -> None
    first_unique_char("z")       -> "z"

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Optional


def first_unique_char(s: str) -> Optional[str]:
    raise NotImplementedError
