"""Rung 2: Fluency drill — narrow the exception types.

Topic: catching the right thing in the exception hierarchy.

Both functions catch `Exception`. That hides bugs. Replace each with
the narrowest exception type that the body could legitimately raise.
"""


def safe_int(text: str) -> int:
    """Parse `text` as an int. Return 0 on parse failure."""
    try:
        return int(text)
    # TODO: this catches everything — narrow it to the specific
    # exception that int("not a number") raises.
    except Exception:
        return 0


def safe_get(mapping: dict, key: str) -> str | None:
    """Return mapping[key], or None if the key is missing."""
    try:
        return mapping[key]
    # TODO: narrow this to the specific exception that dict[missing]
    # raises. Hint: it lives under LookupError.
    except Exception:
        return None
