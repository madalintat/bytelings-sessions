"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.tag_index([]) == {}


def test_single_post():
    posts = [{"id": 1, "tags": ["python"]}]
    assert ex.tag_index(posts) == {"python": [1]}


def test_case_insensitive():
    posts = [
        {"id": 1, "tags": ["Python", "Async"]},
        {"id": 2, "tags": ["python", "ASYNC"]},
    ]
    assert ex.tag_index(posts) == {"python": [1, 2], "async": [1, 2]}


def test_sorted_ids():
    posts = [
        {"id": 9, "tags": ["x"]},
        {"id": 1, "tags": ["x"]},
        {"id": 5, "tags": ["x"]},
    ]
    assert ex.tag_index(posts) == {"x": [1, 5, 9]}


def test_no_tags():
    posts = [{"id": 1, "tags": []}, {"id": 2, "tags": ["a"]}]
    assert ex.tag_index(posts) == {"a": [2]}
