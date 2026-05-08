"""Rung 4: Solo — solved version.

Identical recursion to can_break_naive, but @functools.cache turns the
exponential worst case into O(n²): each position i is computed once and
the result reused for all call sites that reach the same suffix.

The pathological case "a"*30+"b" with words=["a","aa","aaa","aaaa","aaaaa"]
runs in microseconds with the cache; without it, it would take minutes.

Pattern: P-28 (memoize-recursive)
"""
import functools


def can_break(s: str, words: list[str]) -> bool:
    word_set = set(words)

    # @cache keys on i alone — safe because word_set is captured from the
    # outer scope (not a parameter), so the closure is unique per call to
    # can_break. Each fresh call to can_break creates a new solve closure
    # and therefore a fresh cache.
    @functools.cache
    def solve(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False

    return solve(0)
