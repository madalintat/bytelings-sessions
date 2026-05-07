"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_ascii():
    assert ex.roundtrip("hello") == "hello"


def test_empty():
    assert ex.roundtrip("") == ""


def test_unicode_default_utf8():
    assert ex.roundtrip("café") == "café"


def test_emoji():
    assert ex.roundtrip("hi ♥") == "hi ♥"


def test_explicit_ascii_for_ascii():
    assert ex.roundtrip("plain ascii", encoding="ascii") == "plain ascii"


def test_explicit_latin1():
    # Latin-1 covers all 256 single-byte chars including 'é'
    assert ex.roundtrip("café", encoding="latin-1") == "café"
