"""Rung 2: Fluency drill — solved version.

Bridge cases (5 = word break) need two lenses because the natural
implementation is a memoized recursion: backtracking provides the
search structure and @cache turns it into DP.

Activity selection (1) and Dijkstra (4) are purely greedy; their
exchange arguments go through cleanly. Generating permutations (3) and
parenthesizations (7) are pure backtracking — no overlapping subproblems,
no optimisation, just exhaustive enumeration. Coin change (2), 0/1
knapsack (6), and LCS (8) are pure DP — greedy fails, backtracking
alone is exponential.
"""


def pick_lens(problem_id: int) -> set[str]:
    """Return the set of applicable lenses for each problem."""
    _table: dict[int, set[str]] = {
        1: {"greedy"},
        2: {"dp"},
        3: {"backtracking"},
        4: {"greedy"},
        5: {"dp", "backtracking"},  # word break — bridge case
        6: {"dp"},
        7: {"backtracking"},
        8: {"dp"},
    }
    return _table[problem_id]
