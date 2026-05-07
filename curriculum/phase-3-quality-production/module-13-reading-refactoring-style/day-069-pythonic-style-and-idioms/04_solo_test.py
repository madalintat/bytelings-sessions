"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    text = "the quick brown fox the lazy dog the"
    assert ex.top_words(text, 2) == [("the", 3), ("brown", 1)]


def test_case_insensitive():
    assert ex.top_words("Hello hello HELLO", 1) == [("hello", 3)]


def test_punctuation_stripped():
    assert ex.top_words("hello, world! hello.", 2) == [("hello", 2), ("world", 1)]


def test_tie_break_alphabetical():
    text = "banana apple cherry"
    assert ex.top_words(text, 3) == [("apple", 1), ("banana", 1), ("cherry", 1)]


def test_n_bigger_than_unique():
    assert ex.top_words("a b a", 10) == [("a", 2), ("b", 1)]


def test_n_zero_or_negative():
    assert ex.top_words("a b", 0) == []
    assert ex.top_words("a b", -1) == []


def test_empty_text():
    assert ex.top_words("", 3) == []
