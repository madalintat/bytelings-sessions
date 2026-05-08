"""Rung 4: Solo implement — solved version.

Tokenize with strip(punctuation), count with Counter, sort by
(-count, word) for descending count with alphabetical tie-break,
then take the top n via most_common or manual slice.
"""
import string
from collections import Counter


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    if n <= 0:
        return []
    tokens = (
        word.strip(string.punctuation).lower()
        for word in text.split()
    )
    counts = Counter(tok for tok in tokens if tok)
    # Sort: count DESC, word ASC for ties.
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:n]
