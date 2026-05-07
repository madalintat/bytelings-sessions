"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_commits_on_success():
    store = {"a": 1}
    with ex.Transaction(store):
        store["b"] = 2
    assert store == {"a": 1, "b": 2}


def test_rolls_back_on_exception():
    store = {"a": 1}
    with pytest.raises(RuntimeError):
        with ex.Transaction(store):
            store["b"] = 2
            store["a"] = 99
            raise RuntimeError("boom")
    assert store == {"a": 1}


def test_rollback_does_not_swallow_exception():
    store = {}
    with pytest.raises(ValueError):
        with ex.Transaction(store):
            raise ValueError("x")


def test_empty_store():
    store = {}
    with ex.Transaction(store):
        store["x"] = 1
    assert store == {"x": 1}


def test_rollback_on_empty_store():
    store = {}
    with pytest.raises(KeyError):
        with ex.Transaction(store):
            store["x"] = 1
            raise KeyError("x")
    assert store == {}


def test_snapshot_is_independent_of_later_changes_to_original():
    """The snapshot must be a copy, not a reference, so mid-transaction
    mutations don't sneak into the rollback target."""
    store = {"a": 1}
    with pytest.raises(RuntimeError):
        with ex.Transaction(store):
            store["a"] = 999
            raise RuntimeError("boom")
    assert store == {"a": 1}
