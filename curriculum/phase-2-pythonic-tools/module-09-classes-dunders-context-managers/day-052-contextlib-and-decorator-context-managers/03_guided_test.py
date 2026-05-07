"""Tests for rung 3."""
import importlib.util
import time
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_records_label_and_elapsed():
    events = []
    with ex.timing("work", events):
        time.sleep(0.01)
    assert len(events) == 1
    label, elapsed = events[0]
    assert label == "work"
    assert elapsed >= 0.005


def test_records_on_exception():
    events = []
    with pytest.raises(RuntimeError):
        with ex.timing("crashy", events):
            raise RuntimeError("x")
    assert len(events) == 1
    assert events[0][0] == "crashy"


def test_multiple_uses_independent():
    events = []
    with ex.timing("a", events):
        pass
    with ex.timing("b", events):
        pass
    labels = [e[0] for e in events]
    assert labels == ["a", "b"]
