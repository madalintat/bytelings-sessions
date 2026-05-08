"""Rung 2: Fluency drill — fix the broken slices.

Topic: string indexing and slicing
"""


def first_char(s: str) -> str:
    """Return the first character of `s`."""
    # TODO: this returns the second character
    return s[1]


def last_char(s: str) -> str:
    """Return the last character of `s`."""
    # TODO: don't hard-code; use a negative index
    return s[len(s)]


def middle_three(s: str) -> str:
    """Return the 3 chars starting at index 2 (i.e. indices 2, 3, 4)."""
    # TODO: stop is exclusive — fix the slice
    return s[2:4]


def reversed_str(s: str) -> str:
    """Return `s` reversed."""
    # TODO: use slice with step -1
    return s[::1]
