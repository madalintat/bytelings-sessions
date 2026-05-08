"""Rung 4: Solo — can_break with @functools.cache.

Topic: memoized backtracking, bridging search and DP.

Pattern: P-28 (memoize-recursive)

Take the same recursion as can_break_naive but add @functools.cache.
One decorator turns exponential into O(n²).

Pathological case — WITHOUT cache this hangs:
    s = "a" * 30 + "b"
    words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
  Each position has 5 word choices, and every path eventually fails
  on the trailing "b". Without caching, the same suffix is re-explored
  from every ancestor. With @cache, each position is visited once.

>>> can_break("leetcode", ["leet", "code"])
True
>>> can_break("catsandog", ["cats","dog","sand","and","cat"])
False

Tests in solo_test.py are HIDDEN — do not peek before solving.
"""
import functools


def can_break(s: str, words: list[str]) -> bool:
    """Return True iff s can be segmented into words, using memoization.

    Same shape as can_break_naive, but with @functools.cache on the
    inner solve() function. Because solve() is keyed on the integer
    position i, the cache has at most len(s)+1 entries.
    """
    word_set = set(words)

    # TODO: decorate solve with @functools.cache
    def solve(i: int) -> bool:
        # TODO: same body as can_break_naive
        raise NotImplementedError

    return solve(0)
