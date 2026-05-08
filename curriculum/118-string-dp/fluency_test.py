"""Tests for rung 2 — word-break prediction.

Each test checks your intuition against the actual recursive answer.
"""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


# Reference implementation used to check predictions
def _can_break(s: str, words: list[str]) -> bool:
    word_set = set(words)

    def solve(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False

    return solve(0)


def test_leetcode():
    s, words = "leetcode", ["leet", "code"]
    actual = _can_break(s, words)
    prediction = ex.predict_break(s, words)
    diagnose(
        prediction == actual,
        f"predict_break({s!r}, {words}) returned {prediction!r}, "
        f"but the correct answer is {actual!r}.",
        (lambda: prediction is True and actual is False,
         f"{s!r} CANNOT be broken — check that every character is covered."),
        (lambda: prediction is False and actual is True,
         f"{s!r} CAN be broken: 'leet' + 'code'. "
         "Walk left-to-right: does 'leet' match? yes. Does 'code' match? yes."),
    )


def test_applepenapple():
    s, words = "applepenapple", ["apple", "pen"]
    actual = _can_break(s, words)
    prediction = ex.predict_break(s, words)
    diagnose(
        prediction == actual,
        f"predict_break({s!r}, ...) returned {prediction!r}, correct is {actual!r}.",
        (lambda: prediction is False and actual is True,
         "'applepenapple' = 'apple' + 'pen' + 'apple'. Words CAN be reused."),
    )


def test_catsandog():
    s, words = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    actual = _can_break(s, words)
    prediction = ex.predict_break(s, words)
    diagnose(
        prediction == actual,
        f"predict_break({s!r}, ...) returned {prediction!r}, correct is {actual!r}.",
        (lambda: prediction is True and actual is False,
         "'catsandog' ends in 'og' which no word covers. "
         "Every split leaves a suffix that cannot be matched."),
    )


def test_aaab():
    s, words = "aaab", ["a", "aa", "aaa"]
    actual = _can_break(s, words)
    prediction = ex.predict_break(s, words)
    diagnose(
        prediction == actual,
        f"predict_break({s!r}, ...) returned {prediction!r}, correct is {actual!r}.",
        (lambda: prediction is True and actual is False,
         "'aaab' always ends with 'b', which is not in the word set. "
         "No segmentation can consume the final 'b'."),
    )
