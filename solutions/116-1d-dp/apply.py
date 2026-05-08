"""Rung 5: Apply — knapsack optimum + chosen items.

Prints both the maximum value AND the subset of items chosen,
backtracking through the 2-D DP table to recover which items were taken.

Inline assertions verify the main example:
  items = [(1,1),(3,4),(4,5),(5,7)], capacity = 7
  → optimum 9 with chosen items {(3,4),(4,5)}

Usage:
    uv run python apply.py          # uses built-in demo
    uv run python apply.py 1:1,3:4,4:5,5:7 7   # custom (w:v pairs + cap)

Patterns: P-28 (memoize-recursive).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Load solo.py (1-D knapsack) for the optimum value
_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def knapsack_2d_full(items: list[tuple[int, int]], capacity: int):
    """Return (max_value, dp_table) for backtracking."""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi, vi = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wi] + vi)
    return dp[n][capacity], dp


def backtrack(dp: list[list[int]], items: list[tuple[int, int]], capacity: int):
    """Recover the subset of chosen items by tracing back through dp."""
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
    total_w = sum(w for w, v in chosen)
    total_v = sum(v for w, v in chosen)
    print(f"  total weight={total_w}, total value={total_v}")

    # --- inline correctness assertions ---
    test_items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    test_cap = 7

    # 1-D solo matches 2-D full
    solo_val = _solo.knapsack_1d(test_items, test_cap)
    ref_val, ref_dp = knapsack_2d_full(test_items, test_cap)
    assert solo_val == ref_val == 9, (
        f"Expected optimum 9, got solo={solo_val}, 2d={ref_val}"
    )

    # Backtracking finds the right subset
    chosen_ref = backtrack(ref_dp, test_items, test_cap)
    chosen_set = set(chosen_ref)
    assert chosen_set == {(3, 4), (4, 5)}, (
        f"Expected chosen {{(3,4),(4,5)}}, got {chosen_set}"
    )
    assert sum(w for w, v in chosen_ref) <= test_cap

    print("\n✓ Lens choice mattered.")


if __name__ == "__main__":
    main()
