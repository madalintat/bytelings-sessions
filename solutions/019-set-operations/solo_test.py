"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.anagram_groups(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]


def test_empty():
    assert ex.anagram_groups([]) == []


def test_no_anagrams():
    assert ex.anagram_groups(["a", "b", "c"]) == [["a"], ["b"], ["c"]]


def test_all_anagrams():
    assert ex.anagram_groups(["abc", "bca", "cab"]) == [["abc", "bca", "cab"]]


def test_outer_order_by_first_seen():
    # 'tan' appears before 'eat' here; so its group leads the result
    assert ex.anagram_groups(["tan", "eat", "nat", "tea"]) == [
        ["tan", "nat"],
        ["eat", "tea"],
    ]


def test_single_word():
    assert ex.anagram_groups(["only"]) == [["only"]]
