"""Tests for rung 3 — sort_findings."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)

F = ex.Finding


def _f(path: str, line: int, col: int = 0) -> ex.Finding:
    return F(Path(path), line, col, "rule", "msg")


def test_sorts_by_path():
    findings = [_f("b.py", 1), _f("a.py", 1)]
    result = ex.sort_findings(findings)
    diagnose(
        [str(f.path) for f in result] == ["a.py", "b.py"],
        "sort_findings must sort by path first. a.py comes before b.py.",
        (
            lambda: result == findings,
            "The list is unchanged. Did you forget to return a sorted copy? "
            "Use sorted(..., key=lambda f: (str(f.path), f.line, f.col)).",
        ),
    )


def test_sorts_by_line_within_same_path():
    findings = [_f("a.py", 10), _f("a.py", 2), _f("a.py", 5)]
    result = ex.sort_findings(findings)
    lines = [f.line for f in result]
    diagnose(
        lines == [2, 5, 10],
        f"Within the same path, sort by line. Expected [2, 5, 10], got {lines}.",
    )


def test_sorts_by_col_within_same_path_and_line():
    findings = [_f("a.py", 3, 8), _f("a.py", 3, 0), _f("a.py", 3, 4)]
    result = ex.sort_findings(findings)
    cols = [f.col for f in result]
    diagnose(
        cols == [0, 4, 8],
        f"Within the same path+line, sort by col. Expected [0, 4, 8], got {cols}.",
    )


def test_does_not_mutate_input():
    original = [_f("b.py", 1), _f("a.py", 1)]
    copy = list(original)
    ex.sort_findings(original)
    assert original == copy, "sort_findings must not sort the input list in-place."


def test_empty_list():
    assert ex.sort_findings([]) == []


def test_single_element():
    findings = [_f("z.py", 99)]
    assert ex.sort_findings(findings) == findings
