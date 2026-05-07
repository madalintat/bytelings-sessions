"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.top_words("a b a c b a", 2) == [("a", 3), ("b", 2)]


def test_ties_alphabetical():
    assert ex.top_words("zebra apple banana apple zebra", 2) == [
        ("apple", 2),
        ("zebra", 2),
    ]


def test_k_larger_than_unique():
    out = ex.top_words("a b c d", 10)
    assert out == [("a", 1), ("b", 1), ("c", 1), ("d", 1)]


def test_empty():
    assert ex.top_words("", 5) == []


def test_case_folded():
    assert ex.top_words("Hello hello HELLO world", 1) == [("hello", 3)]


def test_apostrophe_word():
    out = ex.top_words("it's it's its", 2)
    assert out == [("it's", 2), ("its", 1)]


def test_strips_punctuation():
    out = ex.top_words("hello, world! hello?", 1)
    assert out == [("hello", 2)]
