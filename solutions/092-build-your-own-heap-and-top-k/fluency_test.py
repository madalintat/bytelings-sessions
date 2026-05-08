"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_parent_root():
    assert ex.parent_index(0) == 0


def test_parent_one():
    assert ex.parent_index(1) == 0
    assert ex.parent_index(2) == 0


def test_parent_two():
    assert ex.parent_index(3) == 1
    assert ex.parent_index(4) == 1


def test_parent_deeper():
    assert ex.parent_index(5) == 2
    assert ex.parent_index(6) == 2
    assert ex.parent_index(10) == 4


def test_smaller_child_left_smaller():
    assert ex.smaller_child_index([1, 3, 5], 0) == 1


def test_smaller_child_right_smaller():
    assert ex.smaller_child_index([1, 5, 3], 0) == 2


def test_smaller_child_only_left():
    assert ex.smaller_child_index([1, 5], 0) == 1


def test_smaller_child_no_children():
    assert ex.smaller_child_index([1, 2, 3], 1) == -1
