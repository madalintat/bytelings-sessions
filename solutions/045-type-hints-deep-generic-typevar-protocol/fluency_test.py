"""Tests for rung 2."""
import importlib.util
from pathlib import Path
from typing import Generic, TypeVar

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_box_value_roundtrip():
    b = ex.Box(7)
    assert b.get() == 7


def test_box_put():
    b = ex.Box("a")
    b.put("b")
    assert b.get() == "b"


def test_T_is_a_typevar():
    assert isinstance(ex.T, TypeVar), (
        "T must be defined as `T = TypeVar('T')`"
    )


def test_box_is_generic_subscriptable():
    """A Generic class can be parameterized: Box[int] should not raise."""
    _ = ex.Box[int]


def test_box_inherits_generic():
    """Box should declare Generic[T] in its bases."""
    # __orig_bases__ is set when a class subclasses a parameterized Generic.
    bases = getattr(ex.Box, "__orig_bases__", ())
    assert any(
        getattr(b, "__origin__", None) is Generic for b in bases
    ), "Box should subclass Generic[T]"
