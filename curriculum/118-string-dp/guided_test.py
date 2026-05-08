"""Tests for rung 3 — can_break_naive (no memoization)."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_true():
    result = ex.can_break_naive("leetcode", ["leet", "code"])
    diagnose(
        result is True,
        "can_break_naive('leetcode', ['leet','code']) should be True.",
        (lambda: result is False,
         "'leetcode' = 'leet' + 'code'. The recursion should find this split."),
    )


def test_applepenapple():
    result = ex.can_break_naive("applepenapple", ["apple", "pen"])
    diagnose(
        result is True,
        "can_break_naive('applepenapple', ...) should be True.",
        (lambda: result is False,
         "'applepenapple' = 'apple' + 'pen' + 'apple'. Words can be reused."),
    )


def test_false_catsandog():
    result = ex.can_break_naive("catsandog", ["cats", "dog", "sand", "and", "cat"])
    diagnose(
        result is False,
        "can_break_naive('catsandog', ...) should be False.",
        (lambda: result is True,
         "No split leaves 'catsandog' fully covered. "
         "Make sure solve() returns False when all paths fail."),
    )


def test_empty_string():
    diagnose(
        ex.can_break_naive("", ["a"]) is True,
        "Empty string should return True (vacuously segmented).",
        (lambda: ex.can_break_naive("", ["a"]) is False,
         "Base case: when i == len(s) == 0, return True immediately."),
    )


def test_single_word():
    diagnose(
        ex.can_break_naive("a", ["a"]) is True,
        "Single character that is in words should be True.",
    )


def test_false_no_match():
    result = ex.can_break_naive("abc", ["ab", "bc"])
    diagnose(
        result is False,
        "can_break_naive('abc', ['ab','bc']) should be False ('ab'+'bc' overlaps 'b').",
        (lambda: result is True,
         "'ab'+'bc' would require 'b' to be counted twice. "
         "Segments must tile the string end-to-end without overlap."),
    )
