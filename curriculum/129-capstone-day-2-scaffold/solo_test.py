"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)


def test_list_default_flagged():
    src = "def f(x=[]): pass\n"
    findings = ex.Linter().run(src)
    assert len(findings) == 1
    assert findings[0].rule == "E002"
    assert "f" in findings[0].message


def test_dict_default_flagged():
    src = "def f(x={}): pass\n"
    findings = ex.Linter().run(src)
    assert len(findings) == 1
    assert findings[0].rule == "E002"


def test_set_default_flagged():
    src = "def f(x={1, 2}): pass\n"
    findings = ex.Linter().run(src)
    assert len(findings) == 1
    assert findings[0].rule == "E002"


def test_tuple_default_not_flagged():
    src = "def f(x=(1, 2)): pass\n"
    assert ex.Linter().run(src) == []


def test_none_default_not_flagged():
    src = "def f(x=None): pass\n"
    assert ex.Linter().run(src) == []


def test_int_default_not_flagged():
    src = "def f(x=0): pass\n"
    assert ex.Linter().run(src) == []


def test_no_defaults_not_flagged():
    src = "def f(x): pass\n"
    assert ex.Linter().run(src) == []


def test_async_function_flagged():
    src = "async def f(x=[]): pass\n"
    findings = ex.Linter().run(src)
    assert len(findings) == 1
    assert findings[0].rule == "E002"


def test_multiple_functions_each_flagged():
    src = "def a(x=[]): pass\ndef b(y={}): pass\n"
    findings = ex.Linter().run(src)
    assert len(findings) == 2
    rules = {f.rule for f in findings}
    assert rules == {"E002"}
