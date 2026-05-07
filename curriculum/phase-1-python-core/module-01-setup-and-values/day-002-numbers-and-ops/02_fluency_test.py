"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_cents_to_dollars_basic():
    assert ex.cents_to_dollars(150) == 1.5


def test_cents_to_dollars_zero():
    assert ex.cents_to_dollars(0) == 0.0


def test_is_divisible_yes():
    assert ex.is_divisible(10, 5) is True


def test_is_divisible_no():
    assert ex.is_divisible(10, 3) is False
