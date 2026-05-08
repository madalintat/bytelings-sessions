"""Rung 5: Apply — solved version.

Verifies sorted output + exit codes with synthetic findings.
"""
from __future__ import annotations

import sys
from importlib.util import module_from_spec, spec_from_file_location
from io import StringIO
from pathlib import Path

_HERE = Path(__file__).parent
_s = spec_from_file_location("_d132s_solo", _HERE / "solo.py")
_solo = module_from_spec(_s)
sys.modules["_d132s_solo"] = _solo
_s.loader.exec_module(_solo)

Finding = _solo.Finding

_FINDINGS = [
    Finding(Path("src/core.py"),    20, 0,  "function-too-long", "process is 55 lines (max 50)"),
    Finding(Path("src/utils.py"),    3, 4,  "bare-except",       "use specific exception"),
    Finding(Path("src/cli.py"),      1, 0,  "print-in-non-cli",  "print outside __main__"),
    Finding(Path("src/core.py"),     5, 8,  "nested-loop-depth", "depth 4 > max 3"),
    Finding(Path("src/utils.py"),   15, 0,  "function-too-long", "helper is 60 lines (max 50)"),
]

_TARGETS = [Path("src/cli.py"), Path("src/core.py"), Path("src/utils.py")]


def main() -> None:
    buf = StringIO()
    real_stdout = sys.stdout
    sys.stdout = buf
    try:
        rc = _solo.main(_TARGETS, list(_FINDINGS))
    finally:
        sys.stdout = real_stdout

    lines = [l for l in buf.getvalue().splitlines() if l.strip()]
    assert rc == 1
    assert len(lines) == 5
    assert lines[0].startswith("src/cli.py:")
    assert lines[1].startswith("src/core.py:5")
    assert lines[2].startswith("src/core.py:20")
    assert lines[3].startswith("src/utils.py:3")
    assert lines[4].startswith("src/utils.py:15")
    print("✓ exit code 1 with findings")
    print("✓ output is sorted by (path, line, col)")

    buf2 = StringIO()
    sys.stdout = buf2
    try:
        rc0 = _solo.main([], [])
    finally:
        sys.stdout = real_stdout

    assert rc0 == 0
    assert buf2.getvalue() == ""
    print("✓ exit code 0 with empty findings")


if __name__ == "__main__":
    main()
