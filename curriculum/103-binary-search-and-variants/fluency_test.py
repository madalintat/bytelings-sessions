"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_hit():
    assert ex.bsearch([1, 3, 5, 7, 9], 5) == 2


def test_first():
    assert ex.bsearch([1, 3, 5, 7, 9], 1) == 0


def test_last():
    assert ex.bsearch([1, 3, 5, 7, 9], 9) == 4


def test_miss_low():
    assert ex.bsearch([1, 3, 5, 7, 9], 0) == -1


def test_miss_high():
    assert ex.bsearch([1, 3, 5, 7, 9], 10) == -1


def test_miss_middle():
    assert ex.bsearch([1, 3, 5, 7, 9], 4) == -1


def test_single_hit():
    assert ex.bsearch([42], 42) == 0


def test_single_miss():
    assert ex.bsearch([42], 7) == -1


def test_empty():
    assert ex.bsearch([], 7) == -1
