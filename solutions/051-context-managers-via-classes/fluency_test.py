"""Tests for rung 2."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_with():
    t = ex.Tracer()
    with t as got:
        assert got is t
        t.log("hi")
    assert t.events == ["enter", "log:hi", "exit"]


def test_exit_runs_on_exception():
    t = ex.Tracer()
    with pytest.raises(RuntimeError):
        with t:
            t.log("before")
            raise RuntimeError("boom")
    assert t.events == ["enter", "log:before", "exit"]


def test_exit_does_not_suppress():
    """__exit__ returning False (or None) lets the exception propagate."""
    t = ex.Tracer()
    with pytest.raises(ValueError):
        with t:
            raise ValueError("x")
