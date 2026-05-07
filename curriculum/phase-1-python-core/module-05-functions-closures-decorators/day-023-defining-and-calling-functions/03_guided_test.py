"""Tests for rung 3."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    out = ex.bucket_by_size(["hi", "hello", "h"], small=2, large=5)
    assert out == {"small": ["hi", "h"], "medium": [], "large": ["hello"]}


def test_with_medium():
    out = ex.bucket_by_size(["abc", "abcd"], small=2, large=5)
    assert out == {"small": [], "medium": ["abc", "abcd"], "large": []}


def test_empty():
    out = ex.bucket_by_size([], small=1, large=5)
    assert out == {"small": [], "medium": [], "large": []}


def test_keyword_only():
    with pytest.raises(TypeError):
        ex.bucket_by_size(["a"], 2, 5)


def test_invalid_thresholds_raises():
    with pytest.raises(ValueError):
        ex.bucket_by_size([], small=5, large=5)
    with pytest.raises(ValueError):
        ex.bucket_by_size([], small=10, large=5)


def test_preserves_order():
    out = ex.bucket_by_size(["aa", "bb", "cc"], small=2, large=10)
    assert out["small"] == ["aa", "bb", "cc"]
