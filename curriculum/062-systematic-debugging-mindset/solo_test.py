"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_predicate_false_returns_empty():
    assert ex.minimize([1, 2, 3], lambda xs: False) == []


def test_full_already_minimal():
    # only the FULL list satisfies — no shrinking possible.
    pred = lambda xs: xs == [1, 2, 3]
    assert ex.minimize([1, 2, 3], pred) == [1, 2, 3]


def test_shrinks_from_start():
    # any slice that includes the 99 still triggers.
    pred = lambda xs: 99 in xs
    result = ex.minimize([1, 2, 99, 4, 5], pred)
    assert result == [99]


def test_shrinks_from_end():
    pred = lambda xs: 7 in xs
    result = ex.minimize([7, 1, 2, 3], pred)
    assert result == [7]


def test_shrinks_from_both():
    # bug needs 5 AND 6 adjacent.
    pred = lambda xs: any(xs[i] == 5 and xs[i + 1] == 6 for i in range(len(xs) - 1))
    result = ex.minimize([1, 2, 5, 6, 9, 10], pred)
    assert result == [5, 6]


def test_keeps_contiguous():
    """Result must be a contiguous slice of the original input."""
    inputs = list(range(20))
    pred = lambda xs: 7 in xs and 13 in xs
    result = ex.minimize(inputs, pred)
    # The minimal contiguous slice containing both 7 and 13 is [7..13].
    assert result == list(range(7, 14))
