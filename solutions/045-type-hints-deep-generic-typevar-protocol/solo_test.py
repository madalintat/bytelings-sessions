"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_longest_string():
    assert ex.longest(["a", "abcd", "ab"]) == "abcd"


def test_longest_list():
    assert ex.longest([[1], [2, 3], [4, 5, 6]]) == [4, 5, 6]


def test_empty_raises():
    with pytest.raises(ValueError):
        ex.longest([])


def test_mixed_sized_things():
    """A Protocol-typed function should accept any object with __len__."""
    items = [["a", "b"], "abcd", {"x": 1, "y": 2, "z": 3}]
    # Tie at 3 between "abcd" (len 4) and dict... actually "abcd" is len 4 -> longest.
    assert ex.longest(items) == "abcd"


def test_first_wins_on_tie():
    a = [1, 2]
    b = [3, 4]
    # Both have len 2. First-encountered wins.
    assert ex.longest([a, b]) is a


def test_sized_is_a_protocol():
    """Sized should be a Protocol (typing.Protocol subclass)."""
    import typing
    assert getattr(ex.Sized, "_is_protocol", False) is True
