"""Tests for rung 2 — should be green after both TODOs are fixed."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = """
[project]
name = "habit-cli"
version = "0.1.0"
dependencies = ["click>=8.1", "rich>=13.7"]
"""

SAMPLE_NO_DEPS = """
[project]
name = "tiny"
version = "0.0.1"
"""


def test_parse_name():
    assert ex.parse_project_name(SAMPLE) == "habit-cli"


def test_parse_name_takes_string():
    # tomllib.loads takes str, not bytes. tomllib.load takes a binary file.
    # The fluency code mistakenly encodes the input.
    assert ex.parse_project_name(SAMPLE) == "habit-cli"


def test_list_deps():
    assert ex.list_dependencies(SAMPLE) == ["click>=8.1", "rich>=13.7"]


def test_list_deps_missing():
    assert ex.list_dependencies(SAMPLE_NO_DEPS) == []
