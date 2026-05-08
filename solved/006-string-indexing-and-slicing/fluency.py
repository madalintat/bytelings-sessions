"""Rung 2: Fluency — solved version.

Four slice bugs, each a different kind of off-by-one:
  1. first_char: indices are 0-based, not 1-based. s[0] is the first.
  2. last_char: s[len(s)] would be out of range. Negative indices count
     from the end: s[-1] is always the last element, regardless of length.
  3. middle_three: slice stop is EXCLUSIVE. For indices 2, 3, 4, the
     stop must be 5, not 4. Pattern: s[start : start + count].
  4. reversed_str: step 1 means forward. Step -1 walks backward. The
     idiom s[::-1] is the canonical Python "reverse sequence" one-liner.
"""


def first_char(s: str) -> str:
    """Return the first character of `s`."""
    return s[0]


def last_char(s: str) -> str:
    """Return the last character of `s`."""
    return s[-1]


def middle_three(s: str) -> str:
    """Return the 3 chars starting at index 2 (i.e. indices 2, 3, 4)."""
    return s[2:5]


def reversed_str(s: str) -> str:
    """Return `s` reversed."""
    return s[::-1]
