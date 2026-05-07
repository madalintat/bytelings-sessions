"""Tests for rung 2 — should be green once both functions use comprehensions."""
import ast
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_squares_basic():
    assert ex.squares(5) == [0, 1, 4, 9, 16]


def test_squares_zero():
    assert ex.squares(0) == []


def test_by_length_basic():
    assert ex.by_length(["a", "abc", "hi"]) == {"a": 1, "abc": 3, "hi": 2}


def test_by_length_empty():
    assert ex.by_length([]) == {}


def test_uses_comprehensions():
    """Both bodies must use a comprehension, not a for-loop statement."""
    src = (_HERE / "02_fluency.py").read_text()
    tree = ast.parse(src)
    for fn in [n for n in tree.body if isinstance(n, ast.FunctionDef)]:
        for node in ast.walk(fn):
            assert not isinstance(node, ast.For), (
                f"{fn.name} still has a `for` statement — use a comprehension"
            )
