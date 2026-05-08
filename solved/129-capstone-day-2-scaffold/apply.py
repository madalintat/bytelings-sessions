"""Solved: apply — runs both rules on a fixture, asserts both fire."""
from __future__ import annotations
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_gs = spec_from_file_location("_d129s_guided", _HERE / "guided.py")
_guided = module_from_spec(_gs)
sys.modules["_d129s_guided"] = _guided
_gs.loader.exec_module(_guided)

_ss = spec_from_file_location("_d129s_solo", _HERE / "solo.py")
_solo = module_from_spec(_ss)
sys.modules["_d129s_solo"] = _solo
_ss.loader.exec_module(_solo)

_SOURCE = """\
def configure(options={}):
    try:
        return options["debug"]
    except:
        return False
"""

if __name__ == "__main__":
    guided_findings = _guided.Linter().run(_SOURCE)
    solo_findings = _solo.Linter().run(_SOURCE)
    all_findings = sorted(guided_findings + solo_findings, key=lambda f: f.line)

    for f in all_findings:
        print(f"  line {f.line}: {f.rule} — {f.message}")

    rules_found = {f.rule for f in all_findings}
    assert "E001" in rules_found
    assert "E002" in rules_found

    print("✓ Both rules registered, both rules fire.")
