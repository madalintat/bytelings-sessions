"""Tests for rung 2."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_correctness():
    out = ex.compute([1, 2, 3, 4])
    assert out == [2, 5, 10, 17]


def test_worker_at_module_level():
    assert hasattr(ex, "_worker"), "define top-level `_worker` function"


def test_lambda_removed():
    src = inspect.getsource(ex.compute)
    assert "lambda" not in src, "remove the lambda — pass `_worker` to pool.map"
