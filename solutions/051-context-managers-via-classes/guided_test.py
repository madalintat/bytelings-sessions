"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_no_exception():
    with ex.Suppress(ValueError):
        x = 1 + 1
    assert x == 2


def test_suppresses_listed_type():
    with ex.Suppress(ValueError):
        int("not a number")  # raises ValueError
    # We get here without raising.


def test_lets_unlisted_propagate():
    with pytest.raises(KeyError):
        with ex.Suppress(ValueError):
            raise KeyError("nope")


def test_multiple_types():
    with ex.Suppress(ValueError, KeyError):
        raise KeyError("ok to suppress")
    with ex.Suppress(ValueError, KeyError):
        raise ValueError("ok to suppress")


def test_subclass_match():
    """A subclass of a listed exception should also be suppressed."""
    class CustomKey(KeyError):
        pass

    with ex.Suppress(KeyError):
        raise CustomKey("nope")
