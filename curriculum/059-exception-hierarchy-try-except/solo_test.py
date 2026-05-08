"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_ok():
    assert ex.classify_failure(lambda: 1 + 1) == ("ok", 2)


def test_keyerror_is_missing():
    assert ex.classify_failure(lambda: {}["x"]) == ("missing", None)


def test_indexerror_is_missing():
    assert ex.classify_failure(lambda: [][0]) == ("missing", None)


def test_valueerror_is_bad_value():
    assert ex.classify_failure(lambda: int("nope")) == ("bad_value", None)


def test_filenotfound_is_io():
    def boom():
        open("/nonexistent/path/xyz123")

    assert ex.classify_failure(boom) == ("io", None)


def test_uncaught_propagates():
    """ZeroDivisionError is none of the above — must propagate."""
    with pytest.raises(ZeroDivisionError):
        ex.classify_failure(lambda: 1 / 0)
