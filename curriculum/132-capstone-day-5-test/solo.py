"""Rung 4: Solo implement — main entry point.

Topic: exit codes, sorted output

Implement `main(targets, findings) -> int`:
- If `findings` is empty: return 0.
- Otherwise:
    1. Sort findings by (path, line, col).
    2. Print each formatted finding (path:line:col: rule-id: message).
    3. Return 1.

Reuse `Finding`, `sort_findings`, and `format_finding` from the
sibling rungs (they are already loaded below).

Patterns: P-13 (enumerate-for-index) — enumerate targets when printing
a per-file summary, if you add one. Not strictly required here.

Hidden tests verify: return value 0 with empty findings, return value 1
with non-empty findings, and sorted print output.
"""
from __future__ import annotations

import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_f_spec = spec_from_file_location("_d132_fluency", _HERE / "fluency.py")
_fluency = module_from_spec(_f_spec)
sys.modules["_d132_fluency"] = _fluency
_f_spec.loader.exec_module(_fluency)

_g_spec = spec_from_file_location("_d132_guided", _HERE / "guided.py")
_guided = module_from_spec(_g_spec)
sys.modules["_d132_guided"] = _guided
_g_spec.loader.exec_module(_guided)

Finding = _guided.Finding


def main(targets: list[Path], findings: list[Finding]) -> int:
    """Print sorted findings and return exit code.

    Returns 0 when `findings` is empty, 1 otherwise.
    """
    raise NotImplementedError
