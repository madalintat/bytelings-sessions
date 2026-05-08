"""Rung 3: Guided implement.

Topic: a function that returns one of a fixed set of strings

Implement `classify(score)`:
- If score >= 90, return "A"
- If score >= 70, return "B"
- If score >= 50, return "C"
- Otherwise return "F"

Type the return as Literal["A", "B", "C", "F"] so callers know the
exact set of possible outputs.
"""
from typing import Literal


Grade = Literal["A", "B", "C", "F"]


def classify(score: int) -> Grade:
    """Return a single-character grade for the score."""
    # TODO: 4-line if/elif/else.
    raise NotImplementedError
