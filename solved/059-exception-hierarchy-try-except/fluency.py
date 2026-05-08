"""Rung 2: Fluency — solved version.

`int("not a number")` raises `ValueError`. `dict[missing_key]` raises
`KeyError`, which is a subclass of `LookupError`. Catching the widest
possible type (`Exception`) hides bugs — use the narrowest type that
the specific operation can raise.
"""


def safe_int(text: str) -> int:
    """Parse `text` as an int. Return 0 on parse failure."""
    try:
        return int(text)
    except ValueError:
        return 0


def safe_get(mapping: dict, key: str) -> str | None:
    """Return mapping[key], or None if the key is missing."""
    try:
        return mapping[key]
    except KeyError:
        return None
