"""Rung 4: Solo — solved version.

`letter_diff` computes the "signed difference" between two character
multisets using Counter arithmetic.

Key insight: `Counter(a) - Counter(b)` keeps only POSITIVE counts
(letters more frequent in `a`). `Counter(b) - Counter(a)` keeps counts
more frequent in `b`. We need BOTH directions.

Algorithm:
  1. Build Counter objects for a and b.
  2. For each unique char across both, compute `ca[c] - cb[c]`.
  3. Skip chars where the difference is zero.

Alternatively:
  pos = Counter(a) - Counter(b)  # a-surplus (only positive)
  neg = Counter(b) - Counter(a)  # b-surplus (only positive, but will be negated)
  result = {k: v for k, v in pos.items()}
  result.update({k: -v for k, v in neg.items()})

The union-of-keys approach is slightly cleaner:
"""
from collections import Counter


def letter_diff(a: str, b: str) -> dict[str, int]:
    ca = Counter(a)
    cb = Counter(b)
    all_chars = set(ca) | set(cb)
    result = {}
    for c in all_chars:
        diff = ca[c] - cb[c]
        if diff != 0:
            result[c] = diff
    return result
