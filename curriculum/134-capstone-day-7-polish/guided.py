"""Rung 3: Guided implement — extract the PyPI environment URL.

Topic: line-by-line string search

A GitHub Actions workflow can declare an `environment` block inside a
job. The shape for the pypi-publish job looks like:

    environment:
      name: pypi
      url: https://pypi.org/project/my-linter/

`extract_pypi_url(yaml_str)` should return the URL value (stripped),
or None if no `url:` line appears under an `environment:` block in
the string.

Simple approach: scan lines, find `environment:`, then scan the
indented lines below it looking for `url:`. No YAML parser needed —
the test inputs are controlled.

Fill in the function body. Use only stdlib.
"""
from __future__ import annotations


def extract_pypi_url(yaml_str: str) -> str | None:
    """Return the URL from the environment block, or None if absent.

    Examples:
        >>> yaml = "environment:\\n  name: pypi\\n  url: https://example.com/\\n"
        >>> extract_pypi_url(yaml)
        'https://example.com/'
        >>> extract_pypi_url("jobs:\\n  build:\\n    runs-on: ubuntu-latest\\n")
        None
    """
    # TODO: split on newlines, iterate looking for a line containing
    # 'environment:'. After finding it, scan the following indented lines
    # for one that contains 'url:'. Strip and return the value after 'url:'.
    raise NotImplementedError
