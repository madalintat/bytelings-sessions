"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_forward_zero():
    assert ex.forward(0) == []


def test_forward_three():
    assert ex.forward(3) == [1, 2, 3]


def test_forward_five():
    assert ex.forward(5) == [1, 2, 3, 4, 5]


def test_backward_zero():
    assert ex.backward(0) == []


def test_backward_three():
    assert ex.backward(3) == [3, 2, 1]


def test_backward_five():
    assert ex.backward(5) == [5, 4, 3, 2, 1]
