"""Rung 4: Solo implement.

Topic: reading code with `grep`-style discipline.

Implement `find_callers(source: str, target: str) -> list[int]`:

  - `source` is a Python module as a single string.
  - `target` is a function name.
  - Return the 1-based line numbers where `target` is *called*
    (i.e., appears as the function in a Call node — `target(...)`).
  - DO NOT include lines where `target` is merely defined, mentioned
    in a string, or imported.
  - Order: ascending line number; duplicates allowed if the same
    line has multiple calls.

Hint: parse with `ast`, walk every node with `ast.walk`, look for
`ast.Call` whose `.func` is `ast.Name(id=target)` or
`ast.Attribute(attr=target)`.

Hidden tests in 04_solo_test.py.
"""
import ast


def find_callers(source: str, target: str) -> list[int]:
    raise NotImplementedError
