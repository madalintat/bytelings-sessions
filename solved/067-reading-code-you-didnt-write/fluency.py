"""Rung 2: Fluency drill — solved version.

mystery() removes consecutive duplicates while preserving order.
The docstring must contain the word "consecutive" to pass the test.
"""


def mystery(items: list[int]) -> list[int]:
    """Remove consecutive duplicates, preserving first-seen order."""
    out: list[int] = []
    for x in items:
        if not out or out[-1] != x:
            out.append(x)
    return out
