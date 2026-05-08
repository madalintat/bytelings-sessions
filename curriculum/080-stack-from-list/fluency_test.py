"""Tests for rung 2 — should be green after both TODOs are fixed."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_push_all_uses_right_end():
    stack: list = []
    ex.push_all(stack, [1, 2, 3])
    assert stack == [1, 2, 3]


def test_pop_top_returns_last():
    stack = [1, 2, 3]
    assert ex.pop_top(stack) == 3
    assert stack == [1, 2]


def test_push_then_pop_lifo():
    stack: list = []
    ex.push_all(stack, ["a", "b", "c"])
    assert ex.pop_top(stack) == "c"
    assert ex.pop_top(stack) == "b"
    assert ex.pop_top(stack) == "a"
