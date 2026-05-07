"""Tests for rung 3."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_immediate_success():
    @ex.retry(times=3)
    def f():
        return "ok"

    assert f() == "ok"
    assert f.attempts == 1


def test_recovers():
    state = {"n": 0}

    @ex.retry(times=3)
    def maybe():
        state["n"] += 1
        if state["n"] < 2:
            raise RuntimeError("nope")
        return "ok"

    assert maybe() == "ok"
    assert maybe.attempts == 2


def test_all_fail_raises():
    @ex.retry(times=3)
    def always():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always()
    assert always.attempts == 3


def test_only_catches_on():
    @ex.retry(times=3, on=ValueError)
    def raises_other():
        raise RuntimeError("not caught")

    with pytest.raises(RuntimeError):
        raises_other()
    # Only one attempt — RuntimeError isn't caught
    assert raises_other.attempts == 1


def test_invalid_times_raises_at_decoration():
    with pytest.raises(ValueError):
        @ex.retry(times=0)
        def f():
            return 1


def test_attempts_resets_per_call():
    @ex.retry(times=2)
    def f():
        return "ok"

    f()
    f()
    f()
    assert f.attempts == 1


def test_preserves_name():
    @ex.retry(times=2)
    def my_fn():
        return 1

    assert my_fn.__name__ == "my_fn"
