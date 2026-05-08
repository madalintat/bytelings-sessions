"""Rung 4: Solo implement.

Topic: reverse a string, recursively.

Given a string s, return the reverse. No s[::-1], no reversed(),
no for/while loops — purely recursive. Trace what your function does
for "abc":

    reverse("abc") = reverse("bc") + "a"
                   = (reverse("c") + "b") + "a"
                   = ((reverse("") + "c") + "b") + "a"
                   = (("" + "c") + "b") + "a"
                   = "cba"

The tests in 04_solo_test.py are HIDDEN.

Patterns: P-16 (yield-from-passthrough), P-28 (memoize-recursive).
"""


def reverse(s: str) -> str:
    raise NotImplementedError
