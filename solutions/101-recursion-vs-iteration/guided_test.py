"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_reverse_basic():
    assert ex.reverse_iter([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_reverse_empty():
    assert ex.reverse_iter([]) == []


def test_reverse_one():
    assert ex.reverse_iter(["a"]) == ["a"]


def test_reverse_does_not_mutate_input():
    src = [1, 2, 3]
    _ = ex.reverse_iter(src)
    assert src == [1, 2, 3]


def test_depth_flat():
    assert ex.tree_depth([1, 2, 3]) == 1


def test_depth_empty():
    assert ex.tree_depth([]) == 1


def test_depth_two():
    assert ex.tree_depth([1, [2, 3], 4]) == 2


def test_depth_deep():
    assert ex.tree_depth([1, [2, [3, [4]]]]) == 4


def test_depth_branching():
    assert ex.tree_depth([[1, [2]], [[3]], 4]) == 3
