"""Rung 2: Fluency drill — memoize the segmenter.

Topic: string DP via @cache + indexing by position.

`can_segment(s, words)` decides whether `s` can be split into a
sequence of dictionary words. Currently exponential. Add @cache to a
helper indexed by position (not by sliced string), and convert
`words` to a set for O(1) lookup.

You should NOT slice s itself in the recursion — pass the start index.
"""
from functools import cache


def can_segment(s: str, words: list[str]) -> bool:
    word_set = set(words)
    max_len = max(map(len, word_set), default=0)

    # TODO: decorate with @cache; keep the helper indexed by `i`,
    # not by the substring.
    def from_index(i: int) -> bool:
        if i == len(s):
            return True
        for L in range(1, min(max_len, len(s) - i) + 1):
            if s[i:i + L] in word_set and from_index(i + L):
                return True
        return False

    return from_index(0)
