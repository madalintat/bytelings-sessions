"""Rung 5: Apply.

Tiny CLI: take a list of task durations, print sequential vs concurrent
elapsed times and the speedup factor.

Try it:
    uv run python apply.py 1 2 3 4
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    durations = [float(arg) for arg in sys.argv[1:]]
    if not durations:
        print("usage: apply.py <duration1> <duration2> ...")
        return
    seq = _solo.elapsed_seconds(durations, concurrent=False)
    conc = _solo.elapsed_seconds(durations, concurrent=True)
    speedup = seq / conc if conc else float("inf")
    print(f"sequential: {seq:.2f}s")
    print(f"concurrent: {conc:.2f}s")
    print(f"speedup:    {speedup:.2f}x")


if __name__ == "__main__":
    main()
