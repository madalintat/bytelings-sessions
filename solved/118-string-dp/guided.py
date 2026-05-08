"""Rung 3: Guided — solved version.

Plain recursive backtracking — no caching. Exponential on adversarial
inputs but correct. The inner solve(i) tries every split point j; when
s[i:j] is in the word set and the remainder solve(j) succeeds, return
True. If nothing works, return False.

Pattern: P-28 (memoize-recursive) — this is the un-memoized baseline.
"""


def can_break_naive(s: str, words: list[str]) -> bool:
    word_set = set(words)

    def solve(i: int) -> bool:
        if i == len(s):
            return True  # consumed the whole string
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False  # no split from i leads to a full segmentation

    return solve(0)
