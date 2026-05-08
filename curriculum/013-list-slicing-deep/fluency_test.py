"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_first_n():
    assert ex.first_n([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert ex.first_n([1, 2, 3], 0) == []


def test_first_n_more_than_len():
    assert ex.first_n([1, 2], 10) == [1, 2]


def test_shallow_copy_equal_but_not_same():
    src = [1, 2, 3]
    out = ex.shallow_copy(src)
    assert out == src
    assert out is not src


def test_replace_middle_same_size():
    items = [1, 2, 3, 4, 5]
    out = ex.replace_middle(items, [99, 99])
    assert out == [1, 99, 99, 4, 5]
    assert out is items


def test_replace_middle_grow():
    items = [1, 2, 3, 4, 5]
    out = ex.replace_middle(items, [9, 9, 9])
    assert out == [1, 9, 9, 9, 4, 5]


def test_replace_middle_shrink():
    items = [1, 2, 3, 4, 5]
    out = ex.replace_middle(items, [])
    assert out == [1, 4, 5]


def test_reverse_in_place_mutates():
    items = [1, 2, 3]
    out = ex.reverse_in_place(items)
    assert out is items, "must mutate, not return a new list"
    assert items == [3, 2, 1]
