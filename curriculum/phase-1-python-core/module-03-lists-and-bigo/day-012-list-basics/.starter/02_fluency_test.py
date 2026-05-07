"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_head():
    assert ex.head([1, 2, 3]) == 1
    assert ex.head(["a"]) == "a"


def test_tail():
    assert ex.tail([1, 2, 3]) == 3
    assert ex.tail(["only"]) == "only"


def test_append_in_place():
    items = [1, 2]
    out = ex.append_x(items, 3)
    assert items == [1, 2, 3], "must mutate the input list"
    assert out is items, "must return the same list, not a copy"


def test_replace_first():
    items = [1, 2, 3]
    out = ex.replace_first(items, 99)
    assert items == [99, 2, 3]
    assert out is items
