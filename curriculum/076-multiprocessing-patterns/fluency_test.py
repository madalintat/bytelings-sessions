"""Tests for rung 2."""
import inspect
from pathlib import Path

from _byte import load_rung

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
ex = load_rung(_HERE / "fluency.py", _NAME)


def test_correctness():
    out = ex.compute([1, 2, 3, 4])
    assert out == [2, 5, 10, 17]


def test_worker_at_module_level():
    assert hasattr(ex, "_worker"), "define top-level `_worker` function"


def test_lambda_removed():
    src = inspect.getsource(ex.compute)
    assert "lambda" not in src, "remove the lambda — pass `_worker` to pool.map"
