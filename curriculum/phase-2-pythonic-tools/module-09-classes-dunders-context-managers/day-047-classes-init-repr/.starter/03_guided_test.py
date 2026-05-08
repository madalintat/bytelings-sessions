"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    u = ex.User("Bytelinger", 30)
    assert u.name == "Bytelinger"
    assert u.age == 30


def test_repr():
    u = ex.User("Bytelinger", 30)
    assert repr(u) == "User(name='Bytelinger', age=30)"


def test_negative_age_raises():
    with pytest.raises(ValueError):
        ex.User("Bytelinger", -1)


def test_empty_name_raises():
    with pytest.raises(ValueError):
        ex.User("", 30)


def test_zero_age_ok():
    u = ex.User("Newborn", 0)
    assert u.age == 0
