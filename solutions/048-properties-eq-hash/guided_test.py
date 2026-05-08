"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_area():
    r = ex.Rectangle(3, 4)
    assert r.area == 12


def test_perimeter():
    r = ex.Rectangle(3, 4)
    assert r.perimeter == 14


def test_area_no_parens():
    """area must be a property, not a method — accessed without ()."""
    r = ex.Rectangle(2, 5)
    assert r.area == 10
    # If area were a method, r.area would be a bound method, not 10.
    assert not callable(r.area)


def test_area_recomputes():
    r = ex.Rectangle(2, 3)
    assert r.area == 6
    r.width = 10
    assert r.area == 30


def test_area_is_readonly():
    r = ex.Rectangle(2, 3)
    with pytest.raises(AttributeError):
        r.area = 999
