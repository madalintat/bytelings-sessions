"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_default_items_is_empty_list():
    c = ex.Cart(owner="Mada")
    assert c.items == []


def test_carts_have_independent_lists():
    a = ex.Cart(owner="Mada")
    b = ex.Cart(owner="Other")
    a.items.append("apple")
    assert b.items == [], "carts must not share their items list"


def test_explicit_items():
    c = ex.Cart(owner="Mada", items=["x"])
    assert c.items == ["x"]


def test_repr_is_useful():
    c = ex.Cart(owner="Mada")
    r = repr(c)
    assert "Cart" in r and "owner" in r and "items" in r
