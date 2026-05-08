"""Tests for rung 3."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


LOG = """\
src/main.py:10:4: bare-except: bare `except:` catches everything
src/main.py:22:0: unused-import: `os` imported but never used
src/utils.py:5:8: bare-except: bare `except:` catches everything
not a valid line at all
src/cli.py:14:0: unused-import: `json` imported but never used
"""


def test_returns_list_of_dicts():
    result = ex.parse_findings_log(LOG)
    diagnose(
        isinstance(result, list) and len(result) == 4,
        f"Expected 4 parsed findings (1 malformed line skipped), got {len(result) if isinstance(result, list) else result!r}",
        (lambda: isinstance(result, list) and len(result) == 5,
         "Returned 5 items — the malformed line should be silently skipped."),
        (lambda: isinstance(result, list) and len(result) == 0,
         "Returned empty list — check the regex pattern matches the log format."),
    )


def test_first_finding_fields():
    result = ex.parse_findings_log(LOG)
    first = result[0]
    diagnose(
        first.get("path") == "src/main.py",
        f"Expected path 'src/main.py', got {first.get('path')!r}",
    )
    diagnose(
        first.get("line") == 10,
        f"Expected line=10 (int), got {first.get('line')!r}",
        (lambda: first.get("line") == "10",
         "line is a string '10' — convert with int()."),
    )
    diagnose(
        first.get("rule") == "bare-except",
        f"Expected rule 'bare-except', got {first.get('rule')!r}",
    )


def test_message_preserved():
    result = ex.parse_findings_log(LOG)
    first = result[0]
    diagnose(
        "bare `except:`" in first.get("message", ""),
        f"Expected message to contain 'bare `except:`', got {first.get('message')!r}",
    )


def test_col_is_int():
    result = ex.parse_findings_log(LOG)
    diagnose(
        all(isinstance(r["col"], int) for r in result),
        "col values should be ints, not strings.",
        (lambda: any(isinstance(r["col"], str) for r in result),
         "col is a string — convert with int()."),
    )


def test_empty_text():
    result = ex.parse_findings_log("")
    diagnose(result == [], f"Expected [] for empty text, got {result!r}")
