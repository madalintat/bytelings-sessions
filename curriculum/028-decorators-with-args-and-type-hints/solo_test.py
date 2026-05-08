"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_pass():
    @ex.validate(x=lambda x: x > 0, y=lambda y: y < 100)
    def f(x, y):
        return x + y

    assert f(1, 2) == 3


def test_fails_on_x():
    @ex.validate(x=lambda x: x > 0)
    def f(x):
        return x

    with pytest.raises(ValueError):
        f(0)


def test_fails_on_y():
    @ex.validate(x=lambda x: x > 0, y=lambda y: y < 100)
    def f(x, y):
        return x + y

    with pytest.raises(ValueError):
        f(1, 100)


def test_works_with_kwargs():
    @ex.validate(x=lambda x: x > 0)
    def f(x):
        return x

    assert f(x=5) == 5


def test_unknown_check_ignored():
    @ex.validate(does_not_exist=lambda _: False)
    def f(x):
        return x

    assert f(1) == 1


def test_no_check_for_param_means_anything_goes():
    @ex.validate(x=lambda x: x > 0)
    def f(x, y):
        return (x, y)

    # y has no check; even silly values pass
    assert f(1, "anything") == (1, "anything")


def test_preserves_name():
    @ex.validate(x=lambda x: True)
    def my_fn(x):
        return x

    assert my_fn.__name__ == "my_fn"
