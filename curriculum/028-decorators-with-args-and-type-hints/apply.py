"""Rung 5: Apply.

Tiny CLI: parse a 'KEY=VALUE' line where KEY is the arg name. Validate
that VALUE is a positive int. Print 'ok' or the error.

Reuses validate from rung 4.

Try it:
  echo "x=5"  | uv run python apply.py
  echo "x=-1" | uv run python apply.py

Patterns: P-18 (decorator-as-wrapper), P-23 (dispatch-by-type).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


@_solo.validate(x=lambda x: isinstance(x, int) and x > 0)
def accept(x):
    return x


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        try:
            n = int(value)
            accept(n)
            print(f"ok: {key}={n}")
        except (ValueError, TypeError) as e:
            print(f"rejected: {key}={value!r} ({e})")


if __name__ == "__main__":
    main()
