"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _build(values: list) -> "ex.Node | None":
    head = None
    for v in reversed(values):
        head = ex.Node(v, head)
    return head


def test_length_empty():
    assert ex.length(None) == 0


def test_length_one():
    assert ex.length(_build([42])) == 1


def test_length_three():
    assert ex.length(_build([1, 2, 3])) == 3


def test_values_empty():
    assert ex.values(None) == []


def test_values_one():
    assert ex.values(_build(["a"])) == ["a"]


def test_values_three():
    assert ex.values(_build([1, 2, 3])) == [1, 2, 3]
