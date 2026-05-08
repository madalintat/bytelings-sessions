"""Tests for rung 2.

Replace the flaky implementations of `test_just_now` and
`test_too_old` with monkeypatched versions that freeze `time.time`
to a known value (e.g., 1_700_000_000.0). After the patch:

  - `is_recent(1_700_000_000.0 - 5,   max=10)` should be True
  - `is_recent(1_700_000_000.0 - 60,  max=10)` should be False

Hint:
    monkeypatch.setattr(ex.time, "time", lambda: 1_700_000_000.0)
"""
import importlib.util
import time
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


# TODO: rewrite both tests to take `monkeypatch` and freeze time.time().
def test_just_now():
    # Flaky: races the wall clock.
    assert ex.is_recent(time.time() - 0.0, max_age_seconds=10) is True


def test_too_old():
    # Flaky for the same reason.
    assert ex.is_recent(time.time() - 60, max_age_seconds=10) is False


def test_uses_monkeypatch():
    """Source check: both tests above should use `monkeypatch`."""
    src = Path(__file__).read_text()
    assert src.count("monkeypatch") >= 2, (
        "rewrite test_just_now and test_too_old to use monkeypatch"
    )
