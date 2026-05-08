"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_djb2_known_value_empty():
    # djb2 of "" must be the seed: 5381.
    assert ex.djb2("") == 5381


def test_djb2_distinguishes_permutations():
    # "cat" and "act" share the same characters; a sum-hash collides.
    assert ex.djb2("cat") != ex.djb2("act")


def test_djb2_known_value_a():
    # h = 5381*33 + ord('a') = 177573 + 97 = 177670
    assert ex.djb2("a") == 177670


def test_djb2_in_32_bit_range():
    for word in ["hello", "world", "alice", "longerstring", "x" * 100]:
        h = ex.djb2(word)
        assert 0 <= h < 2**32


def test_fnv1a_empty():
    # FNV-1a of "" is the offset basis.
    assert ex.fnv1a("") == 0x811c9dc5


def test_fnv1a_distinguishes_permutations():
    assert ex.fnv1a("cat") != ex.fnv1a("act")


def test_fnv1a_a_known_value():
    # FNV-1a "a" should be (0x811c9dc5 ^ ord('a')) * 0x01000193 (mod 2^32).
    expected = ((0x811c9dc5 ^ ord("a")) * 0x01000193) & 0xFFFFFFFF
    assert ex.fnv1a("a") == expected


def test_fnv1a_in_32_bit_range():
    for word in ["hello", "world", "x" * 100]:
        h = ex.fnv1a(word)
        assert 0 <= h < 2**32
