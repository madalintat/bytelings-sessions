"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zip_yes():
    assert ex.is_us_zip("90210") is True


def test_zip_no_letters_after():
    assert ex.is_us_zip("90210x") is False


def test_zip_no_too_short():
    assert ex.is_us_zip("9021") is False


def test_zip_no_too_long():
    assert ex.is_us_zip("902100") is False


def test_find_words():
    assert ex.find_words("hello world 42") == ["hello", "world", "42"]
    assert ex.find_words("a, b, c") == ["a", "b", "c"]
    assert ex.find_words("") == []


def test_hex_color_short():
    assert ex.is_hex_color("#abc") is True


def test_hex_color_long():
    assert ex.is_hex_color("#aabbcc") is True


def test_hex_color_bad():
    assert ex.is_hex_color("#abcd") is False
    assert ex.is_hex_color("abc") is False
    assert ex.is_hex_color("#xyz") is False


def test_replace_digits():
    assert ex.replace_digits("a1b22c333") == "a#b#c#"
    assert ex.replace_digits("no digits") == "no digits"
