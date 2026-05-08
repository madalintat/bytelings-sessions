"""HIDDEN tests for rung 4 — property-based + examples."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

try:
    from hypothesis import given, strategies as st

    HAS_HYPOTHESIS = True
except ImportError:
    HAS_HYPOTHESIS = False


def test_simple():
    assert ex.merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_one_empty():
    assert ex.merge_sorted([], [1, 2, 3]) == [1, 2, 3]
    assert ex.merge_sorted([1, 2, 3], []) == [1, 2, 3]


def test_both_empty():
    assert ex.merge_sorted([], []) == []


def test_duplicates_preserved():
    assert ex.merge_sorted([1, 1, 2], [1, 3]) == [1, 1, 1, 2, 3]


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_property_length():
    @given(st.lists(st.integers()), st.lists(st.integers()))
    def _check(a, b):
        a, b = sorted(a), sorted(b)
        out = ex.merge_sorted(a, b)
        assert len(out) == len(a) + len(b)

    _check()


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_property_sorted():
    @given(st.lists(st.integers()), st.lists(st.integers()))
    def _check(a, b):
        a, b = sorted(a), sorted(b)
        out = ex.merge_sorted(a, b)
        assert out == sorted(out)

    _check()


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_property_multiset_equality():
    @given(st.lists(st.integers()), st.lists(st.integers()))
    def _check(a, b):
        a, b = sorted(a), sorted(b)
        assert sorted(ex.merge_sorted(a, b)) == sorted(a + b)

    _check()
