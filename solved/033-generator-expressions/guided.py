"""Rung 3: Guided — solved version.

`next(generator, default)` short-circuits on the first matching item
without materialising the rest of the iterable. The two-argument form
of `next` avoids a bare `StopIteration` reaching the caller — we get
`None` back instead.
"""


def first_match(strings, needle: str) -> str | None:
    """Return the first string containing `needle` (case-insensitive), else None.

    >>> first_match(["Foo", "Bar", "Baz"], "ba")
    'Bar'
    >>> first_match(["a", "b"], "z") is None
    True
    """
    return next((s for s in strings if needle.lower() in s.lower()), None)
