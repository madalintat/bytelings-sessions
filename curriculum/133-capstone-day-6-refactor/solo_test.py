"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


SAMPLE = """
[project]
name = "my-linter"
version = "0.1.0"
dependencies = [
    "pytest>=8.0",
    "rich",
    "httpx>=0.27.0,<1",
]
"""

NO_DEPS = """
[project]
name = "minimal"
version = "0.0.1"
"""


def test_bare_name():
    result = ex.parse_dependencies(SAMPLE)
    assert ("rich", "") in result


def test_single_specifier():
    result = ex.parse_dependencies(SAMPLE)
    assert ("pytest", ">=8.0") in result


def test_compound_specifier():
    result = ex.parse_dependencies(SAMPLE)
    assert ("httpx", ">=0.27.0,<1") in result


def test_order_preserved():
    result = ex.parse_dependencies(SAMPLE)
    names = [r[0] for r in result]
    assert names == ["pytest", "rich", "httpx"]


def test_missing_deps_returns_empty():
    result = ex.parse_dependencies(NO_DEPS)
    assert result == []
