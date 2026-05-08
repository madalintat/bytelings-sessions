"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.word_count("the cat sat on the mat") == {
        "the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1,
    }


def test_empty():
    assert ex.word_count("") == {}


def test_only_whitespace():
    assert ex.word_count("   \n\t ") == {}


def test_one_word_repeated():
    assert ex.word_count("a a a") == {"a": 3}


def test_case_sensitive():
    assert ex.word_count("The the") == {"The": 1, "the": 1}


def test_returns_dict():
    assert isinstance(ex.word_count("a b c"), dict)


def test_insertion_order():
    """First-seen order is preserved by dict (Py 3.7+)."""
    out = ex.word_count("z y x z y")
    assert list(out.keys()) == ["z", "y", "x"]
