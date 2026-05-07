"""Rung 4: Solo implement.

Topic: function complexity sketch

Implement `function_summary(source)` returning a list of dicts, one per
function definition (top-level or nested). Each dict:

    {
        "name": str,           # function name
        "line": int,           # node.lineno (1-based)
        "args": int,           # number of *positional* parameters,
                                # excluding *args, **kwargs, and posonly/kwonly
                                # — i.e. len(node.args.args)
        "is_async": bool,      # AsyncFunctionDef
        "returns": int,        # count of `return` statements anywhere inside
                                # this function (including in nested fns? NO —
                                # only this function's direct body, not nested).
    }

Functions appear in source order (use ast.walk; sort by line if needed).

Hidden tests exercise: empty body, returns count excludes nested fns,
async, *args/**kwargs not counted, deep nesting.
"""
from __future__ import annotations
import ast


def function_summary(source: str) -> list[dict]:
    raise NotImplementedError
