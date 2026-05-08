"""Tests for rung 3."""
import importlib.util
import math
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def make_calls_counter():
    calls = [0]

    def is_positive(state):
        calls[0] += 1
        return state > 0

    return is_positive, calls


def test_no_failure_returns_none():
    is_ok, _ = make_calls_counter()
    changes = [lambda s: s + 1 for _ in range(8)]
    assert ex.bisect_failures(1, changes, is_ok) is None


def test_first_change_breaks():
    is_ok, _ = make_calls_counter()
    changes = [lambda s: s - 100, lambda s: s + 1]
    assert ex.bisect_failures(1, changes, is_ok) == 0


def test_middle_change_breaks():
    is_ok, _ = make_calls_counter()
    # 1 -> 2 -> 3 -> 4 -> -10 -> -9
    changes = [
        lambda s: s + 1,
        lambda s: s + 1,
        lambda s: s + 1,
        lambda s: s - 14,
        lambda s: s + 1,
    ]
    assert ex.bisect_failures(1, changes, is_ok) == 3


def test_logarithmic_call_count():
    """With 1024 changes, is_ok must be called at most ~12 times."""
    is_ok, calls = make_calls_counter()
    n = 1024
    bad_at = 700
    changes = [
        (lambda s: s - 1_000_000) if i == bad_at else (lambda s: s + 1)
        for i in range(n)
    ]
    result = ex.bisect_failures(1, changes, is_ok)
    assert result == bad_at
    # log2(1024) = 10; allow a couple extra (initial + boundary).
    limit = int(math.log2(n)) + 3
    assert calls[0] <= limit, f"too many is_ok calls: {calls[0]} > {limit}"
