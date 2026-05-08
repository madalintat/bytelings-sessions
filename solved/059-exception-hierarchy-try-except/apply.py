"""Rung 5: Apply — solved version.

apply.py works once solo.py is implemented. Unchanged from the starter.
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        status, result = _solo.classify_failure(Path(line).read_text)
        if status == "ok":
            print(f"{line}: OK ({len(result)} bytes)")
        else:
            print(f"{line}: {status}")


if __name__ == "__main__":
    main()
