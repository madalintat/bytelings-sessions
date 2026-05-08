"""Tests for rung 3."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


WORKFLOW_WITH_URL = """\
name: Release
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/
    steps:
      - uses: actions/checkout@v4
"""

WORKFLOW_NO_ENV = """\
name: Release
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
"""

WORKFLOW_ENV_NO_URL = """\
name: Release
jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    steps:
      - uses: actions/checkout@v4
"""


def test_finds_url():
    result = ex.extract_pypi_url(WORKFLOW_WITH_URL)
    diagnose(
        result == "https://pypi.org/project/my-linter/",
        f"Expected the PyPI URL, got {result!r}",
        (lambda: result is None,
         "Returned None — did you look for 'url:' after the 'environment:' line?"),
    )


def test_no_environment_returns_none():
    result = ex.extract_pypi_url(WORKFLOW_NO_ENV)
    diagnose(
        result is None,
        f"Expected None when there is no environment block, got {result!r}",
    )


def test_environment_without_url_returns_none():
    result = ex.extract_pypi_url(WORKFLOW_ENV_NO_URL)
    diagnose(
        result is None,
        f"Expected None when environment has no url key, got {result!r}",
    )


def test_url_is_stripped():
    yaml = "environment:\n  name: pypi\n  url:   https://example.com/  \n"
    result = ex.extract_pypi_url(yaml)
    diagnose(
        result == "https://example.com/",
        f"Expected stripped URL, got {result!r}",
        (lambda: result is not None and result != result.strip(),
         "URL has extra whitespace — strip the value after splitting on 'url:'."),
    )
