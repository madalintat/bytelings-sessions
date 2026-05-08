"""Tests for rung 2."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

# Canonical answers — bridge cases have 2 lenses.
_ANSWERS = {
    1: {"greedy"},
    2: {"dp"},
    3: {"backtracking"},
    4: {"greedy"},
    5: {"dp", "backtracking"},   # bridge: memoized recursion
    6: {"dp"},
    7: {"backtracking"},
    8: {"dp"},
}


def test_activity_selection():
    actual = ex.pick_lens(1)
    diagnose(
        actual == {"greedy"},
        f"pick_lens(1) returned {actual!r}. Activity selection is purely greedy.",
        (lambda: "dp" in actual and "greedy" not in actual,
         "Activity selection does not need DP — the exchange argument gives a"
         " direct O(n log n) greedy solution. No overlapping subproblems."),
        (lambda: "backtracking" in actual,
         "Backtracking is not needed for activity selection. Greedy makes one"
         " irrevocable choice per step with a provably safe exchange argument."),
    )


def test_coin_change():
    actual = ex.pick_lens(2)
    diagnose(
        actual == {"dp"},
        f"pick_lens(2) returned {actual!r}. Coin change (min coins) needs DP.",
        (lambda: actual == {"greedy"},
         "Greedy fails on arbitrary coin denominations — counterexample:"
         " coins=[1,4,5], amount=8. Greedy picks 5+1+1+1 but DP finds 4+4."),
        (lambda: "backtracking" in actual and "dp" not in actual,
         "Backtracking alone would work but is exponentially slower without"
         " memoization. With memoization it becomes DP. The lens is dp."),
    )


def test_permutations():
    actual = ex.pick_lens(3)
    diagnose(
        actual == {"backtracking"},
        f"pick_lens(3) returned {actual!r}. Generating all permutations is backtracking.",
        (lambda: "dp" in actual,
         "DP doesn't apply to generating all permutations — there's no"
         " optimum to compute, just an exhaustive enumeration. The state"
         " space also has no overlapping subproblems."),
    )


def test_shortest_path():
    actual = ex.pick_lens(4)
    diagnose(
        actual == {"greedy"},
        f"pick_lens(4) returned {actual!r}. Shortest path (non-negative) is greedy (Dijkstra).",
        (lambda: actual == {"dp"},
         "While Bellman-Ford uses DP, Dijkstra (for non-negative weights) is"
         " greedy — always expand the nearest unvisited node. Non-negative"
         " weights make the greedy choice safe."),
    )


def test_word_break_bridge():
    actual = ex.pick_lens(5)
    diagnose(
        actual == {"dp", "backtracking"},
        f"pick_lens(5) returned {actual!r}. Word break is a bridge case: dp + backtracking.",
        (lambda: actual == {"dp"},
         "Partial credit. Word break IS DP, but the natural implementation is"
         " a memoized recursion — backtracking with @cache. Both lenses apply."),
        (lambda: actual == {"backtracking"},
         "Partial credit. Word break IS backtracking, but without memoization"
         " it's exponential. Adding @cache makes it DP. Both lenses apply."),
        (lambda: actual == {"greedy"},
         "Greedy does not apply to word break. There's no safe single local"
         " choice — you must explore all splits (and memoize)."),
    )


def test_knapsack():
    actual = ex.pick_lens(6)
    diagnose(
        actual == {"dp"},
        f"pick_lens(6) returned {actual!r}. 0/1 knapsack needs DP.",
        (lambda: actual == {"greedy"},
         "0/1 knapsack fails greedy. Items cannot be split, so taking the"
         " best ratio first can block a better whole-item combination."),
    )


def test_parenthesizations():
    actual = ex.pick_lens(7)
    diagnose(
        actual == {"backtracking"},
        f"pick_lens(7) returned {actual!r}. Generating all parenthesizations is backtracking.",
        (lambda: "dp" in actual,
         "Counting valid parenthesizations uses Catalan numbers / DP, but"
         " GENERATING all of them requires backtracking enumeration."),
    )


def test_lcs():
    actual = ex.pick_lens(8)
    diagnose(
        actual == {"dp"},
        f"pick_lens(8) returned {actual!r}. LCS is a classic 2D DP problem.",
        (lambda: "backtracking" in actual and "dp" not in actual,
         "LCS can be solved by backtracking but that's O(2^n). The canonical"
         " solution is the 2D DP table, making it purely a DP lens."),
    )
