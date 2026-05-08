"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_no_prereqs():
    assert ex.can_finish(3, []) is True


def test_simple_chain():
    assert ex.can_finish(2, [(1, 0)]) is True


def test_simple_cycle():
    assert ex.can_finish(2, [(1, 0), (0, 1)]) is False


def test_long_chain():
    prereqs = [(i + 1, i) for i in range(99)]
    assert ex.can_finish(100, prereqs) is True


def test_cycle_in_one_part():
    # 0 -> 1 -> 2 -> 0 is a cycle; 3, 4 are fine
    prereqs = [(1, 0), (2, 1), (0, 2)]
    assert ex.can_finish(5, prereqs) is False


def test_two_independent():
    prereqs = [(1, 0), (3, 2)]
    assert ex.can_finish(4, prereqs) is True


def test_zero():
    assert ex.can_finish(0, []) is True


def test_one():
    assert ex.can_finish(1, []) is True
