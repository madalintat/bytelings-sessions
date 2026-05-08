"""Tests for rung 2."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

# Canonical answers
_ANSWERS = {
    1: "greedy",    # activity selection — exchange argument holds
    2: "needs DP",  # coin change [1,4,5]: greedy picks 5+1+1+1 for 8, DP gives 4+4
    3: "greedy",    # Huffman — merge-two-smallest exchange argument holds
    4: "needs DP",  # 0/1 knapsack — can't split; exchange breaks
    5: "greedy",    # fractional knapsack — divisibility makes swap local
}


def test_activity_selection():
    actual = ex.classify(1)
    diagnose(
        actual == "greedy",
        f"classify(1) returned {actual!r}. Activity selection is the canonical"
        " greedy problem — sort by finish time, exchange argument holds.",
        (lambda: actual == "needs DP",
         "Activity selection does NOT need DP. Sort by earliest finish time;"
         " the exchange argument shows any solution can be transformed to"
         " include greedy's first pick without losing optimality."),
    )


def test_coin_change_tricky():
    actual = ex.classify(2)
    diagnose(
        actual == "needs DP",
        f"classify(2) returned {actual!r}. Coin change with [1,4,5] needs DP.",
        (lambda: actual == "greedy",
         "Greedy FAILS on coins [1,4,5] for amount 8. Greedy picks 5+1+1+1 = 4"
         " coins but the optimum is 4+4 = 2 coins. The exchange argument breaks"
         " because replacing greedy's 5 with nothing leaves an unfillable gap."),
    )


def test_huffman():
    actual = ex.classify(3)
    diagnose(
        actual == "greedy",
        f"classify(3) returned {actual!r}. Huffman coding is provably greedy.",
        (lambda: actual == "needs DP",
         "Huffman coding does NOT need DP. Merging the two least-frequent"
         " symbols is safe; the exchange argument shows any other first merge"
         " produces a code no better. It's greedy all the way down."),
    )


def test_01_knapsack():
    actual = ex.classify(4)
    diagnose(
        actual == "needs DP",
        f"classify(4) returned {actual!r}. 0/1 knapsack needs DP.",
        (lambda: actual == "greedy",
         "0/1 knapsack fails greedy. Items cannot be split, so choosing the"
         " best value/weight ratio first can leave wasted capacity that a"
         " different combination of whole items would have filled."),
    )


def test_fractional_knapsack():
    actual = ex.classify(5)
    diagnose(
        actual == "greedy",
        f"classify(5) returned {actual!r}. Fractional knapsack is greedy.",
        (lambda: actual == "needs DP",
         "Fractional knapsack does NOT need DP. Because items can be split,"
         " taking the highest value/weight ratio is always safe — you never"
         " waste capacity. The exchange argument works because partial items"
         " make every swap lossless."),
    )
