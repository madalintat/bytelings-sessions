"""Tests for rung 3 — behavior + structural."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_avg_score():
    assert ex.avg_score([{"score": 80}, {"score": 100}]) == 90.0


def test_avg_age():
    assert ex.avg_age([{"age": 30}, {"age": 40}]) == 35.0


def test_avg_speed():
    assert ex.avg_speed([{"speed": 50}, {"speed": 70}]) == 60.0


def test_empty_score():
    assert ex.avg_score([]) == 0.0


def test_empty_age():
    assert ex.avg_age([]) == 0.0


def test_empty_speed():
    """The bug: the original returned 1.0 here. After dedup -> 0.0."""
    assert ex.avg_speed([]) == 0.0


def test_helper_extracted():
    assert hasattr(ex, "mean_of"), (
        "extract `mean_of(records, field)` and have the three avg_* "
        "functions delegate to it"
    )


def test_all_three_delegate():
    """A small structural check: each avg_* should be short — its
    body should call mean_of, not loop on its own."""
    for name in ("avg_score", "avg_age", "avg_speed"):
        fn = getattr(ex, name)
        src = inspect.getsource(fn)
        assert "mean_of" in src, f"{name} should delegate to mean_of"
        # If the loop is still there, dedup didn't happen.
        assert "for r in records" not in src, (
            f"{name} should not still loop — delegate to mean_of"
        )
