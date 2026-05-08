"""Rung 2 — fix the predicates.

Topic: truthiness vs None checks
"""


def has_value(x) -> bool:
    """Return True if x is not None (regardless of truthiness)."""
    # TODO: wrong check — this fails for empty strings
    return bool(x)


def is_blank_string(s: str) -> bool:
    """Return True if s is an empty string."""
    # TODO: wrong — using `is` for value comparison
    return s is ""


def is_definitely_false(x) -> bool:
    """Return True if x is the literal False (not 0, not None, not '')."""
    # TODO: wrong comparison operator
    return x == False
