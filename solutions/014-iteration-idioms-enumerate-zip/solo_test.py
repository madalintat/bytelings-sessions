"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.running_diffs([10, 12, 9, 14]) == [2, -3, 5]


def test_empty():
    assert ex.running_diffs([]) == []


def test_single():
    assert ex.running_diffs([42]) == []


def test_two():
    assert ex.running_diffs([1, 5]) == [4]


def test_constant():
    assert ex.running_diffs([7, 7, 7, 7]) == [0, 0, 0]


def test_floats():
    out = ex.running_diffs([1.5, 2.0, 1.0])
    assert out == [0.5, -1.0]


def test_does_not_mutate():
    src = [1, 2, 3]
    ex.running_diffs(src)
    assert src == [1, 2, 3]
