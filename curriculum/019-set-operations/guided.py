"""Rung 3: Guided implement.

Topic: a Jaccard similarity score using sets

Implement `jaccard(a, b)`: the Jaccard similarity is the size of the
intersection divided by the size of the union.
"""


def jaccard(a: set, b: set) -> float:
    """Return Jaccard similarity: |a ∩ b| / |a ∪ b|.

    Special case: if BOTH sets are empty, return 1.0 (defined as
    "fully similar" by convention here).

    >>> jaccard({1, 2, 3}, {2, 3, 4})
    0.5
    >>> jaccard({1, 2}, {1, 2})
    1.0
    >>> jaccard(set(), set())
    1.0
    >>> jaccard({1}, set())
    0.0
    >>> jaccard({1, 2, 3}, {4, 5, 6})
    0.0

    Always returns a float.
    """
    # TODO: handle the both-empty edge case, then |a&b| / |a|b|.
    raise NotImplementedError
