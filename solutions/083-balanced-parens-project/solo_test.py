"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_single_number():
    assert ex.evaluate("3") == 3


def test_simple_add():
    assert ex.evaluate("3 4 +") == 7


def test_simple_sub():
    assert ex.evaluate("10 4 -") == 6


def test_simple_mul():
    assert ex.evaluate("3 4 *") == 12


def test_simple_div():
    assert ex.evaluate("10 2 /") == 5


def test_complex_expression():
    assert ex.evaluate("5 1 2 + 4 * + 3 -") == 14


def test_negative_number_token():
    assert ex.evaluate("-3 5 +") == 2


def test_div_by_zero_raises():
    with pytest.raises(ValueError):
        ex.evaluate("5 0 /")


def test_too_few_operands():
    with pytest.raises(ValueError):
        ex.evaluate("+")


def test_too_many_operands():
    with pytest.raises(ValueError):
        ex.evaluate("1 2 3")
