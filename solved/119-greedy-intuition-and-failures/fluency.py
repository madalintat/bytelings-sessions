"""Rung 2: Fluency drill — solved version.

The exchange argument holds for activity selection, Huffman, and fractional
knapsack. It breaks for coin change [1,4,5] (greedy picks 5+1+1+1=4 coins for
8, but 4+4=2 is optimal) and for 0/1 knapsack (items cannot be split, so a
locally best-ratio item can block a better whole-item combination).
"""


def classify(problem_id: int) -> str:
    """Return "greedy" or "needs DP" for each of the five problems."""
    # Problems where exchange argument holds → greedy is safe.
    # Problems where the swap breaks validity → fall back to DP.
    _table = {
        1: "greedy",    # activity selection
        2: "needs DP",  # coin change [1,4,5]: greedy fails on amount 8
        3: "greedy",    # Huffman coding
        4: "needs DP",  # 0/1 knapsack
        5: "greedy",    # fractional knapsack
    }
    return _table[problem_id]
