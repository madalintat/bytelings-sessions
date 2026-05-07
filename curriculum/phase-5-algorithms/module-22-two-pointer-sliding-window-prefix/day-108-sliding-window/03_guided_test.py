"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.longest_unique("abcabcbb") == 3


def test_repeated():
    assert ex.longest_unique("bbbbb") == 1


def test_pwwkew():
    assert ex.longest_unique("pwwkew") == 3


def test_empty():
    assert ex.longest_unique("") == 0


def test_one():
    assert ex.longest_unique("z") == 1


def test_all_unique():
    assert ex.longest_unique("abcdef") == 6


def test_longish():
    assert ex.longest_unique("dvdf") == 3


def test_window_in_middle():
    assert ex.longest_unique("aabcabcdef") == 6
