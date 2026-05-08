"""Tests for rung 2 — green after both TODOs are fixed."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_counts_rules():
    result = ex.count_by_rule(ex.SAMPLE_FINDINGS)
    diagnose(
        result == {"bare-except": 2, "unused-import": 3},
        f"Expected {{'bare-except': 2, 'unused-import': 3}}, got {result!r}",
        (lambda: len(result) == 0,
         "Returned an empty dict — the split on ',' never splits these lines correctly. "
         "Fix TODO 1: split on ':' instead."),
        (lambda: any(len(k) > 30 for k in result),
         "Keys are very long — you're probably not splitting on ':' correctly. "
         "The rule-id is the 4th colon-delimited segment (index 3)."),
    )


def test_empty_text():
    result = ex.count_by_rule("")
    diagnose(
        result == {},
        f"Expected {{}} for empty text, got {result!r}",
    )


def test_blank_lines_skipped():
    text = "\nsrc/a.py:1:0: bare-except: msg\n\n"
    result = ex.count_by_rule(text)
    diagnose(
        result == {"bare-except": 1},
        f"Expected {{'bare-except': 1}}, got {result!r}",
    )


def test_single_rule():
    text = "a.py:1:0: mutable-default: msg\nb.py:2:0: mutable-default: msg\n"
    result = ex.count_by_rule(text)
    diagnose(
        result == {"mutable-default": 2},
        f"Expected {{'mutable-default': 2}}, got {result!r}",
        (lambda: "mutable-default" not in result,
         "Rule 'mutable-default' not found. Check the index: path:line:col: rule: message "
         "→ split by ':' gives index 3 as the rule (with leading space — strip it)."),
    )
