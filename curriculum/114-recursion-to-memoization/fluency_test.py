"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero():
    assert ex.climb(0) == 1


def test_one():
    assert ex.climb(1) == 1


def test_two():
    assert ex.climb(2) == 2


def test_small():
    assert ex.climb(5) == 8


def test_must_be_fast():
    """If you forgot @cache, this would take forever. With it: instant."""
    assert ex.climb(50) == 20365011074
