"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_contains_yes():
    assert ex.contains([1, 2, 3], 2) is True


def test_contains_no():
    assert ex.contains([1, 2, 3], 5) is False


def test_contains_empty():
    assert ex.contains([], 1) is False


def test_contains_with_strings():
    # Note: == not `is` (some short strings are interned, others aren't)
    assert ex.contains(["alice", "bob"], "alice") is True


def test_find_first_present():
    assert ex.find_first([10, 20, 30, 20], 20) == 1


def test_find_first_absent_returns_minus_one():
    assert ex.find_first([1, 2, 3], 999) == -1


def test_find_first_empty():
    assert ex.find_first([], "x") == -1


def test_count_matches_basic():
    assert ex.count_matches([1, 2, 3, 4], lambda x: x % 2 == 0) == 2


def test_count_matches_none():
    assert ex.count_matches([1, 3, 5], lambda x: x % 2 == 0) == 0


def test_count_matches_empty():
    assert ex.count_matches([], lambda x: True) == 0
