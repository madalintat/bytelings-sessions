"""Tests for rung 2."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_first_word_runtime():
    assert ex.first_word("hello world") == "hello"
    assert ex.first_word("") == ""


def test_first_word_annotated():
    sig = inspect.signature(ex.first_word)
    assert sig.parameters["s"].annotation is str
    assert sig.return_annotation is str


def test_repeat_runtime():
    assert ex.repeat("ab", 3) == "ababab"


def test_repeat_annotated():
    sig = inspect.signature(ex.repeat)
    assert sig.parameters["s"].annotation is str
    assert sig.parameters["n"].annotation is int
    assert sig.return_annotation is str
