"""Rung 2: Fluency — solved version.

Three immutability traps:
  1. shout: str.upper() returns a NEW string; calling it without
     assigning the result discards it. Fix: `return s.upper()`.
  2. join_with_dashes: The starter uses += in a loop, which is O(n^2)
     because each += allocates a new string. The fix is `-".join(words)`,
     which internally concatenates once.
  3. replace_spaces: same trap as shout. str.replace returns a new string.
     The original `s` is unchanged; you must return the new string.

The test for join_with_dashes inspects the source for ".join(" — it's
checking that you've learned the pattern, not just that the output is
right. The join form is always preferred.
"""


def shout(s: str) -> str:
    """Return `s` uppercased."""
    return s.upper()


def join_with_dashes(words: list[str]) -> str:
    """Join `words` with '-' between them, in O(n)."""
    return "-".join(words)


def replace_spaces(s: str) -> str:
    """Replace every space with '_'."""
    return s.replace(" ", "_")
