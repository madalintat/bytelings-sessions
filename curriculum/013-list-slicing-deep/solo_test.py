"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_equal_lengths():
    assert ex.interleave([1, 2, 3], ["a", "b", "c"]) == [1, "a", 2, "b", 3, "c"]


def test_a_longer():
    assert ex.interleave([1, 2, 3, 4, 5], ["a", "b"]) == [1, "a", 2, "b", 3, 4, 5]


def test_b_longer():
    assert ex.interleave([1], ["a", "b", "c"]) == [1, "a", "b", "c"]


def test_a_empty():
    assert ex.interleave([], [1, 2]) == [1, 2]


def test_b_empty():
    assert ex.interleave([1, 2], []) == [1, 2]


def test_both_empty():
    assert ex.interleave([], []) == []


def test_does_not_mutate():
    a = [1, 2, 3]
    b = ["x", "y"]
    ex.interleave(a, b)
    assert a == [1, 2, 3]
    assert b == ["x", "y"]
