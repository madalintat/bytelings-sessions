"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = [
    {"id": 1, "email": "a@x.io", "name": "Alice"},
    {"id": 2, "email": "b@x.io", "name": "Bob"},
    {"id": 3, "email": "c@x.io", "name": "Carol"},
]


def test_by_id_present():
    r = ex.Roster(SAMPLE)
    assert r.by_id(2)["name"] == "Bob"


def test_by_id_missing():
    r = ex.Roster(SAMPLE)
    assert r.by_id(99) is None


def test_by_email_present():
    r = ex.Roster(SAMPLE)
    assert r.by_email("c@x.io")["name"] == "Carol"


def test_by_email_missing():
    r = ex.Roster(SAMPLE)
    assert r.by_email("nope@x.io") is None


def test_names_sorted():
    r = ex.Roster(SAMPLE)
    assert r.names_sorted() == ["Alice", "Bob", "Carol"]


def test_names_sorted_handles_unsorted_input():
    rs = [
        {"id": 1, "email": "x@x", "name": "Zach"},
        {"id": 2, "email": "y@x", "name": "Anna"},
    ]
    r = ex.Roster(rs)
    assert r.names_sorted() == ["Anna", "Zach"]


def test_empty():
    r = ex.Roster([])
    assert r.by_id(1) is None
    assert r.by_email("a@x") is None
    assert r.names_sorted() == []
