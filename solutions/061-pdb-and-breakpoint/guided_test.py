"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_ok_path():
    report = ex.debug_call(lambda x, y: x + y, 2, 3)
    assert report == {"status": "ok", "result": 5}


def test_error_basics():
    def bad(a, b):
        c = a + b  # noqa: F841
        return a / 0

    report = ex.debug_call(bad, 4, 5)
    assert report["status"] == "error"
    assert report["error_type"] == "ZeroDivisionError"
    assert "division" in report["message"].lower()


def test_error_captures_locals():
    def bad(a, b):
        c = a + b
        return c / 0

    report = ex.debug_call(bad, 4, 5)
    locals_ = report["frame_locals"]
    assert locals_["a"] == 4
    assert locals_["b"] == 5
    assert locals_["c"] == 9


def test_error_kwargs():
    def bad(*, name):
        x = name * 2  # noqa: F841
        raise ValueError("boom")

    report = ex.debug_call(bad, name="ada")
    assert report["status"] == "error"
    assert report["frame_locals"]["name"] == "ada"
    assert report["frame_locals"]["x"] == "adaada"
