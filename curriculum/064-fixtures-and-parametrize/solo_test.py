"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


@pytest.mark.parametrize(
    "value, low, high, expected",
    [
        (5, 0, 10, 5),       # in range
        (-1, 0, 10, 0),      # below
        (11, 0, 10, 10),     # above
        (0, 0, 10, 0),       # boundary low
        (10, 0, 10, 10),     # boundary high
        (5.5, 0.0, 10.0, 5.5),
        (-0.1, 0.0, 10.0, 0.0),
        ("m", "a", "z", "m"),
        ("aa", "b", "y", "b"),
    ],
)
def test_clamp(value, low, high, expected):
    assert ex.clamp(value, low, high) == expected


def test_invalid_bounds_raise():
    with pytest.raises(ValueError):
        ex.clamp(5, 10, 0)


def test_equal_bounds_ok():
    assert ex.clamp(5, 3, 3) == 3
    assert ex.clamp(3, 3, 3) == 3
