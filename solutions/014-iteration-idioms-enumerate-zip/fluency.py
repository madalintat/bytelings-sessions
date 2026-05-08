"""Rung 2: Fluency drill — pythonic iteration.

Topic: enumerate, zip
"""


def numbered_lines(items: list[str]) -> list[str]:
    """Return ['1: alpha', '2: bravo', ...] (1-based)."""
    # TODO: rewrite with enumerate(items, start=1)
    out = []
    for i in range(len(items)):
        out.append(f"{i + 1}: {items[i]}")
    return out


def pair_up(names: list[str], scores: list[int]) -> list[str]:
    """Return ['alice: 90', 'bob: 85', ...]. Inputs are same length.

    Rewrite with zip — no indexing.
    """
    # TODO: use zip
    out = []
    for i in range(len(names)):
        out.append(f"{names[i]}: {scores[i]}")
    return out


def to_dict(keys: list, values: list) -> dict:
    """Build a dict from parallel keys and values, in O(n)."""
    # TODO: dict + zip is a one-liner
    out = {}
    for i in range(len(keys)):
        out[keys[i]] = values[i]
    return out
