"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_ge():
    assert ex.split_requirement("click>=8.1") == ("click", ">=8.1")


def test_no_specifier():
    assert ex.split_requirement("rich") == ("rich", "")


def test_exact_pin():
    assert ex.split_requirement("httpx==0.27.0") == ("httpx", "==0.27.0")


def test_compatible_release():
    assert ex.split_requirement("hatchling~=1.0") == ("hatchling", "~=1.0")


def test_strips_whitespace():
    assert ex.split_requirement("  pytest >= 8.0  ") == ("pytest", ">=8.0")


def test_lt():
    assert ex.split_requirement("urllib3<2") == ("urllib3", "<2")


def test_not_equal():
    assert ex.split_requirement("foo!=1.2") == ("foo", "!=1.2")
