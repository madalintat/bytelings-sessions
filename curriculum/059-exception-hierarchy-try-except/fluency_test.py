"""Tests for rung 2 — must use narrow exception types, not Exception."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_safe_int_parses():
    assert ex.safe_int("42") == 42
    assert ex.safe_int("-7") == -7


def test_safe_int_returns_zero_on_garbage():
    assert ex.safe_int("N/A") == 0
    assert ex.safe_int("") == 0


def test_safe_get_hits():
    assert ex.safe_get({"a": "x"}, "a") == "x"


def test_safe_get_miss():
    assert ex.safe_get({"a": "x"}, "z") is None


def test_safe_int_does_not_swallow_typeerror():
    """Passing the wrong TYPE should not be silently absorbed."""
    src = inspect.getsource(ex.safe_int)
    assert "except Exception" not in src, "narrow the except clause"


def test_safe_get_does_not_swallow_typeerror():
    src = inspect.getsource(ex.safe_get)
    assert "except Exception" not in src, "narrow the except clause"
