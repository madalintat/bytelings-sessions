"""Rung 3: Guided — solved version.

`word_count` uses the `d.get(k, 0) + 1` pattern: if `k` isn't in `d`
yet, `.get` returns 0, so the first occurrence sets the count to 1.
Subsequent occurrences increment from there.

Alternative: `Counter(text.split())` (Day 20). But for Day 18, the
purpose is to show the underlying dict pattern so it's not magic.

`text.split()` with no args splits on any whitespace and drops empty
tokens, so both `""` and `"   \\n\\t "` correctly return `{}`.
"""


def word_count(text: str) -> dict[str, int]:
    """Count words by occurrence.

    >>> word_count("the cat sat on the mat")
    {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
    >>> word_count("")
    {}
    >>> word_count("a a a")
    {'a': 3}
    """
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
