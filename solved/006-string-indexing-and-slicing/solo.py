"""Rung 4: Solo — solved version.

The canonical palindrome check normalises the string first, then
compares it to its reverse.

Normalisation steps:
  1. Lowercase: 'Racecar' -> 'racecar'.
  2. Keep only alphanumeric characters: `''.join(c for c in s if c.isalnum())`.
     This strips spaces, commas, colons, etc.

After that, comparing the result to `result[::-1]` is a single
expression that handles empty strings correctly (empty == empty -> True).

Alternative shape: a two-pointer walk from both ends, which avoids
building the cleaned string twice, but is harder to read and only
matters at scale. The slice form is the right default.
"""


def is_palindrome(s: str) -> bool:
    cleaned = "".join(c for c in s.lower() if c.isalnum())
    return cleaned == cleaned[::-1]
