"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero_power():
    assert ex.power(2, 0) == 1
    assert ex.power(99, 0) == 1


def test_one_power():
    assert ex.power(7, 1) == 7


def test_small():
    assert ex.power(2, 5) == 32
    assert ex.power(3, 4) == 81


def test_one_base():
    assert ex.power(1, 100) == 1


def test_zero_base():
    assert ex.power(0, 5) == 0
