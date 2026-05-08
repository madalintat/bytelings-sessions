"""Rung 5: Apply.

Tiny CLI: given a sorted list of timestamps and a [start, end] window,
print how many fall inside the window. Two binary searches do the
whole job.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def lower_bound(arr, t):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, t):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= t:
            lo = mid + 1
        else:
            hi = mid
    return lo


def count_in_window(stamps, start, end):
    return upper_bound(stamps, end) - lower_bound(stamps, start)


def main() -> None:
    stamps = sorted([1, 5, 7, 8, 8, 9, 10, 14, 18, 20, 25])
    print(f"timestamps: {stamps}")
    print(f"in [8, 14]: {count_in_window(stamps, 8, 14)}")
    print(f"in [0, 4]:  {count_in_window(stamps, 0, 4)}")
    print(f"in [21, 30]:{count_in_window(stamps, 21, 30)}")
    print(f"max requests fitting capacity 11: {_solo.max_requests([1, 2, 3, 5, 8], 11)}")


if __name__ == "__main__":
    main()
