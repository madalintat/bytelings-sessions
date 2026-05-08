"""Tests for rung 2."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.first_word("hello world") == "hello"


def test_empty():
    assert ex.first_word("") == ""


def test_whitespace_only():
    assert ex.first_word("   \t\n") == ""


def test_single_word():
    assert ex.first_word("solo") == "solo"


def test_eafp_style():
    """The body should use try/except, not len() / is None checks."""
    src = inspect.getsource(ex.first_word)
    assert "try:" in src, "use EAFP — try / except IndexError"
    assert "except" in src, "use EAFP — try / except IndexError"
    assert "if len(parts)" not in src, "drop the len() guard"
