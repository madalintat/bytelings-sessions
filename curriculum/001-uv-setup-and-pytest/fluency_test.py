"""Tests for rung 2 — should be green after both TODOs are fixed.

Canonical demonstration of the bytelings `diagnose` helper. Each test
pairs the main equality check with a list of (predicate, message)
pairs so that when the learner gets it wrong, they see a teaching
message ("Your greeting is missing the comma") instead of a generic
string diff.
"""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_greet_basic():
    expected = "Hello, Bytelinger!"
    actual = ex.greet("Bytelinger")
    diagnose(
        actual == expected,
        f"Expected {expected!r}, got {actual!r}. Re-read the docstring "
        "for the exact format.",
        (lambda: ", " not in actual,
         "Your greeting is missing the comma — the docstring shows "
         "'Hello, <name>!' with a comma after Hello."),
        (lambda: not actual.endswith("!"),
         "Your greeting is missing the trailing '!' — the docstring "
         "ends with one."),
    )


def test_greet_empty():
    expected = "Hello, !"
    actual = ex.greet("")
    diagnose(
        actual == expected,
        f"Expected {expected!r} for empty name, got {actual!r}.",
        (lambda: ", " not in actual,
         "Even with an empty name, the comma stays — the f-string "
         "literal includes it."),
    )


def test_add_one():
    diagnose(
        ex.add_one(0) == 1,
        f"add_one(0) returned {ex.add_one(0)!r}, expected 1.",
        (lambda: ex.add_one(0) == 0,
         "add_one(0) returned 0 — that's the input, not n + 1. "
         "Look at the operator."),
        (lambda: ex.add_one(0) == 2,
         "add_one(0) returned 2 — off-by-one in the OTHER direction. "
         "The function adds ONE, not two."),
    )
    diagnose(
        ex.add_one(41) == 42,
        f"add_one(41) returned {ex.add_one(41)!r}, expected 42.",
        (lambda: ex.add_one(41) == 41,
         "add_one(41) returned 41 — that's the input unchanged."),
    )
    diagnose(
        ex.add_one(-5) == -4,
        f"add_one(-5) returned {ex.add_one(-5)!r}, expected -4.",
        (lambda: ex.add_one(-5) == -6,
         "add_one(-5) returned -6 — you're subtracting one. "
         "Negatives can be tricky; the operation is still '+ 1'."),
    )
