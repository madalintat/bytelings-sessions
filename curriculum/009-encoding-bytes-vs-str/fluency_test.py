"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_to_bytes_ascii():
    assert ex.to_bytes("hello") == b"hello"


def test_to_bytes_unicode():
    # café in UTF-8 is 5 bytes
    assert ex.to_bytes("café") == b"caf\xc3\xa9"


def test_from_bytes_basic():
    assert ex.from_bytes(b"hello") == "hello"


def test_from_bytes_unicode():
    assert ex.from_bytes(b"caf\xc3\xa9") == "café"


def test_byte_length_ascii():
    assert ex.byte_length("hello") == 5


def test_byte_length_unicode():
    assert ex.byte_length("café") == 5  # 'é' is 2 bytes in UTF-8


def test_safe_decode_valid():
    assert ex.safe_decode(b"caf\xc3\xa9") == "café"


def test_safe_decode_invalid_does_not_raise():
    # 0xff is never a valid UTF-8 start byte; replace policy => U+FFFD
    out = ex.safe_decode(b"hi\xff")
    assert "hi" in out
    assert out != "hi"  # the bad byte must show up replaced
