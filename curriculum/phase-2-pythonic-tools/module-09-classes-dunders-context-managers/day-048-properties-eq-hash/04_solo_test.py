"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    t = ex.Temperature(20.0)
    assert t.celsius == 20.0


def test_below_absolute_zero_raises_in_init():
    with pytest.raises(ValueError):
        ex.Temperature(-300.0)


def test_setter_validates():
    t = ex.Temperature(0.0)
    with pytest.raises(ValueError):
        t.celsius = -300


def test_setter_works():
    t = ex.Temperature(0.0)
    t.celsius = 100.0
    assert t.celsius == 100.0


def test_fahrenheit():
    assert ex.Temperature(0).fahrenheit == 32.0
    assert ex.Temperature(100).fahrenheit == 212.0


def test_fahrenheit_readonly():
    t = ex.Temperature(0)
    with pytest.raises(AttributeError):
        t.fahrenheit = 999


def test_equality():
    assert ex.Temperature(20.0) == ex.Temperature(20.0)
    assert ex.Temperature(20.0) != ex.Temperature(21.0)


def test_hash_consistency():
    a = ex.Temperature(20.0)
    b = ex.Temperature(20.0)
    assert hash(a) == hash(b)


def test_works_in_set():
    s = {ex.Temperature(0), ex.Temperature(0), ex.Temperature(100)}
    assert len(s) == 2


def test_repr():
    assert repr(ex.Temperature(20)) == "Temperature(20)"
