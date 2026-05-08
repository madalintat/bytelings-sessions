"""Rung 4: Solo implement — solved version.

Strategy for 'returns excludes nested functions':
Walk the tree to find each FunctionDef / AsyncFunctionDef node.
For each such node, do a *second* restricted walk of that node's body:
collect Return nodes that are NOT inside a nested function definition.
This is achieved by recursing through the body and stopping descent
whenever we hit another function definition.

Result list is sorted by lineno so output matches source order.
"""
from __future__ import annotations

import ast


def _count_direct_returns(func_node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    """Count Return nodes directly inside func_node, excluding nested functions."""
    count = 0
    # Explicit stack-based DFS that does NOT descend into nested fn bodies.
    stack: list[ast.AST] = list(ast.iter_child_nodes(func_node))
    while stack:
        node = stack.pop()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue  # don't descend into nested function bodies
        if isinstance(node, ast.Return):
            count += 1
        stack.extend(ast.iter_child_nodes(node))
    return count


def function_summary(source: str) -> list[dict]:
    """Return one summary dict per function/async-function in source order."""
    tree = ast.parse(source)
    results: list[dict] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            results.append({
                "name": node.name,
                "line": node.lineno,
                "args": len(node.args.args),
                "is_async": isinstance(node, ast.AsyncFunctionDef),
                "returns": _count_direct_returns(node),
            })
    results.sort(key=lambda d: d["line"])
    return results
