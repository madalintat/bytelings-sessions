"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_finds_first():
    assert ex.first_match(["Foo", "Bar", "Baz"], "ba") == "Bar"


def test_case_insensitive():
    assert ex.first_match(["abc", "DEF"], "de") == "DEF"


def test_no_match_returns_none():
    assert ex.first_match(["a", "b", "c"], "z") is None


def test_empty_iterable():
    assert ex.first_match([], "x") is None


def test_works_on_generator_input():
    """The function must accept any iterable, not only lists."""
    src = (s for s in ["alpha", "beta", "gamma"])
    assert ex.first_match(src, "et") == "beta"
