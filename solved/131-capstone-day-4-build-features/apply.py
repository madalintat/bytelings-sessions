"""Rung 5: Apply — solved version.

Parses a fake pyproject.toml with tomllib, then dispatches findings
through apply_threshold. Inline asserts confirm the expected outcomes.
"""
from __future__ import annotations

import sys
import tomllib
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_s = spec_from_file_location("_d131s_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
sys.modules["_d131s_solo"] = _solo
_s.loader.exec_module(_solo)

_FAKE_PYPROJECT = """\
[tool.my-lint]
function-too-long-max = 20
nested-loop-depth-max = 2
"""

_FINDINGS = [
    ("function-too-long", 15, "src/utils.py:check_all"),
    ("function-too-long", 25, "src/core.py:process"),
    ("nested-loop-depth", 2,  "src/core.py:walk_tree"),
    ("nested-loop-depth", 3,  "src/helpers.py:flatten"),
    ("function-too-long", 20, "src/cli.py:main"),
]


def main() -> None:
    raw = tomllib.loads(_FAKE_PYPROJECT)
    tool_cfg = {"function-too-long-max": 50, "nested-loop-depth-max": 3,
                **raw.get("tool", {}).get("my-lint", {})}

    fired = [(rule_id, label)
             for rule_id, value, label in _FINDINGS
             if _solo.apply_threshold(rule_id, tool_cfg, value)]

    for rule_id, label in fired:
        print(f"  {label}: {rule_id}")

    labels = [label for _, label in fired]
    assert "src/core.py:process" in labels
    assert "src/helpers.py:flatten" in labels
    assert "src/utils.py:check_all" not in labels
    assert "src/core.py:walk_tree" not in labels
    assert "src/cli.py:main" not in labels
    print("✓ all threshold checks passed")


if __name__ == "__main__":
    main()
