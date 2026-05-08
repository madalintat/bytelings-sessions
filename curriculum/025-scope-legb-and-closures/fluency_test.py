"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_counter_increments():
    c = ex.make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test_counters_independent():
    c1 = ex.make_counter()
    c2 = ex.make_counter()
    assert c1() == 1
    assert c1() == 2
    assert c2() == 1


def test_multiplier_basic():
    times3 = ex.make_multiplier(3)
    assert times3(5) == 15
    assert times3(0) == 0


def test_multiplier_returns_callable():
    assert callable(ex.make_multiplier(2))


def test_make_listeners_basic():
    fs = ex.make_listeners(3)
    assert [f() for f in fs] == [0, 1, 2]


def test_make_listeners_zero():
    assert ex.make_listeners(0) == []
