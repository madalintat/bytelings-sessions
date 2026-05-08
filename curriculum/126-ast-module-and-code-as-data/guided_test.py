"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_import():
    assert ex.list_imports("import os") == ["os"]


def test_dotted_import():
    assert ex.list_imports("import os.path") == ["os.path"]


def test_import_alias_is_ignored():
    assert ex.list_imports("import numpy as np") == ["numpy"]


def test_multiple_in_one():
    assert ex.list_imports("import os, sys") == ["os", "sys"]


def test_from_import():
    assert ex.list_imports("from pathlib import Path") == ["pathlib.Path"]


def test_from_dotted():
    assert ex.list_imports("from a.b import c") == ["a.b.c"]


def test_relative_one_dot():
    assert ex.list_imports("from . import x") == [".x"]


def test_relative_two_dots():
    assert ex.list_imports("from .. import x") == ["..x"]


def test_relative_with_module():
    assert ex.list_imports("from .helpers import a") == [".helpers.a"]


def test_in_order():
    src = "import a\nfrom b import c\nimport d\n"
    assert ex.list_imports(src) == ["a", "b.c", "d"]
