"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.count_files({}) == 0


def test_only_files():
    assert ex.count_files({"a.py": "f", "b.py": "f"}) == 2


def test_one_subdir():
    tree = {"a.py": "f", "src": {"b.py": "f"}}
    assert ex.count_files(tree) == 2


def test_deep():
    tree = {
        "readme.md": "f",
        "src": {
            "main.py": "f",
            "lib": {"u.py": "f", "d.json": "f"},
        },
        "empty": {},
    }
    assert ex.count_files(tree) == 4


def test_only_dirs():
    tree = {"a": {"b": {"c": {}}}}
    assert ex.count_files(tree) == 0


def test_mixed():
    tree = {
        "x": {"a": "f", "b": "f", "c": {"d": "f"}},
        "y": "f",
        "z": {},
    }
    assert ex.count_files(tree) == 4
