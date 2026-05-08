"""Tests for rung 2 — behavior tests (must keep passing) +
a structural test that letter_grade was extracted."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_summary_basic():
    assert ex.grade_summary([100, 90, 80])["grade"] == "A"


def test_summary_borderline_b():
    assert ex.grade_summary([80])["grade"] == "B"


def test_summary_empty():
    assert ex.grade_summary([]) == {"avg": 0.0, "grade": "F"}


def test_summary_failing():
    assert ex.grade_summary([10, 20, 30])["grade"] == "F"


def test_letter_grade_exists():
    assert hasattr(ex, "letter_grade"), "extract `letter_grade(score)`"


def test_letter_grade_values():
    assert ex.letter_grade(95) == "A"
    assert ex.letter_grade(80) == "B"
    assert ex.letter_grade(70) == "C"
    assert ex.letter_grade(60) == "D"
    assert ex.letter_grade(0) == "F"
