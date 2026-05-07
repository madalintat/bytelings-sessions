"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_three_times():
    assert ex.repeat_word("hi", "-", 3) == "hi-hi-hi"


def test_zero_times():
    assert ex.repeat_word("x", ", ", 0) == ""


def test_one_time_no_sep():
    assert ex.repeat_word("x", ", ", 1) == "x"


def test_empty_word():
    assert ex.repeat_word("", "-", 3) == "--"


def test_long_repeat_is_fast():
    """If you used += in a loop, this would still pass but be slow.
    The key is correctness — speed is the takeaway from the concept page."""
    out = ex.repeat_word("a", "", 1000)
    assert out == "a" * 1000


def test_returns_string():
    assert isinstance(ex.repeat_word("a", "-", 2), str)
