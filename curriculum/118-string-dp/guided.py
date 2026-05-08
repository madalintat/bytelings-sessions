"""Rung 3: Guided — plain recursive word break (no caching).

Topic: backtracking tree-of-choices, before the DP optimisation.

Pattern: P-28 (memoize-recursive)

Implement `can_break_naive(s, words)` as a plain recursive search with
NO memoization. It's correct but exponential on adversarial inputs.

The recursion shape (from the README):

    def solve(i):
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False

Fill in the body below. Do NOT add @cache or any memoization here —
that comes in solo.py. The guided_test checks correctness on short inputs
where exponential time is fine.

>>> can_break_naive("leetcode", ["leet", "code"])
True
>>> can_break_naive("catsandog", ["cats", "dog", "sand", "and", "cat"])
False
"""


def can_break_naive(s: str, words: list[str]) -> bool:
    """Return True iff s can be segmented into a sequence of words.

    Uses plain recursive backtracking — no caching. Exponential worst case.

    Args:
        s:     the string to segment
        words: the available vocabulary (words may be reused)
    """
    word_set = set(words)

    def solve(i: int) -> bool:
        # TODO: base case — if i == len(s), the whole string is consumed
        # TODO: try each split point j in range(i+1, len(s)+1):
        #         if s[i:j] is in word_set and solve(j) succeeds, return True
        # TODO: if no split works, return False
        raise NotImplementedError

    return solve(0)
