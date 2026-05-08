"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_shout():
    assert ex.shout("hello") == "HELLO"
    assert ex.shout("") == ""


def test_join_with_dashes():
    assert ex.join_with_dashes(["a", "b", "c"]) == "a-b-c"
    assert ex.join_with_dashes(["only"]) == "only"
    assert ex.join_with_dashes([]) == ""


def test_join_uses_join_method():
    """Sanity check that the body actually calls str.join (the point of the day)."""
    import inspect
    src = inspect.getsource(ex.join_with_dashes)
    assert ".join(" in src, "Use ''.join(...) instead of += in a loop"


def test_replace_spaces():
    assert ex.replace_spaces("hello world") == "hello_world"
    assert ex.replace_spaces("a b c") == "a_b_c"
    assert ex.replace_spaces("nospaces") == "nospaces"
