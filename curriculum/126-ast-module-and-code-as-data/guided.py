"""Rung 3: Guided implement — list every import in source code.

Topic: ast.Import vs ast.ImportFrom

Two flavors:
    `import foo`           -> ast.Import with names=[alias(name='foo')]
    `import foo as f`      -> ast.Import with names=[alias(name='foo', asname='f')]
    `from x import y`      -> ast.ImportFrom(module='x', names=[alias(name='y')])
    `from x import y as z` -> ast.ImportFrom(module='x', names=[alias(name='y', asname='z')])
    `from . import x`      -> ast.ImportFrom(module=None, names=[...]); level=1

Build a normalized list. Each entry is a string in dotted form:
    "foo"               -> "foo"
    "foo as f"          -> "foo"          (we ignore aliases)
    "from x import y"   -> "x.y"
    "from . import y"   -> ".y"
    "from .. import y"  -> "..y"
"""
from __future__ import annotations
import ast


def list_imports(source: str) -> list[str]:
    """Return imports in source order. See module docstring for format.

    >>> list_imports("import os\\nfrom pathlib import Path")
    ['os', 'pathlib.Path']
    >>> list_imports("from . import a")
    ['.a']
    """
    # TODO: parse source. Walk. For ast.Import, emit each alias.name.
    # For ast.ImportFrom, build prefix from level (n dots) + module (or '')
    # and emit prefix + '.' + alias.name (with care: no leading dot if
    # both module and level are empty, which can't happen in valid code).
    raise NotImplementedError
