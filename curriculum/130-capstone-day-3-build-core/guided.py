"""Rung 3: Guided implement — find_unused_imports with line numbers.

Topic: 2-pass scope tracking, collecting lineno metadata

Implement `find_unused_imports(source)` returning a SORTED LIST of
import names (str) that are never used in *source*.

Algorithm (two passes over the AST):

Pass 1 — collect imported names:
  Walk for ast.Import nodes. For each alias:
    - Use alias.asname if set, else alias.name.
    - Record the name AND its lineno for diagnostics (you can store in a dict).

Pass 2 — collect used names (ALL ast.Name ids + root names of ast.Attribute chains):
  Walk the whole tree. For every ast.Name, add node.id to a `used` set.
  For every ast.Attribute, walk down the .value chain until you reach an
  ast.Name and add that name's .id too.

Result: return sorted(imported_names - used_names).

The `from X import Y` form is out of scope for this exercise.
"""
from __future__ import annotations
import ast


def find_unused_imports(source: str) -> list[str]:
    """Return sorted list of unused import names in *source*.

    >>> find_unused_imports("import os\\nimport sys\\nprint(sys.argv)\\n")
    ['os']
    """
    raise NotImplementedError
