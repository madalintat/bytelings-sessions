"""Rung 3: Guided implement — write summary about a small "codebase".

Topic: extracting structure from unfamiliar code.

You're given a fake module-as-string. Implement `outline(source)`
to return a structural summary — exactly what you'd jot down in
pass-1 of the five-pass read.

The shape: {
    "imports": [...],         # module names imported, in order, deduped
    "classes":  [...],        # class names defined at top level
    "functions": [...],       # function names defined at top level
                              # (does NOT include methods inside classes)
}

Use the `ast` module — it parses the source for you, so you don't
write a regex parser.
"""
import ast


def outline(source: str) -> dict[str, list[str]]:
    """Return a structural outline of `source` (one Python module)."""
    # TODO: parse with ast.parse, walk top-level nodes only.
    # - For ast.Import: each `n.name` in node.names goes into imports.
    # - For ast.ImportFrom: node.module goes into imports.
    # - For ast.ClassDef: node.name -> classes.
    # - For ast.FunctionDef / AsyncFunctionDef: node.name -> functions.
    # Dedupe imports, preserve first-seen order.
    raise NotImplementedError
