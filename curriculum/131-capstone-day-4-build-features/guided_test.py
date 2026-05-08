"""Tests for rung 3 — load_config from disk."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)


def test_returns_defaults_when_no_pyproject(tmp_path):
    """No pyproject.toml → return DEFAULTS."""
    result = ex.load_config(tmp_path, "my-lint")
    diagnose(
        result["function-too-long-max"] == 50,
        "When pyproject.toml is absent, load_config must return a copy of "
        "DEFAULTS. Check (target_root / 'pyproject.toml').is_file() first.",
        (
            lambda: result is ex.DEFAULTS,
            "Return a copy (dict(DEFAULTS) or {**DEFAULTS}), not the original "
            "DEFAULTS object — callers must not mutate shared state.",
        ),
    )


def test_reads_tool_section(tmp_path):
    """Parses [tool.my-lint] and merges with DEFAULTS."""
    (tmp_path / "pyproject.toml").write_text(
        "[tool.my-lint]\nfunction-too-long-max = 10\n"
    )
    result = ex.load_config(tmp_path, "my-lint")
    diagnose(
        result["function-too-long-max"] == 10,
        "load_config must read data['tool']['my-lint'] from the parsed TOML. "
        "The expected value is 10 from the file, not the default 50.",
        (
            lambda: result["function-too-long-max"] == 50,
            "You're returning the default (50). Did you call "
            "data.get('tool', {}).get(tool_name, {}) after parsing?",
        ),
    )


def test_unset_keys_keep_defaults(tmp_path):
    """Partial override leaves other defaults intact."""
    (tmp_path / "pyproject.toml").write_text(
        "[tool.my-lint]\nfunction-too-long-max = 25\n"
    )
    result = ex.load_config(tmp_path, "my-lint")
    assert result["nested-loop-depth-max"] == 3, (
        "nested-loop-depth-max was not overridden and must keep its default of 3"
    )


def test_missing_tool_section_falls_back(tmp_path):
    """pyproject.toml exists but has no [tool.my-lint] → return DEFAULTS."""
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'x'\n")
    result = ex.load_config(tmp_path, "my-lint")
    assert result["function-too-long-max"] == 50


def test_returns_independent_copy(tmp_path):
    """Each call returns a fresh dict, not the same object."""
    r1 = ex.load_config(tmp_path, "my-lint")
    r2 = ex.load_config(tmp_path, "my-lint")
    r1["function-too-long-max"] = 999
    assert r2["function-too-long-max"] == 50, (
        "load_config must return a new dict each call — mutation of one result "
        "must not affect another."
    )
