"""Rung 3: Guided implement.

Topic: combining str methods to clean a name

Implement `make_display_name` per the spec.
"""


def make_display_name(raw: str, max_len: int = 20) -> str:
    """Turn a raw user input into a tidy display name.

    Rules:
        - Strip surrounding whitespace.
        - If empty after stripping, return "(anonymous)".
        - Split on whitespace; capitalize each word.
        - Join with single spaces.
        - If the result is longer than `max_len`, truncate to
          `max_len - 1` characters, rstrip, and append a single "…".

    >>> make_display_name("  alice   wonderland ")
    'Alice Wonderland'
    >>> make_display_name("")
    '(anonymous)'
    >>> make_display_name("   ")
    '(anonymous)'
    >>> make_display_name("alpha bravo charlie delta", max_len=15)
    'Alpha Bravo Ch…'
    """
    # TODO: 4-6 lines using strip, split, capitalize, join, slice.
    raise NotImplementedError
