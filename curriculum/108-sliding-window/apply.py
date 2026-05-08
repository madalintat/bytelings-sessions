"""Rung 5: Apply.

Tiny rolling-average tool: read 30 days of fake revenue numbers and
print the 7-day rolling average. Sliding window, O(n).

Try it: uv run python apply.py

Patterns: P-06 (sliding-window).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


REVENUE = [
    100, 110, 90, 120, 130, 80, 95,
    140, 160, 150, 170, 180, 200, 190,
    210, 220, 200, 230, 250, 240, 260,
    280, 290, 270, 300, 320, 310, 330,
    350, 360,
]


def rolling_average(arr, k):
    if k <= 0 or k > len(arr):
        return []
    out = []
    s = sum(arr[:k])
    out.append(s / k)
    for i in range(k, len(arr)):
        s += arr[i] - arr[i - k]
        out.append(s / k)
    return out


def main() -> None:
    avgs = rolling_average(REVENUE, 7)
    print("7-day rolling average:")
    for i, a in enumerate(avgs):
        print(f"  day {i+7:2d}: {a:6.1f}")
    print(f"\nSmallest window summing to >= 800: "
          f"{_solo.min_subarray_len(REVENUE, 800)} days")


if __name__ == "__main__":
    main()
