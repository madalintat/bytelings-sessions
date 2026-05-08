"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_yields_three_values():
    assert list(ex.Range3()) == [0, 1, 2]


def test_for_loop():
    seen = []
    for v in ex.Range3():
        seen.append(v)
    assert seen == [0, 1, 2]


def test_iter_returns_self():
    r = ex.Range3()
    assert iter(r) is r


def test_stop_iteration_after_three():
    r = ex.Range3()
    next(r)
    next(r)
    next(r)
    import pytest
    with pytest.raises(StopIteration):
        next(r)
