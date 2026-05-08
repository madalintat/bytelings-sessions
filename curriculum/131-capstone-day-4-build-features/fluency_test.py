"""Tests for rung 2 — fix the TOML config loader.

The `diagnose` helper shows a targeted hint when the learner's fix
goes in the right direction but misses a detail.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
sys.modules[_NAME] = ex
_spec.loader.exec_module(ex)

# Minimal valid pyproject.toml content
_TOML_WITH_TOOL = """\
[tool.my-lint]
function-too-long-max = 20
nested-loop-depth-max = 2
"""

_TOML_WITHOUT_TOOL = """\
[project]
name = "my-project"
"""


def test_parses_toml_not_json():
    """Verify that the function no longer uses json.loads."""
    src = (_HERE / "fluency.py").read_text()
    diagnose(
        "json.loads" not in src,
        "Remove json.loads and use tomllib.loads instead — "
        "TOML and JSON are different formats.",
        (
            lambda: "import json" in src,
            "You still import json. Switch to `import tomllib` and call "
            "tomllib.loads(content) to parse the TOML string.",
        ),
    )


def test_reads_tool_section():
    """load_config returns the merged dict for the named tool."""
    result = ex.load_config(_TOML_WITH_TOOL, "my-lint")
    diagnose(
        result["function-too-long-max"] == 20,
        "Expected function-too-long-max=20 from the [tool.my-lint] section. "
        "Check that you read data['tool'][tool_name], not data[tool_name].",
        (
            lambda: result["function-too-long-max"] == 50,
            "You got the DEFAULTS value (50) instead of the override (20). "
            "The TOML section is [tool.my-lint], so use "
            "data.get('tool', {}).get(tool_name, {}) to reach it.",
        ),
    )


def test_returns_defaults_when_no_tool_section():
    """Returns DEFAULTS copy when the tool section is absent."""
    result = ex.load_config(_TOML_WITHOUT_TOOL, "my-lint")
    diagnose(
        result["function-too-long-max"] == 50,
        "When [tool.my-lint] is absent, load_config must return the DEFAULTS "
        "(function-too-long-max=50).",
    )


def test_merges_partial_overrides():
    """Only overridden keys change; unspecified keys keep their defaults."""
    toml = "[tool.my-lint]\nfunction-too-long-max = 30\n"
    result = ex.load_config(toml, "my-lint")
    diagnose(
        result["nested-loop-depth-max"] == 3,
        "Partial overrides must merge with DEFAULTS. "
        "nested-loop-depth-max was not overridden so it should stay 3.",
    )
    assert result["function-too-long-max"] == 30
