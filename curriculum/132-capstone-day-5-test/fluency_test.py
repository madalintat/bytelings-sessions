"""Tests for rung 2 — fix format_finding."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)

_PATTERN = re.compile(r"^(.+?):(\d+):(\d+): ([a-z][a-z0-9-]*): (.+)$")

_F = ex.Finding(
    path=Path("src/foo.py"),
    line=12,
    col=4,
    rule_id="bare-except",
    message="use `except <ExceptionType>:` not bare `except:`",
)


def test_format_matches_standard_pattern():
    result = ex.format_finding(_F)
    diagnose(
        bool(_PATTERN.match(result)),
        f"Expected format: path:line:col: rule-id: message\nGot: {result!r}\n"
        "Fix the f-string so it uses colons, not brackets or equals signs.",
        (
            lambda: "[" in result,
            "Remove the square brackets around the path. "
            "The format is `src/foo.py:12:4: bare-except: ...`, not `[src/foo.py] ...`.",
        ),
        (
            lambda: "line=" in result or "col=" in result,
            "Remove `line=` and `col=` labels. "
            "Use colons: `path:line:col: rule-id: message`.",
        ),
    )


def test_path_is_first_field():
    result = ex.format_finding(_F)
    assert result.startswith("src/foo.py:"), (
        f"Output must start with the path. Got: {result!r}"
    )


def test_line_and_col_are_numeric():
    result = ex.format_finding(_F)
    m = _PATTERN.match(result)
    assert m is not None, f"Does not match standard pattern: {result!r}"
    assert m.group(2) == "12"
    assert m.group(3) == "4"


def test_rule_id_is_present():
    result = ex.format_finding(_F)
    assert "bare-except" in result, (
        f"rule_id 'bare-except' must appear in the output. Got: {result!r}"
    )


def test_message_is_present():
    result = ex.format_finding(_F)
    assert "bare `except:`" in result, (
        f"The message text must appear in the output. Got: {result!r}"
    )
