"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import re
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_ok_returns_none():
    assert ex.last_frame_summary(lambda: 1 + 1) is None


def test_zero_division_format():
    s = ex.last_frame_summary(lambda: 1 / 0)
    assert s is not None
    assert re.match(
        r"ZeroDivisionError at \S+:\d+ in <lambda>: division by zero", s
    ), s


def test_value_error_message():
    def bad():
        int("nope")

    s = ex.last_frame_summary(bad)
    assert s is not None
    assert s.startswith("ValueError at ")
    assert "in bad:" in s
    assert "invalid literal" in s


def test_filename_is_basename():
    s = ex.last_frame_summary(lambda: 1 / 0)
    # basename, not full path
    assert "/" not in s.split(" at ")[1].split(":")[0]


def test_deepest_frame():
    """If func calls another function that raises, the location is
    the deepest one — the actual raise site, not where we caught it."""

    def inner():
        raise RuntimeError("deep")

    def outer():
        inner()

    s = ex.last_frame_summary(outer)
    assert s is not None
    assert " in inner:" in s
    assert " in outer:" not in s
