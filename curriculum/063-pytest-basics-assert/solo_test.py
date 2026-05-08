"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.parse_kv("a=1\nb=2") == {"a": "1", "b": "2"}


def test_empty_returns_empty():
    assert ex.parse_kv("") == {}


def test_blank_lines_ignored():
    assert ex.parse_kv("\n\na=1\n\n") == {"a": "1"}


def test_comments_ignored():
    assert ex.parse_kv("# hello\na=1\n# bye") == {"a": "1"}


def test_strips_whitespace():
    assert ex.parse_kv("  x  =   hello world  ") == {"x": "hello world"}


def test_last_duplicate_wins():
    assert ex.parse_kv("a=1\na=2\na=3") == {"a": "3"}


def test_malformed_raises():
    with pytest.raises(ValueError) as info:
        ex.parse_kv("nope")
    assert "malformed" in str(info.value).lower()


def test_value_can_contain_equals():
    """Only split on the FIRST '=' — values can contain more."""
    assert ex.parse_kv("eq=a=b=c") == {"eq": "a=b=c"}
