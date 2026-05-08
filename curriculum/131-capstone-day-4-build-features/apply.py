"""Rung 5: Apply — mini pipeline with tomllib + threshold checks.

Reads a hardcoded pyproject.toml string, parses it with tomllib,
applies threshold checks on synthetic findings, and prints which
findings survived the configured limits.

Run:
    uv run python apply.py

Patterns: P-04 (dispatch-by-dict).
"""
from __future__ import annotations

import sys
import tomllib
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_s = spec_from_file_location("_d131_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
sys.modules["_d131_solo"] = _solo
_s.loader.exec_module(_solo)

# ---------------------------------------------------------------------------
# Fake pyproject.toml — no real file needed
# ---------------------------------------------------------------------------
_FAKE_PYPROJECT = """\
[tool.my-lint]
function-too-long-max = 20
nested-loop-depth-max = 2
"""

# ---------------------------------------------------------------------------
# Synthetic findings: (rule_id, metric_value, location_label)
# ---------------------------------------------------------------------------
_FINDINGS = [
    ("function-too-long", 15, "src/utils.py:check_all"),   # 15 <= 20 → skip
    ("function-too-long", 25, "src/core.py:process"),       # 25 > 20 → fire
    ("nested-loop-depth", 2,  "src/core.py:walk_tree"),     # 2 <= 2 → skip
    ("nested-loop-depth", 3,  "src/helpers.py:flatten"),    # 3 > 2 → fire
    ("function-too-long", 20, "src/cli.py:main"),           # 20 == 20 → skip
]


def main() -> None:
    config = tomllib.loads(_FAKE_PYPROJECT)
    tool_cfg_raw = config.get("tool", {}).get("my-lint", {})
    # Merge with hard-coded defaults
    tool_cfg = {
        "function-too-long-max": 50,
        "nested-loop-depth-max": 3,
        **tool_cfg_raw,
    }

    fired: list[tuple[str, str]] = []
    for rule_id, value, label in _FINDINGS:
        if _solo.apply_threshold(rule_id, tool_cfg, value):
            fired.append((rule_id, label))

    for rule_id, label in fired:
        print(f"  {label}: {rule_id}")

    # Inline verification
    labels = [label for _, label in fired]
    assert "src/core.py:process" in labels, (
        "function-too-long (25 > 20) must fire"
    )
    assert "src/helpers.py:flatten" in labels, (
        "nested-loop-depth (3 > 2) must fire"
    )
    assert "src/utils.py:check_all" not in labels, (
        "function-too-long (15 <= 20) must NOT fire"
    )
    assert "src/core.py:walk_tree" not in labels, (
        "nested-loop-depth (2 == 2) must NOT fire"
    )
    assert "src/cli.py:main" not in labels, (
        "function-too-long (20 == 20) must NOT fire"
    )
    print("✓ all threshold checks passed")


if __name__ == "__main__":
    main()
