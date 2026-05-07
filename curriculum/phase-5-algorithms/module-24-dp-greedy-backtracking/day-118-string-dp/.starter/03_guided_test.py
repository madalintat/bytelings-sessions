"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.num_decodings("12") == 2


def test_three():
    assert ex.num_decodings("226") == 3


def test_leading_zero():
    assert ex.num_decodings("06") == 0


def test_zero_alone():
    assert ex.num_decodings("0") == 0


def test_empty():
    assert ex.num_decodings("") == 1


def test_long_no_zero():
    assert ex.num_decodings("11106") == 2


def test_single_digit():
    assert ex.num_decodings("5") == 1


def test_all_in_range():
    assert ex.num_decodings("11") == 2
