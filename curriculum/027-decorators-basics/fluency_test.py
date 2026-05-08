"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_log_calls_records():
    @ex.log_calls
    def f(x, y=0):
        return x + y

    assert f(1, 2) == 3
    assert f(5) == 5
    assert f.calls == [((1, 2), {}), ((5,), {})]


def test_log_calls_preserves_name():
    @ex.log_calls
    def my_function(x):
        """Doc."""
        return x

    assert my_function.__name__ == "my_function"


def test_log_calls_returns_value():
    @ex.log_calls
    def double(x):
        return x * 2

    assert double(7) == 14


def test_time_calls_records_elapsed():
    @ex.time_calls
    def slow(n):
        # Just spin a tiny loop
        s = 0
        for i in range(n):
            s += i
        return s

    slow(100)
    slow(100)
    assert hasattr(slow, "times")
    assert len(slow.times) == 2
    assert all(isinstance(t, float) for t in slow.times)
    assert all(t >= 0 for t in slow.times)


def test_time_calls_returns_value():
    @ex.time_calls
    def echo(x):
        return x

    assert echo(42) == 42


def test_pre_decorated_add_works_and_records():
    # `add` is decorated at module level
    ex.add.calls.clear()
    assert ex.add(2, 3) == 5
    assert ex.add(10, 20) == 30
    assert ex.add.calls == [((2, 3), {}), ((10, 20), {})]
