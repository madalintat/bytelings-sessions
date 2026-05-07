"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_within_limit():
    rl = ex.make_rate_limiter(3)
    assert rl(lambda: 1) == 1
    assert rl(lambda: 2) == 2
    assert rl(lambda: 3) == 3


def test_blocked_after_limit():
    rl = ex.make_rate_limiter(2)
    rl(lambda: "ok")
    rl(lambda: "ok")
    assert rl(lambda: "ok") == "__rate_limited__"


def test_rate_limited_does_not_call():
    """When rate-limited, fn should NOT be called (no side effects)."""
    calls = []
    rl = ex.make_rate_limiter(0)
    out = rl(lambda: calls.append("oops"))
    assert out == "__rate_limited__"
    assert calls == []


def test_independent_limiters():
    a = ex.make_rate_limiter(1)
    b = ex.make_rate_limiter(1)
    assert a(lambda: "a") == "a"
    assert b(lambda: "b") == "b"
    assert a(lambda: "a") == "__rate_limited__"
    assert b(lambda: "b") == "__rate_limited__"


def test_passes_args_and_kwargs():
    rl = ex.make_rate_limiter(5)
    assert rl(lambda x, y=0: x + y, 3, y=4) == 7
