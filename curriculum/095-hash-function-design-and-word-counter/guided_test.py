"""Tests for rung 3."""
import importlib.util
import string
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_distribution_all_to_zero():
    out = ex.bucket_distribution(["a", "b", "c", "d"], lambda s: 0, 4)
    assert out == [4, 0, 0, 0]


def test_distribution_uniform():
    # mod-len round-robin
    def h(s): return ord(s)
    out = ex.bucket_distribution(["a", "b", "c", "d"], h, 4)
    # ord('a')..ord('d') are 97..100; mod 4 = 1, 2, 3, 0
    assert sorted(out) == [1, 1, 1, 1]


def test_distribution_total_matches_input():
    out = ex.bucket_distribution(list("abcdefghij"), lambda s: ord(s), 8)
    assert sum(out) == 10
    assert len(out) == 8


def test_collision_score_perfect_when_one_per_bucket():
    # 4 inputs, 4 buckets, one each: score should be 1.0.
    score = ex.collision_score(["a", "b", "c", "d"], lambda s: ord(s), 4)
    assert score == 1.0


def test_collision_score_low_when_all_same_bucket():
    # 8 inputs, 4 buckets, all to 0.
    score = ex.collision_score(["a"] * 8, lambda s: 0, 4)
    assert score < 0.1


def test_collision_score_in_unit_interval():
    score = ex.collision_score(list("aaabbbcc"), lambda s: ord(s), 4)
    assert 0.0 <= score <= 1.0


def test_word_counts_basic():
    out = ex.word_counts("Hello, hello world!")
    assert out == {"hello": 2, "world": 1}


def test_word_counts_empty():
    assert ex.word_counts("") == {}


def test_word_counts_preserves_apostrophe_inside():
    out = ex.word_counts("It's its he's hers")
    assert out["it's"] == 1
    assert out["its"] == 1


def test_word_counts_strips_numbers_and_symbols():
    out = ex.word_counts("a1 b2 c3 a")
    assert out == {"a": 2, "b": 1, "c": 1}
