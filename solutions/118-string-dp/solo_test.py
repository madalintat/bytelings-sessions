"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_true():
    assert ex.can_break("leetcode", ["leet", "code"]) is True


def test_applepenapple():
    assert ex.can_break("applepenapple", ["apple", "pen"]) is True


def test_false_catsandog():
    assert ex.can_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_empty_string():
    assert ex.can_break("", ["a"]) is True


def test_single_word():
    assert ex.can_break("a", ["a"]) is True


def test_false_no_match():
    assert ex.can_break("abc", ["ab", "bc"]) is False


def test_reuse_words():
    assert ex.can_break("aaaa", ["a", "aa"]) is True


def test_pathological_fast():
    """Must complete in well under a second — requires @functools.cache."""
    import time
    s = "a" * 30 + "b"
    words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    t0 = time.monotonic()
    result = ex.can_break(s, words)
    elapsed = time.monotonic() - t0
    assert result is False
    assert elapsed < 1.0, (
        f"can_break took {elapsed:.2f}s — did you add @functools.cache? "
        "Without it this case is exponential."
    )
