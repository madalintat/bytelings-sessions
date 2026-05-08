"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = [
    {"id": 17, "name": "Alice", "active": True},
    {"id": 32, "name": "Bob", "active": False},
    {"id": 41, "name": "Carol", "active": True},
]


def test_index_by_id_basic():
    out = ex.index_by_id(SAMPLE)
    assert out == {
        17: {"id": 17, "name": "Alice", "active": True},
        32: {"id": 32, "name": "Bob", "active": False},
        41: {"id": 41, "name": "Carol", "active": True},
    }


def test_index_by_id_empty():
    assert ex.index_by_id([]) == {}


def test_find_user_present():
    idx = ex.index_by_id(SAMPLE)
    assert ex.find_user(idx, 32)["name"] == "Bob"


def test_find_user_missing():
    assert ex.find_user({1: {"name": "X"}}, 999) is None


def test_names_sorted():
    idx = ex.index_by_id(SAMPLE)
    assert ex.names_sorted(idx) == ["Alice", "Bob", "Carol"]


def test_names_sorted_alpha_not_id_order():
    # Carol has the highest id, but should be 3rd alphabetically
    idx = {
        99: {"name": "Alice"},
        1: {"name": "Bob"},
        50: {"name": "Carol"},
    }
    assert ex.names_sorted(idx) == ["Alice", "Bob", "Carol"]
