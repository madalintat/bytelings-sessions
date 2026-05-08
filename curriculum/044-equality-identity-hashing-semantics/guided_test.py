"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_identical():
    a = [1, 2, 3]
    assert ex.relation(a, a) == "identical"


def test_equal_but_not_identical():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert ex.relation(a, b) == "equal"


def test_distinct():
    assert ex.relation([1, 2], [3, 4]) == "distinct"


def test_strings_intern_count_as_identical():
    """Small interned strings often share the same object."""
    # We don't assert "identical" here because interning is implementation-defined.
    # Just check the answer is one of the two equal kinds.
    result = ex.relation("foo", "foo")
    assert result in ("identical", "equal")


def test_none_with_none():
    assert ex.relation(None, None) == "identical"


def test_none_with_zero():
    assert ex.relation(None, 0) == "distinct"
