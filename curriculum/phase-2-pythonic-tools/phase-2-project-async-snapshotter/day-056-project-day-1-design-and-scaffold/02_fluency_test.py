"""Tests for rung 2."""
import dataclasses
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_is_dataclass():
    assert dataclasses.is_dataclass(ex.Snapshot)


def test_field_names():
    fields = {f.name for f in dataclasses.fields(ex.Snapshot)}
    assert fields == {"url", "status", "body_length", "error"}


def test_defaults():
    s = ex.Snapshot(url="http://x")
    assert s.url == "http://x"
    assert s.status == 0
    assert s.body_length == 0
    assert s.error is None


def test_constructed_with_values():
    s = ex.Snapshot(url="http://y", status=200, body_length=42, error=None)
    assert s.status == 200
    assert s.body_length == 42
