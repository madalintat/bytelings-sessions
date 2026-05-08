"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_immediate_success():
    @ex.retry
    def f():
        return "ok"

    assert f() == "ok"
    assert f.successes == 2
    assert f.failures == 0


def test_recovers_after_two_failures():
    state = {"n": 0}

    @ex.retry
    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise RuntimeError("nope")
        return "good"

    assert flaky() == "good"
    assert flaky.successes == 1
    assert flaky.failures == 2


def test_three_failures_raise():
    @ex.retry
    def always_bad():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always_bad()
    assert always_bad.successes == 0
    assert always_bad.failures == 3


def test_preserves_name():
    @ex.retry
    def my_fn():
        return 1

    assert my_fn.__name__ == "my_fn"


def test_passes_args_and_kwargs():
    @ex.retry
    def add(a, b=0):
        return a + b

    assert add(1, b=2) == 3
