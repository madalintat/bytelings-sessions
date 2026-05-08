"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.passing_users([(1, 90), (2, 50), (3, 80)], 70) == {1, 3}


def test_empty():
    assert ex.passing_users([], 50) == set()


def test_threshold_inclusive():
    assert ex.passing_users([(1, 70), (2, 69)], 70) == {1}


def test_dedupes_user_ids():
    assert ex.passing_users([(1, 90), (1, 95), (2, 80)], 70) == {1, 2}


def test_returns_a_set():
    result = ex.passing_users([(1, 100)], 50)
    assert isinstance(result, set)
