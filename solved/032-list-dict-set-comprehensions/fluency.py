"""Rung 2: Fluency — solved version.

The two functions used explicit `for` + `.append()` loops. The test
enforces no `for` *statements*, so we replace each body with a single
comprehension expression. Comprehensions are not just shorter — they
signal to the reader that a transformation is happening and make the
loop-body side-effect-free.
"""


def squares(n: int) -> list[int]:
    """Return [0, 1, 4, 9, ..., (n-1)**2]."""
    return [i * i for i in range(n)]


def by_length(words: list[str]) -> dict[str, int]:
    """Map each word to its length. Last write wins on duplicates."""
    return {w: len(w) for w in words}
