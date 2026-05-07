"""Tests for rung 3."""
import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex  # required so @dataclass can find the module
_spec.loader.exec_module(ex)


def test_under_limit():
    src = "def f(a, b, c): pass\n"
    assert ex.check_too_many_params(src) == []


def test_at_limit():
    src = "def f(a, b, c, d, e, f): pass\n"
    assert ex.check_too_many_params(src) == []


def test_over_default_limit():
    src = "def f(a, b, c, d, e, f, g): pass\n"
    issues = ex.check_too_many_params(src)
    assert len(issues) == 1
    assert issues[0].code == "M002"
    assert "f" in issues[0].message
    assert "7" in issues[0].message


def test_custom_limit():
    src = "def small(a, b, c): pass\n"
    issues = ex.check_too_many_params(src, limit=2)
    assert len(issues) == 1


def test_kwonly_counted():
    src = "def f(a, b, *, c, d, e, f, g): pass\n"  # 2 + 5 = 7
    assert len(ex.check_too_many_params(src)) == 1


def test_varargs_NOT_counted():
    src = "def f(a, b, c, d, e, f, *args, **kwargs): pass\n"  # 6, not 8
    assert ex.check_too_many_params(src) == []


def test_async():
    src = "async def f(a, b, c, d, e, f, g): pass\n"
    assert len(ex.check_too_many_params(src)) == 1
