"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_caches():
    calls = []

    @ex.cache
    def double(x):
        calls.append(x)
        return x * 2

    assert double(3) == 6
    assert double(3) == 6
    assert calls == [3]


def test_different_args_recompute():
    calls = []

    @ex.cache
    def f(x):
        calls.append(x)
        return x

    f(1)
    f(2)
    f(1)
    assert calls == [1, 2]


def test_kwargs_in_key():
    calls = []

    @ex.cache
    def f(x, y=0):
        calls.append((x, y))
        return x + y

    f(1, y=2)
    f(1, y=2)
    f(1, y=3)
    assert calls == [(1, 2), (1, 3)]


def test_cache_attribute_exposed():
    @ex.cache
    def f(x):
        return x

    f(7)
    assert f.cache[((7,), frozenset())] == 7


def test_preserves_name():
    @ex.cache
    def my_fn(x):
        """Doc."""
        return x

    assert my_fn.__name__ == "my_fn"
