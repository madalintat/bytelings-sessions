"""Rung 5: Apply.

Tiny CLI: read celsius values from stdin, print them as Fahrenheit too.
Skip lines below absolute zero.

Try it:
    printf '0\\n100\\n-400\\n20\\n' | uv run python apply.py

Patterns: P-22 (cached-property).
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
