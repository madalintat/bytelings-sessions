"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_in_range():
    assert ex.clamp(5, 0, 10) == 5


def test_below_range():
    assert ex.clamp(-3, 0, 10) == 0


def test_above_range():
    assert ex.clamp(99, 0, 10) == 10


def test_at_low_boundary():
    assert ex.clamp(0, 0, 10) == 0


def test_at_high_boundary():
    assert ex.clamp(10, 0, 10) == 10
