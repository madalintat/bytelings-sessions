"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_yes():
    assert ex.can_jump([2, 3, 1, 1, 4]) is True


def test_basic_no():
    assert ex.can_jump([3, 2, 1, 0, 4]) is False


def test_single():
    assert ex.can_jump([0]) is True


def test_empty():
    assert ex.can_jump([]) is False


def test_all_zero_after_first():
    assert ex.can_jump([5, 0, 0, 0, 0, 0]) is True


def test_first_is_zero_long():
    assert ex.can_jump([0, 1, 2]) is False


def test_first_is_zero_one_element():
    """Already at last index, no jump needed."""
    assert ex.can_jump([0]) is True


def test_overshoot_ok():
    assert ex.can_jump([10, 0, 0, 0]) is True
