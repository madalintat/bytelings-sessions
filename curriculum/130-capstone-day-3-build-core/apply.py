"""Rung 5: Apply — combine find_unused_imports + function_too_long.

Runs both rules on a fixture source string, prints sorted findings,
then asserts both fired.

Run with:  uv run python apply.py
"""
from __future__ import annotations
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent

_gs = spec_from_file_location("_d130_guided", _HERE / "guided.py")
_guided = module_from_spec(_gs)
sys.modules["_d130_guided"] = _guided
_gs.loader.exec_module(_guided)

_ss = spec_from_file_location("_d130_solo", _HERE / "solo.py")
_solo = module_from_spec(_ss)
sys.modules["_d130_solo"] = _solo
_ss.loader.exec_module(_solo)

# Fixture: one unused import + one function that is too long (max_lines=3).
_SOURCE = """\
import os
import sys

def process(data):
    result = []
    result.append(sys.argv[0])
    result.append(data)
    return result
"""

if __name__ == "__main__":
    unused = _guided.find_unused_imports(_SOURCE)
    too_long = _solo.function_too_long(_SOURCE, max_lines=3)

    print("Unused imports:")
    for name in unused:
        print(f"  unused import: {name!r}")

    print("Long functions:")
    for name, count in too_long:
        print(f"  {name}: {count} body lines (limit: 3)")

    assert unused, f"No unused imports found; expected 'os'. Got {unused!r}"
    assert too_long, f"No long functions found. Got {too_long!r}"

    print("✓ Both rules registered, both rules fire.")
