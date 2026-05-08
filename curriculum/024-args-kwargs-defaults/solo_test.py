"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_tags_only():
    assert ex.tally("a", "b", "a") == {"a": 2, "b": 1}


def test_kwargs_only():
    assert ex.tally(a=3, b=2) == {"a": 3, "b": 2}


def test_combined():
    assert ex.tally("a", a=10) == {"a": 11}


def test_full_example():
    assert ex.tally("x", "y", x=5, z=2) == {"x": 6, "y": 1, "z": 2}


def test_empty():
    assert ex.tally() == {}


def test_underscore_tag_raises():
    with pytest.raises(ValueError):
        ex.tally("_secret")


def test_repeated_tags_combine():
    assert ex.tally("z", "z", "z") == {"z": 3}


def test_returns_dict():
    assert isinstance(ex.tally("a"), dict)
