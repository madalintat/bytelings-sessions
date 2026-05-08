"""Rung 3: Guided — solved version.

`jaccard` is `|a ∩ b| / |a ∪ b|`, using Python's set operators:
  - `a & b` is the intersection.
  - `a | b` is the union.

The "both empty" special case is the only tricky part: when both sets are
empty, the union is also empty, which would cause division by zero. By
convention this function returns 1.0 (the sets are "maximally similar").

The result is cast to float explicitly by dividing with `/` (not `//`).
"""


def jaccard(a: set, b: set) -> float:
    """Return Jaccard similarity: |a ∩ b| / |a ∪ b|.

    >>> jaccard({1, 2, 3}, {2, 3, 4})
    0.5
    >>> jaccard({1, 2}, {1, 2})
    1.0
    >>> jaccard(set(), set())
    1.0
    >>> jaccard({1}, set())
    0.0
    """
    union = a | b
    if not union:
        return 1.0
    return len(a & b) / len(union)
