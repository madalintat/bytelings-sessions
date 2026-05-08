"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.last_or([1, 2, 3], 0) == 3


def test_empty_returns_default():
    assert ex.last_or([], "fallback") == "fallback"


def test_single_item():
    assert ex.last_or([42], 0) == 42


def test_works_for_strings():
    assert ex.last_or(["a", "b"], "z") == "b"


def test_default_used_for_empty_list_of_dicts():
    fallback = {"empty": True}
    assert ex.last_or([], fallback) is fallback
