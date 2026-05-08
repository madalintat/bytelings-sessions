"""Rung 4: Solo — solved version.

nice_sort sorts case-insensitively using str.lower() as the key.
Python's sort is stable, so words that compare equal on their
lowercase form keep their original relative order from the input.
This means earlier occurrences of the same word (regardless of case)
always appear first in the output, satisfying the tiebreaker rule.
"""


def nice_sort(words: list[str]) -> list[str]:
    """Sort case-insensitively; ties preserve original input order."""
    return sorted(words, key=str.lower)
