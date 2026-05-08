"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def double(x):
    return x * 2


def test_io_threads():
    out = ex.run("io", double, [1, 2, 3])
    assert out == [2, 4, 6]


def test_cpu_processes():
    # `double` is module-level, so it's importable for child processes.
    out = ex.run("cpu", double, [1, 2, 3])
    assert out == [2, 4, 6]


def test_invalid_raises():
    with pytest.raises(ValueError):
        ex.run("magic", double, [1, 2])


def test_empty_items():
    assert ex.run("io", double, []) == []
