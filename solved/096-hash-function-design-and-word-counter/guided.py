"""Rung 3: Guided — solved version.

bucket_distribution: hash each value, mod by n_buckets, and count
  arrivals in a tally list of length n_buckets.

collision_score: compute the ideal load (uniform distribution). Count
  the "excess" — total overshoot above ideal across all buckets.
  The worst case is everything in one bucket (n - n_buckets items of
  excess if n > n_buckets, else 0). Score = 1 - excess / worst.

word_counts: use re.findall with [a-zA-Z']+ to extract words, lower
  everything, then tally with a plain dict accumulator.
"""
import re
from typing import Callable


def bucket_distribution(values: list[str], hash_fn: Callable[[str], int],
                        n_buckets: int) -> list[int]:
    """Count how many values land in each bucket."""
    counts = [0] * n_buckets
    for v in values:
        counts[hash_fn(v) % n_buckets] += 1
    return counts


def collision_score(values: list[str], hash_fn: Callable[[str], int],
                    n_buckets: int) -> float:
    """Return a spread quality in [0.0, 1.0]. 1.0 = perfectly uniform."""
    dist = bucket_distribution(values, hash_fn, n_buckets)
    n = len(values)
    if n == 0:
        return 1.0
    ideal = n / n_buckets
    worst = max(0, n - n_buckets)
    if worst == 0:
        return 1.0
    excess = sum(max(0.0, c - ideal) for c in dist)
    score = 1.0 - excess / worst
    return max(0.0, min(1.0, score))


def word_counts(text: str) -> dict[str, int]:
    """Return {word: count} for text. Words are [a-zA-Z'], lowercased."""
    counts: dict[str, int] = {}
    for w in re.findall(r"[a-zA-Z']+", text):
        w = w.lower()
        counts[w] = counts.get(w, 0) + 1
    return counts
