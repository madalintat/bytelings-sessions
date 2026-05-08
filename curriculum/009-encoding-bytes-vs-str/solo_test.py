"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.count_chars(b"") == 0


def test_ascii():
    assert ex.count_chars(b"hello") == 5


def test_unicode_utf8():
    # 'café' is 4 chars but 5 bytes
    assert ex.count_chars(b"caf\xc3\xa9") == 4


def test_invalid_byte_does_not_crash():
    # 0xff is invalid UTF-8 → replaced with one char
    assert ex.count_chars(b"hi\xff") == 3


def test_latin1():
    # In Latin-1, 'café' is exactly 4 bytes / 4 chars
    assert ex.count_chars(b"caf\xe9", encoding="latin-1") == 4


def test_returns_int():
    assert isinstance(ex.count_chars(b"x"), int)
