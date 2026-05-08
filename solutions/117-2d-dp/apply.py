"""Rung 5: Apply — count N-queens and pretty-print a board.

Pattern: P-27 (dfs-with-explicit-stack)

Tasks:
1. Implement `count_n_queens(n)` — count solutions without storing them.
2. Run count_n_queens for N=8 (expect 92) and N=10 (expect 724).
3. Print a pretty board for ONE N=4 solution.

Pretty-print format — each row on its own line, queens as 'Q', empty as '.':
    . Q . .
    . . . Q
    Q . . .
    . . Q .

Run with: uv run python curriculum/117-2d-dp/apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def count_n_queens(n: int) -> int:
    """Return the number of valid N-queens solutions.

    Hint: same backtracking as n_queens but increment a counter instead
    of appending to a list. Avoids storing all solutions in memory.
    """
    # TODO: implement backtracking counter (no list needed)
    raise NotImplementedError


def pretty_board(solution: list[int]) -> str:
    """Return a multi-line string representation of an N-queens solution.

    Args:
        solution: list of column indices, solution[r] = column of queen in row r

    Returns:
        String with N lines, each row showing 'Q' at the queen's column
        and '.' elsewhere, columns separated by spaces.
    """
    n = len(solution)
    rows = []
    for r in range(n):
        row = ["Q" if c == solution[r] else "." for c in range(n)]
        rows.append(" ".join(row))
    return "\n".join(rows)


def main() -> None:
    # Verify counts
    c8 = count_n_queens(8)
    assert c8 == 92, f"N=8: expected 92, got {c8}"
    print(f"N=8  → {c8} solutions ✓")

    c10 = count_n_queens(10)
    assert c10 == 724, f"N=10: expected 724, got {c10}"
    print(f"N=10 → {c10} solutions ✓")

    # Pretty-print one N=4 solution using the solver from solo.py
    solutions_4 = _solo.n_queens(4)
    assert solutions_4, "n_queens(4) returned no solutions — fix solo.py first"
    print(f"\nN=4 solution #{1} of {len(solutions_4)}:")
    print(pretty_board(solutions_4[0]))
    print()

    print("✓ apply.py complete")


if __name__ == "__main__":
    main()
