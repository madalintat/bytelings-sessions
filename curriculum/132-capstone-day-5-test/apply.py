"""Rung 5: Apply — verify sorted output and exit codes.

5 synthetic findings across 3 files in scrambled discovery order.
Runs main(), captures stdout, asserts sorted ordering and exit codes.

Run:
    uv run python apply.py
"""
from __future__ import annotations

import sys
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from pathlib import Path

_HERE = Path(__file__).parent
_s = spec_from_file_location("_d132_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
sys.modules["_d132_solo"] = _solo
_s.loader.exec_module(_solo)

Finding = _solo.Finding

# ---------------------------------------------------------------------------
# 5 findings across 3 files, in scrambled order
# ---------------------------------------------------------------------------
_FINDINGS = [
    Finding(Path("src/core.py"),    20, 0,  "function-too-long", "process is 55 lines (max 50)"),
    Finding(Path("src/utils.py"),    3, 4,  "bare-except",       "use specific exception"),
    Finding(Path("src/cli.py"),      1, 0,  "print-in-non-cli",  "print outside __main__"),
    Finding(Path("src/core.py"),     5, 8,  "nested-loop-depth", "depth 4 > max 3"),
    Finding(Path("src/utils.py"),   15, 0,  "function-too-long", "helper is 60 lines (max 50)"),
]

_TARGETS = [Path("src/cli.py"), Path("src/core.py"), Path("src/utils.py")]


def main() -> None:
    # --- Test 1: non-empty findings → exit code 1, output sorted ---
    buf = StringIO()
    _real_stdout = sys.stdout
    sys.stdout = buf
    try:
        rc = _solo.main(_TARGETS, list(_FINDINGS))
    finally:
        sys.stdout = _real_stdout

    output = buf.getvalue()
    lines = [l for l in output.splitlines() if l.strip()]

    assert rc == 1, f"Expected exit code 1 with findings, got {rc}"
    assert len(lines) == 5, f"Expected 5 output lines, got {len(lines)}"

    # Verify sorted order: cli.py < core.py < utils.py
    assert lines[0].startswith("src/cli.py:"),   f"Line 0 should be cli.py: {lines[0]}"
    assert lines[1].startswith("src/core.py:5"), f"Line 1 should be core.py:5: {lines[1]}"
    assert lines[2].startswith("src/core.py:20"), f"Line 2 should be core.py:20: {lines[2]}"
    assert lines[3].startswith("src/utils.py:3"), f"Line 3 should be utils.py:3: {lines[3]}"
    assert lines[4].startswith("src/utils.py:15"), f"Line 4 should be utils.py:15: {lines[4]}"

    print("✓ exit code 1 with findings")
    print("✓ output is sorted by (path, line, col)")

    # --- Test 2: empty findings → exit code 0, no output ---
    buf2 = StringIO()
    sys.stdout = buf2
    try:
        rc0 = _solo.main([], [])
    finally:
        sys.stdout = _real_stdout

    assert rc0 == 0, f"Expected exit code 0 with no findings, got {rc0}"
    assert buf2.getvalue() == "", "No output expected for empty findings"
    print("✓ exit code 0 with empty findings")


if __name__ == "__main__":
    main()
