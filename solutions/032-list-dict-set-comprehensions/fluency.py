"""Rung 2: Fluency drill — replace the loops with comprehensions.

Topic: list / dict / set comprehensions

Each function below uses an explicit loop. Rewrite the body as a single
comprehension that returns the same value.
"""


def squares(n: int) -> list[int]:
    """Return [0, 1, 4, 9, ..., (n-1)**2]."""
    # TODO: replace this loop with a list comprehension
    out = []
    for i in range(n):
        out.append(i * i)
    return out


def by_length(words: list[str]) -> dict[str, int]:
    """Map each word to its length. Last write wins on duplicates."""
    # TODO: replace this loop with a dict comprehension
    out = {}
    for w in words:
        out[w] = len(w)
    return out
