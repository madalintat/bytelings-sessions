"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.top_n_lengths(["a", "abcd", "ab", "abc"], 2) == [4, 3]


def test_more_n_than_items():
    assert ex.top_n_lengths(["xx", "y"], 5) == [2, 1]


def test_n_zero():
    assert ex.top_n_lengths(["a", "b"], 0) == []


def test_n_negative():
    assert ex.top_n_lengths(["a", "b"], -1) == []


def test_ties_break_by_position():
    # Both length 3 — "foo" appears before "bar", so "foo"'s length comes first.
    assert ex.top_n_lengths(["foo", "bar", "x"], 2) == [3, 3]


def test_accepts_generator_input():
    src = (s for s in ["a", "abc", "ab"])
    assert ex.top_n_lengths(src, 1) == [3]


def test_empty_input():
    assert ex.top_n_lengths([], 3) == []
