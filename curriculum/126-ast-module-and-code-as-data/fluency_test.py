"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_count_functions_basic():
    src = """
def a():
    pass

def b():
    def c():
        pass
"""
    assert ex.count_functions(src) == 3


def test_count_functions_excludes_async():
    src = """
def a():
    pass

async def b():
    pass
"""
    assert ex.count_functions(src) == 1


def test_names_assigned_basic():
    src = "x = 1\ny = 2\nz = x + y\n"
    assert ex.names_assigned(src) == ["x", "y", "z"]


def test_names_assigned_skips_tuples():
    src = "a = 1\nb, c = 2, 3\nd = 4\n"
    assert ex.names_assigned(src) == ["a", "d"]


def test_names_assigned_empty():
    assert ex.names_assigned("") == []
