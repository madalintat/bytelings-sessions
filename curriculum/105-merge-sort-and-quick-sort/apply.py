"""Rung 5: Apply.

Time merge_sort vs quick_sort vs Python's built-in sorted() on the
same random list. Watch the built-in destroy your hand-rolled ones.

Try it: uv run python apply.py
"""
import random
import time
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_solo_spec = spec_from_file_location("_solo", _HERE / "solo.py")
_solo = module_from_spec(_solo_spec)
_solo_spec.loader.exec_module(_solo)
_guided_spec = spec_from_file_location("_guided", _HERE / "guided.py")
_guided = module_from_spec(_guided_spec)
_guided_spec.loader.exec_module(_guided)


def time_it(label, fn, arr):
    t = time.perf_counter()
    fn(arr)
    elapsed = (time.perf_counter() - t) * 1000
    print(f"{label:>16}: {elapsed:7.2f} ms")


def main() -> None:
    random.seed(0)
    arr = [random.randint(0, 1_000_000) for _ in range(10_000)]
    print(f"Sorting {len(arr)} random ints:")
    time_it("merge_sort", _guided.merge_sort, arr)
    time_it("quick_sort", _solo.quick_sort, arr)
    time_it("builtin sorted", sorted, arr)


if __name__ == "__main__":
    main()
