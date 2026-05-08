"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def busy(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


def test_context_manager_returns_self():
    p = ex.Profiler()
    with p as got:
        busy(100)
    assert got is p


def test_top_n_is_string_with_function_names():
    with ex.Profiler() as p:
        busy(2000)
    out = p.top_n(5)
    assert isinstance(out, str)
    assert "busy" in out


def test_total_time_positive():
    with ex.Profiler() as p:
        busy(50_000)
    assert p.total_time() > 0


def test_does_not_swallow_exceptions():
    with pytest.raises(ValueError):
        with ex.Profiler():
            raise ValueError("boom")
