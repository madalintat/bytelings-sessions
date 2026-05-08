"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


FINDINGS = [
    {"path": "src/main.py",  "line": 10, "col": 4, "rule": "bare-except",   "message": "msg"},
    {"path": "src/main.py",  "line": 22, "col": 0, "rule": "unused-import", "message": "msg"},
    {"path": "src/utils.py", "line": 5,  "col": 8, "rule": "bare-except",   "message": "msg"},
    {"path": "src/utils.py", "line": 31, "col": 0, "rule": "unused-import", "message": "msg"},
    {"path": "src/cli.py",   "line": 14, "col": 0, "rule": "unused-import", "message": "msg"},
    {"path": "src/cli.py",   "line": 20, "col": 0, "rule": "bare-except",   "message": "msg"},
    {"path": "src/cli.py",   "line": 30, "col": 0, "rule": "bare-except",   "message": "msg"},
]


def test_title_line():
    s = ex.summary(FINDINGS)
    assert "Linter Findings Summary" in s


def test_total_count():
    s = ex.summary(FINDINGS)
    assert "Total: 7" in s


def test_rule_counts():
    s = ex.summary(FINDINGS)
    # bare-except: 4, unused-import: 3
    assert "bare-except: 4" in s
    assert "unused-import: 3" in s


def test_rules_sorted_desc():
    s = ex.summary(FINDINGS)
    idx_bare = s.index("bare-except")
    idx_unused = s.index("unused-import")
    assert idx_bare < idx_unused, "bare-except (4) should appear before unused-import (3)"


def test_top_3_files():
    s = ex.summary(FINDINGS)
    # src/cli.py has 3, src/main.py and src/utils.py have 2 each
    assert "src/cli.py" in s
    assert "src/main.py" in s
    assert "src/utils.py" in s


def test_empty_findings():
    s = ex.summary([])
    assert "Total: 0" in s
