"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
import textwrap
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_simple_call_sites():
    src = textwrap.dedent(
        """
        def foo():
            return 1

        def main():
            x = foo()
            y = foo()
            return x + y
        """
    ).strip()
    # Lines (1-based after strip):
    # 1: def foo()
    # 2:     return 1
    # 3:
    # 4: def main()
    # 5:     x = foo()
    # 6:     y = foo()
    # 7:     return x + y
    assert ex.find_callers(src, "foo") == [5, 6]


def test_ignores_definition_and_string():
    src = textwrap.dedent(
        '''
        def foo():
            return "foo"

        msg = "call foo() somewhere"
        '''
    ).strip()
    assert ex.find_callers(src, "foo") == []


def test_attribute_call_counts():
    src = textwrap.dedent(
        """
        result = obj.run()
        again = other.run()
        """
    ).strip()
    # both call sites for `.run`
    assert ex.find_callers(src, "run") == [1, 2]


def test_multiple_calls_same_line():
    src = "x = foo() + foo()\n"
    assert ex.find_callers(src, "foo") == [1, 1]


def test_target_not_called():
    src = "def main(): pass\n"
    assert ex.find_callers(src, "missing") == []
