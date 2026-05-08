"""Tests for rung 2."""
import ast
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_count_up_to_basic():
    assert list(ex.count_up_to(3)) == [1, 2, 3]


def test_count_up_to_zero():
    assert list(ex.count_up_to(0)) == []


def test_flatten_basic():
    assert list(ex.flatten([[1, 2], [3], [4, 5]])) == [1, 2, 3, 4, 5]


def test_flatten_empty():
    assert list(ex.flatten([])) == []


def test_flatten_uses_yield_from():
    """flatten must use `yield from`, not a nested loop."""
    src = (_HERE / "02_fluency.py").read_text()
    tree = ast.parse(src)
    flatten = next(
        n for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name == "flatten"
    )
    has_yield_from = any(
        isinstance(node, ast.YieldFrom) for node in ast.walk(flatten)
    )
    assert has_yield_from, "flatten should use `yield from`"
