"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.parallel_sum_of_squares([1, 2, 3, 4]) == 30


def test_empty():
    assert ex.parallel_sum_of_squares([]) == 0


def test_negatives():
    assert ex.parallel_sum_of_squares([-1, -2, 3]) == 14


def test_uses_process_pool():
    src = inspect.getsource(ex.parallel_sum_of_squares)
    assert "ProcessPoolExecutor" in src, "use ProcessPoolExecutor"
    assert "ThreadPoolExecutor" not in src, "use processes, not threads"


def test_calls_top_level_worker():
    src = inspect.getsource(ex.parallel_sum_of_squares)
    assert "_square" in src, "use the top-level `_square` worker"


def test_large_input():
    items = list(range(1, 1001))
    expected = sum(i * i for i in items)
    assert ex.parallel_sum_of_squares(items) == expected
