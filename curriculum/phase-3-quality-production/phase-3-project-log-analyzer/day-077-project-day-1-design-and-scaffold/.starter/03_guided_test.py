"""Tests for rung 3."""
import importlib.util
from datetime import datetime
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_parse_line_ok():
    r = ex.parse_line("2026-05-08T10:00:00 INFO path=/users status=200")
    assert r.ts == datetime(2026, 5, 8, 10, 0, 0)
    assert r.level == "INFO"
    assert r.fields == {"path": "/users", "status": "200"}


def test_parse_line_no_fields():
    r = ex.parse_line("2026-05-08T10:00:00 ERROR")
    assert r.fields == {}


def test_empty_line_raises():
    with pytest.raises(ex.MalformedLine) as info:
        ex.parse_line("   ")
    assert info.value.reason == "empty line"


def test_bad_timestamp_raises():
    with pytest.raises(ex.MalformedLine) as info:
        ex.parse_line("not-a-date INFO")
    assert info.value.reason == "bad timestamp"


def test_bad_level_raises():
    with pytest.raises(ex.MalformedLine) as info:
        ex.parse_line("2026-05-08T10:00:00 PANIC path=/x")
    assert info.value.reason == "bad level"


def test_bad_kv_raises():
    with pytest.raises(ex.MalformedLine) as info:
        ex.parse_line("2026-05-08T10:00:00 INFO standalone")
    assert info.value.reason.startswith("bad key=value")


def test_value_can_contain_equals():
    r = ex.parse_line("2026-05-08T10:00:00 INFO eq=a=b=c")
    assert r.fields["eq"] == "a=b=c"
