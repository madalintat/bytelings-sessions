"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_flip():
    assert ex.flip_name("Smith, John") == "John Smith"


def test_extra_whitespace():
    assert ex.flip_name("Smith,   John") == "John Smith"
    assert ex.flip_name("  Smith , John  ") == "John Smith"


def test_lowercase_input():
    assert ex.flip_name("smith, john") == "John Smith"


def test_no_comma_just_first_name():
    assert ex.flip_name("alice") == "Alice"
    assert ex.flip_name("  bob  ") == "Bob"


def test_empty_returns_empty():
    assert ex.flip_name("") == ""
    assert ex.flip_name("   ") == ""


def test_uppercase_input():
    assert ex.flip_name("DOE, JANE") == "Jane Doe"
