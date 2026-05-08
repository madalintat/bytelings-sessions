"""Rung 5: Apply.

Tiny CLI: read one number from stdin, run it through a 3-step pipeline
(strip / int-parse / square), print the trace.

Reuses pipeline from rung 4.

Try it: echo "  7  " | uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    raw = sys.stdin.read()
    steps = [
        ("strip", str.strip),
        ("to_int", int),
        ("square", lambda x: x * x),
    ]
    run = _solo.pipeline(steps)
    final, trace = run(raw)
    for name, value in trace:
        print(f"{name}: {value!r}")
    print(f"final: {final!r}")


if __name__ == "__main__":
    main()
