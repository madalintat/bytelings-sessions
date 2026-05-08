"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_caches():
    memo = ex.make_memoizer()
    calls = []

    def f(x):
        calls.append(x)
        return x * 2

    fast = memo(f)
    assert fast(5) == 10
    assert fast(5) == 10
    assert calls == [5]


def test_different_args_call_again():
    memo = ex.make_memoizer()
    calls = []

    def f(x):
        calls.append(x)
        return x

    fast = memo(f)
    fast(1)
    fast(2)
    fast(1)
    assert calls == [1, 2]


def test_kwargs_in_cache_key():
    memo = ex.make_memoizer()
    calls = []

    def f(x, y=0):
        calls.append((x, y))
        return x + y

    fast = memo(f)
    assert fast(1, y=2) == 3
    assert fast(1, y=2) == 3
    assert fast(1, y=3) == 4
    assert calls == [(1, 2), (1, 3)]


def test_independent_memos():
    memo = ex.make_memoizer()
    calls = []

    def f(x):
        calls.append(x)
        return x

    a = memo(f)
    b = memo(f)
    a(1)
    b(1)
    assert calls == [1, 1]   # each wrapper has its own cache


def test_returns_value_correctly():
    memo = ex.make_memoizer()
    fast = memo(lambda x: x ** 2)
    assert fast(7) == 49
