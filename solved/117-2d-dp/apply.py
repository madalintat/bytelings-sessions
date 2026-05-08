"""Rung 5: Apply — solved version.

count_n_queens runs the same backtracking as n_queens but increments a
counter instead of building a list — avoids storing 92 / 724 solutions.

Pattern: P-27 (dfs-with-explicit-stack)
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def count_n_queens(n: int) -> int:
    # Use a mutable container so the nested function can increment it
    count = [0]
    cols: list[int] = []

    def is_safe(row: int, col: int) -> bool:
        for r, c in enumerate(cols):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(row: int) -> None:
        if row == n:
            count[0] += 1
            return
        for col in range(n):
            if is_safe(row, col):
                cols.append(col)
                solve(row + 1)
                cols.pop()

    solve(0)
    return count[0]


def pretty_board(solution: list[int]) -> str:
    n = len(solution)
    rows = []
    for r in range(n):
        row = ["Q" if c == solution[r] else "." for c in range(n)]
        rows.append(" ".join(row))
    return "\n".join(rows)


def main() -> None:
    c8 = count_n_queens(8)
    assert c8 == 92, f"N=8: expected 92, got {c8}"
    print(f"N=8  → {c8} solutions ✓")

    c10 = count_n_queens(10)
    assert c10 == 724, f"N=10: expected 724, got {c10}"
    print(f"N=10 → {c10} solutions ✓")

    solutions_4 = _solo.n_queens(4)
    assert solutions_4
    print(f"\nN=4 solution #1 of {len(solutions_4)}:")
    print(pretty_board(solutions_4[0]))
    print()
    print("✓ apply.py complete")


if __name__ == "__main__":
    main()
