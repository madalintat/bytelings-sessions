"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    s = ex.HashSet()
    assert len(s) == 0
    assert "anything" not in s


def test_add_and_contains():
    s = ex.HashSet()
    s.add("a")
    assert "a" in s
    assert len(s) == 1


def test_add_dup_is_idempotent():
    s = ex.HashSet()
    s.add("a"); s.add("a"); s.add("a")
    assert len(s) == 1


def test_remove_present():
    s = ex.HashSet()
    s.add("a"); s.add("b")
    s.remove("a")
    assert "a" not in s
    assert len(s) == 1


def test_remove_missing_raises():
    s = ex.HashSet()
    with pytest.raises(KeyError):
        s.remove("nope")


def test_discard_missing_is_noop():
    s = ex.HashSet()
    s.add("a")
    s.discard("nope")
    assert "a" in s
    assert len(s) == 1


def test_discard_present():
    s = ex.HashSet()
    s.add("a")
    s.discard("a")
    assert "a" not in s


def test_iter_yields_all():
    s = ex.HashSet()
    for x in ["a", "b", "c", "d"]:
        s.add(x)
    assert sorted(list(s)) == ["a", "b", "c", "d"]


def test_many_inserts():
    s = ex.HashSet()
    for i in range(200):
        s.add(i)
    for i in range(200):
        assert i in s
    assert len(s) == 200


def test_int_and_tuple_keys():
    s = ex.HashSet()
    s.add(1); s.add((1, 2)); s.add("1")
    assert 1 in s
    assert (1, 2) in s
    assert "1" in s
    assert len(s) == 3
