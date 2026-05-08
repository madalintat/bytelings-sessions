"""Rung 3: Guided — solved version.

`every_other` is a textbook slice-with-step: s[::2] picks every second
character starting at index 0. The step is applied by the slice protocol
without a loop, making it O(n) and a single expression.

Alternative — a list comprehension is also readable:
    ''.join(c for i, c in enumerate(s) if i % 2 == 0)
but the slice form is idiomatic Python when you don't need the index.
"""


def every_other(s: str) -> str:
    """Return every other character of `s`, starting from index 0.

    >>> every_other("abcdef")
    'ace'
    >>> every_other("")
    ''
    >>> every_other("x")
    'x'
    >>> every_other("panopticon")
    'pnpio'
    """
    return s[::2]
