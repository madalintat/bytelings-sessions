"""Rung 2: Fluency drill — defaultdict and Counter.

Topic: collapse 'if key not in d' ceremonies.
"""
from collections import defaultdict, Counter


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first character.

    Use defaultdict(list).
    Return a plain dict at the end (so 'in d' doesn't create keys for callers).
    """
    # TODO: rewrite using defaultdict(list)
    groups = {}
    for w in words:
        if not w:
            continue
        key = w[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return groups


def count_words(text: str) -> dict[str, int]:
    """Count words split on whitespace. Return a plain dict.

    Use Counter, then convert with dict(...).
    """
    # TODO: this is the slow loop; use Counter
    counts = {}
    for w in text.split():
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts


def top_n_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the top-n most common words as (word, count) pairs.

    Order: descending by count.
    Use Counter.most_common.
    """
    # TODO: handcrafted sort; Counter has most_common(n)
    counts = {}
    for w in text.split():
        counts[w] = counts.get(w, 0) + 1
    pairs = sorted(counts.items(), key=lambda kv: -kv[1])
    return pairs[:n]
