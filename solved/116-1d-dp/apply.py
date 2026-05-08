"""Rung 5: Apply — solved version.

Prints optimum value + chosen items.  Backtracking walks dp in
reverse: if dp[i][w] != dp[i-1][w], item i was taken.

Patterns: P-28 (memoize-recursive).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def knapsack_2d_full(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
    return dp[n][capacity], dp


def backtrack(dp, items, capacity):
    chosen = []
    w = capacity
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(items[i - 1])
            w -= items[i - 1][0]
    return chosen


def main() -> None:
    if len(sys.argv) >= 3:
        items = [tuple(map(int, p.split(":"))) for p in sys.argv[1].split(",")]
        capacity = int(sys.argv[2])
    else:
        items = [(1, 1), (3, 4), (4, 5), (5, 7)]
        capacity = 7

    optimum, dp = knapsack_2d_full(items, capacity)
    chosen = backtrack(dp, items, capacity)

    print(f"Items:    {items}")
    print(f"Capacity: {capacity}")
    print(f"Optimum value: {optimum}")
    print(f"Chosen items:  {sorted(chosen)}")

    test_items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    test_cap = 7
    solo_val = _solo.knapsack_1d(test_items, test_cap)
    ref_val, ref_dp = knapsack_2d_full(test_items, test_cap)
    assert solo_val == ref_val == 9
    chosen_ref = set(backtrack(ref_dp, test_items, test_cap))
    assert chosen_ref == {(3, 4), (4, 5)}

    print("\n✓ Lens choice mattered.")


if __name__ == "__main__":
    main()
