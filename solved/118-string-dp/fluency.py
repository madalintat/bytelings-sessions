"""Rung 2: Fluency drill — solved version.

Predictions filled in by reasoning:
  "applepenapple" + ["apple","pen"] → True  (apple + pen + apple)
  "catsandog"     + mixed words     → False ('og' tail uncovered)
  "aaab"          + ["a","aa","aaa"]→ False ('b' never consumed)
"""


def predict_break(s: str, words: list[str]) -> bool:
    cases = {
        ("leetcode", ("leet", "code")): True,
        ("applepenapple", ("apple", "pen")): True,   # words can repeat
        ("catsandog", ("cats", "dog", "sand", "and", "cat")): False,  # trailing 'og'
        ("aaab", ("a", "aa", "aaa")): False,          # 'b' unmatched
    }
    for (ks, kw), prediction in cases.items():
        if ks == s and set(kw) == set(words):
            return prediction
    raise ValueError(f"Unknown input {s!r}")
