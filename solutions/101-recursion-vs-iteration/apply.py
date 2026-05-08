"""Rung 5: Apply — show iteration vs recursion picking the right tool.

Time both: a recursive sum that crashes on big input, vs an iterative
sum that handles it. The point is to *feel* the difference.

Try it: uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def rec_sum(nums):
    if not nums:
        return 0
    return nums[0] + rec_sum(nums[1:])


def iter_sum(nums):
    s = 0
    for n in nums:
        s += n
    return s


def main() -> None:
    small = list(range(50))
    big = list(range(5000))

    print(f"rec_sum on {len(small)} items: {rec_sum(small)}")
    print(f"iter_sum on {len(big)} items: {iter_sum(big)}")

    # Demonstrate the failure mode
    sys.setrecursionlimit(2000)
    try:
        rec_sum(big)
        print("rec_sum on big somehow worked")
    except RecursionError:
        print("rec_sum on big: RecursionError — exactly why we use iteration here")

    print(f"running_sum head: {_solo.running_sum(small)[:5]}")


if __name__ == "__main__":
    main()
