"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.english_list([]) == ""


def test_one():
    assert ex.english_list(["alice"]) == "alice"


def test_two():
    assert ex.english_list(["alice", "bob"]) == "alice and bob"


def test_three_oxford():
    assert ex.english_list(["a", "b", "c"]) == "a, b, and c"


def test_four():
    assert ex.english_list(["a", "b", "c", "d"]) == "a, b, c, and d"


def test_long_list():
    names = [f"n{i}" for i in range(10)]
    out = ex.english_list(names)
    assert out.startswith("n0, n1")
    assert out.endswith(", and n9")
