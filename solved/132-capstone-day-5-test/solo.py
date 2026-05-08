"""Rung 4: Solo implement — solved version.

main() is the public contract every CI tool reads:
  0 → clean (no findings)
  1 → findings present

Sort before printing so CI diffs are stable across re-runs.
"""
from __future__ import annotations

import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_f_spec = spec_from_file_location("_d132s_fluency", _HERE / "fluency.py")
_fluency = module_from_spec(_f_spec)
sys.modules["_d132s_fluency"] = _fluency
_f_spec.loader.exec_module(_fluency)

_g_spec = spec_from_file_location("_d132s_guided", _HERE / "guided.py")
_guided = module_from_spec(_g_spec)
sys.modules["_d132s_guided"] = _guided
_g_spec.loader.exec_module(_guided)

Finding = _guided.Finding


def main(targets: list[Path], findings: list[Finding]) -> int:
    """Print sorted findings and return exit code 0 or 1."""
    if not findings:
        return 0
    for f in _guided.sort_findings(findings):
        print(_fluency.format_finding(f))
    return 1
