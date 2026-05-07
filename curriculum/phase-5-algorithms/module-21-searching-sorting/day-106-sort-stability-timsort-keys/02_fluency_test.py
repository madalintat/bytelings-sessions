"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_name_then_age():
    people = [("Bob", 30), ("Alice", 25), ("Bob", 22), ("Alice", 40)]
    assert ex.sort_by_name_then_age(people) == [
        ("Alice", 25), ("Alice", 40), ("Bob", 22), ("Bob", 30)
    ]


def test_name_then_age_empty():
    assert ex.sort_by_name_then_age([]) == []


def test_age_desc_then_name():
    people = [("Bob", 30), ("Alice", 30), ("Carol", 22), ("Bob", 22)]
    assert ex.sort_descending_age_then_name(people) == [
        ("Alice", 30), ("Bob", 30), ("Bob", 22), ("Carol", 22)
    ]


def test_age_desc_single():
    assert ex.sort_descending_age_then_name([("X", 1)]) == [("X", 1)]
