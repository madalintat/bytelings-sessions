"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_returns_zero():
    assert ex.elapsed_seconds([], True) == 0.0
    assert ex.elapsed_seconds([], False) == 0.0


def test_sequential():
    assert ex.elapsed_seconds([1.0, 2.0, 3.0], False) == 6.0


def test_concurrent():
    assert ex.elapsed_seconds([1.0, 2.0, 3.0], True) == 3.0


def test_one_item():
    assert ex.elapsed_seconds([5.0], True) == 5.0
    assert ex.elapsed_seconds([5.0], False) == 5.0


def test_zero_durations():
    assert ex.elapsed_seconds([0.0, 0.0], True) == 0.0
    assert ex.elapsed_seconds([0.0, 0.0], False) == 0.0
