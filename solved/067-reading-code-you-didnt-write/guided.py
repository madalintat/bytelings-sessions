"""Rung 3: Guided implement — solved version.

Walk the top-level AST nodes only (not nested bodies). Dedupe imports
by maintaining an ordered set via dict. Classes and functions at the
module level are straightforward ast.ClassDef / ast.FunctionDef checks.
"""
import ast


def outline(source: str) -> dict[str, list[str]]:
    """Return a structural outline of `source` (one Python module)."""
    tree = ast.parse(source)
    imports: dict[str, None] = {}  # ordered set via insertion order
    classes: list[str] = []
    functions: list[str] = []

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.setdefault(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.setdefault(node.module)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)

    return {
        "imports": list(imports),
        "classes": classes,
        "functions": functions,
    }
