"""Rung 2: Fluency drill — fix the unused-import scanner.

Topic: 2-pass ast.walk for scope tracking

The function below finds imported names that are never used. It has a bug:
it only checks ast.Name nodes, so it misses attribute access like `os.path`
where the import is `import os` — `os` appears as the root of an
ast.Attribute node, not a bare ast.Name.

Fix it so attribute-based usage (e.g. `os.path.join(...)`) counts as a
use of `os`.

Hint: in `os.path.join`, the AST is:
    Attribute(value=Attribute(value=Name(id='os'), attr='path'), attr='join')
Walking down to the root Name gives you 'os'.
"""
from __future__ import annotations
import ast


def find_unused_imports(source: str) -> set[str]:
    """Return the set of imported names that are never used in *source*.

    Only handles `import X` and `import X as Y` style (not `from X import Y`).
    """
    tree = ast.parse(source)

    # Pass 1: collect imported names.
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                # Use the alias if given (e.g. `import os as operating_system`)
                name = alias.asname if alias.asname else alias.name
                imported.add(name)

    # Pass 2: collect used names.
    # BUG: this only collects bare Name nodes.
    # `os.path.join(...)` never produces a bare Name for `os` — it's the
    # value of an Attribute node. Fix this by also extracting the root
    # name from Attribute chains.
    used: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        # TODO: handle ast.Attribute nodes so `os.path` counts as using `os`.
        # Walk the .value chain until you hit an ast.Name and collect its .id.

    return imported - used
