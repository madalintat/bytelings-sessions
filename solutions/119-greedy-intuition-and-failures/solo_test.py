"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    assert ex.min_platforms(arr, dep) == 3


def test_no_overlap():
    arr = [100, 300, 500]
    dep = [200, 400, 600]
    assert ex.min_platforms(arr, dep) == 1


def test_all_overlap():
    arr = [100, 100, 100]
    dep = [200, 200, 200]
    assert ex.min_platforms(arr, dep) == 3


def test_single():
    assert ex.min_platforms([800], [900]) == 1


def test_back_to_back():
    """Departure at T and arrival at T: one platform can serve both
    (departure frees before next arrival needs)."""
    arr = [100, 200]
    dep = [200, 300]
    assert ex.min_platforms(arr, dep) == 1


def test_unsorted_input():
    """Arrays may arrive unsorted; function must sort internally."""
    arr = [1800, 1500, 1100, 950, 940, 900]
    dep = [2000, 1900, 1130, 1120, 1200, 910]
    assert ex.min_platforms(arr, dep) == 3
