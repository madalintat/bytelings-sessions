"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_in_order():
    out = ex.parallel_apply([1, 2, 3, 4], lambda x: x * x)
    assert out == [1, 4, 9, 16]


def test_empty():
    assert ex.parallel_apply([], lambda x: x) == []


def test_errors_returned_not_raised():
    def half(n):
        if n == 0:
            raise ZeroDivisionError("nope")
        return 100 // n

    out = ex.parallel_apply([1, 2, 0, 4], half)
    assert out[0] == 100
    assert out[1] == 50
    assert isinstance(out[2], ZeroDivisionError)
    assert out[3] == 25


def test_actually_parallel():
    """10 sleeps of 80ms must complete in << 0.4s on a thread pool."""
    def sleep_then_id(n):
        time.sleep(0.08)
        return n

    items = list(range(10))
    start = time.perf_counter()
    out = ex.parallel_apply(items, sleep_then_id, max_workers=10)
    elapsed = time.perf_counter() - start
    assert out == items
    assert elapsed < 0.4, f"not parallel? took {elapsed:.2f}s"
