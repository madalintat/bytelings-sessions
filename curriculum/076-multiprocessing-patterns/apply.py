"""Rung 5: Apply.

Compare serial vs parallel sum-of-squares on a sizeable input.

Try it: uv run python apply.py
"""
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def serial_sum_of_squares(items: list[int]) -> int:
    return sum(x * x for x in items)


def main() -> None:
    items = list(range(1, 200_001))
    t0 = time.perf_counter()
    a = serial_sum_of_squares(items)
    t1 = time.perf_counter()
    b = _solo.parallel_sum_of_squares(items, max_workers=4)
    t2 = time.perf_counter()
    print(f"serial:   {(t1 - t0) * 1000:7.1f} ms  -> {a}")
    print(f"parallel: {(t2 - t1) * 1000:7.1f} ms  -> {b}")
    assert a == b, "results disagree"


if __name__ == "__main__":
    main()
