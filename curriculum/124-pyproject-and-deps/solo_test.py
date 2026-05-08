"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


FULL = """
[project]
name = "habit-cli"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["click>=8.1", "rich>=13.7"]

[project.optional-dependencies]
dev = ["pytest>=8.0", "mypy"]

[tool.uv]
dev-dependencies = ["pytest>=8.0", "ruff"]
"""

MINIMAL = """
[project]
name = "tiny"
version = "0.0.1"
"""


def test_full():
    s = ex.summarize_project(FULL)
    assert s["name"] == "habit-cli"
    assert s["version"] == "0.1.0"
    assert s["python"] == ">=3.12"
    assert s["deps"] == ["click", "rich"]
    # Merged + deduped + sorted: pytest from both sources, mypy + ruff once each.
    assert s["dev_deps"] == ["mypy", "pytest", "ruff"]


def test_minimal():
    s = ex.summarize_project(MINIMAL)
    assert s["name"] == "tiny"
    assert s["version"] == "0.0.1"
    assert s["python"] == ""
    assert s["deps"] == []
    assert s["dev_deps"] == []


def test_only_optional_dev():
    text = """
[project]
name = "x"
version = "0.1"
[project.optional-dependencies]
dev = ["pytest"]
"""
    s = ex.summarize_project(text)
    assert s["dev_deps"] == ["pytest"]


def test_only_uv_dev():
    text = """
[project]
name = "x"
version = "0.1"
[tool.uv]
dev-dependencies = ["ruff"]
"""
    s = ex.summarize_project(text)
    assert s["dev_deps"] == ["ruff"]
