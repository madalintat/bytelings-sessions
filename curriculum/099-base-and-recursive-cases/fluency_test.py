"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_factorial_base():
    assert ex.factorial(0) == 1
    assert ex.factorial(1) == 1


def test_factorial_small():
    assert ex.factorial(5) == 120


def test_factorial_ten():
    assert ex.factorial(10) == 3628800


def test_length_empty():
    assert ex.length([]) == 0


def test_length_basic():
    assert ex.length([10, 20, 30]) == 3


def test_length_one():
    assert ex.length(["x"]) == 1
