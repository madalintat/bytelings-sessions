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
        raw = raw.strip()
        if not raw:
            continue
        try:
            t = _solo.Temperature(float(raw))
        except (ValueError, TypeError):
            print(f"  SKIP  {raw!r}")
            continue
        print(f"  {t.celsius:>7.2f}°C  =  {t.fahrenheit:>7.2f}°F")


if __name__ == "__main__":
    main()
