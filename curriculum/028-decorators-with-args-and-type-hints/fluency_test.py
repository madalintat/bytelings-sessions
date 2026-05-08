"""Tests for rung 2."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_repeat_basic():
    @ex.repeat(3)
    def f(x):
        return x * 2

    assert f(5) == [10, 10, 10]


def test_repeat_zero():
    @ex.repeat(0)
    def f():
        return 1

    assert f() == []


def test_repeat_one():
    @ex.repeat(1)
    def f():
        return "ok"

    assert f() == ["ok"]


def test_repeat_preserves_name():
    @ex.repeat(2)
    def my_function():
        """Doc."""
        return 1

    assert my_function.__name__ == "my_function"


def test_tag_attaches_label():
    @ex.tag("my_label")
    def f():
        return 1

    assert f.label == "my_label"


def test_tag_preserves_name_and_call():
    @ex.tag("x")
    def my_fn():
        return 42

    assert my_fn.__name__ == "my_fn"
    assert my_fn() == 42


def test_validate_positive_zero_raises():
    @ex.validate_positive
    def f(x):
        return x

    with pytest.raises(ValueError):
        f(0)


def test_validate_positive_negative_raises():
    @ex.validate_positive
    def f(x):
        return x

    with pytest.raises(ValueError):
        f(-1)


def test_validate_positive_positive_ok():
    @ex.validate_positive
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
