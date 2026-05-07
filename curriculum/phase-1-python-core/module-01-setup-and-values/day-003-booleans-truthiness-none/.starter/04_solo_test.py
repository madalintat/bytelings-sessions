"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_list():
    assert ex.count_truthy([]) == 0


def test_all_truthy():
    assert ex.count_truthy([1, "a", [0]]) == 3


def test_all_falsy():
    assert ex.count_truthy([0, "", None, [], {}, False]) == 0


def test_mixed():
    assert ex.count_truthy([0, 1, "", "a", None, "x"]) == 3
