"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_bucket_index_in_range():
    for key in ["alice", "bob", "carol", 1, 2, 3, (1, 2)]:
        idx = ex.bucket_index(key, 8)
        assert 0 <= idx < 8


def test_bucket_index_deterministic():
    a = ex.bucket_index("alice", 8)
    b = ex.bucket_index("alice", 8)
    assert a == b


def test_bucket_index_different_size_different_index_likely():
    # Just sanity: different sizes generally give different indices.
    a = ex.bucket_index("alice", 8)
    b = ex.bucket_index("alice", 16)
    # They CAN happen to match, but for at least one tested key we
    # expect difference. Sample a handful.
    pairs = [(ex.bucket_index(k, 8), ex.bucket_index(k, 16))
             for k in ["a", "b", "c", "d", "e", "f", "g", "h"]]
    assert any(a != b for a, b in pairs)


def test_find_empty_bucket():
    assert ex.find_in_bucket([], "alice") is None


def test_find_hit():
    bucket = [("alice", 31), ("bob", 22)]
    assert ex.find_in_bucket(bucket, "bob") == 22


def test_find_miss():
    bucket = [("alice", 31), ("bob", 22)]
    assert ex.find_in_bucket(bucket, "carol") is None


def test_find_first_entry():
    bucket = [("alice", 31), ("bob", 22)]
    assert ex.find_in_bucket(bucket, "alice") == 31
