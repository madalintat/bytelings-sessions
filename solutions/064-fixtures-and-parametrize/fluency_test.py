"""Tests for rung 2.

The five test functions below all have the same body. Replace them
with ONE @pytest.mark.parametrize test named `test_slugify`.
"""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


# TODO: delete the five functions below and replace them with:
#
#   @pytest.mark.parametrize("text, expected", [
#       ("Hello World",        "hello-world"),
#       ("",                   ""),
#       ("ALL CAPS",           "all-caps"),
#       ("trailing-!!!",       "trailing"),
#       ("multi   spaces",     "multi-spaces"),
#   ])
#   def test_slugify(text, expected):
#       assert ex.slugify(text) == expected


def test_basic():
    assert ex.slugify("Hello World") == "hello-world"


def test_empty():
    assert ex.slugify("") == ""


def test_all_caps():
    assert ex.slugify("ALL CAPS") == "all-caps"


def test_trailing_punct():
    assert ex.slugify("trailing-!!!") == "trailing"


def test_multi_space():
    assert ex.slugify("multi   spaces") == "multi-spaces"


def test_using_parametrize():
    """The grader: this file should define `test_slugify` (the parametrized
    one) AND should NOT still have the five duplicated functions."""
    import inspect
    src = Path(__file__).read_text()
    assert "def test_slugify(" in src, (
        "add a parametrized test_slugify"
    )
    assert "@pytest.mark.parametrize" in src, (
        "use @pytest.mark.parametrize"
    )
