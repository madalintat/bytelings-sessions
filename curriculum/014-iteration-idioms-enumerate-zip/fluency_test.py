"""Tests for rung 2."""
import inspect
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_numbered_lines():
    assert ex.numbered_lines(["alpha", "bravo", "charlie"]) == [
        "1: alpha", "2: bravo", "3: charlie",
    ]


def test_numbered_lines_empty():
    assert ex.numbered_lines([]) == []


def test_numbered_lines_uses_enumerate():
    src = inspect.getsource(ex.numbered_lines)
    assert "enumerate(" in src, "Use enumerate(items, start=1)"


def test_pair_up():
    assert ex.pair_up(["alice", "bob"], [90, 85]) == ["alice: 90", "bob: 85"]


def test_pair_up_uses_zip():
    src = inspect.getsource(ex.pair_up)
    assert "zip(" in src, "Use zip(names, scores)"


def test_to_dict():
    assert ex.to_dict(["a", "b"], [1, 2]) == {"a": 1, "b": 2}


def test_to_dict_uses_zip():
    src = inspect.getsource(ex.to_dict)
    assert "zip(" in src, "Use dict(zip(keys, values))"
