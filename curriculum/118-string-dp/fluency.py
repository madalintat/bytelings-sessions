"""Rung 2: Fluency drill — predict word-break outcomes.

Topic: memoized backtracking — recognising when caching matters.

Pattern: P-28 (memoize-recursive)

Before writing the algorithm, build the intuition: for each (s, words)
pair below, predict whether the string CAN be broken into dictionary
words. Return your prediction as True or False.

You may reason on paper — no code needed inside `predict_break`. The
tests run the actual `can_break` algorithm and compare against your
prediction, so if your intuition is wrong the test message tells you why.

Examples to reason about:
  "leetcode"        ["leet", "code"]         → ?
  "applepenapple"   ["apple", "pen"]          → ?
  "catsandog"       ["cats","dog","sand","and","cat"] → ?
  "aaab"            ["a","aa","aaa"]           → ?  (hint: "b" is not in words)
"""


def predict_break(s: str, words: list[str]) -> bool:
    """Return True if you predict s can be segmented into words, else False.

    Reason through each case:
    - Can every character in s be covered by some word?
    - Are there any suffixes that no word in the dictionary covers?

    Replace each `raise NotImplementedError` with True or False.
    """
    # Four cases — each returns your prediction:
    cases = {
        ("leetcode", ("leet", "code")): True,       # example — given to you
        ("applepenapple", ("apple", "pen")): ...,   # TODO: replace ... with True or False
        ("catsandog", ("cats", "dog", "sand", "and", "cat")): ...,  # TODO
        ("aaab", ("a", "aa", "aaa")): ...,          # TODO
    }
    key = (s, tuple(sorted(words)))
    # normalise key lookup (order-independent)
    for (ks, kw), prediction in cases.items():
        if ks == s and set(kw) == set(words):
            if prediction is ...:
                raise NotImplementedError(
                    f"Fill in your prediction for {s!r}. "
                    "Is it True (segmentable) or False (not segmentable)?"
                )
            return prediction
    raise ValueError(f"Unknown input {s!r} — only the four listed cases are tested.")
