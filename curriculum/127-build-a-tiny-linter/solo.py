"""Rung 4: Solo implement.

Topic: a third rule + a dispatcher.

Implement TWO things:

1. `check_print_statements(source)` -> list[Issue]
   Code: "M003"
   Message: "print() call at top-level — use logging instead"

   Triggers when there is a call to the bare name `print` (not
   `module.print` or `Class.print`) at *module top level* (not inside
   a function or class). Use the `lineno` of the Call node.

2. `lint(source, *, max_params=6)` -> list[Issue]
   Returns the combined output of all three rules (M001, M002, M003)
   from this module's siblings. Sort the result by `line` (stable).

Hidden tests cover: print not at top-level (in a function) is allowed,
print as method call ignored, multiple rules firing on one file.

Hint: M001/M002 live in fluency.py and guided.py — reuse them.
"""
from __future__ import annotations
import ast
import sys
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_f = spec_from_file_location("_d127_fluency", _HERE / "fluency.py")
_fluency = module_from_spec(_f)
sys.modules["_d127_fluency"] = _fluency
_f.loader.exec_module(_fluency)
_g = spec_from_file_location("_d127_guided", _HERE / "guided.py")
_guided = module_from_spec(_g)
sys.modules["_d127_guided"] = _guided
_g.loader.exec_module(_guided)


@dataclass
class Issue:
    line: int
    code: str
    message: str


def check_print_statements(source: str) -> list[Issue]:
    raise NotImplementedError


def lint(source: str, *, max_params: int = 6) -> list[Issue]:
    raise NotImplementedError
