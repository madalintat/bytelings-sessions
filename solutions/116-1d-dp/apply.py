"""Rung 5: Apply.

A tiny "can I split this group into two even-weighted teams?" check
using subset_sum: a subset summing to total/2 means yes.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def can_split_evenly(weights):
    s = sum(weights)
    if s % 2:
        return False
    return _solo.subset_sum(weights, s // 2)


def main() -> None:
    cases = [
        [10, 20, 15, 5, 25, 25],
        [1, 1, 1, 1, 1],
        [3, 3, 3, 3],
    ]
    for arr in cases:
        ok = can_split_evenly(arr)
        print(f"  {arr}  -> evenly splittable: {ok}")


if __name__ == "__main__":
    main()
