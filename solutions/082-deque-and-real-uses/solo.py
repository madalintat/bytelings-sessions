"""Rung 4: Solo implement.

Topic: write `is_palindrome(s)` using a deque.

Return True if `s` reads the same forwards and backwards, False
otherwise. Compare case-sensitively, take the string as-is — no
stripping non-letters, no case folding.

The deque-flavored algorithm:
    1. Push every char onto a deque.
    2. While there are at least 2 chars left, popleft and pop;
       if they differ, return False.
    3. Return True.

Examples:
    is_palindrome("racecar")  -> True
    is_palindrome("a")        -> True
    is_palindrome("")         -> True
    is_palindrome("ab")       -> False
    is_palindrome("abcba")    -> True

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-25 (deque-rotating-buffer).
"""


def is_palindrome(s: str) -> bool:
    raise NotImplementedError
