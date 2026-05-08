"""Rung 5: Apply — run both rules, print sorted findings.

This file is self-contained: it loads guided.py (for bare_except / E001)
and solo.py (for mutable_default_argument / E002), runs both on a fixture
source string, prints findings sorted by line, then asserts both fired.

Run with:  uv run python apply.py
"""
from __future__ import annotations
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

# Load guided module (contains bare_except rule + Linter infrastructure).
_gs = spec_from_file_location("_d129_guided", _HERE / "guided.py")
_guided = module_from_spec(_gs)
sys.modules["_d129_guided"] = _guided
_gs.loader.exec_module(_guided)

# Load solo module (registers mutable_default_argument rule).
_ss = spec_from_file_location("_d129_solo", _HERE / "solo.py")
_solo = module_from_spec(_ss)
sys.modules["_d129_solo"] = _solo
_ss.loader.exec_module(_solo)

# ── fixture source: one bare-except + one mutable default ────────────────────
_SOURCE = """\
def configure(options={}):
    try:
        return options["debug"]
    except:
        return False
"""

if __name__ == "__main__":
    # Collect findings from guided's Linter (which has E001 registered).
    guided_findings = _guided.Linter().run(_SOURCE)

    # Collect findings from solo's Linter (which has E002 registered).
    solo_findings = _solo.Linter().run(_SOURCE)

    all_findings = sorted(guided_findings + solo_findings, key=lambda f: f.line)

    for f in all_findings:
        print(f"  line {f.line}: {f.rule} — {f.message}")

    rules_found = {f.rule for f in all_findings}
    assert "E001" in rules_found, f"bare_except (E001) did not fire; findings={all_findings}"
    assert "E002" in rules_found, f"mutable_default_argument (E002) did not fire; findings={all_findings}"

    print("✓ Both rules registered, both rules fire.")
