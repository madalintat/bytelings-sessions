"""Rung 5: Apply.

Tiny CLI: read integers from stdin, compute the (slow) factorial of each
using a memoizing closure. Print runtime to show the cache wins.

Reuses make_memoizer from rung 4.

Try it: printf "10\n10\n10\n" | uv run python apply.py
"""
import sys
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def slow_fact(n: int) -> int:
    if n < 2:
        return 1
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def main() -> None:
    memo = _solo.make_memoizer()
    fast = memo(slow_fact)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        t0 = time.perf_counter_ns()
        result = fast(n)
        elapsed_us = (time.perf_counter_ns() - t0) / 1000
        print(f"fact({n}) = ...{str(result)[-6:]} (in {elapsed_us:.1f} us)")


if __name__ == "__main__":
    main()
