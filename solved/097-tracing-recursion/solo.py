"""Rung 4: Solo — solved version.

reverse(s) = reverse(s[1:]) + s[0]. The first character is appended
after the reversed tail, so when the stack unwinds, characters are
collected in reverse order. Base case: empty string or single character
reverses to itself.

No slicing shortcuts, no reversed(), no loops.
"""


def reverse(s: str) -> str:
    """Return the reverse of s, purely recursively."""
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
