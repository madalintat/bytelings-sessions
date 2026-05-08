"""Tests for rung 3."""
import importlib.util
import json
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_missing_file_returns_default(tmp_path):
    counter: list[int] = []
    result = ex.read_config_or_default(tmp_path / "nope.json", counter)
    assert result == ex.DEFAULT_CONFIG
    assert counter == [1]


def test_present_file_returns_parsed(tmp_path):
    p = tmp_path / "cfg.json"
    p.write_text(json.dumps({"debug": True, "workers": 4}))
    counter: list[int] = []
    result = ex.read_config_or_default(p, counter)
    assert result == {"debug": True, "workers": 4}
    assert counter == [1]


def test_corrupt_file_propagates(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{not json")
    counter: list[int] = []
    with pytest.raises(json.JSONDecodeError):
        ex.read_config_or_default(p, counter)
    # Counter still ticked — the `finally` ran on the way out.
    assert counter == [1]
