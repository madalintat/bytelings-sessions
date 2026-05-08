"""Rung 4: Solo implement — function_too_long rule.

Topic: P-07 accumulator-into-dict meets P-30 ast-walker-visitor

Implement:

    function_too_long(source: str, max_lines: int = 50)
        -> list[tuple[str, int]]

Returns a list of (function_name, body_line_count) tuples for every
function definition whose BODY exceeds *max_lines*.

Rules:
- Count only the body lines, not the `def` line itself.
- If the first body statement is an `ast.Expr` wrapping an `ast.Constant`
  (i.e. a docstring), skip it: don't count it as a body line and start
  counting from the next statement.
- body_line_count = end_lineno_of_last_body_stmt - lineno_of_first_counted_stmt + 1
- Include BOTH FunctionDef and AsyncFunctionDef.
- Sort results by line number of the function definition.

Hidden tests cover:
  - function exactly at max_lines → NOT returned
  - function one line over → returned
  - docstring-first function: docstring lines are excluded from count
  - async function: included
  - nested function: each counted independently
  - empty function (just `pass`): body_line_count == 1, likely not flagged
    at default threshold
"""
from __future__ import annotations
import ast


def function_too_long(
    source: str, max_lines: int = 50
) -> list[tuple[str, int]]:
    """Return (name, body_line_count) for functions whose body exceeds max_lines."""
    raise NotImplementedError
