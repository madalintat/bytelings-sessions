"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_total_empty():
    o = ex.Order(id=1)
    assert ex.total(o) == 0


def test_total_basic():
    o = ex.Order(id=1, items=[ex.Item("a", 100), ex.Item("b", 250)])
    assert ex.total(o) == 350


def test_orders_have_independent_items():
    a = ex.Order(id=1)
    b = ex.Order(id=2)
    a.items.append(ex.Item("x", 10))
    assert b.items == [], "orders must not share an items list"


def test_item_is_frozen():
    item = ex.Item(name="x", price_cents=10)
    with pytest.raises(FrozenInstanceError):
        item.price_cents = 999


def test_item_is_hashable():
    s = {ex.Item("x", 10), ex.Item("x", 10), ex.Item("y", 20)}
    assert len(s) == 2


def test_order_is_mutable():
    o = ex.Order(id=1)
    o.items.append(ex.Item("x", 5))
    assert ex.total(o) == 5
