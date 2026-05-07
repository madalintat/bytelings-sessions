"""Rung 2: Fluency drill — parsing patterns.

Topic: split, strip, filter-and-rejoin
"""


def csv_fields(line: str) -> list[str]:
    """Split on commas and strip each piece."""
    # TODO: pieces are not stripped
    return line.split(",")


def keep_digits(s: str) -> str:
    """Return only the digit characters of `s`, in order."""
    # TODO: this returns the first digit only
    for c in s:
        if c.isdigit():
            return c
    return ""


def split_on_any(s: str, seps: str) -> list[str]:
    """Split `s` on ANY char appearing in `seps`. Drop empty pieces.

    Example: split_on_any('a, b; c', ',;') -> ['a', 'b', 'c']
    """
    # TODO: only splits on the WHOLE seps string at once
    return [p.strip() for p in s.split(seps) if p.strip()]
