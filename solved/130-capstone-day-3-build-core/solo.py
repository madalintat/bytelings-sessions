"""Solved: solo — function_too_long.

Key points:
- body_lines counts from the first non-docstring statement to the last.
- A docstring is ast.Expr wrapping ast.Constant as the FIRST body node.
- end_lineno - lineno + 1 gives the span of a statement in lines.
- AsyncFunctionDef is a separate type; isinstance checks both.
"""
from __future__ import annotations
import ast


def function_too_long(
    source: str, max_lines: int = 50
) -> list[tuple[str, int]]:
    """Return (name, body_line_count) for functions whose body exceeds max_lines."""
    tree = ast.parse(source)
    results: list[tuple[str, int, int]] = []  # (name, count, def_lineno)

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue

        body = node.body
        # Skip leading docstring.
        if (body and isinstance(body[0], ast.Expr)
                and isinstance(body[0].value, ast.Constant)):
            body = body[1:]

        if not body:
            continue

        # Line span: from first counted statement to last.
        first_line = body[0].lineno
        last_line = body[-1].end_lineno  # type: ignore[attr-defined]
        count = last_line - first_line + 1

        if count > max_lines:
            results.append((node.name, count, node.lineno))

    # Sort by function definition line number.
    results.sort(key=lambda t: t[2])
    return [(name, count) for name, count, _ in results]
