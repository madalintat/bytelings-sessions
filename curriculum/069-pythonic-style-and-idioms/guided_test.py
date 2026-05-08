"""Tests for rung 3."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_count_levels_basic():
    lines = [
        "INFO startup",
        "INFO ready",
        "ERROR db down",
        "WARN slow query",
        "ERROR retry failed",
    ]
    assert ex.count_levels(lines) == {"INFO": 2, "ERROR": 2, "WARN": 1}


def test_count_levels_empty_or_blank():
    assert ex.count_levels([]) == {}
    assert ex.count_levels(["nowhitespace"]) == {}


def test_percentages_basic():
    out = ex.percentages({"INFO": 1, "ERROR": 3})
    assert out == {"INFO": 25.0, "ERROR": 75.0}


def test_percentages_empty():
    assert ex.percentages({}) == {}


def test_count_uses_defaultdict():
    src = inspect.getsource(ex.count_levels)
    assert "defaultdict" in src, "use collections.defaultdict(int)"


def test_percentages_uses_comprehension():
    src = inspect.getsource(ex.percentages)
    # dict comprehension: { ... for ... in ... }
    assert "{" in src and " for " in src and ":" in src, (
        "use a dict comprehension"
    )
