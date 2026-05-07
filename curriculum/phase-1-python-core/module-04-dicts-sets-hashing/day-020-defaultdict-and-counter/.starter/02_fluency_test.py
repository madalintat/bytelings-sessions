"""Tests for rung 2."""
import inspect
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_group_by_first_letter_basic():
    out = ex.group_by_first_letter(["apple", "ant", "banana", "berry", "cherry"])
    assert out == {"a": ["apple", "ant"], "b": ["banana", "berry"], "c": ["cherry"]}


def test_group_by_first_letter_uses_defaultdict():
    src = inspect.getsource(ex.group_by_first_letter)
    assert "defaultdict" in src, "Use defaultdict(list)"


def test_group_by_first_letter_empty():
    assert ex.group_by_first_letter([]) == {}


def test_count_words_basic():
    assert ex.count_words("the cat the dog the") == {"the": 3, "cat": 1, "dog": 1}


def test_count_words_uses_counter():
    src = inspect.getsource(ex.count_words)
    assert "Counter" in src, "Use Counter"


def test_count_words_empty():
    assert ex.count_words("") == {}


def test_top_n_words():
    out = ex.top_n_words("the cat the dog the cat", 2)
    assert out == [("the", 3), ("cat", 2)]


def test_top_n_words_uses_most_common():
    src = inspect.getsource(ex.top_n_words)
    assert "most_common" in src, "Use Counter.most_common(n)"
