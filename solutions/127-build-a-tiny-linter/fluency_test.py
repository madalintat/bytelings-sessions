"""Tests for rung 2."""
import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex  # required so @dataclass can find the module
_spec.loader.exec_module(ex)


def test_list_default_flagged():
    src = "def f(x=[]):\n    pass\n"
    issues = ex.check_mutable_defaults(src)
    assert len(issues) == 1
    assert issues[0].code == "M001"
    assert "f" in issues[0].message


def test_dict_default_flagged():
    src = "def f(x={}):\n    pass\n"
    assert len(ex.check_mutable_defaults(src)) == 1


def test_set_default_flagged():
    src = "def f(x={1, 2}):\n    pass\n"
    assert len(ex.check_mutable_defaults(src)) == 1


def test_tuple_default_NOT_flagged():
    """Tuples are immutable. They're a fine default value."""
    src = "def f(x=(1, 2)):\n    pass\n"
    assert ex.check_mutable_defaults(src) == []


def test_none_default_not_flagged():
    src = "def f(x=None):\n    pass\n"
    assert ex.check_mutable_defaults(src) == []


def test_no_default_not_flagged():
    src = "def f(x):\n    pass\n"
    assert ex.check_mutable_defaults(src) == []


def test_async_function_flagged():
    src = "async def f(x=[]):\n    pass\n"
    assert len(ex.check_mutable_defaults(src)) == 1
