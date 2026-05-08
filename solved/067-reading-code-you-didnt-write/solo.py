"""Rung 4: Solo implement — solved version.

Walk every AST node, look for ast.Call nodes whose .func is either
ast.Name(id=target) or ast.Attribute(attr=target). Collect the
1-based line numbers, sort ascending.
"""
import ast


def find_callers(source: str, target: str) -> list[int]:
    tree = ast.parse(source)
    lines: list[int] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name) and func.id == target:
            lines.append(node.lineno)
        elif isinstance(func, ast.Attribute) and func.attr == target:
            lines.append(node.lineno)
    return sorted(lines)
