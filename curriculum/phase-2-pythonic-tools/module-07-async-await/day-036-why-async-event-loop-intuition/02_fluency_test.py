"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_sync_total():
    """Three 40-minute roasts in sequence = 120 minutes."""
    assert ex.SYNC_MINUTES == 120


def test_async_total():
    """Three 40-minute roasts concurrently = 40 minutes (the longest)."""
    assert ex.ASYNC_MINUTES == 40


def test_async_is_strictly_faster():
    assert ex.ASYNC_MINUTES < ex.SYNC_MINUTES
