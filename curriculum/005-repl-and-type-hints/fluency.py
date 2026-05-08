"""Rung 2 — add type hints.

Topic: surface-level type annotations
"""


def first_word(s):
    """Return the first whitespace-separated word, or '' for empty input."""
    parts = s.split()
    if not parts:
        return ""
    return parts[0]


def repeat(s, n):
    """Return s concatenated n times."""
    return s * n
