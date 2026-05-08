"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_basics():
    t = ex.BST()
    assert len(t) == 0
    assert bool(t) is False
    assert t.min() is None
    assert t.max() is None
    assert list(t) == []


def test_insert_single():
    t = ex.BST()
    t.insert(5)
    assert len(t) == 1
    assert 5 in t
    assert t.min() == 5
    assert t.max() == 5


def test_insert_many_sorted_iter():
    t = ex.BST()
    for x in [5, 3, 7, 1, 4, 6, 8]:
        t.insert(x)
    assert list(t) == [1, 3, 4, 5, 6, 7, 8]
    assert len(t) == 7


def test_duplicates_ignored():
    t = ex.BST()
    for x in [5, 3, 5, 3, 5]:
        t.insert(x)
    assert list(t) == [3, 5]
    assert len(t) == 2


def test_contains_hits_and_misses():
    t = ex.BST()
    for x in [5, 3, 7]:
        t.insert(x)
    assert (3 in t) is True
    assert (4 in t) is False
    assert t.contains(7) is True
    assert t.contains(99) is False


def test_min_max():
    t = ex.BST()
    for x in [5, 3, 7, 1, 8]:
        t.insert(x)
    assert t.min() == 1
    assert t.max() == 8


def test_iter_is_sorted_after_random_inserts():
    import random
    rnd = random.Random(0)
    values = list(range(50))
    rnd.shuffle(values)
    t = ex.BST()
    for x in values:
        t.insert(x)
    assert list(t) == sorted(values)
