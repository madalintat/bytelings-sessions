"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_normalize_strips_and_lowers():
    assert ex.normalize("  Hello ") == "hello"
    assert ex.normalize("WORLD") == "world"


def test_join_words():
    assert ex.join_words(["a", "b", "c"]) == "a b c"
    assert ex.join_words([]) == ""


def test_format_price():
    assert ex.format_price(3, 9.5) == "3 items at $9.50"
    assert ex.format_price(1, 10) == "1 items at $10.00"


def test_is_csv_line():
    assert ex.is_csv_line("data.csv") is True
    assert ex.is_csv_line("DATA.CSV") is True
    assert ex.is_csv_line("data.txt") is False
