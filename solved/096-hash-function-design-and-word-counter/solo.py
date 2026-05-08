"""Rung 4: Solo — solved version.

top_words collects word counts (same regex as word_counts in rung 3),
then sorts by (-count, word) so that higher counts come first and
alphabetical order breaks ties. Slicing to k handles both the
"k < unique words" and "k >= unique words" cases.
"""
import re


def top_words(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most common words, desc by count, alpha on ties."""
    counts: dict[str, int] = {}
    for w in re.findall(r"[a-zA-Z']+", text):
        w = w.lower()
        counts[w] = counts.get(w, 0) + 1
    ranked = sorted(counts.items(), key=lambda p: (-p[1], p[0]))
    return ranked[:k]
