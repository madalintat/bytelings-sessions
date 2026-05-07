"""Rung 3: Guided implement.

Topic: composing generator expressions

Implement `first_match`. Given an iterable of strings and a substring,
return the first string that contains the substring (case-insensitive),
or None if none match.

Use a generator expression with `next(..., default)`. Do NOT build a
full list — bail out at the first hit.
"""


def first_match(strings, needle: str) -> str | None:
    """Return the first string containing `needle` (case-insensitive), else None.

    >>> first_match(["Foo", "Bar", "Baz"], "ba")
    'Bar'
    >>> first_match(["a", "b"], "z") is None
    True
    """
    # TODO: one expression. Pattern: next((s for s in ...), None)
    raise NotImplementedError
