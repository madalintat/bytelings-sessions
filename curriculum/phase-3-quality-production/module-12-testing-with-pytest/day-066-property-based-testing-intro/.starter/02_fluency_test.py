"""Tests for rung 2 — property-based.

If hypothesis isn't installed, the property tests are skipped and
example-based fallbacks still cover the bug.
"""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

try:
    from hypothesis import given, strategies as st

    HAS_HYPOTHESIS = True
except ImportError:
    HAS_HYPOTHESIS = False


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_property_matches_builtin_sum():
    @given(st.lists(st.integers()))
    def _check(xs):
        assert ex.safe_sum(xs) == sum(xs)

    _check()


def test_example_single_element():
    """Example fallback that catches the same bug."""
    assert ex.safe_sum([42]) == 42


def test_example_three_elements():
    assert ex.safe_sum([1, 2, 3]) == 6


def test_example_empty():
    assert ex.safe_sum([]) == 0
