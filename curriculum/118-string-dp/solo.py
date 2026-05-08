"""Rung 4: Solo.

Topic: longest palindromic substring.

Given a string s, return the longest contiguous substring that's a
palindrome. If there are ties, return any one with the maximum length.

>>> longest_palindrome("babad")
'bab'    # or 'aba'
>>> longest_palindrome("cbbd")
'bb'
>>> longest_palindrome("a")
'a'
>>> longest_palindrome("")
''

Hints:
- One clean approach: "expand around each center". For each i:
    - expand around (i, i)   → odd-length palindrome center
    - expand around (i, i+1) → even-length palindrome center
  In each, walk lo and hi outward while s[lo] == s[hi].
- Track the best (lo, hi) seen and slice at the end.
- O(n^2) time, O(1) extra space. Don't reach for Manacher's; the
  expand-around-center version is fine here.

Tests in 04_solo_test.py are HIDDEN.

Patterns: P-28 (memoize-recursive).
"""


def longest_palindrome(s: str) -> str:
    raise NotImplementedError
