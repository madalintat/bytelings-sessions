"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_returns_path_object():
    result = ex.build_report_path("/tmp", "out")
    assert isinstance(result, Path), "must return a Path, not a string"


def test_joins_correctly():
    result = ex.build_report_path("/tmp", "out")
    assert result == Path("/tmp/out.txt")


def test_relative_base():
    result = ex.build_report_path("data", "summary")
    assert result == Path("data/summary.txt")


def test_suffix_and_stem():
    result = ex.build_report_path("/x", "y")
    assert result.suffix == ".txt"
    assert result.stem == "y"
