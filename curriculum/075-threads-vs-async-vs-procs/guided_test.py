"""Tests for rung 3."""
from pathlib import Path

import pytest

from _byte import load_rung

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
ex = load_rung(_HERE / "guided.py", _NAME)


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
