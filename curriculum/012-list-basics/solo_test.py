"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.rotate([], 5) == []


def test_zero():
    assert ex.rotate([1, 2, 3], 0) == [1, 2, 3]


def test_basic_right():
    assert ex.rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_basic_left():
    assert ex.rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]


def test_full_cycle():
    assert ex.rotate([1, 2, 3], 3) == [1, 2, 3]


def test_more_than_length():
    assert ex.rotate([1, 2, 3], 7) == [3, 1, 2]


def test_does_not_mutate():
    src = [1, 2, 3]
    ex.rotate(src, 1)
    assert src == [1, 2, 3]


def test_returns_new_list():
    src = [1, 2, 3]
    out = ex.rotate(src, 0)
    assert out == src
    assert out is not src
