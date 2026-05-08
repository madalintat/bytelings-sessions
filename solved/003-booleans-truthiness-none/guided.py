"""Rung 3: Guided — solved version.

The trap: `value if value else fallback` returns the fallback for
ANY falsy value (None, 0, "", [], False). The docstring is explicit
that 0 and "" should be returned unchanged — they are NOT None.

Correct check: `is not None`. Use `is` (identity) for None
because there's exactly one None object in any Python process —
`x is None` is the canonical sentinel test.
"""


def default_if_none(value, fallback):
    """
    >>> default_if_none(None, "x")
    'x'
    >>> default_if_none("", "x")
    ''
    >>> default_if_none(0, 99)
    0
    """
    return value if value is not None else fallback
