"""Tests for rung 2."""
import inspect
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_greet_default():
    assert ex.greet("Bytelinger") == "Hello, Bytelinger!"


def test_greet_with_keyword():
    assert ex.greet("Bytelinger", greeting="Hi") == "Hi, Bytelinger!"


def test_greet_greeting_is_kw_only():
    with pytest.raises(TypeError):
        ex.greet("Bytelinger", "Hi")  # positional should fail


def test_clamp():
    assert ex.clamp(5, 0, 10) == 5
    assert ex.clamp(-3, 0, 10) == 0
    assert ex.clamp(99, 0, 10) == 10


def test_add_to_list_no_aliasing_bug():
    """Calling without container twice must not share state."""
    a = ex.add_to_list(1)
    b = ex.add_to_list(2)
    assert a == [1]
    assert b == [2]


def test_add_to_list_with_container():
    out = ex.add_to_list(1, [9])
    assert out == [9, 1]
