"""Rung 3: Guided implement — measure hash quality, then a word counter.

Topic: chi-squared-ish bucket distribution, then a real Counter use.
"""
from typing import Callable


def bucket_distribution(values: list[str], hash_fn: Callable[[str], int],
                        n_buckets: int) -> list[int]:
    """Hash each value, mod by n_buckets, count how many land in each bucket.

    Returns a list of length n_buckets. The good news is this is one
    line of bookkeeping — but you'll write it yourself for clarity.

    >>> bucket_distribution(["a", "b", "c"], lambda s: 0, 4)
    [3, 0, 0, 0]
    """
    # TODO
    raise NotImplementedError


def collision_score(values: list[str], hash_fn: Callable[[str], int],
                    n_buckets: int) -> float:
    """Return a "spread quality" score in [0.0, 1.0].

    Compute the bucket distribution. The IDEAL distribution is uniform:
    every bucket gets len(values)/n_buckets items. We compare actual vs
    ideal and scale.

    Formula (a simple, learnable one):
        ideal     = len(values) / n_buckets
        worst     = max(0, len(values) - n_buckets)   # everything in one bucket
        excess    = sum(max(0, count - ideal) for count in distribution)
                    -- how much "extra" piled up in over-full buckets
        if worst == 0:
            return 1.0
        score     = 1.0 - excess / worst
        return clamp(score, 0.0, 1.0)

    A perfectly-uniform hash function scores 1.0. A "everything to one
    bucket" hash scores ~0.0.
    """
    # TODO
    raise NotImplementedError


def word_counts(text: str) -> dict[str, int]:
    """Return a {word: count} dict for `text`. Words are runs of
    [a-zA-Z'] (apostrophes allowed inside words). Case-folded to lower.

    >>> sorted(word_counts("Hello, hello world!").items())
    [('hello', 2), ('world', 1)]
    """
    # TODO: use re.findall (or a tiny manual scan), then accumulate counts.
    raise NotImplementedError
