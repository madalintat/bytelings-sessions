"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_add():
    a = ex.Money("USD", 100)
    b = ex.Money("USD", 250)
    assert ex.add(a, b) == ex.Money("USD", 350)


def test_different_currencies_raise():
    with pytest.raises(ValueError):
        ex.add(ex.Money("USD", 100), ex.Money("EUR", 100))


def test_money_is_frozen():
    """Mutating a frozen dataclass should raise."""
    from dataclasses import FrozenInstanceError
    m = ex.Money("USD", 100)
    with pytest.raises(FrozenInstanceError):
        m.cents = 999


def test_money_is_hashable():
    """Frozen dataclasses are hashable — must work in a set."""
    s = {ex.Money("USD", 1), ex.Money("USD", 2), ex.Money("USD", 1)}
    assert len(s) == 2


def test_equality():
    assert ex.Money("USD", 100) == ex.Money("USD", 100)
    assert ex.Money("USD", 100) != ex.Money("USD", 200)
