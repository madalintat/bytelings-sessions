"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def slow_inner(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


def fast_inner(n):
    return n


def driver(n):
    slow_inner(n)
    fast_inner(n)
    return n


def test_identifies_slow_function():
    out = ex.bottleneck(driver, 100_000)
    assert isinstance(out, str)
    assert "slow_inner" in out
    assert "fast_inner" not in out


def test_format_has_time_and_calls():
    out = ex.bottleneck(driver, 50_000)
    # rough format check: contains a float-with-s and n=
    assert "s n=" in out
    assert "slow_inner" in out


def test_trivial_no_callees():
    """No user-level callees besides func itself -> 'no bottleneck'."""
    out = ex.bottleneck(lambda: 42)
    assert out == "no bottleneck"
