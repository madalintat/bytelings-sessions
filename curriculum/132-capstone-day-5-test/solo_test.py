"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
from __future__ import annotations

import importlib.util
import sys
from io import StringIO
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)

Finding = ex.Finding


def _f(path: str, line: int, col: int, rule: str = "rule", msg: str = "msg"):
    return Finding(Path(path), line, col, rule, msg)


def test_empty_findings_returns_zero(capsys):
    rc = ex.main([], [])
    assert rc == 0


def test_nonempty_findings_returns_one(capsys):
    findings = [_f("a.py", 1, 0)]
    rc = ex.main([Path("a.py")], findings)
    assert rc == 1


def test_output_is_sorted(capsys):
    findings = [
        _f("b.py", 3, 0, "rule", "msg"),
        _f("a.py", 5, 0, "rule", "msg"),
        _f("a.py", 1, 0, "rule", "msg"),
    ]
    ex.main([Path("a.py"), Path("b.py")], findings)
    out = capsys.readouterr().out.splitlines()
    assert len(out) == 3
    assert out[0].startswith("a.py:1:")
    assert out[1].startswith("a.py:5:")
    assert out[2].startswith("b.py:3:")


def test_output_format(capsys):
    findings = [_f("x.py", 7, 2, "bare-except", "use specific exception")]
    ex.main([Path("x.py")], findings)
    out = capsys.readouterr().out.strip()
    assert out == "x.py:7:2: bare-except: use specific exception"


def test_empty_findings_no_output(capsys):
    ex.main([], [])
    out = capsys.readouterr().out
    assert out == ""
