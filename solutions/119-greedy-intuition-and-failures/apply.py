"""Rung 5: Apply.

A counterexample showcase: show greedy succeeding on US-style coins
and FAILING on {1, 4, 6}, side by side with a DP minimum.

Try it: uv run python apply.py
"""
from functools import cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def greedy_coins(amount, coins):
    coins = sorted(coins, reverse=True)
    used = 0
    for c in coins:
        used += amount // c
        amount %= c
    return used if amount == 0 else -1


def dp_coins(amount, coins):
    @cache
    def f(amt):
        if amt == 0:
            return 0
        if amt < 0:
            return float("inf")
        return 1 + min(f(amt - c) for c in coins)
    res = f(amount)
    return res if res != float("inf") else -1


def main() -> None:
    cases = [
        ("US-style {1,5,10,25}", [1, 5, 10, 25], 30),
        ("Tricky    {1,4,6}",    [1, 4, 6],     9),
        ("Tricky    {1,4,6}",    [1, 4, 6],    11),
    ]
    for label, coins, amount in cases:
        g = greedy_coins(amount, coins)
        d = dp_coins(amount, coins)
        marker = "OK   " if g == d else "WRONG"
        print(f"{label}, amt={amount}: greedy={g}, dp={d} [{marker}]")

    print(f"\ncan_jump([2,3,1,1,4]) = {_solo.can_jump([2, 3, 1, 1, 4])}")
    print(f"can_jump([3,2,1,0,4]) = {_solo.can_jump([3, 2, 1, 0, 4])}")


if __name__ == "__main__":
    main()
