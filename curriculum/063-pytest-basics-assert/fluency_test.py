"""Tests for rung 2."""
import importlib.util
import math
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero():
    assert ex.area_of_circle(0) == 0.0


def test_one():
    assert ex.area_of_circle(1.0) == pytest.approx(math.pi)


def test_three():
    assert ex.area_of_circle(3.0) == pytest.approx(9 * math.pi)


def test_negative_raises():
    with pytest.raises(ValueError) as info:
        ex.area_of_circle(-1.0)
    assert "negative" in str(info.value).lower()
