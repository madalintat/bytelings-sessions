"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.lcs_length("abcde", "ace") == 3


def test_disjoint():
    assert ex.lcs_length("abc", "def") == 0


def test_one_empty():
    assert ex.lcs_length("abc", "") == 0
    assert ex.lcs_length("", "abc") == 0


def test_both_empty():
    assert ex.lcs_length("", "") == 0


def test_identical():
    assert ex.lcs_length("hello", "hello") == 5


def test_one_inside_other():
    assert ex.lcs_length("abc", "ababc") == 3


def test_long():
    assert ex.lcs_length("AGGTAB", "GXTXAYB") == 4
