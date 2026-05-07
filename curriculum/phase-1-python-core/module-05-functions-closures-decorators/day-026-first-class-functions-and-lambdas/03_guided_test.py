"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    add1 = lambda x: x + 1
    times2 = lambda x: x * 2
    pipeline = ex.compose(add1, times2)
    assert pipeline(3) == 8


def test_three_functions_with_str():
    pipeline = ex.compose(lambda x: x + 1, lambda x: x * 2, str)
    assert pipeline(3) == "8"


def test_no_functions_is_identity():
    f = ex.compose()
    assert f(5) == 5
    assert f("hi") == "hi"


def test_one_function():
    f = ex.compose(lambda x: x + 1)
    assert f(10) == 11


def test_order_left_to_right():
    """compose(f, g) should be g(f(x)), not f(g(x))."""
    sub1 = lambda x: x - 1
    div2 = lambda x: x / 2
    # (10 - 1) / 2 = 4.5
    assert ex.compose(sub1, div2)(10) == 4.5
    # (10 / 2) - 1 = 4.0
    assert ex.compose(div2, sub1)(10) == 4.0
