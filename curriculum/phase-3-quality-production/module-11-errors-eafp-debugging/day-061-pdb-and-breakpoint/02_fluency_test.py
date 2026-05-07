"""Tests for rung 2."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple():
    assert ex.running_average([10.0]) == [10.0]


def test_two_values():
    assert ex.running_average([10.0, 20.0]) == [10.0, 15.0]


def test_three_values():
    assert ex.running_average([3.0, 6.0, 9.0]) == [3.0, 4.5, 6.0]


def test_empty():
    assert ex.running_average([]) == []


def test_breakpoint_removed():
    """Once the bug is fixed, take the breakpoint() line back out."""
    src = inspect.getsource(ex.running_average)
    assert "breakpoint()" not in src, "remove your breakpoint() before shipping"
