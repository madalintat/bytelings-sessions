"""Rung 3: Guided — solved version.

The `Literal` return type advertises to callers that this function
produces exactly one of four strings. The if/elif chain works from
highest to lowest threshold so the first matching branch is the
correct grade.
"""
from typing import Literal

Grade = Literal["A", "B", "C", "F"]


def classify(score: int) -> Grade:
    """Return a single-character grade for the score."""
    if score >= 90:
        return "A"
    if score >= 70:
        return "B"
    if score >= 50:
        return "C"
    return "F"
