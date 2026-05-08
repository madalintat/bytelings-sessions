"""Rung 2: Fluency — solved version.

The TODO was to add type hints. The bodies were already correct;
the work was reading the docstrings and writing the contract that
matches.

  first_word: takes str, returns str. The empty case still returns
    "" (also a str), so the return type stays str.
  repeat: takes a str and an int (number of repeats), returns str.
    Python's `str * int` does the repeat — annotation must match
    that contract.
"""


def first_word(s: str) -> str:
    """Return the first whitespace-separated word, or '' for empty input."""
    parts = s.split()
    if not parts:
        return ""
    return parts[0]


def repeat(s: str, n: int) -> str:
    """Return s concatenated n times."""
    return s * n
