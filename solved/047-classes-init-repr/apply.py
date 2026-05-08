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
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            email = _solo.Email(line)
        except ValueError:
            print(f"  SKIP  {line.rstrip()!r}")
            continue
        print(f"  OK    {email.address}  (domain: {email.domain()})")


if __name__ == "__main__":
    main()
