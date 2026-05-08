"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_is_zero():
    assert ex.count_vowels("") == 0


def test_no_vowels():
    assert ex.count_vowels("rhythm") == 0


def test_basic_word():
    assert ex.count_vowels("hello") == 2


def test_uppercase_counts():
    assert ex.count_vowels("HELLO") == 2


def test_mixed_case():
    assert ex.count_vowels("HeLLo WorLd") == 3


def test_ignores_numbers_and_symbols():
    assert ex.count_vowels("a1b2c3!") == 1


def test_long_string():
    assert ex.count_vowels("the quick brown fox jumps over the lazy dog") == 11
