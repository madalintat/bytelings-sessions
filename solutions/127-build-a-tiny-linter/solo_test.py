"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex  # required so @dataclass can find the module
_spec.loader.exec_module(ex)


def test_top_level_print_flagged():
    src = "print('hi')\n"
    issues = ex.check_print_statements(src)
    assert len(issues) == 1
    assert issues[0].code == "M003"
    assert issues[0].line == 1


def test_print_inside_function_NOT_flagged():
    src = "def f():\n    print('hi')\n"
    assert ex.check_print_statements(src) == []


def test_print_inside_class_NOT_flagged():
    src = "class A:\n    print('hi')\n"
    assert ex.check_print_statements(src) == []


def test_method_print_ignored():
    src = "logger.print('hi')\n"
    assert ex.check_print_statements(src) == []


def test_multiple_top_level_prints():
    src = "print(1)\nprint(2)\n"
    assert len(ex.check_print_statements(src)) == 2


def test_lint_combines_rules_sorted():
    src = (
        "def f(x=[]):\n"          # line 1: M001
        "    pass\n"
        "print('hi')\n"            # line 3: M003
        "def g(a,b,c,d,e,f,g):\n"  # line 4: M002
        "    pass\n"
    )
    issues = ex.lint(src)
    codes = [i.code for i in issues]
    assert "M001" in codes
    assert "M002" in codes
    assert "M003" in codes
    # sorted by line number
    lines = [i.line for i in issues]
    assert lines == sorted(lines)


def test_lint_respects_max_params():
    src = "def f(a,b,c): pass\n"
    assert ex.lint(src, max_params=2) != []
    assert ex.lint(src, max_params=10) == []
