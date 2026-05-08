"""Rung 2: Fluency — solved version.

Three fluency exercises for defaultdict and Counter:
  1. group_by_first_letter: replace the `if key not in groups` ceremony
     with `defaultdict(list)`. Appending to a missing key auto-creates
     an empty list. Convert to `dict()` before returning so callers
     don't get auto-creation side effects on key misses.
  2. count_words: `Counter(text.split())` counts all words in one call.
     `dict(Counter(...))` gives a plain dict as required.
  3. top_n_words: `Counter.most_common(n)` returns the top-n (word, count)
     pairs sorted by count descending — O(n log n) under the hood.

The tests inspect source code for "defaultdict", "Counter", and
"most_common" respectively.
"""
from collections import defaultdict, Counter


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first character. Return a plain dict."""
    groups: dict[str, list[str]] = defaultdict(list)
    for w in words:
        if not w:
            continue
        groups[w[0]].append(w)
    return dict(groups)


def count_words(text: str) -> dict[str, int]:
    """Count words split on whitespace. Return a plain dict."""
    return dict(Counter(text.split()))


def top_n_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the top-n most common words as (word, count) pairs."""
    return Counter(text.split()).most_common(n)
