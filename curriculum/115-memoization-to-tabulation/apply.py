"""Rung 5: Apply — greedy vs DP side by side.

Prints both the greedy and DP coin counts for a coin set + target.
The inline assertions verify:
  - They AGREE on US coins (both optimal).
  - They DISAGREE on [1, 4, 5] target 8 (greedy=4, DP=2).

Usage:
    uv run python apply.py               # uses built-in demo
    uv run python apply.py 1,4,5 8      # custom coins + target

Patterns: P-28 (memoize-recursive).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Load solo.py (top-down) for DP answer
_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def greedy_count(coins: list[int], target: int) -> int:
    """Greedy: take the largest coin that fits, repeat."""
    coins_sorted = sorted(coins, reverse=True)
    remaining = target
    count = 0
    for c in coins_sorted:
        while remaining >= c:
            remaining -= c
            count += 1
    return count if remaining == 0 else -1


def main() -> None:
    if len(sys.argv) >= 3:
        coins = list(map(int, sys.argv[1].split(",")))
        target = int(sys.argv[2])
    else:
        coins, target = [1, 4, 5], 8

    greedy = greedy_count(coins, target)
    dp = _solo.min_coins_topdown(coins, target)

    print(f"Coins:  {coins}")
    print(f"Target: {target}")
    print(f"  Greedy count : {greedy}")
    print(f"  DP count     : {dp}")
    if greedy == dp:
        print("  (greedy and DP agree)")
    else:
        print(f"  !! Greedy is WRONG — DP saves {greedy - dp} coin(s) !!")

    # --- inline correctness assertions ---
    # US coins: greedy and DP must agree
    us_greedy = greedy_count([1, 5, 10, 25], 30)
    us_dp = _solo.min_coins_topdown([1, 5, 10, 25], 30)
    assert us_greedy == us_dp == 2, (
        f"US coins [1,5,10,25] target 30: expected greedy=2, dp=2, "
        f"got greedy={us_greedy}, dp={us_dp}"
    )

    # Adversarial set: greedy and DP must DISAGREE
    adv_greedy = greedy_count([1, 4, 5], 8)
    adv_dp = _solo.min_coins_topdown([1, 4, 5], 8)
    assert adv_greedy == 4, (
        f"[1,4,5] target 8: expected greedy=4, got {adv_greedy}"
    )
    assert adv_dp == 2, (
        f"[1,4,5] target 8: expected dp=2, got {adv_dp}"
    )
    assert adv_greedy != adv_dp, "Greedy and DP should disagree on [1,4,5]→8."

    print("\n✓ Lens choice mattered.")


if __name__ == "__main__":
    main()
