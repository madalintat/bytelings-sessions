"""Tests for rung 2 — should be green once both bodies use generator expressions."""
import ast
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_sum_of_squares_basic():
    assert ex.sum_of_squares(5) == 0 + 1 + 4 + 9 + 16


def test_sum_of_squares_zero():
    assert ex.sum_of_squares(0) == 0


def test_any_negative_true():
    assert ex.any_negative([1, 2, -0.5, 3]) is True


def test_any_negative_false():
    assert ex.any_negative([1, 2, 3]) is False


def test_any_negative_empty():
    assert ex.any_negative([]) is False


def test_no_list_comprehensions():
    """Both bodies must use a generator expression, not a list comp."""
    src = (_HERE / "fluency.py").read_text()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        assert not isinstance(node, ast.ListComp), (
            "list comprehension found — use a generator expression `(...)` instead"
        )
