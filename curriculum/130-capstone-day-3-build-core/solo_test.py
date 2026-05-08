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

_NEWLINES_51 = "\n".join(["    pass"] * 51)
_NEWLINES_50 = "\n".join(["    pass"] * 50)


def test_short_function_not_flagged():
    src = "def f():\n    pass\n"
    assert ex.function_too_long(src, max_lines=50) == []


def test_long_function_flagged():
    src = f"def long_func():\n{_NEWLINES_51}\n"
    result = ex.function_too_long(src, max_lines=50)
    assert len(result) == 1
    name, count = result[0]
    assert name == "long_func"
    assert count > 50


def test_exactly_at_limit_not_flagged():
    src = f"def exactly():\n{_NEWLINES_50}\n"
    assert ex.function_too_long(src, max_lines=50) == []


def test_docstring_excluded_from_count():
    # 51 pass lines + 1 docstring line — docstring shouldn't be counted
    src = f'def f():\n    """doc"""\n{_NEWLINES_51}\n'
    result = ex.function_too_long(src, max_lines=50)
    assert len(result) == 1


def test_docstring_keeps_short_function_clean():
    # 1 docstring + 1 pass — still very short
    src = 'def f():\n    """doc"""\n    pass\n'
    assert ex.function_too_long(src, max_lines=50) == []


def test_async_function_included():
    src = f"async def af():\n{_NEWLINES_51}\n"
    result = ex.function_too_long(src, max_lines=50)
    assert len(result) == 1
    assert result[0][0] == "af"


def test_returns_list_of_tuples():
    src = "def f():\n    pass\n"
    result = ex.function_too_long(src, max_lines=1)
    # Even for a short result, it must be a list of tuples.
    assert isinstance(result, list)
    if result:
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 2


def test_multiple_long_functions_sorted_by_line():
    body = "\n".join(["    x = 1"] * 55)
    src = f"def alpha():\n{body}\ndef beta():\n{body}\n"
    result = ex.function_too_long(src, max_lines=50)
    assert len(result) == 2
    names = [r[0] for r in result]
    assert names == ["alpha", "beta"]
