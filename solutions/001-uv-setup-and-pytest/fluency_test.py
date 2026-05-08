"""Tests for rung 2 — should be green after both TODOs are fixed."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_greet_basic():
    assert ex.greet("Bytelinger") == "Hello, Bytelinger!"


def test_greet_empty():
    assert ex.greet("") == "Hello, !"


def test_add_one():
    assert ex.add_one(0) == 1
    assert ex.add_one(41) == 42
    assert ex.add_one(-5) == -4
