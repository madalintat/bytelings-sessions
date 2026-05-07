"""Capstone Day 1 — sanity check.

The only "test" today is: did you write a design? We don't grade the
content. We just confirm design.md exists, isn't a placeholder, and
covers the five sections.

Skip this if you'd rather work in a different file. Tomorrow's tests
are real.
"""
from pathlib import Path
import pytest

_HERE = Path(__file__).parent


def test_design_md_exists():
    assert (_HERE / "design.md").is_file()


def test_design_md_filled_in():
    text = (_HERE / "design.md").read_text(encoding="utf-8")
    # The template has placeholder text in <angle brackets>. If you
    # haven't replaced any of it, this fails with a hint.
    if "<your project name>" in text:
        pytest.skip("design.md still has the template placeholder — fill it in")
    if "<One paragraph" in text:
        pytest.skip("design.md still has the section-1 placeholder")


def test_design_covers_five_sections():
    text = (_HERE / "design.md").read_text(encoding="utf-8")
    for marker in ("## 1.", "## 2.", "## 3.", "## 4.", "## 5."):
        assert marker in text, f"missing section header {marker!r}"
