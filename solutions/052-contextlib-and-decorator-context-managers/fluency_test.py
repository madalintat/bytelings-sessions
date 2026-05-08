"""Tests for rung 2."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    events = []
    with ex.scoped(events) as e:
        assert e is events
    assert events == ["enter", "exit"]


def test_exit_runs_on_exception():
    events = []
    with pytest.raises(RuntimeError):
        with ex.scoped(events):
            events.append("body")
            raise RuntimeError("boom")
    assert events == ["enter", "body", "exit"]
