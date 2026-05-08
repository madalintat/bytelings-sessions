"""Rung 3: Guided implement — solved version.

Build a list of "k=v" strings first, then join with "; ". This is
O(n) work and O(n) total string allocation, versus O(n^2) for +=.
"""


def format_pairs(pairs: list[tuple[str, str]]) -> str:
    """Return 'k1=v1; k2=v2; ...' or '' if pairs is empty."""
    parts = [f"{k}={v}" for k, v in pairs]
    return "; ".join(parts)
