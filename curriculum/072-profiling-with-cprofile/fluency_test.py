"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def slow_loop(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def test_returns_result():
    result, _ = ex.profile_call(slow_loop, 1000)
    assert result == sum(i * i for i in range(1000))


def test_stats_mentions_function():
    _, stats_text = ex.profile_call(slow_loop, 1000)
    assert isinstance(stats_text, str)
    assert "slow_loop" in stats_text


def test_stats_sorted_by_cumulative():
    """Header line should mention 'cumulative' sort order."""
    _, stats_text = ex.profile_call(slow_loop, 1000)
    assert "cumulative" in stats_text.lower()
