"""Tests for rung 3 — green after rule_for and Linter.visit are implemented."""
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

_BARE_EXCEPT_SRC = """\
try:
    x = 1
except:
    pass
"""

_NO_VIOLATION_SRC = """\
try:
    x = 1
except ValueError:
    pass
"""


def test_rule_for_registers_function():
    import ast as _ast
    # bare_except was decorated at module load time — it must be in _REGISTRY
    diagnose(
        _ast.ExceptHandler in ex._REGISTRY,
        "ast.ExceptHandler not found in _REGISTRY. "
        "Did rule_for forget to store the function?",
    )
    handlers = ex._REGISTRY.get(_ast.ExceptHandler, [])
    diagnose(
        len(handlers) >= 1,
        f"Expected at least 1 handler for ast.ExceptHandler, got {len(handlers)}.",
        (lambda: len(handlers) == 0,
         "The list exists but is empty — rule_for is not appending the "
         "function into _REGISTRY[node_type]."),
    )


def test_bare_except_fires():
    linter = ex.Linter()
    findings = linter.run(_BARE_EXCEPT_SRC)
    diagnose(
        len(findings) == 1,
        f"Expected 1 finding for bare except, got {len(findings)}: {findings!r}.",
        (lambda: len(findings) == 0,
         "No findings — Linter.visit may not be dispatching to rules. "
         "Check that you look up type(node) in _REGISTRY."),
    )
    diagnose(
        findings[0].rule == "E001",
        f"Finding rule is {findings[0].rule!r}, expected 'E001'.",
    )


def test_typed_except_not_flagged():
    linter = ex.Linter()
    findings = linter.run(_NO_VIOLATION_SRC)
    diagnose(
        findings == [],
        f"Expected no findings for typed except, got {findings!r}.",
        (lambda: len(findings) > 0,
         "False positive — bare_except should return None when "
         "node.type is not None."),
    )


def test_findings_sorted_by_line():
    src = """\
try:
    pass
except:
    pass
try:
    pass
except:
    pass
"""
    linter = ex.Linter()
    findings = linter.run(src)
    lines = [f.line for f in findings]
    diagnose(
        lines == sorted(lines),
        f"Findings not sorted by line: {lines!r}.",
    )
