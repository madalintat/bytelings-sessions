"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_list():
    assert ex.mean([]) == 0.0


def test_single():
    assert ex.mean([7]) == 7.0


def test_two():
    assert ex.mean([1, 3]) == 2.0


def test_negative_and_positive():
    assert ex.mean([-1, 1]) == 0.0


def test_returns_float():
    assert isinstance(ex.mean([1, 2, 3]), float)
